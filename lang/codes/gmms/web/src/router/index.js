import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '首页', icon: 'dashboard' }
    }]
  },
  {
    path: '/user',
    component: Layout,
    redirect: '/user',
    name: 'User',
    meta: { title: '用户管理', icon: 'el-icon-user'},
    children: [{
      path: 'usermg',
      name: 'UserMg',
      component: () => import('@/views/user/usermg/index'),
      meta: { title: '用户修改', icon: 'el-icon-s-help'}
    },
    {
      path: 'userlog',
      name: 'UserLog',
      component: () => import('@/views/user/userlog/index'),
      meta: { title: '用户日志', icon: 'el-icon-s-help'}
    }]
  },
  {
    path: '/game',
    component: Layout,
    redirect: '/game',
    name: 'Game',
    meta: { title: '游戏管理', icon: 'el-icon-menu' },
    children: [{
      path: 'gameopen',
      name: 'GameOpen',
      component: () => import('@/views/game/open/index'),
      meta: { title: '资源配置', icon: 'el-icon-s-help' }
    },
    {
      path: 'gameresou',
      name: 'GameResou',
      component: () => import('@/views/game/resou/index'),
      meta: { title: '资源更新', icon: 'el-icon-s-help' }
    },
    {
      path: 'gamezone',
      name: 'GameZone',
      component: () => import('@/views/game/zone/index'),
      meta: { title: '区服管理', icon: 'el-icon-s-help'}
    }]
  },
  {
    path: '/host',
    component: Layout,
    redirect: '/host',
    name: 'Host',
    meta: { title: '主机管理', icon: 'el-icon-menu' },
    children: [{
      path: 'hostresou',
      name: 'HostResou',
      component: () => import('@/views/host/resou/index'),
      meta: { title: '主机资源', icon: 'el-icon-s-help' }
    },
    {
      path: 'hostcmd',
      name: 'HostCmd',
      component: () => import('@/views/host/cmd/index'),
      meta: { title: '主机命令', icon: 'el-icon-s-help' }
    }]
  }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
