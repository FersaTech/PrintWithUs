from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from .models import UserData


class UserDataRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}


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
