import Vue from 'vue'
import Vuex from 'vuex'
import api from '../services/api'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

const initialState = {
  email: '',
  isLoggedIn: false
}

const authModule = {
  strict: process.env.NODE_ENV !== 'production',
  namespaced: true,
  state: initialState,
  getters: {
    email: state => state.email,
    isLoggedIn: state => state.isLoggedIn,
  },
  mutations: {
    set(state, payload) {
      state.email = payload.user.email
      state.isLoggedIn = true
    },
    clear(state){
      state.email = ''
      state.IsLoggedIn = false
    },
    reset(state) {
      Object.assign(state, getDefaultState())
    }
  },
  actions: {
    // サインアップ
    signup (context, payload) {
      return api.post('/api/user/signup/', {
        'email': payload.email,
        'password': payload.password,
        'name': payload.name,
      })
      .then(response => {
        console.log('response', response)
        // 認証用のトークンをlocalStorageに保存する
        localStorage.setItem('access', response.data.access)
        // ユーザー情報の取得してstoreのユーザー情報を更新
        // return context.dispatch('reload')
      })
    },
    // ログイン
    login (context, payload) {
      return api.post('/api/v1/auth/jwt/create/', {
        'email': payload.email,
        'password': payload.password,
      })
      .then(response => {
        console.log('response', response)
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
    email: null,
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
