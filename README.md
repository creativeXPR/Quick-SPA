# SPA Template - Comprehensive Reusable Single Page Application

A production-ready, modular, class-based SPA template designed for maximum reusability. Built with vanilla JavaScript ES6 modules - no frameworks, no build process, no dependencies. Just clean, organized, scalable code.

---

## 📁 Project Structure

```
SPA/
├── serve.json                      # Local SPA routing config (npx serve)
├── _redirects                      # Netlify SPA routing
├── netlify.toml                    # Netlify config
├── apps/                           # Application logic
│   ├── main.js                    # App orchestrator
│   └── bundles/                   # Modular classes
│       ├── config.js              # Configuration
│       ├── router.js              # Routing engine
│       ├── auth.js                # Authentication
│       ├── pages.js               # Page templates
│       ├── utilities.js           # Helper functions
│       └── firebase-service.js    # Firebase operations
├── styles/                         # CSS styles
│   ├── layout.css                 # Base structural styles
│   ├── components.css             # Reusable components
│   └── pages.css                  # Page-specific styles
├── pages/                          # Page templates and entry point
│   └── index.html                 # SPA entry point
├── docs/                           # Documentation
│   ├── TEMPLATE_USAGE.md          # Quick start
│   ├── FIREBASE_INTEGRATION.md    # Firebase guide
│   ├── GITHUB_TEMPLATE_SETUP.md   # GitHub template
│   └── UPDATE_SUMMARY.md          # What's new
├── .gitignore                      # Git ignore rules
└── README.md                       # This file

```

**Key Points:**
- `pages/index.html` is the SPA entry point (kept in pages folder for organization)
- `serve.json` handles local routing: unmapped routes redirect to `pages/index.html`
- `_redirects` and `netlify.toml` handle production routing on Netlify
- SPA routing works both locally and in production!

---

## ✨ Latest Update: Smart SPA Routing Configuration

### **What Changed**
Previous approach: Moving `index.html` to root required restructuring multiple files and paths.

**New approach (cleaner & more maintainable):**
- ✅ `pages/index.html` stays organized in pages folder
- ✅ `serve.json` intelligently routes unmatched requests to `pages/index.html` locally
- ✅ `_redirects` and `netlify.toml` do the same for Netlify production
- ✅ Relative paths (`../apps/main.js`, `../styles/`) work correctly from pages folder

### **How It Works**

1. **Local Development (`npx serve`)**
   ```json
   // serve.json automatically redirects:
   GET /nonexistent-file → serves pages/index.html
   // App loads, router checks #hash, displays correct page
   ```

2. **Production (Netlify)**
   ```
   // _redirects automatically redirects:
   /* /pages/index.html 200
   // Same SPA behavior as local!
   ```

### **Why This Is Better**
- **Cleaner structure**: Entry point organized in pages/ folder
- **Explicit routing**: Easy to see where index.html lives
- **Configuration-driven**: Routing rules in dedicated config files
- **Consistent approach**: Both local and production use the same pattern
- **No path gymnastics**: Relative paths work intuitively

---

## 🎯 What Does Each Component Do?

### **1. `pages/index.html`** - Application Entry Point
**Purpose**: The single HTML file that loads your entire application.

**What it does**:
- Defines the basic HTML structure (head, body)
- Links CSS stylesheets from parent: `<link rel="stylesheet" href="../styles/layout.css">`
- Creates containers for dynamic content (`#app-root`, `#page-container`, `#message-box`)
- Loads the main JavaScript module: `<script type="module" src="../apps/main.js"></script>`

**Why it matters**: This is the only HTML file you need. All pages are rendered dynamically inside it. When routing redirects unmatched URLs to this file, the router detects the hash and loads the correct page.

---

### **2. `apps/main.js`** - Application Orchestrator
**Purpose**: The central hub that initializes and connects all modules.

**What it does**:
- Creates instances of Router, Auth, Utilities, and Pages classes
- Manages global app state (user, data, loading status)
- Sets up event delegation for forms and buttons
- Listens to route changes and updates the UI
- Handles login/logout workflows
- Coordinates communication between all modules

**Why it matters**: This is the "CEO" of your app - it orchestrates everything. Accessible globally as `window.app`.

**Key Methods**:
```javascript
window.app.setState({...})        // Update app state
window.app.getState()             // Get current state
window.app.handleLoginSubmit()    // Process login
window.app.handleLogout()         // Process logout
window.app.fetchUserData()        // Fetch from API
```

---

### **3. `apps/bundles/config.js`** - Configuration Center
**Purpose**: Single source of truth for all app settings.

**What it does**:
- Stores Firebase/Auth0/Custom authentication credentials
- Defines API base URL and endpoints
- Maps routes to page templates
- Specifies which routes require authentication
- Sets app-wide settings (name, containers, etc.)

**Why it matters**: Change settings in ONE place instead of hunting through code. Makes your app highly adaptable.

**Configuration Sections**:
```javascript
auth: {...}        // Authentication provider settings
api: {...}         // API endpoints and base URL
pages: [...]       // Route definitions (path, template, auth requirement)
app: {...}         // General app settings
```

---

### **4. `apps/bundles/router.js`** - Navigation Manager
**Purpose**: Handles client-side routing without page reloads.

**What it does**:
- Uses pathname-based routing (`/dashboard`, `/profile`) - clean URLs
- Detects URL changes via `popstate` event and History API
- Notifies listeners when routes change
- Tracks current and previous paths
- Validates if routes exist
- Provides navigation methods

**Why it matters**: Enables SPA behavior - navigate between pages without full page refresh, maintaining app state.

**Key Methods**:
```javascript
router.navigate('/path')           // Navigate to a route
router.getCurrentPath()            // Get current path (/dashboard)
router.getPreviousPath()           // Get previous path
router.onChange(callback)          // Listen to route changes
router.getCurrentPageConfig()      // Get route configuration
router.routeExists(path)           // Check if route is defined
```

**How it works**:
1. User clicks `<a href="/dashboard">Dashboard</a>`
2. Browser pathname changes to `/dashboard`
3. Router detects change, extracts `/dashboard`
4. Router notifies `main.js`
5. `main.js` tells `pages.js` to render dashboard template
6. Page appears without reload!

---

### **5. `apps/bundles/auth.js`** - Authentication Handler
**Purpose**: Manages user authentication with flexible provider support.

**What it does**:
- Initializes authentication (Firebase, Auth0, Custom, etc.)
- Handles login, logout, and registration
- Maintains user session (localStorage persistence)
- Checks authentication status
- Provides access to Firebase/Auth0 instances
- Manages user state across page reloads

**Why it matters**: Provides a consistent auth API regardless of provider. Switch from Firebase to Auth0 by just changing config.

**Key Methods**:
```javascript
auth.login(email, password)        // Login user
auth.logout()                      // Logout user
auth.register(userData)            // Register new user
auth.checkAuth()                   // true/false if authenticated
auth.getUser()                     // Get current user object
auth.loadUserSession()             // Restore session from localStorage
auth.saveUserSession()             // Save session to localStorage
auth.resetPassword(email)          // Send password reset (Firebase)
auth.getFirestore()                // Get Firestore instance
auth.getDatabase()                 // Get Realtime Database instance
auth.getStorage()                  // Get Firebase Storage instance
```

**How it works** (Adapter Pattern):
```javascript
// In config.js: set auth type
auth: { type: 'firebase', firebaseConfig: {...} }

// Auth class adapts to the provider
initializeAuth() {
  switch(this.authType) {
    case 'firebase': this.initializeFirebase(); break;
    case 'auth0': this.initializeAuth0(); break;
    case 'custom': this.initializeCustom(); break;
  }
}
```

---

### **6. `apps/bundles/pages.js`** - Template & Page Manager
**Purpose**: Stores page templates and handles page rendering.

**What it does**:
- Stores HTML templates for all pages (home, login, dashboard, etc.)
- Renders templates into the DOM based on route
- Checks authentication requirements before rendering
- Updates page title dynamically
- Initializes page-specific JavaScript (event listeners, etc.)
- Shows 404 page for invalid routes

**Why it matters**: Centralizes all page templates. Add a new page by just adding a template here - no new HTML files needed.

**Key Methods**:
```javascript
pages.renderPage(path, authInstance)  // Render page for path
pages.getTemplate(name)               // Get HTML template
pages.initializePage(name)            // Run page-specific logic
pages.getCurrentPage()                // Get current page name
```

**Template Structure**:
```javascript
templates: {
  home: `<div class="page page-home">
    <h1>Welcome</h1>
    <a href="/dashboard">Dashboard</a>
  </div>`,
  
  login: `<div class="page page-login">
    <form id="login-form">...</form>
  </div>`,
  
  dashboard: `<div class="page page-dashboard">
    <h1>Dashboard</h1>
    <p id="user-info"></p>
  </div>`
}
```

**Page Lifecycle**:
1. Router detects route change → `/dashboard`
2. `main.js` calls `pages.renderPage('/dashboard', auth)`
3. Pages checks if route requires auth
4. If not authenticated → redirect to `/login`
5. If authenticated → get template, inject into `#page-container`
6. Call `initializePage('dashboard')` for setup
7. Page appears with event listeners ready!

---

### **7. `apps/bundles/utilities.js`** - Helper Functions Library
**Purpose**: Provides reusable utilities for common tasks.

**What it does**:
- **API Calls**: GET, POST, PUT, DELETE with error handling
- **DOM Manipulation**: Query, set HTML, add classes, event listeners
- **Messaging**: Show success/error/info notifications
- **Data Formatting**: JSON parse/stringify safely
- **Performance**: Debounce and throttle functions
- **Utilities**: Generate unique IDs

**Why it matters**: Eliminates code duplication. Use these helpers instead of writing fetch/DOM code repeatedly.

**API Methods**:
```javascript
utilities.get(endpoint, options)       // GET request
utilities.post(endpoint, data, options) // POST request
utilities.put(endpoint, data, options)  // PUT request
utilities.delete(endpoint, options)     // DELETE request
utilities.handleResponse(response)      // Process API response
```

**DOM Methods**:
```javascript
utilities.querySelector(selector)      // Get element
utilities.querySelectorAll(selector)   // Get all elements
utilities.setHTML(selector, html)      // Set innerHTML
utilities.addEventListener(selector, event, callback)
utilities.addClass(selector, className)
utilities.removeClass(selector, className)
```

**Messaging Methods**:
```javascript
utilities.showSuccess(message, duration)  // Green success message
utilities.showError(message, duration)    // Red error message
utilities.showInfo(message, duration)     // Blue info message
utilities.showMessage(message, type, duration) // Generic message
```

**Data & Performance Methods**:
```javascript
utilities.parseJSON(json)              // Safe JSON parsing
utilities.stringifyJSON(obj)           // Format JSON
utilities.debounce(func, delay)        // Debounce function (search input)
utilities.throttle(func, delay)        // Throttle function (scroll events)
utilities.generateId()                 // Unique ID generator
```

**Example Usage**:
```javascript
// API call
const users = await window.app.utilities.get('/api/users');

// Show notification
window.app.utilities.showSuccess('User created!');

// DOM manipulation
window.app.utilities.setHTML('#user-info', `<p>Welcome ${user.name}</p>`);

// Debounce search
const searchInput = document.querySelector('#search');
searchInput.addEventListener('input', 
  window.app.utilities.debounce((e) => {
    performSearch(e.target.value);
  }, 300)
);
```

---

### **8. `apps/bundles/firebase-service.js`** - Firebase Database Helper
**Purpose**: Simplifies Firebase Firestore operations with convenient methods.

**What it does**:
- Provides CRUD operations for Firestore (Create, Read, Update, Delete)
- Handles file uploads/downloads with Firebase Storage
- Sets up real-time listeners for data changes
- Adds timestamps and user IDs automatically
- Provides consistent error handling

**Why it matters**: Abstracts complex Firebase SDK calls into simple methods. Write `firebase.addDocument()` instead of 20 lines of Firestore code.

**Key Methods**:
```javascript
firebase.addDocument(collection, data)      // Create document
firebase.getDocument(collection, id)        // Read one document
firebase.getCollection(collection, where, orderBy, limit) // Read collection
firebase.updateDocument(collection, id, data) // Update document
firebase.deleteDocument(collection, id)     // Delete document
firebase.uploadFile(path, file)             // Upload to Storage
firebase.deleteFile(path)                   // Delete from Storage
firebase.listenToCollection(collection, callback, where) // Real-time listener
```

**Example Usage**:
```javascript
// Create a post
const result = await window.app.firebase.addDocument('posts', {
  title: 'My Post',
  content: 'Hello World',
  published: true
});
// Auto-adds: userId, createdAt timestamp

// Get user's posts
const posts = await window.app.firebase.getCollection('posts', 
  { field: 'userId', operator: '==', value: currentUser.id },
  { field: 'createdAt', direction: 'desc' },
  10
);

// Update post
await window.app.firebase.updateDocument('posts', postId, {
  title: 'Updated Title'
});
// Auto-adds: updatedAt timestamp

// Real-time listener
const unsubscribe = window.app.firebase.listenToCollection('posts', 
  (posts) => {
    console.log('Posts updated:', posts);
    // Update UI with new data
  },
  { field: 'published', operator: '==', value: true }
);
// Stop listening: unsubscribe();
```

---

### **9. `styles/layout.css`** - Base Structural Styles
**Purpose**: Defines the foundation layout and structure.

**What it contains**:
- CSS reset (margin, padding, box-sizing)
- Base typography (fonts, line-height, colors)
- Layout containers (#app-root, #page-container)
- Header & navigation styles
- Responsive breakpoints
- Page transition animations

**Why it matters**: Establishes consistent spacing, layout, and responsive behavior across the entire app.

---

### **10. `styles/components.css`** - Reusable UI Components
**Purpose**: Styles for reusable UI elements.

**What it contains**:
- Buttons (primary, danger, success, sizes)
- Form inputs (text, email, password, textarea, select)
- Cards (header, body, footer)
- Alerts (success, error, info, warning)
- Focus states and transitions

**Why it matters**: Consistent UI components. Use `.btn`, `.card`, `.alert-success` anywhere without rewriting CSS.

---

### **11. `styles/pages.css`** - Page-Specific Styles
**Purpose**: Styles unique to specific pages.

**What it contains**:
- `.page-home` - Home page specific styles
- `.page-login` - Login page layout (centered form)
- `.page-dashboard` - Dashboard grid layout
- `.page-profile` - Profile page styles
- `.page-not-found` - 404 page styles
- `.message-box` - Toast notification styles and animations

**Why it matters**: Keeps page-specific styles organized and separate from global styles.

---

## 🚀 Getting Started

### 1. Clone or Use Template
```bash
# Option A: Clone directly
git clone <your-repo-url>
cd SPA

# Option B: Use as GitHub template
# Click "Use this template" on GitHub
```

### 2. Configure Your App
Edit `apps/bundles/config.js`:

```javascript
export const appConfig = {
  // Set your authentication
  auth: { 
    type: 'firebase',  // or 'custom', 'auth0'
    firebaseConfig: {
      // Your Firebase credentials
    }
  },
  
  // Set your API
  api: { 
    baseURL: 'https://your-api.com',
    endpoints: { users: '/users', posts: '/posts' }
  },
  
  // Define your routes
  pages: [
    { path: '/', template: 'home', requireAuth: false, title: 'Home' },
    { path: '/dashboard', template: 'dashboard', requireAuth: true, title: 'Dashboard' }
  ]
};
```

### 3. Add Your Pages
Edit `apps/bundles/pages.js` and add templates:

```javascript
templates: {
  myPage: `<div class="page page-mypage">
    <h1>My Custom Page</h1>
    <p>Your content here</p>
  </div>`
}
```

### 4. Customize Styles
- `styles/layout.css` - Base layout
- `styles/components.css` - UI components
- `styles/pages.css` - Page-specific styles

---

## 🖥️ Local Development

### **Option 1: Node.js `serve` with `serve.json` (Recommended for SPAs)**
Elegant SPA routing using `serve.json` configuration.

#### **How it works:**
```json
// serve.json
{
  "rewrites": [
    { "source": "**", "destination": "/pages/index.html" }
  ]
}
```

**What this does:**
1. When you request a file (e.g., `/js/utils.js`), it checks if file exists
2. If file NOT found in root directory, it returns `pages/index.html`
3. Your app loads, router detects the URL hash, displays correct page

#### **Setup and Run:**
```bash
# Navigate to project root
cd g:\code\SPA

# Run npx serve (it reads serve.json automatically)
npx serve

# Or with specific port
npx serve -l 3000

# Open browser
# http://localhost:3000
```

✅ **Key advantage**: Files are served correctly, unmatched routes fallback to `pages/index.html` for SPA routing

---

### **Option 2: Python HTTP Server (Simplest)**
Quick testing without extra configuration.

```bash
# Navigate to project root
cd g:\code\SPA

# Start server (Python 3)
python -m http.server 8000

# Open browser
# http://localhost:8000/pages/
```

⚠️ **Note**: With Python server, access `http://localhost:8000/pages/` directly (no automatic fallback routing)

---

### **Option 3: Live Server (VS Code Extension)**
Best for automatic browser refresh during development.

1. Install **Live Server** extension in VS Code
2. Right-click `pages/index.html`
3. Select **"Open with Live Server"**
4. Auto-refresh on file changes!
5. Live Server will handle relative paths correctly

---

### **Option 4: PHP Built-in Server**
```bash
# Navigate to project root
cd g:\code\SPA

# Start PHP server
php -S localhost:8000

# Access via
# http://localhost:8000/pages/
```

---

### **Option 5: Node.js Express Server with serve.json logic**
Create `server.js` in project root:

```javascript
const express = require('express');
const path = require('path');
const app = express();

// Serve all static files from root
app.use(express.static('.'));

// SPA: Unmatched routes return pages/index.html
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'pages/index.html'));
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));
```

Run:
```bash
npm install express
node server.js
```

---

## 🚀 Production Deployment

### **Netlify Deployment (Recommended)**

Netlify is perfect for SPAs - handles routing automatically.

#### **Step 1: SPA Routing Configuration (Already Set Up)**

Your project includes SPA routing files at root level:
- `_redirects` - Netlify SPA routing config (Netlify syntax)
- `netlify.toml` - Same config in TOML format

**What the routing config does:**
```
/* /pages/index.html 200
```

This tells Netlify: "For ANY route that doesn't match a real file (`/*`), serve `pages/index.html` with 200 status".

**Why we need this**: 
- User visits `yourdomain.com/dashboard`
- Without redirection: Netlify returns 404 (no dashboard.html file exists)
- With routing config: Netlify serves `pages/index.html`, your app loads, router detects `/dashboard` in URL, page displays!

**Both formats work the same way:**
```toml
# netlify.toml format
[[redirects]]
  from = "/*"
  to = "/pages/index.html"
  status = 200
```

```plaintext
# _redirects format  
/* /pages/index.html 200
```

---

#### **Step 2: Deploy to Netlify**

**Method A: Drag & Drop (Fastest)**
1. Go to [Netlify](https://app.netlify.com)
2. Click **"Add new site"** → **"Deploy manually"**
3. Drag your entire `SPA` folder into the upload area
4. Wait for deployment (~30 seconds)
5. Your site is live at `random-name.netlify.app`

**Method B: GitHub Integration (Best for Teams)**
1. Push your project to GitHub
2. Go to [Netlify](https://app.netlify.com)
3. Click **"Add new site"** → **"Import from Git"**
4. Connect GitHub and select your repo
5. **Build settings**:
   - **Base directory**: (leave empty - use root)
   - **Build command**: (leave empty - no build needed)
   - **Publish directory**: `.` (current directory / root)
6. Click **"Deploy"**
7. Every git push auto-deploys!

**Method C: Netlify CLI**
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Initialize (one-time setup, in project root)
cd SPA
netlify init

# Deploy
netlify deploy --prod
```

---

#### **Step 3: Custom Domain (Optional)**
1. In Netlify dashboard → **Domain settings**
2. Click **"Add custom domain"**
3. Enter your domain (e.g., `myapp.com`)
4. Update DNS records at your domain registrar:
   - **Type**: `A`
   - **Name**: `@`
   - **Value**: Netlify's IP (Netlify shows you this)
5. SSL certificate auto-generated (free HTTPS)

---

### **Vercel Deployment**

Similar to Netlify, great for SPAs.

#### **Method A: Vercel CLI**
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
cd SPA
vercel --prod

# Follow prompts:
# - Project name: my-spa-app
# - Root directory: ./pages
# - Build command: (empty)
# - Output directory: ./
```

#### **Method B: GitHub Integration**
1. Push to GitHub
2. Go to [Vercel](https://vercel.com)
3. Import repository
4. Set root directory to `pages`
5. Deploy!

**Vercel Redirects**: Create `pages/vercel.json`:
```json
{
  "rewrites": [
    { "source": "/:path*", "destination": "/index.html" }
  ]
}
```

---

### **GitHub Pages Deployment**

Free hosting for public repos.

#### **Option 1: gh-pages Branch**
```bash
# Install gh-pages
npm install -g gh-pages

# Deploy
gh-pages -d pages

# Your site: https://username.github.io/repo-name
```

#### **Option 2: GitHub Actions (Automated)**

Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./pages
```

Enable GitHub Pages in repo settings → Pages → Source: `gh-pages` branch.

**Note**: GitHub Pages doesn't support SPA redirects natively. Add this to `pages/404.html`:

```html
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="refresh" content="0;url=/repo-name/">
  <script>
    // Redirect to index with hash
    const path = window.location.pathname.replace('/repo-name', '');
    window.location.href = '/repo-name/#' + path;
  </script>
</head>
<body></body>
</html>
```

---

### **Firebase Hosting**

Perfect if you're already using Firebase Auth/Firestore.

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login
firebase login

# Initialize
firebase init hosting

# Prompts:
# - Public directory: pages
# - Single-page app: Yes
# - Overwrite index.html: No

# Deploy
firebase deploy --only hosting

# Your site: https://your-project-id.web.app
```

Firebase automatically adds SPA redirects with "Single-page app: Yes".

---

### **AWS S3 + CloudFront**

For enterprise-scale hosting.

#### **1. Create S3 Bucket**
```bash
aws s3 mb s3://my-spa-app
```

#### **2. Upload Files**
```bash
aws s3 sync ./pages s3://my-spa-app --acl public-read
```

#### **3. Enable Static Website Hosting**
- Go to S3 → Bucket → Properties → Static website hosting
- Index document: `index.html`
- Error document: `index.html` (for SPA routing)

#### **4. Create CloudFront Distribution**
- Origin domain: Your S3 bucket URL
- Origin path: (empty)
- Custom error responses:
  - 403: Return `/index.html` with 200
  - 404: Return `/index.html` with 200

---

### **Environment-Specific Configuration**

Use environment detection in `config.js`:

```javascript
const isDev = window.location.hostname === 'localhost';
const isProd = window.location.hostname.includes('yourapp.com');

export const appConfig = {
  api: {
    baseURL: isDev 
      ? 'http://localhost:5000/api'
      : 'https://api.yourapp.com'
  },
  auth: {
    type: 'firebase',
    firebaseConfig: isDev
      ? { /* dev credentials */ }
      : { /* prod credentials */ }
  }
};
```

---

## 📚 Core Modules API Reference

### **Router API** (`apps/bundles/router.js`)

```javascript
// Navigate to a route
window.app.router.navigate('/dashboard');
window.app.router.navigate('/profile');

// Get current path
const path = window.app.router.getCurrentPath();
// Returns: '/dashboard'

// Get previous path (useful for "back" functionality)
const prev = window.app.router.getPreviousPath();

// Check if route exists
if (window.app.router.routeExists('/admin')) {
  // Route is defined in config
}

// Listen for route changes
window.app.router.onChange((newPath) => {
  console.log(`Route changed to: ${newPath}`);
  // Run custom logic on route change
});

// Get page configuration for current route
const config = window.app.router.getCurrentPageConfig();
// Returns: { path: '/dashboard', template: 'dashboard', requireAuth: true, title: 'Dashboard' }
```

---

### **Auth API** (`apps/bundles/auth.js`)

```javascript
// Login
const result = await window.app.auth.login('user@example.com', 'password123');
if (result.success) {
  console.log('Logged in:', result.user);
} else {
  console.error('Login failed:', result.error);
}

// Register
const signupResult = await window.app.auth.register({
  email: 'newuser@example.com',
  password: 'password123',
  displayName: 'John Doe'
});

// Logout
await window.app.auth.logout();

// Check authentication status
if (window.app.auth.checkAuth()) {
  // User is authenticated
}

// Get current user
const user = window.app.auth.getUser();
// Returns: { id: 'abc123', email: 'user@example.com', displayName: 'John' }

// Password reset (Firebase)
await window.app.auth.resetPassword('user@example.com');

// Access Firebase instances (if using Firebase)
const firestore = window.app.auth.getFirestore();
const database = window.app.auth.getDatabase();
const storage = window.app.auth.getStorage();
```

---

### **Pages API** (`apps/bundles/pages.js`)

```javascript
// Render a page (usually called by router/main.js)
window.app.pages.renderPage('/dashboard', window.app.auth);

// Get page template HTML
const html = window.app.pages.getTemplate('dashboard');

// Get current page name
const currentPage = window.app.pages.getCurrentPage();
// Returns: 'dashboard'

// Add custom page templates dynamically
window.app.pages.templates.customPage = `
  <div class="page page-custom">
    <h1>Dynamic Page</h1>
  </div>
`;
```

---

### **Utilities API** (`apps/bundles/utilities.js`)

#### **API Calls**
```javascript
// GET request
const users = await window.app.utilities.get('/users');
const user = await window.app.utilities.get('/users/123');

// POST request
const newUser = await window.app.utilities.post('/users', {
  name: 'John Doe',
  email: 'john@example.com'
});

// PUT request
const updated = await window.app.utilities.put('/users/123', {
  name: 'Jane Doe'
});

// DELETE request
await window.app.utilities.delete('/users/123');

// Custom headers
const data = await window.app.utilities.get('/protected', {
  headers: { 'Authorization': 'Bearer token123' }
});
```

#### **DOM Manipulation**
```javascript
// Query elements
const element = window.app.utilities.querySelector('#my-element');
const elements = window.app.utilities.querySelectorAll('.my-class');

// Set HTML content
window.app.utilities.setHTML('#container', '<p>New content</p>');

// Add event listener
window.app.utilities.addEventListener('#button', 'click', () => {
  console.log('Button clicked!');
});

// Add/remove classes
window.app.utilities.addClass('#element', 'active');
window.app.utilities.removeClass('#element', 'inactive');
```

#### **Messaging**
```javascript
// Success message (green, 3 seconds)
window.app.utilities.showSuccess('User created successfully!');

// Error message (red, 5 seconds)
window.app.utilities.showError('Failed to load data');

// Info message (blue, 3 seconds)
window.app.utilities.showInfo('Loading...');

// Custom duration
window.app.utilities.showSuccess('Saved!', 1000); // 1 second
```

#### **Data & Performance**
```javascript
// Safe JSON parsing
const obj = window.app.utilities.parseJSON('{"name":"John"}');

// Stringify with formatting
const json = window.app.utilities.stringifyJSON({ name: 'John' });

// Debounce (for search inputs - waits until user stops typing)
const searchInput = document.querySelector('#search');
const debouncedSearch = window.app.utilities.debounce((value) => {
  performSearch(value);
}, 300); // 300ms delay

searchInput.addEventListener('input', (e) => {
  debouncedSearch(e.target.value);
});

// Throttle (for scroll events - limits execution rate)
const throttledScroll = window.app.utilities.throttle(() => {
  console.log('Scrolled!');
}, 300); // Maximum once per 300ms

window.addEventListener('scroll', throttledScroll);

// Generate unique ID
const id = window.app.utilities.generateId();
// Returns: "1709000000000-abc123def"
```

---

### **Firebase Service API** (`apps/bundles/firebase-service.js`)

#### **Create (Add Document)**
```javascript
// Add document to collection
const result = await window.app.firebase.addDocument('posts', {
  title: 'My First Post',
  content: 'Hello World',
  published: true
});

if (result.success) {
  console.log('Created with ID:', result.id);
  // Auto-added: userId, createdAt timestamp
}
```

#### **Read (Get Documents)**
```javascript
// Get single document by ID
const post = await window.app.firebase.getDocument('posts', 'post123');
if (post.success) {
  console.log(post.data); // { id: 'post123', title: '...', ... }
}

// Get all documents in collection
const allPosts = await window.app.firebase.getCollection('posts');

// Get with WHERE filter
const myPosts = await window.app.firebase.getCollection('posts',
  { field: 'userId', operator: '==', value: currentUser.id }
);

// Get with ORDER BY
const sortedPosts = await window.app.firebase.getCollection('posts',
  null,  // no filter
  { field: 'createdAt', direction: 'desc' }  // newest first
);

// Get with LIMIT
const recentPosts = await window.app.firebase.getCollection('posts',
  { field: 'published', operator: '==', value: true },  // published only
  { field: 'createdAt', direction: 'desc' },             // newest first
  10                                                       // limit 10
);
```

#### **Update**
```javascript
// Update document
const result = await window.app.firebase.updateDocument('posts', 'post123', {
  title: 'Updated Title',
  published: true
});
// Auto-added: updatedAt timestamp
```

#### **Delete**
```javascript
// Delete document
await window.app.firebase.deleteDocument('posts', 'post123');
```

#### **File Upload/Delete**
```javascript
// Upload file to Firebase Storage
const fileInput = document.querySelector('#file-input');
const file = fileInput.files[0];

const result = await window.app.firebase.uploadFile(`uploads/${file.name}`, file);
if (result.success) {
  console.log('File URL:', result.url);
  // Save URL to Firestore
  await window.app.firebase.updateDocument('users', userId, {
    avatarURL: result.url
  });
}

// Delete file
await window.app.firebase.deleteFile(`uploads/${file.name}`);
```

#### **Real-Time Listeners**
```javascript
// Listen for real-time updates
const unsubscribe = window.app.firebase.listenToCollection('posts',
  (posts) => {
    console.log('Posts updated:', posts);
    // Update UI with new data
    renderPosts(posts);
  },
  { field: 'published', operator: '==', value: true }  // optional filter
);

// Stop listening when component unmounts
unsubscribe();
```

---

### **Main App API** (`apps/main.js`)

```javascript
// Access app state
const state = window.app.getState();
console.log(state.user);          // Current user
console.log(state.currentPage);   // Current page
console.log(state.isLoading);     // Loading status
console.log(state.data);          // App data

// Update app state
window.app.setState({ 
  theme: 'dark',
  notifications: 5
});

// Access modules
window.app.router.navigate('/home');
window.app.auth.getUser();
window.app.utilities.showSuccess('Hello!');
window.app.pages.getCurrentPage();
window.app.firebase.addDocument('collection', {});

// Fetch user data (uses Utilities API internally)
const userData = await window.app.fetchUserData();
```

---

## � Firebase Integration - Complete Guide

### **What is Firebase?**

Firebase is Google's Backend-as-a-Service (BaaS) platform. Instead of building your own backend server, database, and authentication system, Firebase provides them ready-to-use.

**Firebase Services We Use:**
1. **Firebase Authentication** - User login/signup
2. **Cloud Firestore** - NoSQL database
3. **Firebase Storage** - File storage (images, videos, PDFs)
4. **Firebase Hosting** - Website hosting

---

### **How Firebase Works in This Template**

```
Your App (Frontend)
    ↓
Firebase SDK (JavaScript)
    ↓
Firebase Services (Cloud)
    ↓
Your Data/Users/Files
```

**No backend code needed!** Firebase SDK communicates directly with Firebase cloud services.

---

### **1. Firebase Authentication**

#### **What It Does**
Handles user signup, login, logout, and session management.

#### **Supported Methods**
- Email/Password
- Google Sign-In
- GitHub Sign-In
- Facebook Sign-In
- Anonymous Auth
- Phone Number Auth

#### **How It Works**
```javascript
// 1. User submits login form
await window.app.auth.login('user@example.com', 'password123');

// 2. Firebase validates credentials
// 3. Returns user object with ID token
// 4. Token stored in browser (persists across reloads)
// 5. Token sent with every Firestore request for authorization
```

#### **Implementation Example**

**Enable Email/Password in Firebase Console:**
1. Go to [Firebase Console](https://console.firebase.google.com)
2. Select your project
3. Click **Authentication** → **Sign-in method**
4. Enable **Email/Password**
5. (Optional) Enable **Google**, **GitHub**, etc.

**Login Flow:**
```javascript
// User fills out login form
const email = document.querySelector('#email').value;
const password = document.querySelector('#password').value;

// Attempt login
const result = await window.app.auth.login(email, password);

if (result.success) {
  // Login successful
  window.app.utilities.showSuccess('Welcome back!');
  window.app.router.navigate('/dashboard');
} else {
  // Login failed
  window.app.utilities.showError(result.error);
}
```

**Session Persistence:**
Firebase automatically keeps users logged in across:
- Browser refreshes
- Tab closes/reopens
- Computer restarts

**Logout:**
```javascript
await window.app.auth.logout();
// User session cleared, redirected to home
```

---

### **2. Cloud Firestore (Database)**

#### **What It Does**
NoSQL document database for storing app data (posts, users, comments, products, etc.)

#### **Structure**
```
Firestore Database
│
├── Collection: "users"
│   ├── Document: "user123" → { name: "John", email: "john@example.com" }
│   └── Document: "user456" → { name: "Jane", email: "jane@example.com" }
│
├── Collection: "posts"
│   ├── Document: "post789" → { title: "Hello", content: "...", userId: "user123" }
│   └── Document: "post012" → { title: "World", content: "...", userId: "user456" }
│
└── Collection: "comments"
    ├── Document: "comment1" → { text: "Great post!", postId: "post789" }
    └── Document: "comment2" → { text: "Thanks!", postId: "post789" }
```

**Collections** = Tables (but more flexible)
**Documents** = Rows (but can have nested objects/arrays)

#### **CRUD Operations**

**Create:**
```javascript
// Add a blog post
const result = await window.app.firebase.addDocument('posts', {
  title: 'My First Post',
  content: 'This is the content of my post...',
  tags: ['javascript', 'spa'],
  published: true
});

console.log('Post ID:', result.id);
// Auto-added fields: userId, createdAt
```

**Read:**
```javascript
// Get all posts
const allPosts = await window.app.firebase.getCollection('posts');
console.log(allPosts.data); // Array of post objects

// Get one post
const post = await window.app.firebase.getDocument('posts', 'post789');
console.log(post.data); // Single post object

// Get with filter (only published posts)
const publishedPosts = await window.app.firebase.getCollection('posts',
  { field: 'published', operator: '==', value: true }
);

// Get user's posts only
const myPosts = await window.app.firebase.getCollection('posts',
  { field: 'userId', operator: '==', value: window.app.auth.getUser().id }
);

// Get sorted by date (newest first)
const sortedPosts = await window.app.firebase.getCollection('posts',
  null,
  { field: 'createdAt', direction: 'desc' }
);

// Get latest 10 posts
const recentPosts = await window.app.firebase.getCollection('posts',
  null,
  { field: 'createdAt', direction: 'desc' },
  10  // limit
);
```

**Update:**
```javascript
// Update a post
await window.app.firebase.updateDocument('posts', 'post789', {
  title: 'Updated Title',
  published: false
});
// Auto-added: updatedAt timestamp
```

**Delete:**
```javascript
// Delete a post
await window.app.firebase.deleteDocument('posts', 'post789');
```

#### **Real-Time Updates**

Firestore can notify your app when data changes (without refreshing).

```javascript
// Listen for changes to posts collection
const unsubscribe = window.app.firebase.listenToCollection('posts',
  (posts) => {
    // This runs whenever posts change
    console.log('Posts updated:', posts);
    renderPostsUI(posts);
  },
  { field: 'published', operator: '==', value: true }
);

// When user navigates away, stop listening
unsubscribe();
```

**Use cases:**
- Chat apps: New messages appear instantly
- Collaborative docs: See others' edits in real-time
- Live dashboards: Data updates without refresh

---

### **3. Firebase Storage (File Storage)**

#### **What It Does**
Stores and serves files (images, videos, PDFs, etc.)

#### **How It Works**
```javascript
// 1. User selects file
const fileInput = document.querySelector('#file-input');
const file = fileInput.files[0];

// 2. Upload to Firebase Storage
const result = await window.app.firebase.uploadFile(
  `avatars/${window.app.auth.getUser().id}/${file.name}`,
  file
);

// 3. Get download URL
console.log('File URL:', result.url);
// https://firebasestorage.googleapis.com/v0/b/.../avatar.jpg

// 4. Save URL to Firestore
await window.app.firebase.updateDocument('users', userId, {
  avatarURL: result.url
});

// 5. Display image
document.querySelector('#avatar').src = result.url;
```

**Delete File:**
```javascript
await window.app.firebase.deleteFile(`avatars/${userId}/avatar.jpg`);
```

#### **Complete Upload Example**

```html
<!-- File input -->
<input type="file" id="file-input" accept="image/*">
<button id="upload-btn">Upload</button>
<img id="preview" style="display:none;">
```

```javascript
document.querySelector('#upload-btn').addEventListener('click', async () => {
  const fileInput = document.querySelector('#file-input');
  const file = fileInput.files[0];
  
  if (!file) {
    window.app.utilities.showError('Please select a file');
    return;
  }
  
  window.app.utilities.showInfo('Uploading...');
  
  // Upload to storage
  const path = `uploads/${window.app.auth.getUser().id}/${Date.now()}_${file.name}`;
  const result = await window.app.firebase.uploadFile(path, file);
  
  if (result.success) {
    window.app.utilities.showSuccess('Upload successful!');
    
    // Display uploaded image
    document.querySelector('#preview').src = result.url;
    document.querySelector('#preview').style.display = 'block';
    
    // Save URL to user profile
    await window.app.firebase.updateDocument('users', 
      window.app.auth.getUser().id, 
      { profilePicture: result.url }
    );
  } else {
    window.app.utilities.showError('Upload failed: ' + result.error);
  }
});
```

---

### **4. Firebase Security Rules**

#### **Why They Matter**
Without security rules, anyone can read/write ANY data in your Firestore!

#### **Firestore Rules**

Go to Firebase Console → **Firestore Database** → **Rules** tab.

**Default (INSECURE - DO NOT USE IN PRODUCTION):**
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if true; // Anyone can read/write everything!
    }
  }
}
```

**Secure Rules (USE THIS):**
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    
    // Users collection: users can only access their own document
    match /users/{userId} {
      allow read: if request.auth != null && request.auth.uid == userId;
      allow write: if request.auth != null && request.auth.uid == userId;
    }
    
    // Posts collection
    match /posts/{postId} {
      // Anyone can read published posts
      allow read: if resource.data.published == true;
      
      // Only authenticated users can create posts
      allow create: if request.auth != null 
                    && request.resource.data.userId == request.auth.uid;
      
      // Only post owner can update/delete
      allow update, delete: if request.auth != null 
                            && resource.data.userId == request.auth.uid;
    }
    
    // Comments collection
    match /comments/{commentId} {
      // Anyone can read comments
      allow read: if true;
      
      // Authenticated users can create comments
      allow create: if request.auth != null
                    && request.resource.data.userId == request.auth.uid;
      
      // Only comment author can delete
      allow delete: if request.auth != null
                    && resource.data.userId == request.auth.uid;
    }
  }
}
```

**Storage Rules:**

Go to Firebase Console → **Storage** → **Rules** tab.

```javascript
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    
    // Users can only upload to their own folder
    match /uploads/{userId}/{fileName} {
      allow read: if true; // Anyone can view
      allow write: if request.auth != null && request.auth.uid == userId;
    }
    
    // Avatar uploads
    match /avatars/{userId}/{fileName} {
      // Only allow image files under 5MB
      allow write: if request.auth != null 
                   && request.auth.uid == userId
                   && request.resource.size < 5 * 1024 * 1024
                   && request.resource.contentType.matches('image/.*');
    }
  }
}
```

---

### **5. Complete Blog App Example**

Let's build a simple blog with Firebase.

**Step 1: Create Post**
```javascript
async function createPost() {
  const title = document.querySelector('#post-title').value;
  const content = document.querySelector('#post-content').value;
  
  const result = await window.app.firebase.addDocument('posts', {
    title,
    content,
    published: true,
    likes: 0
  });
  
  if (result.success) {
    window.app.utilities.showSuccess('Post created!');
    window.app.router.navigate('/posts');
  }
}
```

**Step 2: Display Posts**
```javascript
async function loadPosts() {
  const result = await window.app.firebase.getCollection('posts',
    { field: 'published', operator: '==', value: true },
    { field: 'createdAt', direction: 'desc' }
  );
  
  if (result.success) {
    const postsContainer = document.querySelector('#posts');
    postsContainer.innerHTML = result.data.map(post => `
      <div class="post">
        <h2>${post.title}</h2>
        <p>${post.content}</p>
        <button onclick="likePost('${post.id}')">Like (${post.likes})</button>
      </div>
    `).join('');
  }
}
```

**Step 3: Like Post**
```javascript
async function likePost(postId) {
  const post = await window.app.firebase.getDocument('posts', postId);
  
  if (post.success) {
    await window.app.firebase.updateDocument('posts', postId, {
      likes: post.data.likes + 1
    });
    
    loadPosts(); // Refresh posts
  }
}
```

**Step 4: Delete Post (Owner Only)**
```javascript
async function deletePost(postId) {
  const currentUser = window.app.auth.getUser();
  const post = await window.app.firebase.getDocument('posts', postId);
  
  if (post.data.userId === currentUser.id) {
    await window.app.firebase.deleteDocument('posts', postId);
    window.app.utilities.showSuccess('Post deleted');
    loadPosts();
  } else {
    window.app.utilities.showError('Not authorized');
  }
}
```

---

### **6. Firebase Pricing**

**Free Tier (Spark Plan):**
- **Firestore**: 50K reads/day, 20K writes/day, 1GB storage
- **Authentication**: Unlimited users
- **Storage**: 5GB transferred/day, 1GB stored
- **Hosting**: 10GB transferred/month

**Good for:** Small projects, prototypes, learning

**Paid Tier (Blaze Plan):**
- Pay-as-you-go
- **Firestore**: $0.06 per 100K reads, $0.18 per 100K writes
- **Storage**: $0.026/GB stored, $0.12/GB transferred

**Good for:** Production apps with traffic

---

### **7. Firebase Setup Checklist**

✅ Create Firebase project
✅ Enable Authentication (Email/Password)
✅ Create Firestore database (Start in test mode, then add rules)
✅ Enable Storage
✅ Copy Firebase config to `apps/bundles/config.js`
✅ Add Firebase SDK to `pages/index.html`
✅ Update security rules for Firestore and Storage
✅ Test login/signup
✅ Test Firestore CRUD operations
✅ Test file upload

---

## �🔧 Usage Examples

## 🔧 Complete Usage Examples

### **Example 1: Add a New Page**

**Step 1:** Add template in `apps/bundles/pages.js`
```javascript
templates: {
  products: `
    <div class="page page-products">
      <h1>Products</h1>
      <div id="products-list"></div>
      <button id="load-products">Load Products</button>
    </div>
  `
}
```

**Step 2:** Add route in `apps/bundles/config.js`
```javascript
pages: [
  // ... existing pages
  { path: '/products', template: 'products', requireAuth: false, title: 'Products' }
]
```

**Step 3:** Add page initialization in `apps/bundles/pages.js`
```javascript
initializePage(templateName) {
  switch (templateName) {
    case 'products':
      this.initProductsPage();
      break;
    // ... other cases
  }
}

initProductsPage() {
  document.querySelector('#load-products').addEventListener('click', async () => {
    const products = await window.app.utilities.get('/api/products');
    const html = products.map(p => `<div>${p.name}</div>`).join('');
    document.querySelector('#products-list').innerHTML = html;
  });
}
```

**Step 4:** Link to page
```html
<a href="#/products">View Products</a>
```

---

### **Example 2: Protected Route (Auth Required)**

**In `config.js`:**
```javascript
{ path: '/admin', template: 'admin', requireAuth: true, title: 'Admin Panel' }
```

When user tries to access `/admin`:
- If authenticated → Shows admin page
- If not authenticated → Redirects to `/login`

This is handled automatically by `pages.js`:
```javascript
renderPage(path, authInstance) {
  const pageConfig = this.config.pages.find(page => page.path === path);
  
  if (pageConfig.requireAuth && !authInstance.checkAuth()) {
    window.app.router.navigate('/login'); // Redirect using clean URLs
    return;
  }
  
  // Render page
}
```

---

### **Example 3: Form Handling with Validation**

```html
<!-- In pages.js template -->
<form id="contact-form">
  <input type="text" id="name" placeholder="Name" required>
  <input type="email" id="email" placeholder="Email" required>
  <textarea id="message" placeholder="Message" required></textarea>
  <button type="submit">Send</button>
</form>
```

```javascript
// In main.js setupEventDelegates or pages.js
document.addEventListener('submit', async (e) => {
  if (e.target.id === 'contact-form') {
    e.preventDefault();
    
    const name = document.querySelector('#name').value;
    const email = document.querySelector('#email').value;
    const message = document.querySelector('#message').value;
    
    // Validate
    if (name.length < 2) {
      window.app.utilities.showError('Name too short');
      return;
    }
    
    if (!email.includes('@')) {
      window.app.utilities.showError('Invalid email');
      return;
    }
    
    // Submit
    window.app.utilities.showInfo('Sending...');
    
    const result = await window.app.utilities.post('/api/contact', {
      name, email, message
    });
    
    if (result) {
      window.app.utilities.showSuccess('Message sent!');
      e.target.reset();
    } else {
      window.app.utilities.showError('Failed to send');
    }
  }
});
```

---

### **Example 4: User Profile with Firebase**

**Create Profile Page** in `pages.js`:
```javascript
profile: `
  <div class="page page-profile">
    <h1>My Profile</h1>
    <div id="profile-info">Loading...</div>
    <button id="edit-profile-btn">Edit Profile</button>
  </div>
`
```

**Load Profile Data**:
```javascript
initProfilePage() {
  this.loadUserProfile();
}

async loadUserProfile() {
  const userId = window.app.auth.getUser().id;
  const result = await window.app.firebase.getDocument('users', userId);
  
  if (result.success) {
    const user = result.data;
    document.querySelector('#profile-info').innerHTML = `
      <p><strong>Name:</strong> ${user.displayName}</p>
      <p><strong>Email:</strong> ${user.email}</p>
      <p><strong>Joined:</strong> ${user.createdAt}</p>
      ${user.avatarURL ? `<img src="${user.avatarURL}" alt="Avatar">` : ''}
    `;
  }
}
```

---

### **Example 5: Real-Time Chat**

**Chat Template**:
```javascript
chat: `
  <div class="page page-chat">
    <h1>Chat Room</h1>
    <div id="messages"></div>
    <form id="chat-form">
      <input type="text" id="message-input" placeholder="Type message...">
      <button type="submit">Send</button>
    </form>
  </div>
`
```

**Initialize Chat**:
```javascript
initChatPage() {
  // Listen for new messages in real-time
  this.chatUnsubscribe = window.app.firebase.listenToCollection('messages',
    (messages) => {
      // Sort by timestamp
      messages.sort((a, b) => a.createdAt - b.createdAt);
      
      // Render messages
      const html = messages.map(msg => `
        <div class="message">
          <strong>${msg.userName}:</strong> ${msg.text}
        </div>
      `).join('');
      
      document.querySelector('#messages').innerHTML = html;
      
      // Scroll to bottom
      const container = document.querySelector('#messages');
      container.scrollTop = container.scrollHeight;
    }
  );
  
  // Send message
  document.querySelector('#chat-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const input = document.querySelector('#message-input');
    const text = input.value.trim();
    
    if (text) {
      await window.app.firebase.addDocument('messages', {
        text,
        userName: window.app.auth.getUser().displayName || 'Anonymous'
      });
      
      input.value = '';
    }
  });
}

// Clean up when leaving chat page
destroyChatPage() {
  if (this.chatUnsubscribe) {
    this.chatUnsubscribe(); // Stop listening
  }
}
```

---

### **Example 6: Image Upload with Preview**

```html
<!-- Template -->
<div class="upload-container">
  <input type="file" id="image-input" accept="image/*">
  <img id="preview" style="max-width: 300px; display:none;">
  <button id="upload-btn">Upload</button>
  <div id="upload-progress"></div>
</div>
```

```javascript
document.querySelector('#image-input').addEventListener('change', (e) => {
  const file = e.target.files[0];
  if (file) {
    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
      const preview = document.querySelector('#preview');
      preview.src = e.target.result;
      preview.style.display = 'block';
    };
    reader.readAsDataURL(file);
  }
});

document.querySelector('#upload-btn').addEventListener('click', async () => {
  const fileInput = document.querySelector('#image-input');
  const file = fileInput.files[0];
  
  if (!file) {
    window.app.utilities.showError('Select an image first');
    return;
  }
  
  // Show progress
  document.querySelector('#upload-progress').textContent = 'Uploading...';
  
  // Upload
  const path = `images/${Date.now()}_${file.name}`;
  const result = await window.app.firebase.uploadFile(path, file);
  
  if (result.success) {
    window.app.utilities.showSuccess('Upload complete!');
    document.querySelector('#upload-progress').textContent = `URL: ${result.url}`;
    
    // Save to Firestore
    await window.app.firebase.addDocument('images', {
      url: result.url,
      name: file.name,
      size: file.size
    });
  } else {
    window.app.utilities.showError('Upload failed');
    document.querySelector('#upload-progress').textContent = '';
  }
});
```

---

### **Example 7: Search with Debounce**

```html
<input type="text" id="search-input" placeholder="Search products...">
<div id="search-results"></div>
```

```javascript
const searchInput = document.querySelector('#search-input');

// Debounce search (wait 300ms after user stops typing)
const debouncedSearch = window.app.utilities.debounce(async (query) => {
  if (!query) {
    document.querySelector('#search-results').innerHTML = '';
    return;
  }
  
  // Search in Firestore
  const results = await window.app.firebase.getCollection('products',
    { field: 'name', operator: '>=', value: query },
    null,
    20
  );
  
  if (results.success) {
    const html = results.data.map(product => `
      <div class="search-result">
        <h3>${product.name}</h3>
        <p>${product.price}</p>
      </div>
    `).join('');
    
    document.querySelector('#search-results').innerHTML = html || '<p>No results</p>';
  }
}, 300);

searchInput.addEventListener('input', (e) => {
  debouncedSearch(e.target.value);
});
```

---

### **Example 8: Pagination**

```javascript
let currentPage = 0;
const pageSize = 10;

async function loadPage(page) {
  const skip = page * pageSize;
  
  const result = await window.app.firebase.getCollection('posts',
    { field: 'published', operator: '==', value: true },
    { field: 'createdAt', direction: 'desc' },
    pageSize
    // Note: For true pagination, you'd need to implement cursor-based pagination
  );
  
  if (result.success) {
    renderPosts(result.data);
  }
}

function renderPosts(posts) {
  const html = posts.map(post => `
    <div class="post">
      <h2>${post.title}</h2>
      <p>${post.content}</p>
    </div>
  `).join('');
  
  document.querySelector('#posts').innerHTML = html;
}

// Next/Previous buttons
document.querySelector('#next-btn').addEventListener('click', () => {
  currentPage++;
  loadPage(currentPage);
});

document.querySelector('#prev-btn').addEventListener('click', () => {
  if (currentPage > 0) {
    currentPage--;
    loadPage(currentPage);
  }
});

// Load initial page
loadPage(0);
```

---

## 🎨 Styling Tips

### **Custom Themes**

Add theme toggle in `styles/layout.css`:

```css
:root {
  --primary-color: #3498db;
  --bg-color: #ffffff;
  --text-color: #333333;
}

[data-theme="dark"] {
  --primary-color: #4ea8f5;
  --bg-color: #1a1a1a;
  --text-color: #f0f0f0;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
}

.btn {
  background-color: var(--primary-color);
}
```

**Toggle Theme:**
```javascript
function toggleTheme() {
  const root = document.documentElement;
  const currentTheme = root.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  root.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
}

// Load saved theme
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
  document.documentElement.setAttribute('data-theme', savedTheme);
}
```

---

## 📊 Performance Optimization

### **1. Lazy Load Components**
```javascript
// Load heavy components only when needed
async function loadChart() {
  const ChartModule = await import('./chart-library.js');
  const chart = new ChartModule.Chart('#canvas', data);
}
```

### **2. Cache API Responses**
```javascript
const cache = {};

async function getCachedData(endpoint) {
  if (cache[endpoint]) {
    return cache[endpoint];
  }
  
  const data = await window.app.utilities.get(endpoint);
  cache[endpoint] = data;
  return data;
}
```

### **3. Optimize Images**
```css
img {
  loading: lazy; /* Native lazy loading */
}
```

---

## 🔑 Key Features Summary

✅ **Zero Dependencies** - Pure vanilla JavaScript
✅ **No Build Step** - Works directly in browser
✅ **Modular Architecture** - Clean separation of concerns
✅ **Class-Based** - Organized, maintainable code
✅ **Hash-Based Routing** - No backend routing needed
✅ **Flexible Auth** - Firebase, Auth0, Custom adapters
✅ **State Management** - Centralized app state
✅ **Firebase Integration** - Full CRUD + real-time
✅ **Responsive Design** - Mobile-friendly out of the box
✅ **Production Ready** - Netlify/Vercel deployment guides
✅ **Well Documented** - Comprehensive comments & guides

---

## 📚 Additional Resources

- **[TEMPLATE_USAGE.md](docs/TEMPLATE_USAGE.md)** - Quick start guide (5 min setup)
- **[FIREBASE_INTEGRATION.md](docs/FIREBASE_INTEGRATION.md)** - Complete Firebase setup
- **[GITHUB_TEMPLATE_SETUP.md](docs/GITHUB_TEMPLATE_SETUP.md)** - Create GitHub template

---

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

---

## 📝 License

Free to use and modify for any project (personal or commercial).

---

## 🎉 You're Ready!

**Next Steps:**
1. ✅ Configure `apps/bundles/config.js` with your API/Firebase
2. ✅ Add your page templates in `apps/bundles/pages.js`
3. ✅ Customize styles in `styles/` folder
4. ✅ Run locally with `npx serve` (uses serve.json routing)
5. ✅ Deploy to Netlify/Vercel (uses _redirects routing)

**Need help?** Check the docs folder for detailed guides!

**Happy coding!** 🚀
