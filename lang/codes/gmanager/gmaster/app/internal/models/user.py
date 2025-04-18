from datetime import datetime
from mongoengine import Document, StringField, ListField


class User(Document):
    name = StringField(min_length=3, max_length=24, unique=True)
    password = StringField(min_length=6, max_length=255)
    desc = StringField()
    avatar = StringField()
    roles = ListField()
    create_time = StringField()
    update_time = StringField()
