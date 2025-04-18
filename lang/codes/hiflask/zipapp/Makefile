# python标准库zipapp打包python项目
# 注意SRC和ENTRYPOINT变量的路径, 与项目导包和程序运行入口有关
# setup.py文件必须存在并运行: python setup.py install

PYTHON := .venv/bin/python
ENVPYTHON := "/usr/bin/env python"
BUILD := build
TARGET := hiflask.pyz
LIBS := .venv/lib/python3.10/site-packages/*
SRC := src/*
ENTRYPOINT := hiflask.main:main

build:
	[ ! -d $(BUILD) ] && mkdir $(BUILD)
	cp -r $(SRC) $(BUILD)
	cp -r $(LIBS) $(BUILD)
	$(PYTHON) -m zipapp $(BUILD) -p $(ENVPYTHON) -c -m $(ENTRYPOINT) -o $(TARGET)
	
.PHONY: all clean

clean:
	rm -fr $(BUILD) $(TARGET)
