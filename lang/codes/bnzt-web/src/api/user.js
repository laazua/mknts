import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/user/api/login',
    method: 'post',
    data
  })
}

export function getInfo(data) {
  return request({
    url: '/user/api/users',
    method: 'get',
    params: data
  })
}

// 获取动态路由
export function getMoveRoute() {
  return request({
    url: '/',
    method: 'get'
  })
}

// 添加用户
export function addUser(data) {
  return request({
    url: '/user/api/users',
    method: 'post',
    data
  })
 
}

// 获取用户列表
export function getUserLists() {
  return request({
    url: '/user/api/users',
    method: 'get'
  })
}

// 更新用户
export function updateUser(data) {
  return request({
    url: "/user/api/users",
    method: "put",
    data
  })
}

// 删除用户
export function delUser(data) {
  return request({
    url: '/user/api/users',
    method: 'delete',
    data
  })
}

// 用户分配角色
export function userRole(data) {
  return request({
    url: '/user/api/users',
    method: 'patch',
    data
  })
}

// 获取角色列表
export function getRoleLists() {
  return request({
    url: "/role/api/roles",
    method: "get"
  })
}

// 删除角色列表
export function delRole(data) {
  return request({
    url: "/role/api/roles",
    method: "delete",
    data
  })
}

// 添加角色列表
export function addRole(data) {
  return request({
    url: "/role/api/roles",
    method: "post",
    data
  })
}

// 角色分配权限
export function rolePermisson(data) {
  return request({
    url: "/role/api/roles",
    method: "patch",
    data
  })
}

// 获取菜单列表
export function getPermLists() {
  return request({
    url: "/perm/api/perms",
    method: "get"
  })
}

// 删除菜单
export function delPerm(data) {
  return request({
    url: "/perm/api/perms",
    method: "delete",
    data
  })
}

// 添加菜单
export function addPerm(data) {
  return request({
    url: "/perm/api/perms",
    method: "post",
    data
  })
}

export function logout() {
  return request({
    url: '/vue-admin-template/user/logout',
    method: 'post'
  })
}
