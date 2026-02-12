const statusEl = document.getElementById('status');
const form = document.getElementById('publisherForm');
const tokenInput = document.getElementById('token');
const saveTokenBtn = document.getElementById('saveToken');
const clearTokenBtn = document.getElementById('clearToken');
const verifyTokenBtn = document.getElementById('verifyToken');
const accessDeniedEl = document.getElementById('accessDenied');

const { OWNER, REPO, BRANCH } = window.blogRepoConfig;
const INDEX_PATH = 'content/posts/index.json';
const TOKEN_KEY = 'blog_publish_token';
let authenticatedOwner = false;

function setStatus(message, isError = false) {
  statusEl.textContent = message;
  statusEl.style.borderColor = isError ? 'rgba(255,95,95,0.6)' : 'rgba(77,163,255,0.35)';
  statusEl.style.background = isError ? 'rgba(255,95,95,0.12)' : 'rgba(77,163,255,0.12)';
}

function setAccessState(isAuthorized) {
  authenticatedOwner = isAuthorized;
  form.style.display = isAuthorized ? 'grid' : 'none';
  accessDeniedEl.style.display = isAuthorized ? 'none' : 'block';
}

function slugify(value) {
  return value
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9\s-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-');
}

function getToken() {
  return localStorage.getItem(TOKEN_KEY) || '';
}

function saveToken() {
  const token = tokenInput.value.trim();
  if (!token) {
    setStatus('Provide a valid token before saving.', true);
    return;
  }

  localStorage.setItem(TOKEN_KEY, token);
  setStatus('Token saved in browser storage. Use Sign In to verify access.');
}

function clearToken() {
  localStorage.removeItem(TOKEN_KEY);
  tokenInput.value = '';
  setAccessState(false);
  setStatus('Signed out.', false);
}

async function githubRequest(path, token, method = 'GET', body) {
  const response = await fetch(`https://api.github.com/repos/${OWNER}/${REPO}/contents/${path}`, {
    method,
    headers: {
      Accept: 'application/vnd.github+json',
      Authorization: `Bearer ${token}`,
      'X-GitHub-Api-Version': '2022-11-28'
    },
    body: body ? JSON.stringify(body) : undefined
  });

  const payload = await response.json();
  if (!response.ok) {
    throw new Error(payload.message || `GitHub API error (${response.status})`);
  }

  return payload;
}

async function fetchAuthenticatedUser(token) {
  const response = await fetch('https://api.github.com/user', {
    headers: {
      Accept: 'application/vnd.github+json',
      Authorization: `Bearer ${token}`,
      'X-GitHub-Api-Version': '2022-11-28'
    }
  });

  const payload = await response.json();
  if (!response.ok) {
    throw new Error(payload.message || 'Authentication failed.');
  }

  return payload;
}

function decodeBase64(content) {
  return decodeURIComponent(
    atob(content.replace(/\n/g, ''))
      .split('')
      .map((c) => `%${`00${c.charCodeAt(0).toString(16)}`.slice(-2)}`)
      .join('')
  );
}

function encodeBase64(content) {
  return btoa(unescape(encodeURIComponent(content)));
}

async function verifyOwnerAccess() {
  const token = tokenInput.value.trim() || getToken();
  if (!token) {
    setAccessState(false);
    setStatus('Authentication required.', true);
    return;
  }

  try {
    setStatus('Verifying GitHub account...');
    const user = await fetchAuthenticatedUser(token);

    if ((user.login || '').toLowerCase() !== OWNER.toLowerCase()) {
      setAccessState(false);
      setStatus('Access denied. This account is not authorized for publishing.', true);
      return;
    }

    setAccessState(true);
    setStatus(`Authenticated as ${user.login}. Publishing enabled.`);
  } catch (error) {
    setAccessState(false);
    setStatus(`Authentication failed: ${error.message}`, true);
  }
}

async function publishPost(event) {
  event.preventDefault();
  const token = getToken() || tokenInput.value.trim();
  if (!token) {
    setStatus('Authentication required.', true);
    return;
  }

  if (!authenticatedOwner) {
    setStatus('Access denied. Verify owner account first.', true);
    return;
  }

  const formData = new FormData(form);
  const title = formData.get('title').toString().trim();
  const summary = formData.get('summary').toString().trim();
  const date = formData.get('date').toString().trim();
  const tags = formData
    .get('tags')
    .toString()
    .split(',')
    .map((tag) => tag.trim())
    .filter(Boolean);
  const markdown = formData.get('markdown').toString().trim();
  const type = formData.get('type').toString().trim() || 'writeup';

  if (!title || !date || !markdown) {
    setStatus('Title, date, and markdown body are required.', true);
    return;
  }

  const slug = slugify(title);
  const postPath = `content/posts/${slug}.md`;

  try {
    setStatus('Publishing post...');
    const indexFile = await githubRequest(INDEX_PATH, token);
    const indexJson = JSON.parse(decodeBase64(indexFile.content));

    if (indexJson.some((item) => item.slug === slug)) {
      throw new Error(`A post with slug "${slug}" already exists. Change the title.`);
    }

    const record = {
      slug,
      title,
      summary,
      date,
      tags,
      type,
      path: `./${postPath}`
    };

    const newIndex = [record, ...indexJson];

    await githubRequest(postPath, token, 'PUT', {
      message: `feat(blog): publish ${slug}`,
      content: encodeBase64(markdown),
      branch: BRANCH
    });

    await githubRequest(INDEX_PATH, token, 'PUT', {
      message: `chore(blog): update index for ${slug}`,
      content: encodeBase64(`${JSON.stringify(newIndex, null, 2)}\n`),
      sha: indexFile.sha,
      branch: BRANCH
    });

    setStatus(`Post "${title}" published successfully.`);
    form.reset();
  } catch (error) {
    setStatus(`Publish failed: ${error.message}`, true);
  }
}

tokenInput.value = getToken();
setAccessState(false);
saveTokenBtn.addEventListener('click', saveToken);
clearTokenBtn.addEventListener('click', clearToken);
verifyTokenBtn.addEventListener('click', verifyOwnerAccess);
form.addEventListener('submit', publishPost);

if (getToken()) {
  verifyOwnerAccess();
}
