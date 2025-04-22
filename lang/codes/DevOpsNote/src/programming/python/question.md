### question

- [问题]
1. 一个关于pydantic_core包的问题:
   ModuleNotFoundError: No module named 'pydantic_core._pydantic_core'  
   解决方案: pip install pydantic_core==2.23.4 -t vendor/ --only-binary=:all: --platform manylinux2014_x86_64 --python-version 3.10 --upgrade
