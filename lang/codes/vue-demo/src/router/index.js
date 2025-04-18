import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

// 这里的routes命名不能错,不然加载不到路由
const routes = [
  {
    path: '/',
    name: 'Main',
    component: () =>import('../views/main'),
    children: [
      {
        path: '/home',
        name: 'home',
        component: () => import('../views/home')
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router