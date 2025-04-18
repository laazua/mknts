// 接受请求,调用service层接口方法,
// 出来请求参数,返回响应结果
package endpoint

type Request struct {
    Name     string
    password string
}

type Response struct {
    User *service.User
}
