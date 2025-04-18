# zombie 项目打包

PYTHON := .venv/bin/python
ENVPYTHON := "/usr/bin/env python"
BUILD := build
TARGET := zombie.pyz
SRC := src/*
ENTRYPOINT := zombie.main:main
LIBS := .venv/lib/python3.12/site-packages/*

build:
	[ ! -d $(BUILD) ] && mkdir $(BUILD)
	cp -r $(SRC) $(BUILD)
	cp -r $(LIBS) $(BUILD)
	$(PYTHON) -m zipapp $(BUILD) -p $(ENVPYTHON) -c -m $(ENTRYPOINT) -o $(TARGET)

.PHONY: all clean

clean:
	rm -fr $(BUILD) $(TARGET)
