# Cybersec Journey

A GitHub Pages-ready cybersecurity blog for writeups, labs, and security notes.

## What's included

- `index.html` + `post.html`: clean blog frontend.
- `content/posts/index.json`: post manifest used by homepage and post page.
- `admin/index.html`: publisher screen for adding markdown posts.

Your previous writeups and notes remain untouched under `htb/`, `portswigger/`, and other folders.

## Deploy to GitHub Pages

1. Open repo settings → **Pages**.
2. Set source to **Deploy from a branch**.
3. Select branch `main` and folder `/ (root)`.
4. Save.

GitHub Pages will serve:
- Home: `https://<username>.github.io/Cybersec-journey/`

## Publish posts from browser UI

1. Open the publisher route.
2. Paste a GitHub token with repository `Contents: Read and write` permission.
3. Fill title/date/tags/summary/markdown and publish.

The publisher will:
- create `content/posts/<slug>.md`
- update `content/posts/index.json`

## Legacy content

`/htb` still tracks Hack The Box progress and writeups exactly as before.
