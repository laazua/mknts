import axios from "./axios"

export const apiTest = (param) => {
  return axios.request({
    url: '/api/example',
    method: 'post',
    data: param
  })
}