from rest_framework import routers
from .viewsets import TodoViewSet

todo_router = routers.DefaultRouter()

todo_router.register(r'', TodoViewSet, basename = 'todo')