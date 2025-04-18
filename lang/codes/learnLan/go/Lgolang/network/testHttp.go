/*
客户端:
http变成基本方法:
func (c *Client) Get(url string) (r *Response, err error)
func (c *Client) Post(url string, bodyType string, body io.Reader) (r *Response, error)
func (c *Client) PostForm(url string, data url.Values) (r *Response, err error)
func (c *Client) Head(url string) (r *Response, err error)
func (c *Client) Do(req *Request) (resp *Response, err error)
*/
package network

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"
)

func main() {

}

//get请求
func testGet() {
	resp, err := http.Get("https://www.baidu.com/")
	if err != nil {
		fmt.Println("Get response error, ", err)
		return
	}
	defer resp.Body.Close()

	//将网页内容输出到标准输出流中
	io.Copy(os.Stdout, resp.Body)
}

//post请求
func testPost() {
	resp, err := http.Post("http://test.com/upload", "image/jpeg", &imageDataBuf)
	if err != nil {
		fmt.Println("Post response error", err)
		return
	}
	if resp.StatusCode != http.StatusOK {
		//handle err
		return
	}
	//...
}

//PostForm请求
func testPostForm() {
	resp, err := http.PostForm("http://test.com/posts", url.Values{
		"title":{"article title"}, "content": {"article body"}
	})
	if err != nil {
		//handle err
		return
	}
	// ...
	fmt.Println(resp.Body)
}

//设置请求定制信息
func testResponse() {
	req, err := http.NewRequest("GET", "http://test.com", nil)
	if err != nil {
		//handle err
		return
	}
	req.Header.Add("User-Agent", "Gobook Custom User-Agent")

	client := &http.Client{
		//...
	}
	resp, err := client.Do(req)
	if err != nil {
		//handle err
		return
	}
	//...

	resp.Body.Close()
}

/*
http.Client类型
type Client struct {
    //用于确定HTTP请求的创建机制,如果为空,将使用DefaultTransport类型
    Transport      RoundTripper
    //定义重定向策略,如果CheckRedirect不为空,客户端将在跟踪HTTP重定向前调用该函数.
    //两个参数req和via分别为即将发起的请求和已经发起的所有请求,最早的已发起的请求在最前面
    //如果CheckRedirect返回错误,客户端将直接返回错误,不会再发起该请求.
    //如果CheckRedirect为空,Client将采用一种确认策略,将在10个连续请求后终止
    CheckRedirect  func(req *Request, via []*Request) error
    //如果Jar为空,Cookie将不会在请求中发送,并会在响应中被忽略
    Jar    CookieJar
}
*/