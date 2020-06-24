from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .serializers import SignInSerializer, SignUpSerializer

class SignUpViewSet(viewsets.ModelViewSet):
    queryset = ''
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context = self.get_serializer_context()).data,
            'token': TokenObtainPairView(user)
        })

class SignInViewSet(viewsets.ModelViewSet):
    queryset = ''
    serializer_class = SignInSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context = self.get_serializer_context()).data,
            'token': TokenObtainPairView(user)
        })
