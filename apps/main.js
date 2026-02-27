/**
 * Main App Class
 * Master orchestrator that connects all modules
 * Central hub for routing, auth, pages, and utilities
 */

import { appConfig } from './bundles/config.js';
import { Router } from './bundles/router.js';
import { Auth } from './bundles/auth.js';
import { Utilities } from './bundles/utilities.js';
import { Pages } from './bundles/pages.js';

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

    // Render initial page
    this.pages.renderPage(this.router.getCurrentPath(), this.auth);

    console.log('App initialized successfully');
  }

  /**
   * Handle route changes
   * @param {string} path - New route path
   */
  handleRouteChange(path) {
    // Render appropriate page
    this.pages.renderPage(path, this.auth);
    
    // Update app state
    this.state.currentPage = path;

    console.log(`Navigated to: ${path}`);
  }

  /**
   * Set up global event delegation
   * Connect pages to auth and utilities
   */
  setupEventDelegates() {
    // Example: Login form submission
    document.addEventListener('submit', (e) => {
      if (e.target.id === 'login-form') {
        this.handleLoginSubmit(e);
      }
    });

    // Example: Logout button click
    document.addEventListener('click', (e) => {
      if (e.target.id === 'logout-btn') {
        this.handleLogout();
      }
    });
  }

  /**
   * Handle login form submission
   * @param {Event} event - Form submission event
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
   * Get app state
   */
  getState() {
    return this.state;
  }

  /**
   * Update state
   * @param {object} newState - Partial state update
   */
  setState(newState) {
    this.state = { ...this.state, ...newState };
  }

  /**
   * Fetch user data
   */
  async fetchUserData() {
    if (!this.auth.checkAuth()) {
      this.utilities.showError('Not authenticated');
      return null;
    }

    const data = await this.utilities.get(this.config.api.endpoints.users);
    if (data) {
      this.setState({ data });
    }
    return data;
  }
}

/**
 * Initialize and start the app when DOM is ready
 */
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    window.app = new App();
  });
} else {
  window.app = new App();
}
