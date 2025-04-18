import request from '@/api/request.js'


export const addTask = (data) => {
  return request({
    url: '/task/add',
    method: 'post',
    data
  })
}


export const deleteTask = (id) => {
  return request({
    url: `/task/del/${id}`,
    method: 'delete'
  })
}


export const updateTask = (data) => {
  return request({
    url: '/task/upt',
    method: 'put',
    data
  })
}


export const getTasks = () => {
  return request({
    url: '/task/list',
    method: 'get'
  })
}


export const apiRunTask = (data) => {
  console.log(data)
  return request({
    url: '/task/run',
    method: 'post',
    data
  })
}


export const apiCancelTask = (id) => {
  return request({
    url: `/task/cancel/${id}`,
    method: 'post'
  })
}


export const taskStatus = (name) => {
  return request({
    url: `/task/state/${name}`,
    method: 'get'
  })
}

export const apiToggleTaskDisabled = (name) => {
  return request({
    url: `/task/disable/${name}`,
    method: 'post'
  })
}