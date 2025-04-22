### jetbrains


[激活服务器](https://jetbrains.asiones.com/)

[查找服务器激活]
1. [激活方式: fofa](https://fofa.info/): 搜索-> header="https://account.jetbrains.com/fls-auth"
2. [激活方式: shodan](https://www.shodan.io/): 搜索-> Location: https://account.jetbrains.com/fls-auth
3. [激活方式: censys](https://search.censys.io/): 搜索-> services.http.response.headers.location: account.jetbrains.com/fls-auth
以上三种方式搜索到的服务器显示的状态码要为302才可以用
