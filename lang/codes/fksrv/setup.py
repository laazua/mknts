import pathlib

import setuptools


path = pathlib.Path(__file__).parent.resolve()
install_requires = (path / "requirements.txt").read_text(encoding="utf-8").splitlines()


setuptools.setup(
    name="fksrv",
    version="0.0.1",
    description="flask demo",
    author="confucuis",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["fksrv = fksrv.main:main"]},
    package_data={
        "fksrv": [
            "static/css/*.css",
            "static/js/*.js",
            "templates/*.html",
        ]
    },
    install_requires=install_requires,
)
