# -*- coding: utf-8 -*-
"""
lua表合并
"""
import os
import re
import sys


def replace_file_content(file_name, new_str):
    new_text = ""
    with open(file_name, "r", encoding="utf-8") as fd:
        text = fd.read()
        result = re.search(r"return", text, re.M|re.I).group()
        if result:
            if new_str.isdigit():
                # new_str = 
                new_text = text.replace(result, '[' + new_str + ']' + ' =')
            else:
                new_text = text.replace(result, new_str + ' =')
            return new_text
    return None
        

def all_lua_file(lua_file: str, lua_dir: str):
    if not os.path.exists(lua_dir):
        print("路径不正确!")
        sys.exit(0)

    # with open(lua_file, 'r+') as fd_lua:
    with open(lua_file, 'w', encoding="utf-8") as fd:
        fd.write("return {\n")
        for _, _, files in os.walk(lua_dir):
            num = len(files)
            for index, file_name in enumerate(files):
                if file_name.endswith('lua') and file_name != lua_file:
                    new_str = file_name.split('.')[0]
                    result = replace_file_content(lua_dir + '\\' + file_name, new_str)
                    if (num - 1) != index:
                        fd.write(result + ",\n")
                    else:
                        fd.write(result + ",")
        fd.write("\n}")



if __name__ == "__main__":
    if len(sys.argv) != 5 or sys.argv[1] != '-f' or sys.argv[3] != '-d':
        print("python {} -f fileName -d dirname".format(sys.argv[0]))
        sys.exit(0)

    all_lua_file(sys.argv[2], sys.argv[4])
