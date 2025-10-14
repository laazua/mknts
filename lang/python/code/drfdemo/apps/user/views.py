from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from apps.user.models import UserModel
from apps.user.serializers import UserSerializer, UserRegisterSerializer
from apps.user.authentication import generate_token


class RegisterView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'msg': '注册成功', 'user': UserSerializer(user).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = UserModel.objects.get(username=username, password=password)
        except UserModel.DoesNotExist:
            return Response({'error': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)

        token = generate_token(user)
        return Response({'token': token, 'user': UserSerializer(user).data})


class UserListView(APIView):
    def get(self, request: Request) -> Response:
        # 经过中间件验证后，这里一定有 request.user
        users = UserModel.objects.all()
        return Response(UserSerializer(users, many=True).data)


class UserDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response({'error': '用户不存在'}, status=status.HTTP_404_NOT_FOUND)
        return Response(UserSerializer(user).data)

    def put(self, request: Request, pk: int) -> Response:
        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response({'error': '用户不存在'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response:
        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response({'error': '用户不存在'}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({'msg': '删除成功'})
