from setuptools import setup, find_packages

setup(
    name="zombie",  # 项目名称
    version="0.0.1",  # 项目版本
    packages=find_packages("src"),  # 查找包的路径
    package_dir={"": "src"},  # 指定包的根目录
)
