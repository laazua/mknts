import request from '@/utils/request'


// 区服列表
export function ZoneList() {
    return request({
        url: "/api/zones",
        method: "get"
    })
}

// 添加区服
export function AddZone(data) {
    return request({
        url: "/api/zone",
        method: "post",
        data: data,
        timeout: 600000
    })
}

// 区服操作
export function ManZone(data) {
    return request({
        url: "/api/zone",
        method: "post",
        data: data,
        timeout: 600000
    })
}

// 获取操作结果
export function GetTasks() {
    return request({
        url: "/api/zone",
        method: "get",
        timeout: 600000
    })
}