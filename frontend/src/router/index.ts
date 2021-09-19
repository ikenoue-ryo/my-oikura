import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '../views/Home.vue'
import OfferForm from '../views/OfferForm.vue'
import LoginForm from '../views/LoginForm.vue'
import Mypage from '../views/Mypage.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/offer-form',
    name: 'OfferForm',
    component: OfferForm
  },
  {
    path: '/login',
    name: 'LoginForm',
    component: LoginForm
  },
  {
    path: '/mypage',
    name: 'Mypage',
    component: Mypage
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
