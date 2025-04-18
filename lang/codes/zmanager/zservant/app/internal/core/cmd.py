import svn
from app import cfg


def svn_check(version: str) -> bool:
    if version:
        r = svn.remote.RemoteClient(cfg.get("svn", "addr"))
        r.checkout(cfg.get("svn", ""))