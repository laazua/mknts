> 利用sshd服务写的一个远程批量操作主机的bash脚本

```
microReop是一个用于远程操作主机的工具,用shell语言完成.
    usage: ./microReop [选项]... [参数]...
        -h             打印此工具的帮助信息.
        -c 'command'   在远程主机上执行命令.
        -s  script     在远程主机上执行脚本.
        -i 'ip'        被操作的主机ip.
    注意:当不指定-i参数时,在配置文件microReop.cnf中的所有主机都要执行命令行传入的命令.
    ./microReop -c "sudo su -c 'ls'"
```