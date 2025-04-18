PEX := pex
TARGET := taoist
ENTRYPOINT := taoist.main:main
PIPSOURCE := https://pypi.tuna.tsinghua.edu.cn/simple

build:
	$(PEX) -r requirements.txt -e $(ENTRYPOINT) -i $(PIPSOURCE) -D src -o $(TARGET)

.PHONY: all clean

clean:
	rm -fr $(TARGET)
