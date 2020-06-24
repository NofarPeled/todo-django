from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

#TODO: CHECK ID NEEDED!
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('_id', 'username', 'email', 'password')
        extra_kwarg = { 'password' : {
            'write_only' : True
        }}


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('_id', 'username', 'email', 'password')

        extra_kwarg = { 'password' : {
            'write_only' : True
        }}

    def create_user(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, data):
      email = data.get("email", None)
      password = data.get("password", None)
      user = authenticate(email=email, password=password)

      if user is None:
          raise serializers.ValidationError('A user with this email and password is not found.')

