import axios from 'axios'

const api = axios.create({
  baseURL: process.env.VUE_APP_ROOT_API,
  timeout: 50000,
  headers: {
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
  }
})

// 共通前処理
api.interceptors.request.use(function (config) {
  // メッセージをクリア
  // 認証用トークンがあればリクエストヘッダに乗せる
  const token = localStorage.getItem('access')
  if (token) {
    config.headers.Authorization = 'JWT ' + token
    return config
  }
  return config
}, function (error) {
  return Promise.reject(error)
})

export default api
