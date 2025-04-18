"""
数据库连接
"""

from sqlmodel import Session, create_engine

from taoist.core.config import settings


engine = create_engine(
    f"mysql+mysqldb://{settings.db_user}:{settings.db_pass}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
)


def init_db(session: Session):
    pass
