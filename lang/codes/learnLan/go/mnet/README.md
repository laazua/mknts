## go 标准库创建web server
```
   方式1:
   http.ListenAndServer()   (HTTP)
   http.ListenAndServeTLS() (HTTPS)
   方式2:
   server := http.Server{}  配置
   server.ListenAndSeve()  (HTTP)
   server.ListenAndServeTLS() (HTTPS)

   handler(接口)
   http.HandlFunc
```