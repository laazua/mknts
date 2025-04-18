import axios from 'axios'
import { ElMessage } from 'element-plus'
import { useAuthStore } from '@/store/user.js'

const service = axios.create({
  baseURL: 'http://192.168.165.88:8084',
  timeout: 50000
})

service.interceptors.request.use((config) => {
  const authStore = useAuthStore()
  if (authStore.token) {
    config.headers['Authorization'] = authStore.token
  }
  return config 
}, (error) => {
  ElMessage({
    message: 'Request Failure',
    type: 'error',
    duration: 5000
  })
  return Promise.reject(error)
})

service.interceptors.response.use((response) => {
  // console.log("响应拦截处理: ", response)
  if (response.data.code === 401) {
    // Token has expired, handle logout
    const authStore = useAuthStore()
    authStore.cleanToken()
    ElMessage({
      message: '登录已过期，请重新登录',
      type: 'warning',
      duration: 5000
    })
    return Promise.reject(response.data)
  }

  if (response.data.code !== 200) {
    ElMessage({
      message: response.data.message || 'Response Data Error',
      type: 'error',
      duration: 5000
    })
  }
  
  return response.data
}, (error) => {
  if (error.response && error.response.status === 401) {
    // Token has expired, handle logout
    const authStore = useAuthStore()
    authStore.cleanToken()
    ElMessage({
      message: '登录已过期，请重新登录',
      type: 'warning',
      duration: 5000
    })
  } else {
    ElMessage({
      message: error.message || 'Response Error',
      type: 'error',
      duration: 5000
    })
  }
  return Promise.reject(error)
})

export default service
