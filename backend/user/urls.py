from rest_framework import routers
from .viewsets import SignUpViewSet, SignInViewSet, GetUserViewSet

user_router = routers.DefaultRouter()

user_router.register(r'sign_up', SignUpViewSet, basename='sign_up')
user_router.register(r'sign_in', SignInViewSet, basename='sign_in')
user_router.register(r'user', GetUserViewSet, basename='user')
