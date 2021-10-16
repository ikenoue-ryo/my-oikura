import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import OfferForm from '../views/OfferForm.vue'
import OfferFormDetail from '../views/OfferFormDetail.vue'
import UserInfoDetail from '../views/UserInfoDetail.vue'
import SignupForm from '../views/SignupForm.vue'
import LoginForm from '../views/LoginForm.vue'
import Mypage from '../views/Mypage.vue'
import OfferUser from '../views/OfferUser.vue'
import ClientLoginForm from '../views/client/ClientLoginForm.vue'
import ClientSignupForm from '../views/client/ClientSignupForm.vue'
import ClientMypage from '../views/client/ClientMypage.vue'
import ClientAuction from '../views/client/ClientAuction.vue'
import ClientShoppage from '../views/client/ClientShoppage.vue'
import ClientContact from '../views/client/ClientContact.vue'
import ClientContactUser from '../views/client/ClientContactUser.vue'
import store from '@/store'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { path: '/', component: Home, meta: { requiresAuth: true } },
    { path: '/mypage/', component: Mypage},
    { path: '/offer-user/:username', component: OfferUser},
    { path: '/signup', component: SignupForm },
    { path: '/login', component: LoginForm },
    { path: '/offer-form', component: OfferForm },
    { path: '/offer-form/:id', component: OfferFormDetail },
    { path: '/offer-form/:username', component: UserInfoDetail },

    { path: '/client/signup', component: ClientSignupForm },
    { path: '/client/login', component: ClientLoginForm },
    { path: '/client/auction', component: ClientAuction },
    // { path: '/client/:userid', component: ClientMypage },
    { path: '/client/shop', component: ClientMypage },
    { path: '/client/shop/:id', component: ClientShoppage },
    { path: '/client/contact', component: ClientContact },
    { path: '/client/contact/:username', component: ClientContactUser },

    // { path: '*', redirect: '/login' },
  ]
})
/**
 * Routerによって画面遷移する際に毎回実行される
 */
router.beforeEach((to, from, next) => {
  const isLoggedIn = store.getters["auth/isLoggedIn"];
  const token = localStorage.getItem("access");
  console.log("to.path=", to.path);
  console.log("isLoggedIn=", isLoggedIn);

  // ログインが必要な画面に遷移しようとした場合
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    // ログインしている状態の場合
    if (isLoggedIn) {
      console.log("User is already logged in. So, free to next.");
      next();

      // ログインしていない状態の場合
    } else {
      // まだ認証用トークンが残っていればユーザー情報を再取得
      if (token != null) {
        console.log("User is not logged in. Trying to reload again.");

        store
          .dispatch("auth/reload")
          .then(() => {
            // 再取得できたらそのまま次へ
            console.log("Succeeded to reload. So, free to next.");
            next();
          })
          .catch(() => {
            // 再取得できなければログイン画面へ
            forceToLoginPage(to, from, next);
          });
      } else {
        // 認証用トークンが無い場合は、ログイン画面へ
        forceToLoginPage(to, from, next);
      }
    }
  } else {
    // ログインが不要な画面であればそのまま次へ
    console.log("Go to public page.");
    next();
  }
});

/**
 * ログイン画面へ強制送還
 */
function forceToLoginPage(to, from, next) {
  console.log("Force user to login page.");
  next({
    path: "/login",
    // 遷移先のURLはクエリ文字列として付加
    query: { next: to.fullPath },
  });
}

export default router
