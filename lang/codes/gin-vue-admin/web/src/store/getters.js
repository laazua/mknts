const getters = {
  sidebar: state => state.app.sidebar,
  device: state => state.app.device,
  token: state => state.user.token,
  avatar: state => state.user.avatar,
  name: state => state.user.name,
  visitedViews: state => state.tagsView.visitedViews, // 新增
  cachedViews: state => state.tagsView.cachedViews, // 新增
  permission_routes: state => state.permission.routes // 新增
}
export default getters
