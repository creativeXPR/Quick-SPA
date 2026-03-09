/**
 * Auth Class
 * Flexible authentication handling - adaptable to firebase, custom, auth0, etc.
 */

export class Auth {
  constructor(config) {
    this.config = config;
    this.user = null;
    this.authType = config.auth.type;
    this.isAuthenticated = false;
    this.initializeAuth();
  }

  /**
   * Initialize authentication based on config type
   */
  initializeAuth() {
    switch (this.authType) {
      case 'firebase':
        this.initializeFirebase();
        break;
      case 'custom':
        this.initializeCustom();
        break;
      default:
        console.warn(`Auth type '${this.authType}' not recognized`);
    }
  }

  /**
   * Initialize Firebase Auth
   */
  initializeFirebase() {
    if (!window.firebase) {
      console.error('Firebase SDK not loaded - ensure win-dec.js loads before main.js');
      return;
    }

    // Get Firebase instances from win-dec.js
    this.firebaseApp = window.firebase.app;
    this.firebaseAuth = window.firebase.auth;
    this.firestore = window.firebase.firestore;
    this.storage = window.firebase.storage;

    // Set persistence to LOCAL to prevent auto-logout from storage events
    if (window.firebase.setPersistence && window.firebase.browserLocalPersistence) {
      window.firebase.setPersistence(this.firebaseAuth, window.firebase.browserLocalPersistence)
        .then(() => {
          console.log('[Auth.initializeFirebase] persistence set to LOCAL');
        })
        .catch((error) => {
          console.warn('[Auth.initializeFirebase] failed to set persistence (non-critical)', error);
        });
    }

    // Set up auth state listener
    window.firebase.onAuthStateChanged(this.firebaseAuth, (firebaseUser) => {
      const timestamp = new Date().toISOString();
      console.log('[Auth.onAuthStateChanged] callback triggered', { 
        hasUser: !!firebaseUser, 
        uid: firebaseUser?.uid,
        timestamp,
        wasAuthenticated: this.isAuthenticated,
        transition: this.isAuthenticated ? (firebaseUser ? 'staying-logged-in' : 'LOGGING-OUT') : (firebaseUser ? 'LOGGING-IN' : 'staying-logged-out')
      });
      if (firebaseUser) {
        this.user = {
          id: firebaseUser.uid,
          email: firebaseUser.email,
          displayName: firebaseUser.displayName || '',
          photoURL: firebaseUser.photoURL || ''
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
   * Initialize Custom Auth
   */
  initializeCustom() {
    // Custom auth implementation would go here
    console.log('Custom Auth initialized');
  }

  /**
   * Login with credentials (flexible - adapter pattern)
   * @param {string} email - User email
   * @param {string} password - User password
   */
  async login(email, password) {
    try {
      if (this.authType === 'firebase') {
        const cred = await window.firebase.signInWithEmailAndPassword(this.firebaseAuth, email, password);
        const u = cred.user;
        this.user = {
          id: u.uid,
          email: u.email,
          displayName: u.displayName || '',
          photoURL: u.photoURL || ''
        };
        this.isAuthenticated = true;
        this.saveUserSession();
        return { success: true, user: this.user };
      }

      return { success: false, error: 'Unsupported auth type' };
    } catch (error) {
      console.error('Login error:', error);
      return { success: false, error: this.mapFirebaseError(error.code) || error.message };
    }
  }

  /**
   * Logout user
   */
  async logout() {
    try {
      // Sign out from Firebase
      if (this.authType === 'firebase' && this.firebaseAuth && window.firebase) {
        await this.firebaseAuth.signOut();
      }
      
      // Clear local state
      this.user = null;
      this.isAuthenticated = false;
      localStorage.removeItem('user_session');
      return { success: true };
    } catch (error) {
      console.error('Logout error:', error);
      return { success: false, error: error.message };
    }
  }

  /**
   * Register new user
   * @param {object} userData - User data (email, password, etc.)
   */
  async register(userData) {
    try {
      if (this.authType === 'firebase') {
        const { username, universityRole, email, password, displayName } = userData;
        const cred = await window.firebase.createUserWithEmailAndPassword(this.firebaseAuth, email, password);

        // Update profile with display name
        if (displayName && cred.user.updateProfile) {
          await cred.user.updateProfile({ displayName });
        }

        this.user = {
          id: cred.user.uid,
          email: cred.user.email,
          username: username || '',
          universityRole: universityRole || '',
          photoURL: cred.user.photoURL || ''
        };
        this.isAuthenticated = true;
        this.saveUserSession();
        return { success: true, user: this.user };
      }

      return { success: false, error: 'Unsupported auth type' };
    } catch (error) {
      console.error('Registration error:', this.mapFirebaseError(error.code) || error.message);
      return { success: false, error: this.mapFirebaseError(error.code) || error.message };
    }
  }

  /**
   * Map Firebase Error Code
   * @param {string} errorCode - Firebase error code
   * @returns {string} User-friendly error message
   */
  mapFirebaseError(errorCode) {
    const errorMap = {
      'auth/user-not-found': 'Email not registered. Please sign up.',
      'auth/wrong-password': 'Incorrect password. Please try again.',
      'auth/email-already-in-use': 'Email already has an account.',
      'auth/weak-password': 'Password must meet all strength criteria.',
      'auth/invalid-email': 'Please enter a valid email.',
      'auth/too-many-requests': 'Too many failed attempts. Try again later.',
      'auth/network-request-failed': 'Connection failed. Check your internet.',
    };
    return errorMap[errorCode] || 'An error occurred. Please try again.';
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
    if (saved && !this.isAuthenticated) {
      try {
        this.user = JSON.parse(saved);
      } catch {
        localStorage.removeItem('user_session');
      }
    }
  }

  /**
   * Get Firestore instance
   */
  getFirestore() {
    return this.firestore;
  }

  /**
   * Get Storage instance
   */
  getStorage() {
    return this.storage;
  }

  /**
   * Get Firebase instance (for firebase-service.js compatibility)
   */
  getDatabase() {
    return window.firebase;
  }
}
