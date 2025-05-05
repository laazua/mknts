"""
工具集
"""

class Token:
    @staticmethod
    def generate() -> str:
        pass

    @staticmethod
    def verify(token: str) -> bool:
        pass


class Passwd:
    @staticmethod
    def hash(passwd: str) -> str:
        pass
    
    @staticmethod
    def verify(passwd: str, hash: str) -> bool:
        pass