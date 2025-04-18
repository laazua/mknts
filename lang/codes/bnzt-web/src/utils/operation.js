
export function GradeDistNum(data) {
    let level = []
    data.forEach(v => {
        level.push(v._source.properties.role_level)
    })

    return level.reduce((prev, next) => {
        prev[next] = (prev[next] + 1) || 1
        return prev
    },{})
}