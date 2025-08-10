import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import QrGenerator from '../pages/QrGenerator.vue'
import About from '../pages/About.vue'

const routes = [
    { path: '/', name: 'home', component: Home },
    { path: '/qr', name: 'qr', component: QrGenerator },
    { path: '/about', name: 'about', component: About }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router