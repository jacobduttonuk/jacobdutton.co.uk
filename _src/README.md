# Site source

- `index.src.html` is the master template for the site. Don't edit `index.html` in the repo root by hand: it's generated.
- `build.py` builds `index.html` from the template, swaps in `llms.txt` for the Agent tab, and writes the preview.
- This folder is publicly readable (the repo has .nojekyll), so nothing private goes in here. The CV source is kept outside the repo.
- Hosting: GitHub Pages (this repo, branch main). Domain and HTTPS: Cloudflare (nameservers chloe/yadiel). Registrar: easily.uk.
