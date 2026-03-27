# Quick Start - SPA Template

Welcome! This is a reusable SPA template. Get started in 5 minutes.

## 1️⃣ Clone or Use This Template

**Option A: GitHub Template (Recommended)**
- Click "Use this template" button on GitHub
- Create your new repository
- Clone it locally

**Option B: Clone Directly**
```bash
git clone https://github.com/YOUR_USERNAME/SPA-Template.git my-app
cd my-app
```

---

## 2️⃣ Configure Your App

Edit `config.js` and update:

```javascript
export const appConfig = {
  // Choose your auth provider
  auth: {
    type: 'firebase', // or 'custom', 'auth0'
    firebaseConfig: {
      apiKey: "YOUR_API_KEY",
      authDomain: "your-project.firebaseapp.com",
      projectId: "your-project-id",
      storageBucket: "your-project.appspot.com",
      messagingSenderId: "YOUR_SENDER_ID",
      appId: "YOUR_APP_ID"
    }
  },

  // Set your API endpoint
  api: {
    baseURL: 'https://your-api.com',
    endpoints: {
      users: '/users',
      // Add your endpoints here
    }
  },

  // Define your routes
  pages: [
    { path: '/', template: 'home', requireAuth: false, title: 'Home' },
    { path: '/login', template: 'login', requireAuth: false, title: 'Login' },
    { path: '/dashboard', template: 'dashboard', requireAuth: true, title: 'Dashboard' },
    // Add your custom routes
  ]
};
```

---

## 3️⃣ Add Your Pages

Edit `apps/bundles/pages.js` and add templates:

```javascript
templates: {
  myPage: `
    <div class="page page-mypage">
      <h1>My Custom Page</h1>
      <p>Your HTML here</p>
      <button id="my-button">Click Me</button>
    </div>
  `
}
```

---

## 4️⃣ Add Route to Config

In `config.js`, add your new page:

```javascript
pages: [
  // ... existing pages
  { path: '/mypage', template: 'mypage', requireAuth: false, title: 'My Page' }
]
```

---

## 5️⃣ Link Between Pages

Use hash-based links:

```html
<a href="/">Home</a>
<a href="/dashboard">Dashboard</a>
<a href="/mypage">My Page</a>
```

Or programmatically:

```javascript
window.app.router.navigate('/dashboard');
```

---

## 6️⃣ Customize Styles

**Global styles** - `styles/layout.css`
**Component styles** - `styles/components.css`
**Page styles** - `styles/pages.css`

Example:
```css
.page-mypage {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 2rem;
}

.page-mypage h1 {
  color: white;
  text-align: center;
}
```

---

## 7️⃣ Run Locally

```bash
# Python 3 (built-in)
python -m http.server 8000

# Node.js
npx serve

# Then open: http://localhost:8000
```

---

## 8️⃣ Use App Functions

Access the app globally:

```javascript
// Router
window.app.router.navigate('/path');
window.app.router.getCurrentPath();

// Auth
window.app.auth.login(email, password);
window.app.auth.logout();
window.app.auth.checkAuth();
window.app.auth.getUser();

// Utilities
window.app.utilities.get('/endpoint');
window.app.utilities.post('/endpoint', data);
window.app.utilities.showSuccess('Message');
window.app.utilities.showError('Error');

// App State
window.app.state;
window.app.setState({ key: value });

// Firebase (if configured)
window.app.firebase.addDocument('collection', data);
window.app.firebase.getCollection('collection');
window.app.firebase.updateDocument('collection', id, data);
```

---

## 📚 Full Documentation

- **[README.md](README.md)** - Complete architecture & features
- **[FIREBASE_INTEGRATION.md](FIREBASE_INTEGRATION.md)** - Firebase setup guide
- **[GITHUB_TEMPLATE_SETUP.md](GITHUB_TEMPLATE_SETUP.md)** - How to use as GitHub template

---

## 🚀 Deploy

### Deploy to Netlify
```bash
# Build folder contents
```
Drag & drop your project folder to Netlify

### Deploy to GitHub Pages
```bash
git push origin main
# Enable Pages in Settings → Pages
```

### Deploy to Firebase Hosting
```bash
npm install -g firebase-tools
firebase login
firebase init hosting
firebase deploy
```

---

## 💡 Common Tasks

### Add a Form
```html
<form id="my-form">
  <input type="text" placeholder="Name" required>
  <button type="submit">Submit</button>
</form>
```

### Handle Form Submit
```javascript
document.addEventListener('submit', (e) => {
  if (e.target.id === 'my-form') {
    e.preventDefault();
    // Handle submission
    window.app.utilities.showSuccess('Form submitted!');
  }
});
```

### Protect Routes
```javascript
// In config.js
{ path: '/admin', template: 'admin', requireAuth: true }
// User redirected to /login if not authenticated
```

### Show Messages
```javascript
window.app.utilities.showSuccess('Success!');
window.app.utilities.showError('Error!');
window.app.utilities.showInfo('Info');
```

### Make API Calls
```javascript
const data = await window.app.utilities.get('/users');
const result = await window.app.utilities.post('/users', { name: 'John' });
```

---

## ❓ Need Help?

- Check [README.md](README.md) for full API reference
- See [FIREBASE_INTEGRATION.md](FIREBASE_INTEGRATION.md) for Firebase setup
- Review existing page templates in `pages.js`

**Happy coding!** 🎉

