## 打包脚本

.PHONY: build, clean

build:
	PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple $(PYTHON) python -m build -v

clean:
	rm -fr dist src/lanpy.egg-info
