# 项目打包管理

SCRIPT := setup.py
PYTHON := /usr/bin/python
TARGET := build dist src/taoist.egg-info

build:
	$(PYTHON) $(SCRIPT) bdist_wheel

.PHONY: all clean

clean:
	rm -fr $(TARGET)
