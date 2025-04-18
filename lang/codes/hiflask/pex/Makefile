# .venv/bin/python -m pip install pex

PEX := .venv/bin/pex
TARGET := hiflask
ENTRYPOINT := hiflask.main:main


build:
	$(PEX) -r requirements.txt -e $(ENTRYPOINT) -D src -o $(TARGET)
check:
	@[ -f $(PEX) ] && echo $(PEX) exist. || echo $(PEX) not exist.

.PHONY: all clean

clean:
	rm -fr $(TARGET)
