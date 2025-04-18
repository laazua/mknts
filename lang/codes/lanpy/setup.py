"""
项目打包脚本
"""
import pathlib
from setuptools import setup, find_packages


path = pathlib.Path(__file__).parent.resolve()
install_requires = (path / "requirements.txt").read_text(encoding="utf-8").splitlines()


setup(
    # name="lanpy",
    # version="0.0.1",
    # description="python base",
    # packages=find_packages(where="src"),
    # package_dir={"": "src"},
    # include_package_data=True, # MANIFEST.in是否生效
    # package_data={"": ["manage.sh", "requirements.txt", ".env.example"]},
    # zip_safe=False,
    # install_requires=install_requires,
    # entry_points={"console_scripts": ["lanpy = lanpy.__main__:main"]},
)