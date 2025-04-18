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
// 基本路由表
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },
  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '首页', icon: 'dashboard' }
    }]
  }
]

// 静态路由表
export const asyncRoutes = {
  /*===================用户管理===================*/
  // 一级菜单
  "user": {
    path: "/user",
    component: Layout,
    meta: {title: "系统管理", icon: "el-icon-menu"}
  },
  // 二级菜单
  "用户列表": {
    path: "/userlist",
    component: () => import("@/views/user/userlist/index"),
    meta: {title: "用户列表", icon: "el-icon-help"}
  },
  // 二级菜单
  "角色列表": {
    path: "/rolelist",
    component: () => import("@/views/user/rolelist/index"),
    meta: {title: "角色列表", icon: "el-icon-help"}
  },
  // 二级菜单
  "权限列表": {
    path: "/permlist",
    component: () => import("@/views/user/permlist/index"),
    meta: {title: "权限列表", icon: "el-icon-help"}
  },
  /*==================运营管理====================*/
  // 一级菜单
  "operation": {
    path: "/operation",
    component: Layout,
    meta: {title: "运营管理", icon: "el-icon-menu"}
  },
  // 二级菜单
  "充值排行": {
    path: "/recharank",
    component: () => import("@/views/operation/recharank/index"),
    meta: {title: "充值排行", icon: "el-icon-help"}
  },
  // 二级菜单
  "等级分布": {
    path: "/gradedist",
    component: () => import("@/views/operation/gradedist"),
    meta: {title: "等级分布", icon: "el-icon-help"}
  },
  // 二级菜单
  "滚服数据": {
    path: "/rollsdata",
    component: () => import("@/views/operation/rollsdata/index"),
    meta: {title: "滚服数据", icon: "el-icon-help"}
  },
  // 二级菜单
  "留存数据": {
    path: "/retendata",
    component: () => import("@/views/operation/retendata/index"),
    meta: {title: "留存数据", icon: "el-icon-help"}
  },
  // 二级菜单
  "LTV数据": {
    path: "/ltvsdata",
    component: () => import("@/views/operation/ltvsdata/index"),
    meta: {title: "LTV数据", icon: "el-icon-help"}
  },
  // 二级菜单
  "数据查询": {
    path: "/countdata",
    component: () => import("@/views/operation/countdata"),
    meta: {title: "数据查询", icon: "el-icon-help"}
  },
  // 二级菜单
  "VIP等级": {
    path: "/vipsdata",
    component: () => import("@/views/operation/vipsdata/index"),
    meta: {title: "VIP等级", icon: "el-icon-help"}
  },
  /*===============玩家相关==============*/
  // 一级菜单
  "player": {
    path: "/player",
    component: Layout,
    meta: {title: "玩家相关", icon: "el-icon-menu"}
  },
  // 二级菜单
  "订单查询": {
    path: "/orderdata",
    component: () => import("@/views/player/orderdata/index"),
    meta: {title: "订单查询", icon: "el-icon-help"}
  },
  // 二级菜单
  "货币查询": {
    path: "/currdata",
    component: () => import("@/views/player/currdata/index"),
    meta: {title: "货币查询", icon: "el-icon-help"}
  },
  // 二级菜单
  "角色查询": {
    path: "/roledata",
    component: () => import("@/views/player/roledata/index"),
    meta: {title: "角色查询", icon: "el-icon-help"}
  },
  /*==============gm工具===============*/
  // 一级菜单
  "gmtools": {
    path: "/gmtools",
    component: Layout,
    meta: {title: "GM工具", icon: "el-icon-menu"}
  },
  // 二级菜单
  "awardRecord": {
    path: "/awardrecord",
    component: () => import("@/views/gmtools/awardrecord/index"),
    meta: {title: "发奖记录", icon: "el-icon-help"}
  },
  // 二级菜单
  "announQuery": {
    path: "/announquery",
    component: () => import("@/views/gmtools/announquery/index"),
    meta: {title: "公告查询", icon: "el-icon-help"}
  },
  // 二级菜单
  "zoneAnnoun": {
    path: "/zoneannoun",
    component: () => import("@/views/gmtools/zoneannoun/index"),
    meta: {title: "区服公告", icon: "el-icon-help"}
  },
  // 二级菜单
  "zoneRewards": {
    path: "/zonerewards",
    component: () => import("@/views/gmtools/zonerewards/index"),
    meta: {title: "区服奖励", icon: "el-icon-help"}
  },
  // 二级菜单
  "homePage": {
    path: "/homepage",
    component: () => import("@/views/gmtools/homepage/index"),
    meta: {title: "首页公告", icon: "el-icon-help"}
  },
  // 二级菜单
  "playerAward": {
    path: "/playeraward",
    component: () => import("@/views/gmtools/playeraward/index"),
    meta: {title: "玩家奖励", icon: "el-icon-help"}
  },
  /*==============礼包相关=============*/
  // 一级菜单
  "gifts": {
    path: "/gifts",
    component: Layout,
    meta:{title: "礼包管理", icon: "el-icon-menu"}
  },
  // 二级菜单
  "activeList": {
    path: "/activelist",
    component: () => import("@/views/gifts/activelist/index"),
    meta: {title: "激活码列表", icon: "el-icon-help" }
  },
  // 二级菜单
  "activeData": {
    path: "/activedata",
    component: () => import("@/views/gifts/activedata/index"),
    meta: {title: "激活码数据", icon: "el-icon-help"}
  },
  // 二级菜单
  "configPackage": {
    path: "/configpackage",
    component: () => import("@/views/gifts/configpackage/index"),
    meta: {title: "配置礼包", icon: "el-icon-help"}
  },
  // ===============运维管理============
  // 一级菜单
  "devops": {
    path: "/devops",
    component: Layout,
    meta: {title: "运维管理", icon: "el-icon-menu"}
  },
  // 二级菜单
  "区服列表": {
    path: "/zonelist",
    component: () => import("@/views/devops/zonelist/index"),
    meta: {title: "区服列表", icon: "el-icon-help"}
  },
  // 二级菜单
  "主机状态": {
    path: "/hostlist",
    component: () => import("@/views/devops/hostlist/index"),
    meta: {title: "主机状态", icon: "el-icon-help"}
  }
}

const createRouter = () => new Router({
  mode: 'hash',
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