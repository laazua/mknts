import { asyncRoutes, constantRoutes } from '@/router'

const state = {
  routes: [],
  addRoutes: []
}

const mutations = {
  SET_ROUTES: (state, routes) => {
    state.addRoutes = routes
    state.routes = constantRoutes.concat(routes)
  }
}


// 将菜单信息转成对应的路由信息 动态添加
const actions = {
  menusToRoutes({ commit }, data) {
    return new Promise(resolve => {
      // console.log("xxx", data)
      const menus = []
      menus.push({
        path: '/404',
        redirect: '404',
        hidden: true
      },{
          path: '*',
          redirect: '/404',
          hidden: true
      })
      // 将需要的菜单添加到mainMenu列表中
      const mainMenu = ['user', 'operation', 'player', 'devops']
      mainMenu.forEach(Mmenu => {
          const main = asyncRoutes[Mmenu]
          main.children = []
          main.hidden = false
          data.forEach(Smenu => {
            if (Smenu.PermDesc === Mmenu) {
              main.children.push(asyncRoutes[Smenu.SubDesc])
            }
        })
        if (main.children.length !== 0 ) {
          menus.push(main)
        }
      })
      commit('SET_ROUTES', menus)
      resolve(menus)
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}