### subpricess

- **run**
```python
import subprocess


# subprocess.run
try:
    subprocess.run(
        ["ls", "-l"], 
        check=True, timeout=5, text=True)
except subprocess.TimeoutExpired:
    print("timeout")
except subprocess.CalledProcessError as e:
    print(e)
```

- **Popen**
```python
import subprocess


# subprocess.Popen
try:
    cmd = ["ping", "-c", "4", "baidu.com"]
    process = subprocess.Popen(
        cmd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    # 获取标准输出，标准错误:
    # input参数: 向子进程的标准输入写入数据
    stdout, stderr = process.communicate(timeout=5, input=None)
    if process.returncode != 0:
        print(stderr)
    else:
        print(stdout)
except subprocess.TimeoutExpired:
    process.kill()
    print("timeout")
except subprocess.CalledProcessError as e:
    print(e)
```