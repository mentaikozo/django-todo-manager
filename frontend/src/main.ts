import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})

// vue-router
import router from '@/router'

// icon
import '@mdi/font/css/materialdesignicons.css'

createApp(App).use(vuetify).use(router).mount('#app')
