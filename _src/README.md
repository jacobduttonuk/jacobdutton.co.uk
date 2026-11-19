# Site source

- `index.src.html` is the master template for the site. Don't edit `index.html` in the repo root by hand: it's generated.
- `build.py` builds `index.html` from the template, swaps in `llms.txt` for the Agent tab, and writes the preview.
- `cv.html` is the source of the two-page CV (render to PDF with Chromium, A4).
- Folders starting with `_` aren't published by GitHub Pages.
- Hosting: GitHub Pages (this repo, branch main). Domain and HTTPS: Cloudflare (nameservers chloe/yadiel). Registrar: easily.uk.
