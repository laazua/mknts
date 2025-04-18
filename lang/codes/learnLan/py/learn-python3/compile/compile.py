# -*- coding: utf-8 -*-

"""
pip install pyinstaller
pip3 isntall pyinstaller

apt install nuitka  打包工具
nuitka3 --standalone --show-memory --show-progress --nofollow-imports --output-dir=build sunflower.py
"""

import compileall

compileall.compile_dir("/home/wnot/sunflower")
