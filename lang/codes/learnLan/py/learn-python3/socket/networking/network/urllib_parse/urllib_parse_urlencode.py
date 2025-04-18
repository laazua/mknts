# -*- coding:utf-8 -*-
"""
解码查询参数:
    参数在被增加到一个url之前，需要先编码
"""

from urllib.parse import urlencode


query_args = {
    'q': 'query string',
    'foo': 'bar',
}

encoded_args = urlencode(query_args)
print('Encoded: ', encoded_args)
