from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from .models import UserData


class UserDataRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = UserData
        fields = ['username', 'password', 'password2', 'email', 'user_phone']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        if self.validated_data['password'] != self.validated_data['password2']:
            raise ValidationError({'error': 'Passwords must match'})
        
        if ('email' not in self.validated_data and 'user_phone' not in self.validated_data) or (self.validated_data['email'] == "" and self.validated_data['user_phone'] == ""):
            raise ValidationError({'error': 'Email or Phone is required'})
        
        user = UserData.objects.create(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            user_phone=self.validated_data['user_phone'],
            password=self.validated_data['password2']
        )
        user.save()
        return user

class UserDataLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def save(self):
        try:
            a = UserData.objects.get(email=self.validated_data['email'])
            if a:
                passData = a.password
                if passData == self.validated_data['password']:
                    token, created= Token.objects.get_or_create(user=a)
                    return {'token': token.key, 'user_id': a.user_id}
                raise ValidationError({'error': 'Password Invalid'}) 
        except User.DoesNotExist:
            raise ValidationError({"error":"Account or Email Does Not Exist"})
        


class UserDataMerchantLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['user_phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        try:
            a = UserData.objects.get(user_phone=self.validated_data['user_phone'])
            if a:
                passData = a.password
                if passData == self.validated_data['password']:
                    token, created= Token.objects.get_or_create(user=a)
                    return {'token': token.key, 'user_id': a.user_id}
                raise ValidationError({'error': 'Password Invalid'}) 
        except User.DoesNotExist:
            raise ValidationError({"error":"Merchant Account or Phone Does Not Exist"})

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['first_name','last_name', 'username','email', 'user_address', 'user_phone', 'user_profile_pic', 'user_id']
