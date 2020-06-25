from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import generics, permissions
from .serializers import SignInSerializer, SignUpSerializer, UserSerializer

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = SignUpSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            _, token = AuthToken.objects.create(user)
            return Response({'user': serializer.data, 'token': token})
        else:
            return Response(serializer.errors)

class SignInView(generics.GenericAPIView):
    serializer_class = SignInSerializer

    def post(self, request, *args, **kwargs):
        serializer = SignInSerializer(data = request.data)

        user = serializer.validate(data = request.data)
        _, token = AuthToken.objects.create(user)

        return Response({
            'user': UserSerializer(user, context = self.get_serializer_context()).data,
            'token': token
        })

class GetUserView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = UserSerializer

    def get_user(self):
        return self.request.user