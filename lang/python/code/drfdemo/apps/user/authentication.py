from django.conf import settings
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired


SECRET_KEY = getattr(settings, 'SECRET_KEY', 'default-key')
TOKEN_EXPIRES = 3600 * 2  # 2小时有效期
serializer = URLSafeTimedSerializer(SECRET_KEY)


def generate_token(user):
    return serializer.dumps({'user_id': user.id})


def verify_token(token):
    try:
        data = serializer.loads(token, max_age=TOKEN_EXPIRES)
        return data.get('user_id')
    except SignatureExpired:
        return None  # 过期
    except BadSignature:
        return None  # 无效
