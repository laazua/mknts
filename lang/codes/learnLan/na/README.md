## nakupenda

### 收集github上比较好的仓库用于学习  
### https://github.com/freeCodeCamp  
### https://github.com/TutorialEdge(golang教程)
### https://github.com/fanjianhai/Go

### 编程语言库  
### https://devdocs.io/

### cheatsheet
### https://devhints.io/

### 程序思想
### https://www.52wiki.cn/
### https://www.zutuanxue.com
### book.ayitula.com

### geetutu
### https://geektutu.com/


### go && gin
### https://www.gin-vue-admin.com/
### https://www.kancloud.cn/shuangdeyu/gin_book/949413  搜索gin中文文档


### 技术文档
### https://learnku.com/
### http://www.banshujiang.cn/

### https://github.com/coreos


### https://www.junmajinlong.com/  骏马金龙博客


### https://www.programiz.com/

### search book
### https://bookfere.com/search


## authority
```
-- 登录：当用户填写完账号和密码后向服务端验证是否正确，验证通过之后，服务端会返回一个token，
   拿到token之后（我会将这个token存贮到cookie中，保证刷新页面后能记住用户登录状态），
   前端会根据token再去拉取一个 user_info 的接口来获取用户的详细信息（如用户权限，用户名等等信息）.
-- 权限验证：通过token获取用户对应的 role，动态根据用户的 role 算出其对应有权限的路由，通过 router.addRoutes 动态挂载这些路由.

-- 前端会有一份路由表，它表示了每一个路由可访问的权限。当用户登录之后，通过 token 获取用户的 role ，
   动态根据用户的 role 算出其对应有权限的路由，再通过router.addRoutes动态挂载路由。但这些控制都只是页面级的，
   说白了前端再怎么做权限控制都不是绝对安全的，后端的权限验证是逃不掉的.
-- 前端来控制页面级的权限，不同权限的用户显示不同的侧边栏和限制其所能进入的页面(也做了少许按钮级别的权限控制)，
   后端则会验证每一个涉及请求的操作，验证其是否有该操作的权限，
   每一个后台的请求不管是 get 还是 post 都会让前端在请求 header里面携带用户的 token，
   后端会根据该 token 来验证用户是否有权限执行该操作。若没有权限则抛出一个对应的状态码，前端检测到该状态码，做出相对应的操作.
```
>>>>>>> 7a8590ed0561a281d899a38e9be89729ee54135f
