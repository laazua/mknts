### lanpy

* **描述**
1. 基础知识: [官网](https://python.org/)
2. [Python 发行版的压缩包](https://github.com/astral-sh/python-build-standalone/releases/download/20231002/cpython-3.10.13+20231002-x86_64_v2-unknown-linux-gnu-pgo+lto-full.tar.zst)
3. 项目代码组织结构
4. 项目打包和部署方式

* **打包**
- 使用build模块打包:
  1. 依赖: python -m pip install --upgrade build setuptools wheel 
  2. 构建: python -m build
- 使用setup.py脚本打包:
  1. 依赖: python -m pip install --upgrade setuptools wheel
  2. 构建: python setup.py sdist
- 以上两种打包方式任选其一即可
  1. 第一种打包方式需要包含: pyproject.toml配置文件和README.md
  2. 第二种打包方式需要包含: setup.py, requirements.txt, README.md 和 MANIFEST.in

* **部署**
- 二进制部署
  1. 拷贝dist目录下的打包文件到目标机器上
  2. 安装打包文件: python -m pip install lanpy-0.0.1-py3-none-any.whl -t lanpy
  3. 设置 PYTHONPATH 环境变量: export PYTHONPATH=lanpy
  4. 运行项目: python -m lanpy
  5. 注意: 可以将上面第3步和第4步放在shell脚本中进行项目管理(例如: manage.sh脚本)
- 源码部署
  1. 拷贝dist目录下的源码压缩包到目标机器上
  2. 安装压缩包文件: python -m pip install lanpy-0.0.1.tar.gz -t lanpy
  