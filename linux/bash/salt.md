### salt:zhangsan

- salt加密和解密
```bash
########## 方式一 ##########
## 加密: salt="abc123"
echo "hello world" | openssl enc -aes-256-cbc -base64 -salt -pass pass:abc123 -pbkdf2
## 上面输出: U2FsdGVkX19r/CCY9WENfn35G/cRckfvph1OvzOIzZM=
## 解密: salt="abc123"
echo "U2FsdGVkX19r/CCY9WENfn35G/cRckfvph1OvzOIzZM=" | openssl enc -aes-256-cbc -d -base64 -salt -pass pass:abc123 -pbkdf2

########## 方式二 ##########
## 加密: salt="xxxooo"
echo "hello world"| openssl enc -aes-256-cbc -base64 -salt -pass pass:xxxooo -iter 10000
## 上面输出: U2FsdGVkX1+crGdSJDqfH0xsTNF3UKOlvWrfa+wSbl8=
## 解密: salt="xxxooo"
echo "U2FsdGVkX1+crGdSJDqfH0xsTNF3UKOlvWrfa+wSbl8=" | openssl enc -aes-256-cbc -d -base64 -salt -pass pass:xxxooo -iter 10000
## 上面输出: hello world
```

- base64编码解码
```bash
## 编码
echo "hello world" | base64
## 输出: aGVsbG8gd29ybGQK
## 解码
echo "aGVsbG8gd29ybGQK" | base64 -d
## 输出: hello world
```
