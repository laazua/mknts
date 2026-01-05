"""
用户数据库模型
"""
from typing import Annotated

from sqlalchemy import (
    String,
    Boolean,
    DateTime,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column

from app.shared.db import Base


class User(Base):
    """
    User表模型
    """
    __tablename__ = "op_user"
    __table_args__ = {'comment': '用户表'}

    # id = Column(Integer, primary_key=True, index=True)
    # username = Column(String(64), unique=True, index=True, nullable=False)
    # email = Column(String(128), unique=True, index=True, nullable=False)
    # password = Column(String(512), nullable=False)
    # full_name = Column(String(128), nullable=True)
    # is_active = Column(Boolean, default=True)
    # created_at = Column(DateTime(timezone=True), server_default=func.now()) # pylint: disable=not-callable
    # updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()) # pylint: disable=not-callable

    id: Mapped[Annotated[int, mapped_column(primary_key=True, index=True)]]
    username: Mapped[Annotated[str, mapped_column(String(64), unique=True, index=True, nullable=False)]]
    email: Mapped[Annotated[str, mapped_column(String(128), unique=True, index=True, nullable=False)]]
    password: Mapped[Annotated[str, mapped_column(String(512), nullable=False)]]
    full_name: Mapped[Annotated[str | None, mapped_column(String(128), nullable=True)]]
    is_active: Mapped[Annotated[bool, mapped_column(Boolean, default=True)]]
    created_at: Mapped[Annotated[DateTime, mapped_column(DateTime(timezone=True), server_default=func.now())]]  # pylint: disable=not-callable
    updated_at: Mapped[Annotated[DateTime, mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())]]  # pylint: disable=not-callable