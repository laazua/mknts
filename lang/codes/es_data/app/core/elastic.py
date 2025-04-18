"""Elasticserch连接"""
import elasticsearch as es
from app.core.setting import config


class ESConn:
    """连接ES的上下文管理器"""
    def __init__(self):
        self.conn = None
        self.hosts = config.get("es", "hosts")
        self.auth  = (config.get("es", "username"), config.get("es", "password"))
    
    def __enter__(self):
        self.conn = es.Elasticsearch(
            http_auth = self.auth,
            hosts     = self.hosts,
        )
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
