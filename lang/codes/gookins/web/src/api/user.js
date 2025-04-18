import request from '@/api/request.js'


export const userLogin = (data) => {
  return request({
    url: '/login',
    method: 'post',
    data
  })
}


export const getUsers = () => {
  return request({
    url: '/user/list',
    method: 'get'
  })
}


export const addUser = (data) => {
  return request({
    url: '/user/add',
    method: 'post',
    data
  })
}

export const updateUser = (data) => {
  return request({
    url: '/user/upt',
    method: 'put',
    data
  })
}


export const deleteUser = (id) => {
  return request({
    url: `/user/del/${id}`,
    method: 'delete'
  })
}