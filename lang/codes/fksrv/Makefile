SCRIPT := setup.py
PYTHON := /usr/bin/python3
TARGET := build dist src/fksrv.egg-info

build:
	$(PYTHON) $(SCRIPT) bdist_wheel

.PHONY: all clean

clean:
	rm -fr $(TARGET)
