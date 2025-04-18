from mongoengine import Document, StringField, IntField, BooleanField


class Zone(Document):
    zid: IntField(unique=True)
    name: StringField(min_length=3, max_length=24)
    public_ip: StringField()
    priviate_ip: StringField()
    domain_name: StringField()
    create_time: StringField()
    is_close: BooleanField(default=False)