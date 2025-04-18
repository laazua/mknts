import request from '@/utils/request'
import qs from 'qs'

export function login(data) {
  return request({
    url: '/api/login',
    method: 'post',
    data: qs.stringify(data),
    headers: {
      'content-type': 'application/x-www-form-urlencoded'
    }
  })
}

export function getInfo(token) {
  return request({
    url: '/api/user',
    method: 'get',
    params: { token }
  })
}

export function GetUserList(token) {
  return request({
    url: '/api/users',
    method: 'get',
    params: { token }
  })
}

export function AddUser(data) {
  return request({
    url: '/api/user',
    method: 'post',
    data: data
  })
}

export function DelUser(data) {
  return request({
    url: '/api/user',
    method: 'delete',
    data: data
  })
}

export function logout() {
  return request({
    url: '/api/logout',
    method: 'post'
  })
}
