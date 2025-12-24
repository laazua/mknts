"""
用户数据库模型
"""
import sqlalchemy as sa
import app.shared.db as mdb


class User(mdb.Base):
    __tablename__ = "op_user"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    username = sa.Column(sa.String(64), unique=True, index=True, nullable=False)
    email = sa.Column(sa.String(64), unique=True, index=True, nullable=False)
    hashed_password = sa.Column(sa.String(256), nullable=False)
    full_name = sa.Column(sa.String(128), nullable=True)
    is_active = sa.Column(sa.Boolean, default=True)
    created_at = sa.Column(sa.DateTime(timezone=True), server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime(timezone=True), onupdate=sa.func.now())