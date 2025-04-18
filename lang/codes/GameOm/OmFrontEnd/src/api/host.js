import request from '@/utils/request'

export function GetHostResource() {
    return request({
        url: '/host/api/host',
        method: 'get',
        timeout: 6000000
    })
}
