/**
 * SPA Template Configuration
 * Configure auth, API endpoints, and pages here
 */

export const appConfig = {
  // Authentication Configuration
  auth: {
    type: 'firebase', // Options: 'firebase', 'custom', 'auth0', etc.
    firebaseConfig: {
      apiKey: 'YOUR_API_KEY',
      authDomain: 'your-project.firebaseapp.com',
      projectId: 'your-project-id',
      storageBucket: 'your-project.appspot.com',
      messagingSenderId: 'YOUR_SENDER_ID',
      appId: 'YOUR_APP_ID'
    }
  },

  // API Configuration
  api: {
    baseURL: 'https://api.example.com',
    timeout: 10000,
    endpoints: {
      users: '/users',
      data: '/data',
      products: '/products'
    }
  },

  // Page Routes Configuration
  pages: [
    { path: '/', template: 'home', requireAuth: false, title: 'Home' },
    { path: '/login', template: 'login', requireAuth: false, title: 'Login' },
    { path: '/dashboard', template: 'dashboard', requireAuth: true, title: 'Dashboard' },
    { path: '/profile', template: 'profile', requireAuth: true, title: 'Profile' },
    { path: '/settings', template: 'settings', requireAuth: true, title: 'Settings' }
  ],

  // App Settings
  app: {
    name: 'My SPA App',
    appRoot: '#app-root',
    pageContainer: '#page-container',
    messageBox: '#message-box'
  }
};
