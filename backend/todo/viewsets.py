from rest_framework import viewsets, permissions

from knox.auth import TokenAuthentication

from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = TodoSerializer

    def get_queryset(self):
        return self.request.user.todo.all()

    def preform_create(self, serializer):
        serializer.save(owner = self.request.user)