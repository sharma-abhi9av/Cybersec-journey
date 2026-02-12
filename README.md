# Cybersec Journey

Cybersec Journey is a static cybersecurity blog built for GitHub Pages. It consolidates hands-on writeups, lab notes, and security learning material in a clean, searchable format.

## Features

- **Public blog frontend** with homepage listing and single-post view.
- **Markdown-driven content** loaded from a post manifest (`content/posts/index.json`).
- **Tag and keyword filtering** on the homepage.
- **Owner-restricted publisher route** with GitHub account verification before publishing is enabled.
- **Legacy content preserved** under existing directories (`htb/`, `portswigger/`, etc.).

## Structure

- `index.html` — homepage and post listing
- `post.html` — individual post renderer
- `content/posts/index.json` — post registry
- `content/posts/*.md` — newly published markdown posts
- `admin/index.html` — restricted publisher interface
- `assets/js/app.js` — blog rendering logic
- `assets/js/admin.js` — publisher authentication and publish workflow
- `assets/css/style.css` — shared styles

## Deployment (GitHub Pages)

1. Open repository settings → **Pages**.
2. Set source to **Deploy from a branch**.
3. Select branch `main` and folder `/ (root)`.
4. Save and wait for deployment.

## Publishing workflow

1. Open the publisher route (`/admin/`).
2. Authenticate with a GitHub token.
3. Access is granted only when the authenticated GitHub login matches the configured repository owner.
4. Publish creates a new markdown file in `content/posts/` and updates `content/posts/index.json`.

## Existing writeups

Historical HTB and PortSwigger material remains in place and can continue to be referenced directly.
