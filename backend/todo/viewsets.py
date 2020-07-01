from rest_framework import viewsets, permissions

from knox.auth import TokenAuthentication

from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner = self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)