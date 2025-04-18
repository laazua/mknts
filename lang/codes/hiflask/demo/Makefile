# python 标准库: zipapp打包

# 项目结构如下:
# .
# ├── main.py
# ├── Makefile
# ├── requirements.txt
# └── router
#     └── user.py
# └──.venv

# 将项目打包成独立包即可运行
# 要求目标机器只需要有对应版本的python解释器即可
# 要求源码文件中各个包之间引入项目自定义包时用绝对路径

PYTHON := .venv/bin/python
DEPENDENCE := ../deps
TARGET := demo.pyz
LIBS := .venv/lib/python3.10/site-packages/*
SRC := ../demo
ENTRYPOINT := "demo.main:main"

build:
	[ ! -d $(DEPENDENCE) ] && mkdir $(DEPENDENCE)
	cp -r $(SRC) $(DEPENDENCE)
	cp -r $(LIBS) $(DEPENDENCE)
	$(PYTHON) -m zipapp $(DEPENDENCE) -c -m $(ENTRYPOINT) -o $(TARGET)
	
.PHONY: all clean

clean:
	rm -fr $(DEPENDENCE) $(TARGET)
