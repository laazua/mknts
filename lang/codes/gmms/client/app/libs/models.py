# -*- coding: utf-8 -*-
import sqlalchemy


metadata = sqlalchemy.MetaData()


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("username", sqlalchemy.String, unique=True, Index=True),
    sqlalchemy.Column("password", sqlalchemy.String),
    sqlalchemy.Column("create_at", sqlalchemy.String),
    sqlalchemy.Column("update_at", sqlalchemy.String)
)

zones = sqlalchemy.Table(
    "zones",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("server_name", sqlalchemy.String),
    sqlalchemy.Column("server_id", sqlalchemy.Integer, unique=True),
    sqlalchemy.Column("server_ip", sqlalchemy.String),
    sqlalchemy.Column("create_at", sqlalchemy.String),
    sqlalchemy.Column("update_at", sqlalchemy.String)
)