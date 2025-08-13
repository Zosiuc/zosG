import { createApp } from 'vue'
import './assets/style.css'
import App from './App.vue'
import router from './router'
import { createI18n } from 'vue-i18n'
import { Analytics } from '@vercel/analytics/vue'




import en from './locales/en.json'
import nl from './locales/nl.json'
import ar from './locales/ar.json'

const i18n = createI18n({
    legacy: false,
    locale: 'en', // standaard
    fallbackLocale: 'en',
    messages: { en, nl, ar }
})

const app = createApp(App)
app.use(router)
app.use(i18n)
app.use(Analytics)
app.mount('#app')
