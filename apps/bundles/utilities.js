/**
 * Utilities Class
 * Provides helper functions: API calls, DOM manipulation, messaging, etc.
 */

export class Utilities {
  constructor(config) {
    this.config = config;
    this.apiBaseURL = config.api.baseURL;
    this.messageBox = document.querySelector(config.app.messageBox);
  }

  /**
   * =============== API CALLS ===============
   */

  /**
   * Make GET request
   * @param {string} endpoint - API endpoint
   * @param {object} options - Fetch options
   */
  async get(endpoint, options = {}) {
    try {
      const response = await fetch(`${this.apiBaseURL}${endpoint}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json', ...options.headers },
        ...options
      });
      return await this.handleResponse(response);
    } catch (error) {
      this.showError(`Error fetching from ${endpoint}: ${error.message}`);
      return null;
    }
  }

  /**
   * Make POST request
   * @param {string} endpoint - API endpoint
   * @param {object} data - Request body
   * @param {object} options - Fetch options
   */
  async post(endpoint, data = {}, options = {}) {
    try {
      const response = await fetch(`${this.apiBaseURL}${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', ...options.headers },
        body: JSON.stringify(data),
        ...options
      });
      return await this.handleResponse(response);
    } catch (error) {
      this.showError(`Error posting to ${endpoint}: ${error.message}`);
      return null;
    }
  }

  /**
   * Make PUT request
   * @param {string} endpoint - API endpoint
   * @param {object} data - Request body
   * @param {object} options - Fetch options
   */
  async put(endpoint, data = {}, options = {}) {
    try {
      const response = await fetch(`${this.apiBaseURL}${endpoint}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', ...options.headers },
        body: JSON.stringify(data),
        ...options
      });
      return await this.handleResponse(response);
    } catch (error) {
      this.showError(`Error updating ${endpoint}: ${error.message}`);
      return null;
    }
  }

  /**
   * Make DELETE request
   * @param {string} endpoint - API endpoint
   * @param {object} options - Fetch options
   */
  async delete(endpoint, options = {}) {
    try {
      const response = await fetch(`${this.apiBaseURL}${endpoint}`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json', ...options.headers },
        ...options
      });
      return await this.handleResponse(response);
    } catch (error) {
      this.showError(`Error deleting ${endpoint}: ${error.message}`);
      return null;
    }
  }

  /**
   * Handle API response
   */
  async handleResponse(response) {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    return await response.json();
  }

  /**
   * =============== DOM MANIPULATION ===============
   */

  /**
   * Get element by selector
   * @param {string} selector - CSS selector
   */
  querySelector(selector) {
    return document.querySelector(selector);
  }

  /**
   * Get all elements by selector
   * @param {string} selector - CSS selector
   */
  querySelectorAll(selector) {
    return document.querySelectorAll(selector);
  }

  /**
   * Set innerHTML
   * @param {string} selector - CSS selector
   * @param {string} html - HTML content
   */
  setHTML(selector, html) {
    const element = this.querySelector(selector);
    if (element) element.innerHTML = html;
  }

  /**
   * Add event listener
   * @param {string} selector - CSS selector
   * @param {string} event - Event name
   * @param {function} callback - Callback function
   */
  addEventListener(selector, event, callback) {
    const element = this.querySelector(selector);
    if (element) element.addEventListener(event, callback);
  }

  /**
   * Add class to element
   * @param {string} selector - CSS selector
   * @param {string} className - Class name
   */
  addClass(selector, className) {
    const element = this.querySelector(selector);
    if (element) element.classList.add(className);
  }

  /**
   * Remove class from element
   * @param {string} selector - CSS selector
   * @param {string} className - Class name
   */
  removeClass(selector, className) {
    const element = this.querySelector(selector);
    if (element) element.classList.remove(className);
  }

  /**
   * =============== MESSAGING ===============
   */

  /**
   * Show success message
   * @param {string} message - Message text
   * @param {number} duration - Duration in ms (default: 3000)
   */
  showSuccess(message, duration = 3000) {
    this.showMessage(message, 'success', duration);
  }

  /**
   * Show error message
   * @param {string} message - Message text
   * @param {number} duration - Duration in ms (default: 5000)
   */
  showError(message, duration = 5000) {
    this.showMessage(message, 'error', duration);
  }

  /**
   * Show info message
   * @param {string} message - Message text
   * @param {number} duration - Duration in ms (default: 3000)
   */
  showInfo(message, duration = 3000) {
    this.showMessage(message, 'info', duration);
  }

  /**
   * Show message in message box
   * @param {string} message - Message text
   * @param {string} type - Message type (success, error, info, warning)
   * @param {number} duration - Duration to show message
   */
  showMessage(message, type = 'info', duration = 3000) {
    if (!this.messageBox) return;

    const messageEl = document.createElement('div');
    messageEl.className = `message message-${type}`;
    messageEl.textContent = message;

    this.messageBox.appendChild(messageEl);

    if (duration > 0) {
      setTimeout(() => messageEl.remove(), duration);
    }
  }

  /**
   * =============== DATA FORMATTING ===============
   */

  /**
   * Parse JSON safely
   * @param {string} json - JSON string
   */
  parseJSON(json) {
    try {
      return JSON.parse(json);
    } catch (error) {
      console.error('JSON parse error:', error);
      return null;
    }
  }

  /**
   * Stringify object
   * @param {object} obj - Object to stringify
   */
  stringifyJSON(obj) {
    return JSON.stringify(obj, null, 2);
  }

  /**
   * =============== UTILITY HELPERS ===============
   */

  /**
   * Debounce function
   * @param {function} func - Function to debounce
   * @param {number} delay - Delay in ms
   */
  debounce(func, delay = 300) {
    let timeoutId;
    return (...args) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => func(...args), delay);
    };
  }

  /**
   * Throttle function
   * @param {function} func - Function to throttle
   * @param {number} delay - Delay in ms
   */
  throttle(func, delay = 300) {
    let lastCall = 0;
    return (...args) => {
      const now = Date.now();
      if (now - lastCall >= delay) {
        lastCall = now;
        func(...args);
      }
    };
  }

  /**
   * Generate unique ID
   */
  generateId() {
    return `${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  }
}
