/**
 * Firebase Service Helper
 * Convenient methods for Firestore operations
 * Requires Auth module to be initialized first
 */

export class FirebaseService {
  constructor(auth) {
    this.auth = auth;
    this.db = null;
    this.storage = null;
    this.initialized = false;
    this.initCheck();
  }

  /**
   * Check if Firebase is properly initialized
   */
  initCheck() {
    if (window.firebase && window.firebase.firestore) {
      this.db = window.firebase.firestore;
      this.storage = window.firebase.storage;
      this.initialized = true;
      console.log('FirebaseService initialized successfully');
    } else {
      console.error('Firebase not loaded - ensure win-dec.js loads before main.js');
    }
  }

  /**
   * Add document to collection with auto-generated ID
   * @param {string} collectionName - Collection name
   * @param {object} data - Document data
   */
  async addDocument(collectionName, data) {
    try {
      if (!this.initialized) {
        return { success: false, error: 'Firebase not initialized' };
      }

      const colRef = window.firebase.collection(this.db, collectionName);
      const docRef = await window.firebase.addDoc(colRef, {
        ...data,
        createdAt: window.firebase.serverTimestamp(),
        userId: this.auth.getUser()?.id
      });
      return { success: true, id: docRef.id };
    } catch (error) {
      console.error('Error adding document:', error);
      return { success: false, error: error.message };
    }
  }

  /**
   * Set document to collection (create or overwrite)
   * @param {string} collectionName - Collection name
   * @param {string} docId - Document ID
   * @param {object} data - Document data
   * @param {boolean} merge - Whether to merge with existing document
   */
  async setDocument(collectionName, data, docId, merge = true) {
    try {
      if (!this.initialized) {
        return { success: false, error: 'Firebase not initialized' };
      }
      
      const docRef = window.firebase.doc(this.db, collectionName, docId);
      await window.firebase.setDoc(docRef, {
        ...data,
        updatedAt: window.firebase.serverTimestamp()
      }, { merge });
      
      return { success: true, id: docId };
    } catch (error) {
      console.error('Error setting document:', error);
      return { success: false, error: error.message };
    }
  }

  /**
   * Get document by ID
   * @param {string} collection - Collection name
   * @param {string} docId - Document ID
   */
  async getDocument(collection, docId) {
    try {
      if (!this.initialized) {
        return { success: false, error: 'Firebase not initialized' };
      }

      const docRef = window.firebase.doc(this.db, collection, docId);
      const docSnap = await window.firebase.getDoc(docRef);

      if (docSnap.exists()) {
        return { success: true, data: { id: docSnap.id, ...docSnap.data() } };
      } else {
        return { success: false, error: 'Document not found' };
      }
    } catch (error) {
      console.error('Error getting document:', error);
      return { success: false, error: error.message };
    }
  }

  /**
   * Get all documents from collection
   * @param {string} collection - Collection name
   * @param {object} whereCondition - Optional: {field, operator, value}
   * @param {object} orderByCondition - Optional: {field, direction}
   * @param {number} limit - Optional: max documents to fetch
   */
  async getCollection(collection, whereCondition = null, orderByCondition = null, limit = null) {
    try {
      if (!this.initialized) {
        return { success: false, error: 'Firebase not initialized' };
      }

      let q = window.firebase.collection(this.db, collection);
      let constraints = [];

      if (whereCondition) {
        constraints.push(window.firebase.where(whereCondition.field, whereCondition.operator, whereCondition.value));
      }

      if (orderByCondition) {
        constraints.push(window.firebase.orderBy(orderByCondition.field, orderByCondition.direction || 'asc'));
      }

      if (limit) {
        constraints.push(window.firebase.limit(limit));
      }

      if (constraints.length > 0) {
        q = window.firebase.query(q, ...constraints);
      }

      const querySnapshot = await window.firebase.getDocs(q);
      const documents = [];
      querySnapshot.forEach((doc) => {
        documents.push({ id: doc.id, ...doc.data() });
      });

      return { success: true, data: documents };
    } catch (error) {
      console.error('Error getting collection:', error);
      return { success: false, error: error.message };
    }
  }

  /**
   * Update document
   * @param {string} collection - Collection name
   * @param {string} docId - Document ID
   * @param {object} data - Data to update
   */
  async updateDocument(collection, docId, data) {
    try {
      if (!this.initialized) {
        return { success: false, error: 'Firebase not initialized' };
      }

      const docRef = window.firebase.doc(this.db, collection, docId);
      await window.firebase.updateDoc(docRef, {
        ...data,
        updatedAt: window.firebase.serverTimestamp()
      });
      return { success: true };
    } catch (error) {
      console.error('Error updating document:', error);
      return { success: false, error: error.message };
    }
  }

  /**
   * Delete document
   * @param {string} collection - Collection name
   * @param {string} docId - Document ID
   */
  async deleteDocument(collection, docId) {
    try {
      if (!this.initialized) {
        return { success: false, error: 'Firebase not initialized' };
      }

      const docRef = window.firebase.doc(this.db, collection, docId);
      await window.firebase.deleteDoc(docRef);
      return { success: true };
    } catch (error) {
      console.error('Error deleting document:', error);
      return { success: false, error: error.message };
    }
  }

  /**
   * Upload file to storage
   * @param {string} path - Storage path
   * @param {File} file - File to upload
   */
  async uploadFile(path, file) {
    try {
      if (!this.storage) {
        return { success: false, error: 'Storage not available' };
      }

      const storageRef = window.firebase.ref(this.storage, path);
      await window.firebase.uploadBytes(storageRef, file);
      const url = await window.firebase.getDownloadURL(storageRef);

      return { success: true, url };
    } catch (error) {
      console.error('Error uploading file:', error);
      return { success: false, error: error.message };
    }
  }

  /**
   * Delete file from storage
   * @param {string} path - Storage path
   */
  async deleteFile(path) {
    try {
      if (!this.storage) {
        return { success: false, error: 'Storage not available' };
      }

      const fileRef = window.firebase.ref(this.storage, path);
      await window.firebase.deleteObject(fileRef);
      return { success: true };
    } catch (error) {
      console.error('Error deleting file:', error);
      return { success: false, error: error.message };
    }
  }

  /**
   * Real-time listener for collection changes
   * @param {string} collection - Collection name
   * @param {function} callback - Callback when data changes
   * @param {object} whereCondition - Optional filter
   */
  listenToCollection(collection, callback, whereCondition = null) {
    try {
      if (!this.initialized) {
        console.error('Firebase not initialized');
        return null;
      }

      let q = window.firebase.collection(this.db, collection);

      if (whereCondition) {
        q = window.firebase.query(q, window.firebase.where(whereCondition.field, whereCondition.operator, whereCondition.value));
      }

      // Return unsubscribe function
      return window.firebase.onSnapshot(q, (snapshot) => {
        const documents = [];
        snapshot.forEach((doc) => {
          documents.push({ id: doc.id, ...doc.data() });
        });
        callback(documents);
      });
    } catch (error) {
      console.error('Error setting up listener:', error);
      return null;
    }
  }
}
