import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'
import './assets/css/main.css'
import { useAuthStore } from './stores/auth'

// Create Vue app
const app = createApp(App)

// Install Pinia store
const pinia = createPinia()
app.use(pinia)

// Install Vue Router
app.use(router)

// Install Toast notifications
app.use(Toast, {
  timeout: 5000,
  closeOnClick: true,
  pauseOnFocusLoss: true,
  pauseOnHover: true,
  draggable: true,
  draggablePercent: 0.6,
  showCloseButtonOnHover: false,
  hideProgressBar: false,
  closeButton: 'button',
  icon: true,
  rtl: false,
  position: 'top-right',
  transition: 'Vue-Toastification__bounce',
})

// Initialize auth before mounting the app
async function initializeApp() {
  try {
    console.log('Initializing auth store before app mount...')
    const authStore = useAuthStore()
    
    // Only initialize if not already initialized (could be done by router guard)
    if (!authStore.isInitialized) {
      await authStore.initializeAuth()
      console.log('Auth store initialized successfully')
    } else {
      console.log('Auth store already initialized, skipping...')
    }
  } catch (error) {
    console.error('Failed to initialize auth store:', error)
  } finally {
    // Mount the app regardless of auth initialization result
    app.mount('#app')
  }
}

// Start the initialization process
initializeApp()