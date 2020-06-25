from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwarg = { 'password' : {'write_only' : True }}

    def create_user(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
        user.save()
        return user

class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwarg = { 'password' : {'write_only' : True }}

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        user = User.objects.get(username=username, password=password)
        #user = authenticate(username=username, password=password)

        if self.model.DoesNotExist:
           raise serializers.ValidationError({'error': 'A User with This Username and Password is Not Found'})

        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwarg = { 'password' : { 'write_only' : True }}

