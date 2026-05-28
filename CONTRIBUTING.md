# Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

All issues use standardized labels (type, severity, milestone).

## GitHub Pages / Jekyll Liquid gotcha

GitHub Pages renders this repo's Markdown through Jekyll. Jekyll's Liquid
templating engine treats two CDSL markup conventions as template syntax:

- `{%…%}` — the italic-span marker; collides with Liquid tag syntax.
- `{{…}}` — the correction-record format `{{old -> new || date | author | URL |}}`;
  collides with Liquid variable interpolation.

A `.md` file containing either marker — even inside a fenced code block — breaks
the Pages build. The fix is to wrap the whole file in `{% raw %}` and the matching
closing tag. See [`pwgissues/issue174/comment_markup_fix.md`](pwgissues/issue174/comment_markup_fix.md)
for a working example, and MWS PRs
[#198](https://github.com/sanskrit-lexicon/MWS/pull/198),
[#200](https://github.com/sanskrit-lexicon/MWS/pull/200),
[#201](https://github.com/sanskrit-lexicon/MWS/pull/201)
for the full org-wide precedent.

When adding any new `.md` that quotes `<L>` records, italic markers, or sample
entry text — wrap it.