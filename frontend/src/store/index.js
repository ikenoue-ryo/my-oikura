import Vue from 'vue'
import Vuex from 'vuex'
import api from '../services/api'
import createPersistedState from "vuex-persistedstate";

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
    },
    reset(state) {
      Object.assign(state, getDefaultState())
    }
  },
  actions: {
    // ログイン
    login (context, payload) {
      return api.post('/api/v1/auth/jwt/create/', {
        'email': payload.email,
        'password': payload.password,
      })
      .then(response => {
        console.log(response)
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
      context.commit('reset')
    },
    // ユーザー情報更新
    reload (context) {
      return api.get('/api/v1/auth/users/me')
        .then(response => {
          const user = response.data
          context.commit('set', { user: user })
          return user
        })
    }
  },
};

// stateの初期値としたい任意のデータを定義する
function getDefaultState() {
  return {
    username: null,
    isLoggedIn: null,
  }
}

const store = new Vuex.Store({
  modules: {
    
    auth: authModule,
  },
  plugins: [createPersistedState({
    key: 'OikuraApp',
    paths: ['auth'],
    storage: window.sessionStorage
})]
})

export default store
