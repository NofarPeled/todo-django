from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('_id', 'username', 'email', 'password')

        extra_kwarg = { 'password' : {
            'write_only' : True
        }}

    def create(self, validated_data):
        if password != re_password:
            raise serializers.ValidationError('Passwords Must Match')
        user = user.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], validated_data['re_password'])

        return user

class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields: ('username', 'password')

        extra_kwarg = { 'password' : {
            'write_only' : True
        }}

    def get(self, validated_data):
        user = user.objects.get_user(validated_data['password'], validated_data['email'])
        
        return user
