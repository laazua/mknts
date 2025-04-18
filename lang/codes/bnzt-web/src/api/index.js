import request from '@/utils/request'


// 登录接口
export function login(data) {
  return request({
    url: '/user/api/login',
    method: 'post',
    data
  })
}

// 获取用户信息
export function getUserInfo(data) {
  return request({
    url: '/user/api/users',
    method: 'get',
    data  
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
export function AddUser(data) {
  return request({
    url: '/user/api/users',
    method: 'post',
    data
  })
 
}

// 获取用户列表
export function GetUserLists() {
  return request({
    url: '/user/api/userlist',
    method: 'get'
  })
}

// 更新用户
export function UpdateUser(data) {
  console.log("xxbbbxxx",data)
  return request({
    url: "/user/api/users",
    method: "put",
    data
  })
}

// 删除用户
export function DelUser(data) {
  return request({
    url: '/user/api/users',
    method: 'delete',
    data
  })
}

// 获取角色列表
export function GetRoleList() {
  return request({
    url: "/role/api/rolelist",
    method: "get"
  })
}

// 删除角色列表
export function DelRole(data) {
  return request({
    url: "/role/api/roles",
    method: "delete",
    data
  })
}

// 添加角色列表
export function AddRole(data) {
  return request({
    url: "/role/api/roles",
    method: "post",
    data
  })
}

// 获取菜单列表
export function GetPermList() {
  return request({
    url: "/perm/api/permlist",
    method: "get"
  })
}

// 删除菜单
export function DelPerm(data) {
  return request({
    url: "/perm/api/perms",
    method: "delete",
    data
  })
}

// 添加菜单
export function AddPerm(data) {
  return request({
    url: "/perm/api/perms",
    method: "post",
    data
  })
}