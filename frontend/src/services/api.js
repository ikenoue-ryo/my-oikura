import axios from 'axios'
import store from '@/store'

const api = axios.create({
  baseURL: process.env.VUE_APP_ROOT_API,
  timeout: 5000,
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
  console.log("どう？", token);
  if (token) {
    config.headers.Authorization = 'JWT ' + token
    return config
  }
  return config
}, function (error) {
  return Promise.reject(error)
})

// api.interceptors.response.use(response => {
//   console.log("?????", response);
//   console.log("1", localStorage);
//   return response
// })

export default api