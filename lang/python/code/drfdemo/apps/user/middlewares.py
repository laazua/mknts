from django.http import JsonResponse
from apps.user.models import UserModel
from apps.user.authentication import verify_token


class TokenAuthMiddleware:
    """
    全局Token认证中间件:
    - 检查除白名单外的所有请求
    - 验证HTTP Header中的Token是否合法
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.white_list = [
            '/api/users/login/',
            '/api/users/register/',
            '/admin/',
        ]

    def __call__(self, request):
        path = request.path

        # 白名单路径直接放行
        if any(path.startswith(w) for w in self.white_list):
            return self.get_response(request)

        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Token '):
            return JsonResponse({'error': 'Missing or invalid Authorization header'}, status=401)

        token = auth_header.split(' ')[1]
        user_id = verify_token(token)
        if not user_id:
            return JsonResponse({'error': 'Invalid or expired token'}, status=401)

        # 验证用户是否存在
        try:
            user = UserModel.objects.get(id=user_id, is_active=True)
        except UserModel.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=401)

        # 将当前用户挂载到 request.user
        request.user = user

        # 继续处理请求
        return self.get_response(request)
