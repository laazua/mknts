### sudo

- 新增组和用户zhangsan
```bash
groupadd zhangsan
useradd -m -g zhangsan zhangsan
password zhangsan

#查看是否创建成功: id zhangsan
```

- 编辑 vim /etc/sudoers.d/zhangsan
```text
zhangsan  ALL=(ALL) NOPASSWD: ALL
```
