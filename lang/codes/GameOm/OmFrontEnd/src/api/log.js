import request from '@/utils/request'


export function GetLog(name) {
    return request({
        url: "/log/api/log/",
        method: 'get',
        params: { name }
    })
}