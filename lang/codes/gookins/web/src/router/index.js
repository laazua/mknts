import { useAuthStore } from '@/store/user.js'
import { createRouter, createWebHistory } from "vue-router"

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/login/index.vue')
  },
  {
    path: '/',
    name: 'Layout',
    component: () => import('@/components/Layout.vue'),
    children: [
      {
        path: '/home',
        name: 'Home',
        component: () => import('@/views/home/index.vue'),
        meta: { title: '首页', icon: 'HomeFilled', requiresAuth: true }
      },
      {
        path: 'user',
        name: 'User',
        component: () => import('@/views/user/index.vue'),
        meta: { title: '用户管理', icon: 'Avatar', requiresAuth: true }
      },
      {
        path: 'task',
        name: 'Task',
        component: () => import('@/views/task/index.vue'),
        meta: { title: '任务管理', icon: 'Grid', requiresAuth: true}
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})


// vue-router 导航守卫
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  if (to.matched.some(record => record.meta.requiresAuth) && !authStore.token) {
    // 如果路由需要认证且没有 token，重定向到登录页面
    next('/login')
  } else {
    next()
  }
})
export default router