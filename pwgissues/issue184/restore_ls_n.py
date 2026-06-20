#!/usr/bin/env python3
"""
Restore <ls n="..."> tags in temp_pwg.txt that were consolidated away.

Reads old version from temp_pwg0.txt to build a lookup of content → prefix.
Reads new version from temp_pwg.txt.
Splits consolidated <ls> tags back into individual <ls> and <ls n=""> tags.
Also restores standalone bare <ls> tags whose content matches a unique lookup entry.
Writes result to temp_pwg1.txt.

Place in the same directory as temp_pwg0.txt, temp_pwg.txt.
"""

import os
import re
import sys


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_file(name):
    path = os.path.join(SCRIPT_DIR, name)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def get_old_version():
    return read_file('temp_pwg0.txt')


def get_new_version():
    return read_file('temp_pwg.txt')


def build_lookup(old_text):
    lookup = {}
    for m in re.finditer(r'<ls n="([^"]*)">([^<]*)</ls>', old_text):
        prefix = m.group(1)
        content = m.group(2).strip().rstrip('.')
        if content:
            if content not in lookup:
                lookup[content] = set()
            lookup[content].add(prefix)
    return lookup


def split_references(inner_text):
    parts = []
    remaining = inner_text

    while remaining:
        m = re.search(r'(?<=[\d])\. ', remaining)
        if m:
            part = remaining[:m.end() - 2]
            remaining = remaining[m.end():]
            parts.append((part, True))
        else:
            has_trailing_period = remaining.endswith('.')
            if has_trailing_period:
                parts.append((remaining[:-1], True))
            else:
                parts.append((remaining, False))
            remaining = ''

    return parts


def derive_prefix(first_ref):
    m = re.search(r'\d+$', first_ref)
    if m:
        return first_ref[:m.start()]
    return first_ref.rstrip('0123456789,.')


def decompose_first_ref(ref_text, lookup):
    """
    Try multi-level prefix decomposition of a merged reference.

    "P. 7,3,30" → ("P.", "7,3,30")  if "7,3,30" in lookup with prefix "P."
    Returns (prefix, content) or None.
    """
    m = re.search(r'\d+$', ref_text)
    if not m:
        return None

    prefix = ref_text[:m.start()]
    while prefix:
        content = ref_text[len(prefix):]
        if content in lookup and prefix in lookup[content]:
            return (prefix, content)
        m2 = re.search(r',\d+$', prefix)
        if m2:
            prefix = prefix[:m2.start()]
        else:
            break
    return None


def find_unique_prefix(content, lookup):
    """Return the single prefix for content, or empty string if 0 or >1."""
    if content in lookup and len(lookup[content]) == 1:
        return list(lookup[content])[0]
    return ''


def prefix_find(derived, candidates):
    best = ''
    for c in candidates:
        if not c:
            continue
        if derived == c:
            return c
        if derived.startswith(c) and len(c) > len(best):
            best = c
        if c.startswith(derived) and len(c) > len(best):
            best = c
    return best


def period_suffix(needs):
    return '.' if needs else ''


def split_n_tags(text):
    """Split <ls n='...'> tags with multi-ref content into separate tags.
    Tracks the last full reference (most comma-separated numbers) to compute
    inherited prefixes for partial references.
    3-number source: '1,63,7. 107,1. 5.' → <ls n="ṚV.">1,63,7</ls>.<ls n="ṚV. 1,">107,1</ls>.<ls n="ṚV. 1,63,">5</ls>.
    2-number source: '9,242. 11,45. 46. 89. 127' → <ls n="M.">9,242</ls>.<ls n="M.">11,45</ls>.<ls n="M. 11,">46</ls>. ..."""
    n_pattern = re.compile(r'<ls n="([^"]*)">([^<]*)</ls>([.)])?')
    def repl(m):
        prefix = m.group(1)
        content = m.group(2).strip()
        trailing = m.group(3) or ''
        if '. ' not in content:
            return m.group(0)
        pieces = content.split('. ')
        last_full_content = None
        max_commas = 0
        out = []
        for piece in pieces:
            clean = piece.strip().rstrip('.')
            has_period = piece.strip().endswith('.')
            commas = clean.count(',')
            if commas > max_commas:
                max_commas = commas
            if commas == max_commas and commas > 0:
                last_full_content = clean
                tag = f'<ls n="{prefix}">{clean}</ls>'
            elif last_full_content is not None:
                num_to_inherit = max_commas - commas
                last_parts = last_full_content.split(',')
                inherited = ','.join(last_parts[:num_to_inherit])
                tag = f'<ls n="{prefix} {inherited},">{clean}</ls>'
            else:
                tag = f'<ls n="{prefix}">{clean}</ls>'
            if has_period:
                tag += '.'
            out.append(tag)
        return ''.join(out) + trailing
    return n_pattern.sub(repl, text)


def split_dash_ref(ref_text, ref_period, lookup, cur_prefix, expected_prefix):
    """Split em-dash consolidated ref like 'P. 6,2,155—158' into individual <ls> tags.
    Returns (combined_string, updated_expected_prefix)."""
    parts = [p.strip() for p in ref_text.split('—')]
    sub_refs = []
    for idx, part in enumerate(parts):
        part_norm = part.rstrip('.')
        if idx == 0:
            sub_refs.append(f'<ls>{part}</ls>')
            cur_prefix = derive_prefix(part)
            expected_prefix = cur_prefix
        else:
            prefix = get_ref_prefix(part_norm, lookup, cur_prefix, expected_prefix)
            if prefix:
                sub_refs.append(f'<ls n="{prefix}">{part}</ls>')
                expected_prefix = derive_prefix(prefix.rstrip() + ' ' + part_norm)
            else:
                sub_refs.append(f'<ls>{part}</ls>')
    combined = '—'.join(sub_refs)
    if ref_period:
        combined += '.'
    return combined, expected_prefix


def get_ref_prefix(ref_norm, lookup, derived_prefix, expected_prefix):
    if ref_norm not in lookup:
        return ''
    candidates = lookup[ref_norm]
    p = prefix_find(expected_prefix, candidates)
    if not p:
        p = prefix_find(derived_prefix, candidates)
    return p


def check_ref_match(ref_text, lookup, derived_prefix, expected_prefix):
    raw = ref_text.rstrip('.')
    if '—' in raw:
        for part in re.split(r'\s*—\s*', raw):
            p = get_ref_prefix(part, lookup, derived_prefix, expected_prefix)
            if p:
                return True
        return False
    return bool(get_ref_prefix(raw, lookup, derived_prefix, expected_prefix))


def process_ref(ref_text, ref_period, lookup, derived_prefix, expected_prefix):
    ref_norm = ref_text.rstrip('.')
    if '—' not in ref_norm:
        prefix = get_ref_prefix(ref_norm, lookup, derived_prefix, expected_prefix)
        if prefix:
            new_expected = derive_prefix(prefix.rstrip() + ' ' + ref_norm)
            return [f' <ls n="{prefix}">{ref_text}</ls>{period_suffix(ref_period)}'], new_expected
        return [f' <ls>{ref_text}</ls>{period_suffix(ref_period)}'], expected_prefix

    parts = re.split(r'\s*—\s*', ref_text)
    sub_results = []
    cur_prefix = expected_prefix
    for i, part in enumerate(parts):
        part_norm = part.rstrip('.')
        prefix = get_ref_prefix(part_norm, lookup, derived_prefix, cur_prefix)
        if prefix:
            sub_results.append(f'<ls n="{prefix}">{part}</ls>')
            cur_prefix = derive_prefix(prefix.rstrip() + ' ' + part_norm)
        else:
            sub_results.append(f'<ls>{part}</ls>')
    combined = '—'.join(sub_results) + period_suffix(ref_period)
    return [f' {combined}'], cur_prefix


def process_new_text(new_text, lookup):
    """Process new text: first split multi-ref <ls n='...'> tags, then restore n=."""
    new_text = split_n_tags(new_text)
    result_parts = []
    pos = 0
    ls_pattern = re.compile(r'<ls>([^<]*)</ls>')

    while pos < len(new_text):
        m = ls_pattern.search(new_text, pos)
        if not m:
            result_parts.append(new_text[pos:])
            break

        result_parts.append(new_text[pos:m.start()])
        inner_text = m.group(1)
        inner_text_stripped = inner_text.strip()

        refs = split_references(inner_text_stripped)

        if len(refs) == 1:
            first_text, first_needs_period = refs[0]

            # If text already contains a book abbreviation (has letters),
            # it's a complete reference; don't add n=.
            if re.search(r'[A-Za-z]', first_text):
                # But if it contains an em-dash, it may have consolidated
                # separate <ls> tags; try to split them back.
                if '—' in first_text:
                    combined, _ = split_dash_ref(first_text, first_needs_period, lookup, '', '')
                    result_parts.append(f' {combined}')
                else:
                    result_parts.append(m.group(0))
                pos = m.end()
                continue

            prefix = ''
            decomp = decompose_first_ref(first_text, lookup)
            if decomp:
                prefix = decomp[0]
            elif first_text.rstrip('.') in lookup:
                prefix = find_unique_prefix(first_text.rstrip('.'), lookup)
                if prefix and not first_text.startswith(prefix):
                    prefix = ''

            if prefix:
                result_parts.append(
                    f'<ls n="{prefix}">{first_text[len(prefix):]}</ls>'
                    f'{period_suffix(first_needs_period)}'
                )
            else:
                result_parts.append(m.group(0))
            pos = m.end()
            continue

        first_text, first_period = refs[0]
        derived_prefix = derive_prefix(first_text)

        decomp = decompose_first_ref(first_text, lookup)
        if decomp:
            derived_prefix = decomp[0]

        # Handle em-dash in first ref (e.g., "P. 6,2,155—158" → "P. 6,2,")
        if '—' in first_text:
            first_before_dash = first_text.split('—')[0]
            dash_prefix = derive_prefix(first_before_dash)
            if dash_prefix and dash_prefix != derived_prefix:
                derived_prefix = dash_prefix

        has_valid_match = False
        sim_expected = derived_prefix
        for ref_text, _ in refs[1:]:
            if not check_ref_match(ref_text, lookup, derived_prefix, sim_expected):
                continue
            has_valid_match = True
            ref_norm = ref_text.rstrip('.')
            if '—' in ref_norm:
                parts = re.split(r'\s*—\s*', ref_norm)
                sub = parts[-1] if parts else ref_norm
                sim_expected = derive_prefix(sim_expected.rstrip() + ' ' + sub)
            else:
                sim_expected = derive_prefix(sim_expected.rstrip() + ' ' + ref_norm)

        if not has_valid_match:
            result_parts.append(m.group(0))
            pos = m.end()
            continue

        out_refs = []
        if '—' in first_text:
            dash_result, dash_prefix = split_dash_ref(first_text, first_period, lookup, derived_prefix, derived_prefix)
            out_refs.append(dash_result)
            if dash_prefix:
                derived_prefix = dash_prefix
        else:
            out_refs.append(f'<ls>{first_text}</ls>{period_suffix(first_period)}')

        expected_prefix = derived_prefix
        for ref_text, ref_period in refs[1:]:
            result, expected_prefix = process_ref(ref_text, ref_period, lookup, derived_prefix, expected_prefix)
            out_refs.extend(result)

        result_parts.append(''.join(out_refs))
        pos = m.end()

    return ''.join(result_parts)


def main():
    print("Reading old version...", file=sys.stderr)
    old_text = get_old_version()
    print(f"  {len(old_text)} chars, {old_text.count(chr(10))} lines", file=sys.stderr)

    print("Building lookup from old version...", file=sys.stderr)
    lookup = build_lookup(old_text)
    print(f"  {len(lookup)} lookup entries", file=sys.stderr)

    print("Reading new version...", file=sys.stderr)
    new_text = get_new_version()
    print(f"  {len(new_text)} chars, {new_text.count(chr(10))} lines", file=sys.stderr)

    print("Processing...", file=sys.stderr)
    result = process_new_text(new_text, lookup)

    out_path = os.path.join(SCRIPT_DIR, 'temp_pwg1.txt')
    print(f"Writing {out_path}...", file=sys.stderr)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(result)

    old_n_count = len(re.findall(r'<ls n="[^"]*">[^<]*</ls>', old_text))
    new_n_count = len(re.findall(r'<ls n="[^"]*">[^<]*</ls>', result))
    print(f"\nOld <ls n=''> count: {old_n_count}", file=sys.stderr)
    print(f"New <ls n=''> count: {new_n_count}", file=sys.stderr)

    tag_count_new = len(re.findall(r'<ls>', new_text))
    tag_count_result = len(re.findall(r'<ls>', result))
    print(f"Total <ls> (without n=) in new:  {tag_count_new - new_n_count}", file=sys.stderr)
    print(f"Total <ls> (without n=) in out:  {tag_count_result - new_n_count}", file=sys.stderr)


if __name__ == '__main__':
    main()
