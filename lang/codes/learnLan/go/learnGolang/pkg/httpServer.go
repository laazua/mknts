// http serve
package main

import (
	"fmt"
	"io/ioutil"
	"net"
	"net/http"
	"net/url"
	"strings"
	"time"
)

type bbb struct{}

func (b bbb) ServeHTTP(w http.ResponseWriter, req *http.Request) {
	w.Write([]byte("hahah"))
}

func main() {
	http.HandleFunc("/", testHandler)
	http.ListenAndServe("0.0.0.0:8080", nil)

	// 自定义Server
	// s := &http.Server{
	//	Addr:           ":8080",
	//	Handler:        bbb{},
	//	ReadTimeout:    100 * time.Second,
	//	WriteTimeout:   100 * time.Second,
	//	MaxHeaderBytes: 1 << 20,
	// }
	// s.ListenAndServe()
}

func testHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.RemoteAddr, "connect successful.")
	data := fmt.Sprintf("%v:%v:%v:%v", r.Header, r.Method, r.URL, r.URL.Path)
	w.Write(([]byte(data)))
}

// client操作
func httpGet() {
	resp, err := http.Get("https://www.baidu.com")
	if err != nil {
		return
	}

	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return
	}
	fmt.Println(string(body))

	// 带参数的get
	apiUrl := "http://www.missu.com/xxx"
	// url param
	data := url.Values{}
	data.Set("name", "wangwu")
	data.Set("age", "20")
	u, err := url.ParseRequestURI(apiUrl)
	if err != nil {
		return
	}
	u.RawQuery = data.Encode() // url encode

	resp, err = http.Get(u.String())
	if err != nil {
		return
	}
	defer resp.Body.Close()

	b, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return
	}
	fmt.Println(string(b))
}

func httpPost() {
	data := `{"name": "zhangsan", "age": "18"}`
	resp, err := http.Post("http://www.missu.com/upload", "application/json", strings.NewReader(data))
	if err != nil {
		return
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return
	}
	fmt.Println(string(body))
}

func httpPostForm() {
	resp, err := http.PostForm("http://www.missu.com/data", url.Values{"key": {"value"}, "id": {"123"}})
	if err != nil {
		return
	}
	defer resp.Body.Close()
}

func customClient() {
	// 自定义Transport
	tr := &http.Transport{
		Dial: func(network, addr string) (net.Conn, error) {
			return net.DialTimeout(network, addr, time.Duration(20*time.Second))
		},
		ResponseHeaderTimeout: time.Second * 2,
	}
	// 自定义Client
	client := &http.Client{
		Transport: tr,
		Timeout:   10 * time.Second,
	}

	if resp, err := client.Get("http://www.missun.com"); err != nil {
		return
	} else {
		defer resp.Body.Close()
	}

	if req, err := http.NewRequest("GET", "http://www.missu.com", nil); err != nil {
		return
	} else {
		defer req.Body.Close()

		req.Header.Add("content-type", "text/plain")
		if resp, err := client.Do(req); err != nil {
			return
		} else {
			defer resp.Body.Close()
		}
	}
}
