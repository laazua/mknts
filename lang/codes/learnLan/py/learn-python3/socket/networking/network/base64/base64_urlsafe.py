# -*-coding:utf-8-*-
"""
默认的Base64字母表可能使用 + 和 /,这两个字符在URL中会用到, 所以通常很有必要使用一个候选编码替换这些字符
"""

import base64


encdes_with_pluses = b'\xfd\xef'
encodes_with_slashes = b'\xff\xff'

for original in [encdes_with_pluses, encodes_with_slashes]:
    print('Original           : ', repr(original))
    print('Standard encoding  : ', base64.standard_b64encode(original))
    print('URL-safe encoding  : ',base64.urlsafe_b64encode(original))
