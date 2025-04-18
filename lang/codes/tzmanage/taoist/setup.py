import pathlib

import setuptools


path = pathlib.Path(__file__).parent.resolve()
install_requires = (path / "requirements.txt").read_text(encoding="utf-8").splitlines()


setuptools.setup(
    name="taoist",
    version="0.0.1",
    description="游戏运维管理下达命令程序",
    author="Sseve",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["taoist = taoist.main:main"]},
    package_data={
        "taoist": [
            "static/css/*.css",
            "static/js/*.js",
            "static/imgs/*.svg",
            "templates/*.html",
        ]
    },
    install_requires=install_requires,
)