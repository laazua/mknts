import axios from 'axios'
import config from '../config'

const baseUrl = process.env.NODE_ENV === 'development' ? config.baseUrl.dev: config.baseUrl.pro

class HttpRequest {
  constructor(baseUrl) {
    this.baseUrl = baseUrl
  }
  getInsideConfig() {
    const config = {
      baseUrl: this.baseUrl,
      header: {}
    }
    return config
  }
  interceptor(instance) {
    instance.interceptor.request.use(function(config) {
      // 做点什么
      return config
    }, function(error) {
      // 做点什么
      return Promise.reject(error)
    })
    instance.interceptor.response.use(function(response) {
      // 做点什么
      return response
    }, function(error) {
       // 做点什么  
      return Promise.reject(error)
    })
  }
  request(options) {
    const instance = axios.create()
    options = { ...this.getInsideConfig(), ...options }
    this.interceptor(instance)
    return instance(options)
  }
}

export default new HttpRequest(baseUrl)