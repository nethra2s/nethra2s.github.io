# Build tools for nethra2s.com (not published)

Folders starting with "_" are not published by GitHub Pages.

- `pages.py`: English + Tamil content for nine service pages (plus `NAMES` and `CARD` maps)
- `ai_strategy_content.py`: content for the AI Strategy & Roadmap page
- `make_service_page.py`: builds a service page from a content module, reusing header, styles, footer and core script from `index.html`

Regenerate a page (run from the repo root, after writing a content module from `pages.py`):

    python3 _build/make_service_page.py <content.py> index.html <slug>/index.html "../" "../"

Note: `make_service_page.py` imports `NAMES` from `pages.py`; adjust `sys.path` in the script if you move it (it currently points at /home/claude/build).

Versioning: bump the version string (e.g. `2026-10-20 v6`) in index.html (meta tag + footer) for every change, then regenerate service pages so they carry the same version.
