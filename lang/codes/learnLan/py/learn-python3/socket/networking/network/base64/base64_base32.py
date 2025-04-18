# -*-coding:utf-8-*-


import base64


# base32
original_data = b'this is the data, in the clear.'
print('Original: ', original_data)

encoded_data = base64.b32encode(original_data)
print('Encoded : ', encoded_data)

decoded_data = base64.b32decode(encoded_data)
print('Decoded : ', decoded_data)

# base16
encoded_data = base64.b16encode(original_data)
print('Encode : ', encoded_data)

decoded_data = base64.b16encode(encoded_data)
print('Decoded : ', decoded_data)
