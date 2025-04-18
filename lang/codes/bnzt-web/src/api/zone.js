import request from '@/utils/request'


// 区服列表
export function ZoneList() {
    return request({
        url: "/zone/api/zones",
        method: "get"
    })
}

// 添加区服
export function AddZone(data) {
    return request({
        url: "/zone/api/zones",
        method: "post",
        data: data,
        timeout: 600000
    })
}

// 区服操作
export function ManZone(data) {
    return request({
        url: "/zone/api/man",
        method: "post",
        data: data,
        timeout: 600000
    })
}

// 获取主机资源
export function GetHostData(data) {
    return request({
        url: "/zone/api/host",
        method: "post",
        data: data,
        timeout: 600000
    })
}