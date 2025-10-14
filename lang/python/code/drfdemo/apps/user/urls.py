from django.urls import path
from apps.user.views import (
    RegisterView, LoginView, UserListView, UserDetailView
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name="user-register"),
    path('login/', LoginView.as_view(), name="user-login"),
    path('', UserListView.as_view(), name="user-list"),
    path('<int:pk>/', UserDetailView.as_view(), name="user-detail"),
]
