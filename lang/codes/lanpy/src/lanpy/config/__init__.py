"""
加载项目配置
"""
import os


def load_env(name: str = ".env"):
    """加载环境配置"""
    if not os.path.exists(name):
        raise FileNotFoundError(".env not found")
    with open(name, encoding="utf-8", mode="r") as fd:
        for line in fd:
            line = line.strip()
            if line.startswith("#") or len(line) == 0:
                continue
            parts = line.split("=", maxsplit=1)
            if len(parts) != 2:
                continue
            key, value = parts
            os.environ[key.strip()] = value.strip()
