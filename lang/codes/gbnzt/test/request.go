package test

import (
	"bytes"
	"net/http"
)

type Request struct {
	Key   string
	Value string
}

// 简单封装请求
func (r *Request) Post(data []byte, url string) (*http.Response, error) {
	// 构造请求
	req, err := http.NewRequest("POST",
		url,
		bytes.NewBuffer(data))
	req.Header.Set(r.Key, r.Value)
	if err != nil {
		return nil, err
	}
	// 发送请求
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	return resp, nil
}
