from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwarg = { 'password' : { 'write_only' : True }}


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwarg = { 'password' : {'write_only' : True }}

    def create_user(self, validated_data):
        if not username :
            raise ValueError('User Name is Must Field')
        if not email :
            raise ValueError('Email is a Must Field')
        if not password : 
            raise ValueError('Password is a Must Field')
    
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
        user.save()
        return user

class SignInSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
           raise serializers.ValidationError({'error': 'A User with This Username and Password is Not Found'})

        return user
    

