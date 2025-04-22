### compgen && complete

- **自定义命令补全**
1. 代码
```bash
#!/bin/bash

_supervisorctl_complete() {
    local cur="${COMP_WORDS[COMP_CWORD]}"
    local cmd="${COMP_WORDS[1]}"
    
    # 检查第一个参数是 supervisorctl
    if [[ ${COMP_CWORD} -eq 1 ]]; then
        # 给出 supervisorctl 命令补全
        COMPREPLY=( $(compgen -W "status start stop restart reread reload pid eventlog tail" -- ${cur}) )
    elif [[ ${cmd} == "status" || ${cmd} == "tail" ]]; then
        # 如果是 status 或 tail 命令，补全可以是进程名
        COMPREPLY=( $(compgen -W "$(supervisorctl status)" -- ${cur}) )
    elif [[ ${cmd} == "start" || ${cmd} == "stop" || ${cmd} == "restart" ]]; then
        # 如果是 start, stop 或 restart 命令，补全可以是进程名
        COMPREPLY=( $(compgen -W "$(supervisorctl status)" -- ${cur}) )
    else
        COMPREPLY=()
    fi
}

complete -F _supervisorctl_complete supervisorctl

```
2. 使用
```bash
1. 将上面的脚本放在: /etc/bash_completion.d/supervisorctl
2. 执行命令: source /etc/bash_completion.d/supervisorctl
```