/**
 * Firebase Service Helper
 * Convenient methods for Firestore operations
 * Requires Auth module to be initialized first
 */

export class FirebaseService {
  constructor(auth) {
    this.auth = auth;
    this.firestore = auth.getFirestore ? auth.getFirestore() : null;
    this.initialized = false;
    this.initCheck();
  }

  /**
   * Check if Firebase is properly initialized
   */
  initCheck() {
    if (this.firestore) {
      this.initialized = true;
    }
  }

  /**
   * Add document to collection
   * @param {string} collection - Collection name
   * @param {object} data - Document data
   */
  async addDocument(collection, data) {
    try {
      if (!this.initialized) {
        console.error('Firebase not initialized');
        return { success: false, error: 'Firebase not initialized' };
      }

      const { collection: firestoreCollection, addDoc, serverTimestamp } = window.firebase.firestore;
      const ref = firestoreCollection(this.firestore, collection);
      const docRef = await addDoc(ref, {
        ...data,
        createdAt: serverTimestamp(),
        userId: this.auth.getUser().id
      });
      return { success: true, id: docRef.id };
    } catch (error) {
      console.error('Error adding document:', error);
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

      const { collection: firestoreCollection, doc, getDoc } = window.firebase.firestore;
      const docRef = doc(firestoreCollection(this.firestore, collection), docId);
      const docSnap = await getDoc(docRef);

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

      const { collection: firestoreCollection, query, where, orderBy, getDocs, limit: firestoreLimit } = window.firebase.firestore;
      let q = firestoreCollection(this.firestore, collection);
      let constraints = [];

      if (whereCondition) {
        constraints.push(where(whereCondition.field, whereCondition.operator, whereCondition.value));
      }

      if (orderByCondition) {
        constraints.push(orderBy(orderByCondition.field, orderByCondition.direction || 'asc'));
      }

      if (limit) {
        constraints.push(firestoreLimit(limit));
      }

      if (constraints.length > 0) {
        q = query(q, ...constraints);
      }

      const querySnapshot = await getDocs(q);
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

      const { collection: firestoreCollection, doc, updateDoc, serverTimestamp } = window.firebase.firestore;
      const docRef = doc(firestoreCollection(this.firestore, collection), docId);
      await updateDoc(docRef, {
        ...data,
        updatedAt: serverTimestamp()
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

      const { collection: firestoreCollection, doc, deleteDoc } = window.firebase.firestore;
      const docRef = doc(firestoreCollection(this.firestore, collection), docId);
      await deleteDoc(docRef);
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
      if (!window.firebase.storage) {
        return { success: false, error: 'Storage not available' };
      }

      const { ref, uploadBytes, getDownloadURL } = window.firebase.storage;
      const storage = this.auth.getStorage();
      const storageRef = ref(storage, path);

      await uploadBytes(storageRef, file);
      const url = await getDownloadURL(storageRef);

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
      if (!window.firebase.storage) {
        return { success: false, error: 'Storage not available' };
      }

      const { ref, deleteObject } = window.firebase.storage;
      const storage = this.auth.getStorage();
      const fileRef = ref(storage, path);

      await deleteObject(fileRef);
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

      const { collection: firestoreCollection, query, where, onSnapshot } = window.firebase.firestore;
      let q = firestoreCollection(this.firestore, collection);

      if (whereCondition) {
        q = query(q, where(whereCondition.field, whereCondition.operator, whereCondition.value));
      }

      // Return unsubscribe function
      return onSnapshot(q, (snapshot) => {
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
