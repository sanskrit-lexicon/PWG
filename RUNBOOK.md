# Repo Documentation & Issue Cleanup Runbook

This file is an instruction set for Claude Code operating **autonomously** on a Sanskrit Lexicon repository. It covers the complete documentation and issue-organisation pass that was first applied to the PWG repo in 2026.

---

## Autonomy Rules

- Execute all steps below **without asking for user confirmation** unless the step is marked **[ASK]**.
- Batch all **[ASK]** items and ask at most once per hour.
- All GitHub API calls, file edits, git commits, and pushes may be executed freely.
- If a step fails transiently (5xx, timeout), retry once before continuing.
- Prefer batching API calls with loops over one-by-one manual steps.

---

## 0. Setup

Set these variables at the start and use them throughout:

```
ORG=sanskrit-lexicon
REPO=<target repo name, e.g. MWS>
```

Verify the repo is accessible:

```sh
gh api repos/$ORG/$REPO --jq '{name,description,has_issues}'
```

---

## Phase 1 — Audit current state

Fetch all issues (open + closed):

```sh
gh api "repos/$ORG/$REPO/issues?state=all&per_page=100&page=1" \
  --jq '[.[] | {n:.number,state:.state,labels:[.labels[].name],milestone:.milestone.title}]'
# repeat for page=2, page=3 … until an empty array is returned
```

For each issue, record:
- Has a **type label** (see Phase 3 for the list)
- Has a **severity label** (`minor`, `medium`, `hard`)
- Has a **milestone** (one of the four standard ones — see Phase 4)
- Is in a **project** (see Phase 6)

Also fetch existing labels and milestones:

```sh
gh api repos/$ORG/$REPO/labels --jq '[.[].name]'
gh api repos/$ORG/$REPO/milestones --jq '[.[] | {n:.number,title}]'
```

**[ASK]** Are there any issue numbers that should be skipped throughout (admin noise, flood-control, meta issues)? For PWG the skip list was `{89, 99}`. Identify equivalents for the target repo.

---

## Phase 2 — Create labels

Create any of the following that are missing. Existing labels with the same name must not be duplicated.

### Type labels — color `#0075ca`

```sh
for label in link-target link-splitting markup text-correction \
             content-enhancement encoding scan-quality bug question; do
  gh api repos/$ORG/$REPO/labels -X POST -f name="$label" -f color="0075ca" 2>/dev/null || true
done
```

### Severity labels

```sh
gh api repos/$ORG/$REPO/labels -X POST -f name="minor"  -f color="e4e669" 2>/dev/null || true
gh api repos/$ORG/$REPO/labels -X POST -f name="medium" -f color="fbca04" 2>/dev/null || true
gh api repos/$ORG/$REPO/labels -X POST -f name="hard"   -f color="d93f0b" 2>/dev/null || true
```

---

## Phase 3 — Type label assignment rules

Every non-skipped issue must carry **exactly one** type label (two labels are acceptable when an issue genuinely spans both areas).

| Label | When to apply |
|---|---|
| `link-target` | Building a click-through from a `<ls>` abbreviation to scanned PDF pages: researching the source, constructing an index, installing links across all related dictionaries |
| `link-splitting` | Splitting combined `SOURCE N,N` refs that resolve to a single target into individual per-page links |
| `markup` | Normalising XML tag content or structure (`<ls>`, `<lex>`, and similar) |
| `text-correction` | Corrections to German definitions or Sanskrit headwords in the dictionary text |
| `content-enhancement` | New material, display upgrades, or structural additions that go beyond correction |
| `encoding` | SLP1/AS/IAST transcoding, character rendering (Greek, accents), hyphen/dash normalisation |
| `scan-quality` | Replacing blurry, skewed, or missing scan pages with clearer images |
| `bug` | Broken links, XML structure errors, broken download files, page-number bugs |
| `question` | Scholarly or editorial questions requiring research before any code change |

To assign a type label:

```sh
gh api repos/$ORG/$REPO/issues/$N/labels -X POST -f labels[]="<type>"
```

---

## Phase 4 — Severity label assignment rules

Every non-skipped issue must carry **exactly one** severity label.

| Label | When to apply |
|---|---|
| `minor` | Targeted, self-contained fix — a handful of lines or a single file. Typical for: markup, encoding, bug, question, scan-quality |
| `medium` | Standard unit of work — one link-target index, a batch of markup corrections, a moderate content addition. Typical for: link-target, link-splitting, content-enhancement |
| `hard` | Large, complex effort spanning many sources, files, or dictionaries |

Default heuristics when in doubt:
- `link-target` → `medium`
- `link-splitting` (single source) → `medium`
- `link-splitting` (10+ sources in one issue) → `hard`
- `markup`, `encoding`, `bug`, `question`, `scan-quality` → `minor`
- `content-enhancement` → `medium` (use `hard` only for very large additions)
- `text-correction` → `minor`

---

## Phase 5 — Milestone setup

Create the four standard milestones if they do not already exist:

```sh
for title in "Dictionary to Book" "Digitization Quality" "Structured Data" "Major Enhancements"; do
  gh api repos/$ORG/$REPO/milestones -X POST -f title="$title" 2>/dev/null || true
done
```

Note the assigned milestone numbers (`gh api repos/$ORG/$REPO/milestones --jq '[.[] | {n:.number,title}]'`) — they may not be 1–4 if the repo already had milestones.

### Milestone assignment by type label

| Milestone | Type labels that belong here |
|---|---|
| Dictionary to Book | `link-target`, `link-splitting` |
| Digitization Quality | `scan-quality`, `encoding`, `bug`, `text-correction` |
| Structured Data | `markup`, `question` |
| Major Enhancements | `content-enhancement` |

For issues with two type labels, assign to the milestone of the **dominant** type (the one that describes the primary work). If genuinely unclear, **[ASK]**.

To assign a milestone:

```sh
gh api repos/$ORG/$REPO/issues/$N -X PATCH -f milestone=<milestone_number>
```

---

## Phase 6 — GitHub Projects setup

Four org-level Projects V2 (kanban boards) mirror the four milestones. Check if they already exist:

```sh
gh api graphql -f query='{ organization(login: "sanskrit-lexicon") {
  projectsV2(first: 20) { nodes { id number title } } } }'
```

If the four projects do not exist, **[ASK]** the user to create them (project creation requires owner permissions that may not be available via API). Provide the user with the four names: **Dictionary to Book**, **Digitization Quality**, **Structured Data**, **Major Enhancements**.

Once project IDs are known, add every issue to the project that matches its milestone:

```python
# Pseudocode — adapt to Python with subprocess + gh api graphql
for issue_number, milestone_title in all_issues:
    project_id = milestone_to_project_id[milestone_title]
    node_id = get_issue_node_id(issue_number)
    graphql_mutation_add_item(project_id, node_id)
```

GraphQL mutation:

```graphql
mutation {
  addProjectV2ItemById(input: {
    projectId: "<project_node_id>"
    contentId: "<issue_node_id>"
  }) { item { id } }
}
```

Fetch issue node IDs in bulk (100 per page):

```sh
gh api "repos/$ORG/$REPO/issues?state=all&per_page=100&page=N" \
  --jq '[.[] | {n:.number, id:.node_id}]'
```

---

## Phase 7 — Verification

Re-fetch all issues and confirm:

```python
assert missing_type_labels   == 0
assert missing_severity      == 0
assert missing_milestones    == 0
assert not_in_any_project    == 0
assert in_multiple_projects  == 0
assert wrong_project         == 0   # project matches milestone
```

Fix any gaps found before proceeding to documentation.

---

## Phase 8 — CLAUDE.md

Create or update `CLAUDE.md` in the repository root. Adapt the PWG version at `https://github.com/sanskrit-lexicon/PWG/blob/master/CLAUDE.md` to the target repo:

- Replace PWG-specific commands, directory names, and pipeline descriptions with the target repo's equivalents.
- Keep the **GitHub Issue Conventions** section verbatim (milestones, type labels, severity labels are the same across all Sanskrit Lexicon repos).
- Fetch the target repo's directory structure and key scripts to fill in the architecture section.

Commit: `CLAUDE.md: initial guidance for Claude Code`

---

## Phase 9 — README.md

Create or update `README.md`. The structure should follow the PWG readme as a template. Adapt each section:

### Required sections (in order)

1. **Title + one-paragraph description** — what the repo contains, its place in the Sanskrit Lexicon project, primary input file and sibling repos.

2. **Directories table** — one row per top-level directory with a short description. Derive from `ls` of the repo.

3. **How It Works** — correction workflow (change files + `updateByLine.py` if applicable), issue workflow, link-target workflow with Mermaid flowchart:

```mermaid
flowchart LR
    PDF["Source PDF"]
    IDX["index file\nTSV: section → page"]
    JS["index.js"]
    DICTS["<dict> · PW · MW\n..."]
    PDF -->|"research"| IDX
    IDX -->|"make_js_index.py\nvalidate + build"| JS
    JS -->|"lsfix2.py\ninstall links"| DICTS
```

4. **Project Timeline** — table of `Period | Work`, one row per year of activity. Derive from git log and issue dates.

5. **Projects & Milestones** — table with live counts fetched from the API, plus two Mermaid pie charts:

```mermaid
pie title Closed issues by milestone
    "Dictionary to Book" : <N>
    "Digitization Quality" : <N>
    "Structured Data" : <N>
    "Major Enhancements" : <N>
```

```mermaid
pie title Open issues by milestone
    "Dictionary to Book" : <N>
    "Digitization Quality" : <N>
    "Structured Data" : <N>
    "Major Enhancements" : <N>
```

6. **Issue Typology** — two subsections (Solved / Open), each a table with columns Type | Description | Examples. Include live counts per type in each description. Add a Mermaid pie chart of all issues by type:

```mermaid
pie title Issues by type label (some issues carry two types)
    "link-target" : <N>
    ...
```

7. **Labels** — copy verbatim from the PWG readme Labels section (type and severity tables are the same across repos).

8. **Contributors** — list contributors with GitHub handles and roles. Derive from git log authors and issue participants.

### Counts

All counts in the readme must be fetched live from the API immediately before the final commit — do not hard-code stale numbers.

### Mermaid validation

Before committing, validate each Mermaid block via the GitHub markdown render API:

```sh
gh api markdown -X POST \
  -f text="$(cat <<'EOF'
\`\`\`mermaid
<diagram content>
\`\`\`
EOF
)" -f mode="markdown"
```

A rendered diagram is confirmed when the response contains `highlight-source-mermaid` **with syntax-highlighting span classes** (`pl-k`, `pl-ent`, `pl-s`, etc.) on the diagram keywords. Plain unstyled text inside the block means the diagram type is not supported — replace it with a supported type (`pie`, `flowchart`, `graph`, `sequenceDiagram`, `gantt`). Do **not** use `xychart-beta` — it is not supported on GitHub.

---

## Phase 10 — Final commit and push

```sh
git add README.md CLAUDE.md
git commit -m "docs: initial README and CLAUDE.md; full issue triage (labels, milestones, projects)"
git push
```

---

## Checklist

- [ ] All issues have a type label
- [ ] All issues have a severity label
- [ ] All issues have a milestone
- [ ] All issues are in exactly one project
- [ ] Each issue's project matches its milestone
- [ ] `CLAUDE.md` committed
- [ ] `README.md` committed with live counts
- [ ] All Mermaid diagrams validated via GitHub API
- [ ] Changes pushed to `origin/master`
