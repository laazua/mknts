import request from '@/utils/request'


// 区服列表
export function ZoneList() {
    return request({
        url: "/zone/api/zone",
        method: "get"
    })
}

// 添加区服
export function AddZone(data) {
    return request({
        url: "/zone/api/zone",
        method: "post",
        data: data,
        timeout: 600000
    })
}

// 区服操作
export function ManZone(data) {
    return request({
        url: "/zone/api/zone",
        method: "put",
        data: data,
        timeout: 600000
    })
}