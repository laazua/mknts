# setuptools打包项目
# 查看帮助信息: python setup.py --help-command
# 安装: python -m pip install wheel setuptools \
#   -i http://mirrors.aliyun.com/pypi/simple \
#   --trusted-host mirrors.aliyun.com

SCRIPT := setup.py
PYTHON := /usr/bin/python
TARGET := build dist src/demo.egg-info

build:
	$(PYTHON) $(SCRIPT) bdist_wheel

.PHONY: all clean

clean:
	rm -fr $(TARGET)


## 运行上面的打包命令后, 得到如下文件:
##    |-- build
##    |   |-- bdist.linux-x86_64
##    |   `-- lib
##    |       `-- demo
##    |           |-- __init__.py
##    |           |-- config.py
##    |           `-- main.py
##    |-- dist
##    |   `-- demo-0.0.1-py3-none-any.whl
##
## 安装到指定目录:
##    pip install demo-0.0.1-py3-none-any.whl -t path_name
## 运行安装后的包:
##    1. export PYTHONPATH=$PYTHONPATH:path_name
##    2. $path_name/bin/demo
