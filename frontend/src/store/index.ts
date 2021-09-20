import Vue from 'vue'
import Vuex from 'vuex'
import api from '@/services/api'

Vue.use(Vuex)

const authModule = {
  strict: process.env.NODE_ENV !== 'production',
  namespaced: true,
  state: {
    username: '',
    isLoggedIn: false,
  },
  getters: {
    username: state => state.username,
    isLoggedIn: state => state.isLoggedIn,
  },
  mutations: {
    set(state, payload) {
      state.username = payload.user.username
      state.isLoggedIn = true
    },
    clear(state){
      state.username = ''
      state.IsLoggedIn = false
    }
  },
  actions: {
    // ログイン
    login (context, payload) {
      return api.post('/auth/jwt/create/', {
        'username': payload.username,
        'password': payload.password,
      })
      .then(response => {
        // 認証用のトークンをlocalStorageに保存する
        localStorage.setItem('access', response.data.access)
        // ユーザー情報の取得してstoreのユーザー情報を更新
        return context.dispatch('reload')
      })
    },
    // ログアウト
    logout (context) {
      localStorage.removeItem('access')
      context.commit('clear')
    }
  },
};

const store = new Vuex.Store({
  modules: {
    auth: authModule,
  }
})

export default store
