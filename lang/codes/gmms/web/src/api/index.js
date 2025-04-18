import request from "@/utils/request"
import qs from "qs"
// 发送api请求


export function login(data) {
  return request({
    url: '/user/api/login',
    method: 'post',
    data: qs.stringify(data)
  })
}

export function getInfo() {
  return request({
    url: '/user/api/userinfo',
    method: 'get',
  })
}

export function getUserLists() {
  return request({
    url: '/user/api/userlists',
    method: 'get'
  })
}

export function delUser(data) {
  return request({
    url: '/user/api/deluser',
    method: 'post',
    data
  })
}

export function register(data) {
  return request({
    url: '/user/api/register',
    method: 'post',
    data
  })
}

export function getUserLog(data) {
  return request({
    url: '/user/api/userlog',
    method: 'post',
    data
  })
}

// game api
export function createProName(data) {
  return request({
    url: '/game/api/createzones',
    method: 'post',
    data
  })
}

export function getProNames(params) {
  return request({
    url: '/game/api/getpronames',
    method: 'get'
  })
}

export function openServeZone(data) {
  return request({
    url: '/game/api/openzone',
    method: 'post',
    timeout: 600000,
    data
  })
}

export function svnUpHost(params) {
  return request({
    url: '/game/api/svnuphost',
    method: 'get',
    timeout: 600000,
    params
  })
}


export function getZones(params) {
  return request({
    url: '/game/api/zonelist',
    method: 'get',
    params
  })
}

export function zoneCmd(data) {
  return request({
    url: '/game/api/zonecmd',
    method: 'post',
    timeout: 6000000,
    data
  })
}