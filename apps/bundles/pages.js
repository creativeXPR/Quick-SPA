/**
 * Pages Class
 * Manages page templates and page states
 * Maps router values to corresponding templates
 */

export class Pages {
  constructor(config) {
    this.config = config;
    this.templates = this.initializeTemplates();
    this.currentPage = null;
    this.pageContainer = document.querySelector(config.app.pageContainer);
    console.log('Pages module initialized');
  }

  /**
   * Initialize page templates
   * Templates can be stored as strings or fetched from files
   */
  initializeTemplates() {
    return {
      home: `
        <div class="page page-home">
          <h1>Welcome Home</h1>
          <p>This is the home page template</p>
          <a href="/dashboard" class="btn">Go to Dashboard</a>
        </div>
      `,
      login: `
        <div class="page page-login">
          <div class="login-container">
            <h1>Login</h1>
            <form id="login-form">
              <input type="email" id="email" placeholder="Email" required>
              <input type="password" id="password" placeholder="Password" required>
              <button type="submit" class="btn">Login</button>
            </form>
            <p>Don't have an account? <a href="/register">Register</a></p>
          </div>
        </div>
      `,
      dashboard: `
        <div class="page page-dashboard">
          <h1>Dashboard</h1>
          <p>Welcome to your dashboard</p>
          <div class="dashboard-content">
            <p id="user-info">Loading user info...</p>
          </div>
          <a href="/" class="btn">Back Home</a>
        </div>
      `,
      profile: `
        <div class="page page-profile">
          <h1>User Profile</h1>
          <div class="profile-container">
            <p id="profile-info">Loading profile...</p>
          </div>
          <a href="/dashboard" class="btn">Back to Dashboard</a>
        </div>
      `,
      settings: `
        <div class="page page-settings">
          <h1>Settings</h1>
          <div class="settings-container">
            <button id="logout-btn" class="btn btn-danger">Logout</button>
          </div>
        </div>
      `,
      notFound: `
        <div class="page page-not-found">
          <h1>404 - Page Not Found</h1>
          <p>The page you're looking for doesn't exist.</p>
          <a href="/" class="btn">Go Home</a>
        </div>
      `
    };
  }

  /**
   * Load page template
   * @param {string} templateName - Name of the template to load
   * @returns {string} - HTML template
   */
  getTemplate(templateName) {
    return this.templates[templateName] || this.templates.notFound;
  }

  /**
   * Render page based on route
   * @param {string} path - Current path
   * @param {Auth} authInstance - Auth instance for permission checking
   */
  renderPage(path, authInstance) {
    const pageConfig = this.config.pages.find(page => page.path === path);

    // If page not found, show 404
    if (!pageConfig) {
      this.renderTemplate('notFound');
      this.currentPage = 'notFound';
      return;
    }

    // Check authentication requirement
    if (pageConfig.requireAuth && !authInstance.checkAuth()) {
      // Redirect to login if auth required but not authenticated
      if (window.app && window.app.router) {
        window.app.router.navigate('/login');
      } else {
        window.location.pathname = '/login';
      }
      return;
    }

    // Render template
    this.renderTemplate(pageConfig.template);
    this.currentPage = pageConfig.template;
    document.title = pageConfig.title || 'SPA Template';
  }

  /**
   * Render template to page container
   * @param {string} templateName - Name of template to render
   */
  renderTemplate(templateName) {
    if (!this.pageContainer) {
      console.error('Page container not found');
      return;
    }

    const template = this.getTemplate(templateName);
    this.pageContainer.innerHTML = template;

    // Trigger page-specific initialization
    this.initializePage(templateName);
  }

  /**
   * Initialize page-specific logic
   * Override this method or add page-specific handlers here
   * @param {string} templateName - Name of the page being initialized
   */
  initializePage(templateName) {
    // Page-specific initialization logic
    // Can be extended for different pages
    switch (templateName) {
      case 'login':
        this.initLoginPage();
        break;
      case 'dashboard':
        this.initDashboardPage();
        break;
      case 'profile':
        this.initProfilePage();
        break;
      case 'settings':
        this.initSettingsPage();
        break;
    }
  }

  /**
   * Initialize login page
   */
  initLoginPage() {
    // Add event listeners and logic for login page
    const form = document.querySelector('#login-form');
    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        // Handle login - will be connected to Auth in main.js
      });
    }
  }

  /**
   * Initialize dashboard page
   */
  initDashboardPage() {
    // Add event listeners and logic for dashboard page
  }

  /**
   * Initialize profile page
   */
  initProfilePage() {
    // Add event listeners and logic for profile page
  }

  /**
   * Initialize settings page
   */
  initSettingsPage() {
    // Add event listeners and logic for settings page
    const logoutBtn = document.querySelector('#logout-btn');
    if (logoutBtn) {
      logoutBtn.addEventListener('click', () => {
        // Handle logout - will be connected to Auth in main.js
        if (window.app && window.app.router) {
          window.app.router.navigate('/');
        } else {
          window.location.pathname = '/';
        }
      });
    }
  }

  /**
   * Get current page
   */
  getCurrentPage() {
    return this.currentPage;
  }
}
