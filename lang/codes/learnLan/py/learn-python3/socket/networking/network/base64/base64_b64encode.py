# -*-coding:utf-8-*-
"""
对文本进行编码的简单示例
"""

import base64
import textwrap


# load this source file and strip the header
with open(__file__, 'r', encoding='utf-8') as input:
    raw = input.read()
    inital_data = raw.split('#end_pymotw_header')[1]

byte_string = inital_data.encode('utf-8')
encoded_data = base64.b64encode(byte_string)

num_initial = len(byte_string)

# there will never be more than 2 padding bytes.
padding = 3 - (num_initial % 3)
print('{} bytes before encoding'.format(num_initial))
print('Expect {} padding bytes'.format(padding))
print('{} bytes after encoding\n'.format(len(encoded_data)))
print(encoded_data)
