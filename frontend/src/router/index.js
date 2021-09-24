import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import OfferForm from '../views/OfferForm.vue'
import OfferFormDetail from '../views/OfferFormDetail.vue'
import UserInfoDetail from '../views/UserInfoDetail.vue'
import LoginForm from '../views/LoginForm.vue'
import Mypage from '../views/Mypage.vue'
import store from '@/store'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { path: '/', component: Home, meta: { requiresAuth: true } },
    { path: '/mypage', component: Mypage, meta: { requiresAuth: true } },
    { path: '/login', component: LoginForm },
    { path: '/offer-form', component: OfferForm },
    { path: '/offer-form/:id', component: OfferFormDetail },
    { path: '/offer-form/:username', component: UserInfoDetail },
    { path: '*', redirect: '/' },
  ]
})

router.beforeEach((to, from, next) => {

  const isLoggedIn = store.getters['auth/isLoggedIn']
  // const token = localStorage.getItem('access')
  console.log("ログイン状態", isLoggedIn)

  // ログインしている場合
  if (isLoggedIn) {
    console.log('Loginしています')
    next()
  } else {
    // ログインしていない場合
    console.log('Loginしてください')
    next()
  }

})

export default router
