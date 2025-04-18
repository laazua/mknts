"""
加载认证文件
"""

import os


def _load_credential_file(filepath):
    real_path = os.path.join(os.path.dirname(__file__), filepath)
    with open(real_path, 'rb') as fd:
        return fd.read()


ROOT_CERTIFICATE = _load_credential_file("../../../cert/ca.crt")
SERVER_CERTIFICATE_CRT = _load_credential_file("../../../cert/server.crt")
SERVER_CERTIFICATE_KEY = _load_credential_file("../../../cert/server.key")
