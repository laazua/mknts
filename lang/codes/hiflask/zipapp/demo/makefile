PYTHON := .venv/bin/python
DEPENDENCE := ../deps
TARGET := demo.pyz
LIBS := .venv/lib/python3.10/site-packages/*
SRC := src/*
ENTRYPOINT := "demo.main:main"

build:
	[ ! -d $(DEPENDENCE) ] && mkdir $(DEPENDENCE)
	cp -r $(SRC) $(DEPENDENCE)
	cp -r $(LIBS) $(DEPENDENCE)
	$(PYTHON) -m zipapp $(DEPENDENCE) -c -m $(ENTRYPOINT) -o $(TARGET)
	
.PHONY: all clean

clean:
	rm -fr $(DEPENDENCE) $(TARGET)
