const OWNER = 'sharma-abhi9av';
const REPO = 'Cybersec-journey';
const BRANCH = 'main';

async function fetchIndex() {
  const res = await fetch('./content/posts/index.json', { cache: 'no-store' });
  if (!res.ok) throw new Error('Could not load post index');
  const data = await res.json();
  return data.sort((a, b) => new Date(b.date) - new Date(a.date));
}

function cardTemplate(item) {
  const tags = (item.tags || []).map((t) => `<span class="tag">${t}</span>`).join('');
  return `
    <article class="card">
      <div class="meta">
        <span>${item.date}</span>
        <span>•</span>
        <span>${item.type || 'writeup'}</span>
      </div>
      <h3><a href="post.html?slug=${encodeURIComponent(item.slug)}">${item.title}</a></h3>
      <p>${item.summary || ''}</p>
      <div class="meta">${tags}</div>
    </article>
  `;
}

function filterPosts(posts, keyword) {
  const q = keyword.trim().toLowerCase();
  if (!q) return posts;
  return posts.filter((post) => {
    const haystack = `${post.title} ${post.summary || ''} ${(post.tags || []).join(' ')}`.toLowerCase();
    return haystack.includes(q);
  });
}

async function renderHomepage() {
  const root = document.getElementById('postGrid');
  const search = document.getElementById('search');
  if (!root || !search) return;

  try {
    const posts = await fetchIndex();
    const paint = () => {
      const filtered = filterPosts(posts, search.value);
      root.innerHTML = filtered.map(cardTemplate).join('') || '<p>No posts matched your search.</p>';
    };
    paint();
    search.addEventListener('input', paint);
  } catch (err) {
    root.innerHTML = `<p>Failed to load posts: ${err.message}</p>`;
  }
}

async function renderPostPage() {
  const article = document.getElementById('article');
  if (!article) return;

  const slug = new URLSearchParams(window.location.search).get('slug');
  if (!slug) {
    article.innerHTML = '<p>Missing slug in URL.</p>';
    return;
  }

  try {
    const posts = await fetchIndex();
    const post = posts.find((item) => item.slug === slug);
    if (!post) {
      article.innerHTML = '<p>Post not found.</p>';
      return;
    }

    const mdRes = await fetch(post.path, { cache: 'no-store' });
    const markdown = await mdRes.text();
    const html = marked.parse(markdown);
    document.title = `${post.title} | Cybersec Journey`;
    article.innerHTML = `
      <h1>${post.title}</h1>
      <div class="meta">
        <span>${post.date}</span>
        <span>•</span>
        <span>${post.type || 'writeup'}</span>
      </div>
      <hr style="border-color: var(--border); border-style: solid; margin: 1rem 0;" />
      ${html}
    `;
  } catch (err) {
    article.innerHTML = `<p>Error loading post: ${err.message}</p>`;
  }
}

renderHomepage();
renderPostPage();

window.blogRepoConfig = { OWNER, REPO, BRANCH };
