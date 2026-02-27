# GitHub Template Setup Guide

Convert this SPA into a reusable GitHub template that others can clone with one click.

## Step 1: Create a GitHub Repository

### Option A: Using GitHub Web Interface
1. Go to [GitHub.com](https://github.com)
2. Click **New Repository**
3. Name it: `SPA-Template` (or your preferred name)
4. Description: "Reusable Single Page Application Template - Modular, Class-Based, Vanilla JS"
5. Make it **Public** (required for templates)
6. Initialize with README (optional - we have one)
7. Click **Create Repository**

### Option B: Using Git Commands
```bash
# Navigate to your SPA folder
cd g:\code\SPA

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: SPA template"

# Add remote (replace USERNAME and REPO)
git remote add origin https://github.com/USERNAME/SPA-Template.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Step 2: Mark Repository as Template

### Go to Repository Settings
1. On GitHub, click **Settings** (top right of repo)
2. Scroll down to **Repository Template** section
3. Check the box: ✅ **This is a template repository**
4. Click **Save**

**Now your repo is a template!** Users will see a **"Use this template"** button instead of "Fork".

---

## Step 3: Create Template-Specific Files

Add these files to improve template experience:

### A. `.github/workflows/` or `.gitignore` Updates

Create `.gitignore` to exclude unnecessary files:

```bash
# OS files
.DS_Store
Thumbs.db
*.log

# IDE
.vscode/
.idea/
*.swp

# Dependencies (if you add npm later)
node_modules/
package-lock.json
yarn.lock

# Build output
dist/
build/

# Environment
.env
.env.local
```

### B. `.github/ISSUE_TEMPLATE/` (Optional but Professional)

Create `.github/ISSUE_TEMPLATE/bug_report.md`:
```markdown
---
name: Bug Report
about: Report a bug in the template
---

## Description
Describe the bug clearly.

## Steps to Reproduce
1. Step one
2. Step two
3. ...

## Expected Behavior
What should happen?

## Actual Behavior
What actually happens?

## Environment
- OS: 
- Browser:
- Template Version:
```

### C. `TEMPLATE_USAGE.md` (New File)

Create a quick start guide specifically for new users:

```markdown
# Quick Start - SPA Template

Welcome! This is a reusable SPA template. Here's how to get started:

## 1. Customize Configuration
Edit `config.js`:
```javascript
export const appConfig = {
  auth: {
    type: 'firebase', // or 'custom', 'auth0'
    firebaseConfig: {
      apiKey: 'YOUR_API_KEY',
      // ... your config
    }
  },
  api: {
    baseURL: 'https://your-api.com'
  },
  pages: [
    { path: '/', template: 'home', title: 'Home' },
    // Add your routes here
  ]
};
```

## 2. Add Your Pages
In `apps/bundles/pages.js`, add your templates:
```javascript
templates: {
  myPage: `<div class="page">Your HTML</div>`
}
```

## 3. Customize Styles
- `styles/layout.css` - Edit base styles
- `styles/components.css` - Component styles
- `styles/pages.css` - Page-specific styles

## 4. Run Local Server
```bash
# Python 3
python -m http.server 8000

# Node.js
npx serve

# Then open http://localhost:8000
```

## Documentation
See [README.md](README.md) for full documentation.
```

---

## Step 4: Add Template-Specific Files to Git

```bash
# Add the new files
git add .gitignore TEMPLATE_USAGE.md .github/

# Commit
git commit -m "Add template setup files and documentation"

# Push
git push origin main
```

---

## Step 5: Create GitHub Release (Optional but Recommended)

### From GitHub Web
1. Go to **Releases** (right sidebar)
2. Click **Create a new release**
3. Tag: `v1.0.0`
4. Title: `SPA Template v1.0`
5. Description:
```markdown
## Features
- ✅ Modular class-based architecture
- ✅ Hash-based routing
- ✅ Flexible authentication (Firebase, Custom, Auth0)
- ✅ Built-in utilities (API, DOM, messaging)
- ✅ Responsive design
- ✅ Zero build step - vanilla JS

## Getting Started
Click "Use this template" to get started!

See [README.md](README.md) for full documentation.
```
6. Click **Publish Release**

---

## Step 6: Users Using Your Template

### For End Users:
1. Go to your repo: `https://github.com/USERNAME/SPA-Template`
2. Click green **"Use this template"** button
3. Name their new repo
4. Click **"Create repository from template"**
5. Clone their new repo and start developing!

---

## Optional: Automate with Cookiecutter (Advanced)

For even more automation, use Cookiecutter to prompt for configuration:

### Create `cookiecutter.json`:
```json
{
  "project_name": "My SPA App",
  "project_slug": "{{ cookiecutter.project_name.lower().replace(' ', '_') }}",
  "author_name": "Your Name",
  "auth_type": "firebase",
  "api_baseurl": "https://api.example.com"
}
```

Then users can run:
```bash
cookiecutter https://github.com/USERNAME/SPA-Template
```

---

## Step 7: Promote Your Template

- Add to GitHub Topics: `spa-template`, `vanilla-js`, `reusable-template`
- Update repository **About** section
- Share on:
  - Dev.to
  - Twitter/X
  - Reddit r/webdev
  - Your blog

---

## Managing Template Updates

When you improve the template, users who created repos from it won't auto-update. They need to:

1. Manually pull changes from your original repo
2. Or create PRs to your template

Consider creating a **GitHub Discussion** section for template updates:
- Go to **Settings** → **Features** → Enable **Discussions**
- Users can discuss improvements

---

## Example Repository Structure for Distribution

```
SPA-Template/
├── README.md                    # Main documentation
├── TEMPLATE_USAGE.md           # Quick start for users
├── GITHUB_TEMPLATE_SETUP.md    # (This file)
├── FIREBASE_INTEGRATION.md     # Firebase guide
├── .gitignore
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── index.html
├── config.js
├── apps/
│   ├── main.js
│   └── bundles/
│       ├── router.js
│       ├── auth.js
│       ├── utilities.js
│       └── pages.js
├── pages/
├── styles/
│   ├── layout.css
│   ├── components.css
│   └── pages.css
└── docs/                       # Optional: extended documentation
    ├── ARCHITECTURE.md
    ├── API_REFERENCE.md
    └── EXAMPLES.md
```

---

## Verification Checklist

Before releasing your template:

- [ ] Repository is Public
- [ ] "This is a template repository" is checked
- [ ] README.md is comprehensive
- [ ] config.js has example values with comments
- [ ] .gitignore is present
- [ ] All bundles work without errors
- [ ] Styles are responsive (mobile-friendly)
- [ ] Documentation is clear and complete
- [ ] GitHub Topics are set
- [ ] "Use this template" button appears

**You're all set!** 🎉

