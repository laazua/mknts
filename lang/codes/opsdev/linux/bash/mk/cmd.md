### cmd

- **xargs**
```bash
## xargs -n 1 -P 10
# 每次将输入的一个参数传递给后续命令
# 开启十个进程并行执行
# 示例：supervisorctl status | awk '{print $1}' | xargs -n 1 -P 10 supervisorctl restart
```