from rest_framework import routers
from user.viewsets import SignInViewSet, SignUpViewSet
from todo.viewsets import TodoViewSet

router = routers.DefaultRouter()

# todo paths
router.register(r'todo', TodoViewSet, basename = 'todo')

# user paths
router.register(r'user/sign_in', SignUpViewSet, basename='user_sign_in')
router.register(r'user/sign_up',SignInViewSet, basename='user_sign_up')

