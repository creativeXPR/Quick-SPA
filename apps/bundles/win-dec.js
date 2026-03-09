// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-analytics.js";

// Add SDKs for Auth, Firestore, and Storage
import { getAuth, GoogleAuthProvider, 
        signInWithPopup, 
        onAuthStateChanged,
        signInWithEmailAndPassword,
        createUserWithEmailAndPassword,
        setPersistence,
        browserLocalPersistence } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";
import { getFirestore, collection, 
        addDoc, 
        onSnapshot, 
        deleteDoc, 
        doc, 
        updateDoc,
        setDoc,
        getDoc,
        serverTimestamp,
        query,
        where,
        orderBy,
        limit,
        getDocs } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";
import { getStorage, ref, uploadBytes, getDownloadURL, deleteObject } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-storage.js";

// Your web app's Firebase configuration
const firebaseConfig = await import("./config.js")
  .then(module => module.appConfig.auth.firebaseConfig)
  .catch(error => {
    console.error('Error loading Firebase config:', error);
    return null;
  });

if (firebaseConfig) {
  const app = initializeApp(firebaseConfig);
  
  // Initialize services
  const analytics = getAnalytics(app);
  const auth = getAuth(app);
  const db = getFirestore(app);
  const storage = getStorage(app);
  
  window.firebase = {
      app,
      auth,
      GoogleAuthProvider, 
      signInWithPopup, 
      onAuthStateChanged,
      signInWithEmailAndPassword,
      createUserWithEmailAndPassword,
      setPersistence,
      browserLocalPersistence,
      firestore: db,
      storage,
      collection, 
      addDoc, 
      onSnapshot, 
      deleteDoc, 
      doc, 
      updateDoc,
      setDoc,
      getDoc,
      serverTimestamp,
      query,
      where,
      orderBy,
      limit,
      getDocs,
      ref,
      uploadBytes,
      getDownloadURL,
      deleteObject
  };
}
