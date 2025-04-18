# -*- coding: utf-8 -*-

"""
文件操作
"""

def test_fileopt() -> None:
    """
    test file opt
    :return: None
    """
    with open("fileName", 'w') as fd:
        all_data = fd.read([size])    # 省略size读取整个文件
        line_data = fd.readable()     # 按行读取

        
    with open("fileName", "r") as fd:
        fd.write("string")            # 把字符串写入文件中

        # fd.tell() 返回一个整数,给出文件对象在文件中的当前位置
        # fd.seek(offset, whence) 改变文件对象在文件中的位置, offset为偏移量, whence(0,1,2)参考位置