import pathlib

import setuptools


path = pathlib.Path(__file__).parent.resolve()
install_requires = (path / "requirements.txt").read_text(encoding="utf-8").splitlines()


setuptools.setup(
    name="zombie",
    version="0.0.1",
    description="游戏运维管理执行命令程序",
    author="Sseve",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["zombie = zombie.main:main"]},
    package_data={
        "zombie": [
        ]
    },
    install_requires=install_requires,
)
