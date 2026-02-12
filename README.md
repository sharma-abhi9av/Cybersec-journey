# Cybersec Journey

This repository now includes a GitHub Pages-ready cybersecurity blog frontend and an owner-only publish UI.

## What's included

- `index.html` + `post.html`: clean blog experience inspired by modern security blogs.
- `content/posts/index.json`: post manifest used by the homepage.
- `admin/index.html`: owner control panel to publish markdown directly to this repository from browser UI.
- `assets/js/admin.js`: GitHub API publishing workflow.

Your previous writeups and notes remain untouched under `htb/`, `portswigger/`, and other folders.

## Deploy to GitHub Pages

1. Open repo settings → **Pages**.
2. Set source to **Deploy from a branch**.
3. Select branch `main` and folder `/ (root)`.
4. Save.

GitHub Pages will serve:
- Home: `https://<username>.github.io/Cybersec-journey/`
- Admin: `https://<username>.github.io/Cybersec-journey/admin/`

## Publish posts from UI (no local code editing)

1. Visit `/admin/`.
2. Create a **fine-grained PAT** on GitHub with repository `Contents: Read and write` permission.
3. Paste token, click **Save token**.
4. Fill title/date/tags/summary/markdown and click **Publish Post**.

The admin panel will:
- create `content/posts/<slug>.md`
- update `content/posts/index.json`

## Legacy content

`/htb` still tracks Hack The Box progress and writeups exactly as before.
