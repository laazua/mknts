import mongoengine
from datetime import datetime


class DBZone(mongoengine.Document):
    name = mongoengine.StringField(min_length=3, max_length=24)
    number = mongoengine.StringField(
        min_length=1, max_length=4, primary_key=True, required=True)
    ip = mongoengine.StringField(min_length=7, max_length=15)
    create_time = mongoengine.StringField()
    is_close = mongoengine.BooleanField(default=False)


class DBUser(mongoengine.Document):
    name = mongoengine.StringField(min_length=2, max_length=64)
    password = mongoengine.StringField(min_length=6, max_length=255)
    description = mongoengine.StringField()
    roles = mongoengine.ListField()
    avatar = mongoengine.StringField()
    create_time = mongoengine.StringField(
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
