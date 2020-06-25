from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import SignInSerializer, SignUpSerializer, UserSerializer

class SignUpViewSet(APIView):
    serializer_class = SignUpSerializer
    queryset = ''

    def create_user(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        user = serializer.save()
        _, token = AuthToken.objects.create(user)

        return Response({
            'user': UserSerializer(user, context = self.get_serializer_context()).data,
            'token': token
        })

class SignInViewSet(APIView):
    serializer_class = SignInSerializer
    queryset = ''

    def list_user(self, request, *args, **kwargs):
        serializer = SignInSerializer()

        user = serializer.validate(attrs=request.data)
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
