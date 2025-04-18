import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// 导入element-ui
// import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// 按需导入element-ui
import './plugins/element.js'
// 引入axios
import http from 'axios'

Vue.prototype.$http = http
Vue.config.productionTip = false
// Vue.use(ElementUI)

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
