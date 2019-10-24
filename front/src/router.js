import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from './views/Home.vue'

Vue.use(VueRouter)



export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/about',
            name: 'about',
            component: () => import('./views/About.vue')
        },
        {
            path: '/team',
            name: 'team',
            component: () => import('./views/Team.vue')
        },
        {
            path: '/contact',
            name: 'contact',
            component: () => import('./views/Contact.vue')
        },
        {
            path: '/result',
            name: 'result',
            component: () => import('./views/Result.vue')
        },
    ]
})