# -*- coding:utf-8 -*-
"""
可以使用专门的高效读写文件的内置方法将数组的内容写入文件或从文件中读出数组
"""
import array
import binascii
import tempfile


a = array.array('i', range(5))
print('A1: ', a)

# write the array of numbers to a temporary file.
output = tempfile.NamedTemporaryFile()
a.tofile(output.file)    # must pass an actual + file
output.flush()

# read the raw data.
with open(output.name, 'rb') as fd:
    raw_data = fd.read()
    print('Raw Contents:', binascii.hexlify(raw_data))

    # read the data into an array
    fd.seek(0)
    aa = array.array('i')
    aa.fromfile(fd, len(a))
    print('AA: ',aa)
