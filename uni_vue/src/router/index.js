import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import HomeView from '../views/Login.vue'
import Register from '../views/Register.vue'
import Form from '../views/Form.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/form',
    name: 'form',
    component: Form,
    meta: {
      requireLogin: true
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next)=> {
  if(to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated){
    next('/')
  } else {
    next()
  }
})

export default router
