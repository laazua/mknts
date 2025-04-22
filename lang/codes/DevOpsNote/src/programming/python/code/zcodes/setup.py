import setuptools

setuptools.setup(
    name="zcodes",
    version="0.1.0",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
)