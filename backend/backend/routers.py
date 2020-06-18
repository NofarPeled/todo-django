from rest_framework import routers
from todo.viewsets import TodoViewSet

router = routers.DefaultRouter()

router.register(r'todo', TodoViewSet)