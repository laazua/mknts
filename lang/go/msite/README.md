### msite

- golang标准库实现个人网站
- 主要用于学习golang编程语言

- [测试]  
curl -XPOST   http://localhost:8077/api/auth/login -d '{"name":"zhangsan", "passwd":"123456"}'  
curl -XPOST   http://localhost:8077/api/user/create  
curl -XDELETE http://localhost:8077/api/user/delete  
curl -XPUT    http://localhost:8077/api/user/update  
curl -XGET    http://localhost:8077/api/user/query  
curl -XGET    http://localhost:8077/api/user/query/{id}  
