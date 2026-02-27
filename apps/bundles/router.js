/**
 * Router Class
 * Manages client-side routing using pathname-based navigation (clean URLs)
 * Works with serve.json and _redirects routing configuration
 */

export class Router {
  constructor(config) {
    this.config = config;
    this.currentPath = '/';
    this.previousPath = '/';
    this.listeners = [];
    this.initializeRouter();
  }

  /**
   * Initialize router and listen for URL changes
   */
  initializeRouter() {
    window.addEventListener('popstate', () => this.handleNavigation());
    // Handle initial load
    this.handleNavigation();
  }

  /**
   * Handle navigation when URL pathname changes
   */
  handleNavigation() {
    // Get pathname and remove /pages prefix if present, clean up multiple slashes
    let pathname = window.location.pathname.replace(/^\/pages/, '').replace(/\/+/g, '/') || '/';
    
    // Remove trailing slash unless it's root
    if (pathname !== '/' && pathname.endsWith('/')) {
      pathname = pathname.slice(0, -1);
    }
    
    this.previousPath = this.currentPath;
    this.currentPath = pathname;
    this.notifyListeners();
  }

  /**
   * Navigate to a path using History API
   * @param {string} path - Path to navigate to (e.g., '/dashboard')
   */
  navigate(path) {
    if (this.currentPath !== path) {
      window.history.pushState({ path }, '', path);
      this.handleNavigation();
    }
  }

  /**
   * Get current path
   */
  getCurrentPath() {
    return this.currentPath;
  }

  /**
   * Get previous path
   */
  getPreviousPath() {
    return this.previousPath;
  }

  /**
   * Subscribe to route changes
   * @param {function} callback - Function to call on route change
   */
  onChange(callback) {
    this.listeners.push(callback);
  }

  /**
   * Notify all listeners of route change
   */
  notifyListeners() {
    this.listeners.forEach(callback => callback(this.currentPath));
  }

  /**
   * Get page config for current path
   */
  getCurrentPageConfig() {
    return this.config.pages.find(page => page.path === this.currentPath);
  }

  /**
   * Check if a route exists
   */
  routeExists(path) {
    return this.config.pages.some(page => page.path === path);
  }
}
