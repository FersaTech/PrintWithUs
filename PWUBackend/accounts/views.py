from django.shortcuts import render
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .models import UserData
from .serializers import UserDataRegistrationSerializer, UserDataSerializer, UserDataLoginSerializer, UserDataMerchantLoginSerializer

# Create your views here.

@api_view(['POST'])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'message':'Successfully Logged Out!'}, status=200)
            


@api_view(['POST'])
def login_view(request):

    if request.method == 'POST':
        print(request.data)
        serializer = UserDataLoginSerializer(data=request.data)
        if serializer.is_valid():
            a = serializer.save()
            return Response(a, status=200)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = UserDataRegistrationSerializer(data=request.data)

        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email
            data['user_id'] = account.user_id

            token = Token.objects.create(user=account)
            data['token'] = token.key

            # refresh = RefreshToken.for_user(account)
            # data['token'] = {
            #     'refresh': str(refresh),
            #     'access':str(refresh.access_token),
            # }
            
        else:
            data = serializer.errors

        return Response(data, status=201)


@api_view(['POST'])
def merchant_login_view(request):

    if request.method == 'POST':
        serializer = UserDataMerchantLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(user, status=200)
        else:
            return Response(serializer.errors, status=400)


@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def user_view(request, uID):
    
    if request.method == 'GET':
        user = UserData.objects.get(user_id=uID)
        serializer = UserDataSerializer(user)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        user = UserData.objects.get(user_id=uID)
        serializer = UserDataSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
        user = UserData.objects.get(user_id=uID)
        serializer = UserDataSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user = UserData.objects.get(user_id=uID)
        user.delete()
        return Response(status=204)

