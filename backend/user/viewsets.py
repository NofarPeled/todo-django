from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import SignInSerializer, SignUpSerializer, UserSerializer

class SignUpViewSet(viewsets.ModelViewSet):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()

        return Response({
            'user': SignUpSerializer(user, context = self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)
        })

class SignInViewSet(viewsets.ModelViewSet):
    serializer_class = SignInSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)

        return Response({
            'user': UserSerializer(user, context = self.get_serializer_context()).data,
            'token': token
        })

class GetUserViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ] 
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
