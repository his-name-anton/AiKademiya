import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'
import './assets/css/main.css'
import 'flowbite'

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

// Initialize Flowbite
import('flowbite').then(({ initFlowbite }) => {
  initFlowbite()
})

// Mount the app
app.mount('#app')