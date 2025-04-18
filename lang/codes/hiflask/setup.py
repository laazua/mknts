from setuptools import find_packages, setup


setup(
    name="hiflask",
    version="0.0.1",
    description="test package",
    maintainer="zhangsan",
    packages=find_packages("src"),
    package_dir={"": "src"},
)
