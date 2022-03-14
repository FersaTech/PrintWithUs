from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from .models import CartDataModel, User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = [ 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        if self.validated_data['password'] != self.validated_data['password2']:
            raise ValidationError({'error': 'Passwords must match'})
        
        if ('email' not in self.validated_data ):
            raise ValidationError({'error': 'Email is required'})
        
        user = User.objects.create(
            email=self.validated_data['email'],
        )
        user.set_password(self.validated_data['password2'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
    
    def save(self, *args, **kwargs):
        try:
            a = User.objects.filter(email=self.validated_data['email']).exists()
            if a:
                passData = User.objects.get(email=self.validated_data['email']).check_password(self.validated_data['password'])
                if passData:
                    token, created = Token.objects.get_or_create(user=User.objects.get(email=self.validated_data['email']))
                    return {'token': token.key, 'user_id': User.objects.get(email=self.validated_data['email']).id}
                raise ValidationError({'error': 'Password Invalid'}) 
        except User.DoesNotExist:
            raise ValidationError({"error":"Account or Email Does Not Exist"})
        


class UserMerchantLoginSerializer(serializers.Serializer):
    mobile = serializers.CharField()
    password = serializers.CharField()

    def save(self):
        try:
            a = User.objects.filter(mobile=self.validated_data['mobile']).exists()
            if a:
                userData = User.objects.get(mobile=self.validated_data['mobile'])
                passData = userData.check_password(self.validated_data['password'])
                if passData:
                    token, created= Token.objects.get_or_create(user=userData)
                    return {'token': token.key, 'user_id': userData.id}
                raise ValidationError({'error': 'Password Invalid!'}) 
            raise ValidationError({'error':'Merchant does not exist!'})
        except User.DoesNotExist:
            raise ValidationError({"error":"Merchant Account or mobile Does Not Exist"})

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name','last_name', 'email', 'address', 'mobile', 'profile_picture', 'is_merchant']


# class UserforCartData(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id']


class CartDataSerializer(serializers.ModelSerializer):
    # user = UserforCartData()
    class Meta:
        model = CartDataModel
        fields = ['user', 'data']