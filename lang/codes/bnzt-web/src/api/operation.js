import request from '@/utils/request'

// 充值排行查询
export function Recharank(data) {
    return request({
        url: '/oa/api/recharank',
        method: 'post',
        data
    })
}

// 等级分布
export function GradeDist(data) {
    return request({
        url: '/oa/api/gradedist',
        method: 'post',
        data
    })
}

// 数据查询
export function CountData(data) {
    return request({
        url: '/oa/api/countdata',
        method: 'post',
        data
    })
}