# Firebase Integration Guide

Step-by-step guide to integrate Firebase into the SPA template for authentication and database operations.

---

## Step 1: Create a Firebase Project

### A. Go to Firebase Console
1. Visit [Firebase Console](https://console.firebase.google.com/)
2. Click **Add Project**
3. Enter project name (e.g., "My SPA App")
4. Disable Google Analytics (optional)
5. Click **Create Project**
6. Wait for project creation (~1-2 minutes)

### B. Register Your Web App
1. Click the **Web** icon (</>) to add a web app
2. App nickname: "My SPA App"
3. Check **Also set up Firebase Hosting** (optional)
4. Click **Register App**
5. Copy your Firebase config (you'll need it)

---

## Step 2: Get Firebase Configuration

Firebase will display your config. It looks like:

```javascript
const firebaseConfig = {
  apiKey: "AIzaSyDxKQE...",
  authDomain: "my-spa-app.firebaseapp.com",
  projectId: "my-spa-app",
  storageBucket: "my-spa-app.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abc123def456"
};
```

Copy and save this config.

---

## Step 3: Update Your Configuration

### Edit `config.js`

Replace the Firebase config with your actual credentials:

```javascript
export const appConfig = {
  auth: {
    type: 'firebase',
    firebaseConfig: {
      apiKey: "YOUR_API_KEY",
      authDomain: "your-project.firebaseapp.com",
      projectId: "your-project-id",
      storageBucket: "your-project.appspot.com",
      messagingSenderId: "YOUR_SENDER_ID",
      appId: "YOUR_APP_ID"
    }
  },
  // ... rest of config
};
```

> ⚠️ **Security Note**: In production, consider using environment variables instead of hardcoding credentials.

---

## Step 4: Add Firebase SDK to HTML

### Edit `index.html`

Add Firebase scripts before the main app script:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SPA Template</title>
    
    <!-- Styles -->
    <link rel="stylesheet" href="styles/layout.css">
    <link rel="stylesheet" href="styles/components.css">
    <link rel="stylesheet" href="styles/pages.css">
</head>
<body>
    <!-- Main App Container -->
    <div id="app-root">
        <div id="page-container"></div>
    </div>

    <!-- Message Box for notifications -->
    <div id="message-box" class="message-box"></div>

    <!-- Firebase SDK -->
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-storage.js"></script>

    <!-- JavaScript Entry Point -->
    <script type="module" src="apps/main.js"></script>
</body>
</html>
```

---

## Step 5: Update Auth Module for Firebase

### Replace `apps/bundles/auth.js`

```javascript
/**
 * Auth Class - Firebase Implementation
 * Handles authentication with Firebase
 */

export class Auth {
  constructor(config) {
    this.config = config;
    this.user = null;
    this.authType = config.auth.type;
    this.isAuthenticated = false;
    this.firebaseApp = null;
    this.firebaseAuth = null;
    this.initializeAuth();
  }

  /**
   * Initialize Firebase Auth
   */
  initializeAuth() {
    try {
      if (this.authType === 'firebase') {
        this.initializeFirebase();
      }
    } catch (error) {
      console.error('Auth initialization error:', error);
    }
  }

  /**
   * Initialize Firebase
   */
  initializeFirebase() {
    // Import Firebase (global from CDN)
    const { initializeApp } = window.firebase;
    const { getAuth, onAuthStateChanged } = window.firebase.auth;

    // Initialize Firebase
    this.firebaseApp = initializeApp(this.config.auth.firebaseConfig);
    this.firebaseAuth = getAuth(this.firebaseApp);

    // Listen for authentication state changes
    onAuthStateChanged(this.firebaseAuth, (firebaseUser) => {
      if (firebaseUser) {
        this.user = {
          id: firebaseUser.uid,
          email: firebaseUser.email,
          displayName: firebaseUser.displayName,
          photoURL: firebaseUser.photoURL
        };
        this.isAuthenticated = true;
        this.saveUserSession();
      } else {
        this.user = null;
        this.isAuthenticated = false;
        localStorage.removeItem('user_session');
      }
    });

    console.log('Firebase Auth initialized');
  }

  /**
   * Login with email and password
   * @param {string} email - User email
   * @param {string} password - User password
   */
  async login(email, password) {
    try {
      const { signInWithEmailAndPassword } = window.firebase.auth;

      const userCredential = await signInWithEmailAndPassword(
        this.firebaseAuth,
        email,
        password
      );

      this.user = {
        id: userCredential.user.uid,
        email: userCredential.user.email,
        displayName: userCredential.user.displayName
      };
      this.isAuthenticated = true;
      this.saveUserSession();

      return { success: true, user: this.user };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  /**
   * Register with email and password
   * @param {object} userData - {email, password, displayName}
   */
  async register(userData) {
    try {
      const { createUserWithEmailAndPassword, updateProfile } = window.firebase.auth;

      const userCredential = await createUserWithEmailAndPassword(
        this.firebaseAuth,
        userData.email,
        userData.password
      );

      // Update user profile with display name
      if (userData.displayName) {
        await updateProfile(userCredential.user, {
          displayName: userData.displayName
        });
      }

      this.user = {
        id: userCredential.user.uid,
        email: userCredential.user.email,
        displayName: userData.displayName || ''
      };
      this.isAuthenticated = true;
      this.saveUserSession();

      return { success: true, user: this.user };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  /**
   * Logout user
   */
  async logout() {
    try {
      await this.firebaseAuth.signOut();
      this.user = null;
      this.isAuthenticated = false;
      localStorage.removeItem('user_session');
      return { success: true };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  /**
   * Get current user
   */
  getUser() {
    return this.user;
  }

  /**
   * Check if user is authenticated
   */
  checkAuth() {
    return this.isAuthenticated;
  }

  /**
   * Get Firebase Auth instance
   */
  getFirebaseAuth() {
    return this.firebaseAuth;
  }

  /**
   * Get Firebase App instance
   */
  getFirebaseApp() {
    return this.firebaseApp;
  }

  /**
   * Save user session to localStorage
   */
  saveUserSession() {
    if (this.user) {
      localStorage.setItem('user_session', JSON.stringify(this.user));
    }
  }

  /**
   * Load user session from localStorage
   */
  loadUserSession() {
    const saved = localStorage.getItem('user_session');
    if (saved) {
      this.user = JSON.parse(saved);
      this.isAuthenticated = true;
    }
  }

  /**
   * Send password reset email
   * @param {string} email - User email
   */
  async resetPassword(email) {
    try {
      const { sendPasswordResetEmail } = window.firebase.auth;
      await sendPasswordResetEmail(this.firebaseAuth, email);
      return { success: true };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  /**
   * Get Firebase Firestore database
   */
  getFirestore() {
    const { getFirestore } = window.firebase.firestore;
    return getFirestore(this.firebaseApp);
  }

  /**
   * Get Firebase Realtime Database
   */
  getDatabase() {
    const { getDatabase } = window.firebase.database;
    return getDatabase(this.firebaseApp);
  }

  /**
   * Get Firebase Storage
   */
  getStorage() {
    const { getStorage } = window.firebase.storage;
    return getStorage(this.firebaseApp);
  }
}
```

---

## Step 6: Create Firebase Service Helper

### Create `apps/bundles/firebase-service.js`

```javascript
/**
 * Firebase Service Helper
 * Convenient methods for Firestore operations
 * Requires Auth module to be initialized first
 */

export class FirebaseService {
  constructor(auth) {
    this.auth = auth;
    this.firestore = auth.getFirestore();
  }

  /**
   * Add document to collection
   */
  async addDocument(collection, data) {
    try {
      const { collection: firestoreCollection, addDoc } = window.firebase.firestore;
      const ref = firestoreCollection(this.firestore, collection);
      const docRef = await addDoc(ref, {
        ...data,
        createdAt: new Date(),
        userId: this.auth.getUser().id
      });
      return { success: true, id: docRef.id };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  /**
   * Get document by ID
   */
  async getDocument(collection, docId) {
    try {
      const { collection: firestoreCollection, doc, getDoc } = window.firebase.firestore;
      const docRef = doc(firestoreCollection(this.firestore, collection), docId);
      const docSnap = await getDoc(docRef);

      if (docSnap.exists()) {
        return { success: true, data: { id: docSnap.id, ...docSnap.data() } };
      } else {
        return { success: false, error: 'Document not found' };
      }
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  /**
   * Get all documents from collection
   */
  async getCollection(collection, whereCondition = null) {
    try {
      const { collection: firestoreCollection, query, where, getDocs } = window.firebase.firestore;
      let q = firestoreCollection(this.firestore, collection);

      if (whereCondition) {
        q = query(q, where(whereCondition.field, whereCondition.operator, whereCondition.value));
      }

      const querySnapshot = await getDocs(q);
      const documents = [];
      querySnapshot.forEach((doc) => {
        documents.push({ id: doc.id, ...doc.data() });
      });

      return { success: true, data: documents };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  /**
   * Update document
   */
  async updateDocument(collection, docId, data) {
    try {
      const { collection: firestoreCollection, doc, updateDoc } = window.firebase.firestore;
      const docRef = doc(firestoreCollection(this.firestore, collection), docId);
      await updateDoc(docRef, {
        ...data,
        updatedAt: new Date()
      });
      return { success: true };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  /**
   * Delete document
   */
  async deleteDocument(collection, docId) {
    try {
      const { collection: firestoreCollection, doc, deleteDoc } = window.firebase.firestore;
      const docRef = doc(firestoreCollection(this.firestore, collection), docId);
      await deleteDoc(docRef);
      return { success: true };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  /**
   * Upload file to storage
   */
  async uploadFile(path, file) {
    try {
      const { ref, uploadBytes, getDownloadURL } = window.firebase.storage;
      const storage = this.auth.getStorage();
      const storageRef = ref(storage, path);

      await uploadBytes(storageRef, file);
      const url = await getDownloadURL(storageRef);

      return { success: true, url };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }
}
```

---

## Step 7: Update Main App to Use Firebase

### Update imports in `apps/main.js`

```javascript
import { appConfig } from '../config.js';
import { Router } from './bundles/router.js';
import { Auth } from './bundles/auth.js';
import { Utilities } from './bundles/utilities.js';
import { Pages } from './bundles/pages.js';
import { FirebaseService } from './bundles/firebase-service.js';

export class App {
  constructor(config = appConfig) {
    this.config = config;
    this.state = {
      user: null,
      data: {},
      isLoading: false,
      currentPage: null
    };

    // Initialize modules
    this.router = new Router(config);
    this.auth = new Auth(config);
    this.utilities = new Utilities(config);
    this.pages = new Pages(config);
    this.firebase = new FirebaseService(this.auth);  // Add Firebase service

    // Restore user session if exists
    this.auth.loadUserSession();

    this.initialize();
  }

  /**
   * Initialize the app
   */
  initialize() {
    // Listen for route changes
    this.router.onChange((path) => this.handleRouteChange(path));

    // Set up global event delegates
    this.setupEventDelegates();

    console.log('App initialized successfully');
  }

  /**
   * Handle route changes
   */
  handleRouteChange(path) {
    this.pages.renderPage(path, this.auth);
    this.state.currentPage = path;
    console.log(`Navigated to: ${path}`);
  }

  /**
   * Set up global event delegation
   */
  setupEventDelegates() {
    document.addEventListener('submit', (e) => {
      if (e.target.id === 'login-form') {
        this.handleLoginSubmit(e);
      }
    });

    document.addEventListener('click', (e) => {
      if (e.target.id === 'logout-btn') {
        this.handleLogout();
      }
    });
  }

  /**
   * Handle login form submission
   */
  async handleLoginSubmit(event) {
    event.preventDefault();

    const email = document.querySelector('#email').value;
    const password = document.querySelector('#password').value;

    this.state.isLoading = true;
    this.utilities.showInfo('Logging in...');

    const result = await this.auth.login(email, password);

    if (result.success) {
      this.state.user = result.user;
      this.utilities.showSuccess('Login successful!');
      setTimeout(() => {
        this.router.navigate('/dashboard');
      }, 1000);
    } else {
      this.utilities.showError(`Login failed: ${result.error}`);
    }

    this.state.isLoading = false;
  }

  /**
   * Handle logout
   */
  async handleLogout() {
    const result = await this.auth.logout();

    if (result.success) {
      this.state.user = null;
      this.utilities.showSuccess('Logged out successfully');
      this.router.navigate('/');
    } else {
      this.utilities.showError(`Logout failed: ${result.error}`);
    }
  }

  /**
   * Fetch user data from Firestore
   */
  async fetchUserData() {
    if (!this.auth.checkAuth()) {
      this.utilities.showError('Not authenticated');
      return null;
    }

    const result = await this.firebase.getCollection('users', {
      field: 'userId',
      operator: '==',
      value: this.auth.getUser().id
    });

    if (result.success) {
      this.setState({ data: result.data });
    }
    return result.data;
  }

  getState() {
    return this.state;
  }

  setState(newState) {
    this.state = { ...this.state, ...newState };
  }
}

/**
 * Initialize app when DOM is ready
 */
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    window.app = new App();
  });
} else {
  window.app = new App();
}
```

---

## Step 8: Enable Firebase Authentication Methods

### Go to Firebase Console
1. Click **Authentication** (left sidebar)
2. Go to **Sign-in method** tab
3. Enable authentication providers:
   - ✅ **Email/Password**
   - ✅ **Google** (optional)
   - ✅ **GitHub** (optional)

---

## Step 9: Testing Firebase Authentication

### Create a test user:
1. In Firebase Console → **Authentication** → **Users**
2. Click **Create user**
3. Email: `test@example.com`
4. Password: `Test123!`
5. Click **Create**

### Test in your app:
1. Open `http://localhost:8000`
2. Click "Go to Dashboard" or navigate to `/login`
3. Enter credentials from step above
4. You should see login success message
5. Redirect to dashboard

---

## Step 10: Using Firestore Database

### Example: Save user data after registration

```javascript
// In main.js handleLoginSubmit or after registration
async handleUserRegistration() {
  const result = await this.firebase.addDocument('users', {
    email: this.auth.getUser().email,
    displayName: this.auth.getUser().displayName,
    createdAt: new Date()
  });

  if (result.success) {
    this.utilities.showSuccess('User data saved!');
  }
}
```

### Example: Fetch user's items from Firestore

```javascript
async fetchUserItems() {
  const result = await this.firebase.getCollection('items', {
    field: 'userId',
    operator: '==',
    value: this.auth.getUser().id
  });

  if (result.success) {
    console.log('Items:', result.data);
  }
}
```

### Example: Update user profile

```javascript
async updateUserProfile(name) {
  const result = await this.firebase.updateDocument(
    'users',
    this.auth.getUser().id,
    { displayName: name }
  );

  if (result.success) {
    this.utilities.showSuccess('Profile updated!');
  }
}
```

---

## Security Rules (Important!)

### Set Firestore Security Rules

1. Go to Firebase Console → **Firestore Database** → **Rules**
2. Replace with:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    
    // Users can only read/write their own data
    match /users/{userId} {
      allow read, write: if request.auth.uid == userId;
    }
    
    // Items belong to users
    match /items/{itemId} {
      allow read, write: if request.auth.uid == resource.data.userId;
      allow create: if request.auth.uid == request.resource.data.userId;
    }
  }
}
```

**This prevents users from accessing other users' data.**

---

## Troubleshooting

### Auth not persisting
- Check browser console for errors
- Verify Firebase config in `config.js`
- Check Firebase project has Email/Password enabled

### CORS errors
- Usually means Firebase SDK not loading
- Check CDN URLs in `index.html` have correct version

### Firestore queries not working
- Ensure Cloud Firestore is created in Firebase console
- Check collection names match exactly
- Verify security rules allow the operation

### File not found errors
- Ensure all files are created in correct directories
- Check import paths in `main.js`

---

## Next Steps

1. ✅ Set up Firestore collections for your app
2. ✅ Create custom page templates
3. ✅ Add form validation
4. ✅ Implement error handling
5. ✅ Deploy to Firebase Hosting

**Firebase is now integrated!** 🎉

