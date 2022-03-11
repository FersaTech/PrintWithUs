from django.shortcuts import render
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .models import User
from .serializers import UserRegistrationSerializer, UserSerializer, UserLoginSerializer, UserMerchantLoginSerializer

# Create your views here.

@api_view(['POST'])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        if 'user_id' in request.COOKIES and 'token' in request.COOKIES:
            a = Response({'message':'Successfully Logged Out!'}, status=200)
            a.delete_cookie('user_id')
            a.delete_cookie('token')
            return a
        return Response({'message':'Successfully Logged Out!'}, status=200)
            


@api_view(['GET', 'POST'])
def login_view(request):
    if request.method == 'GET':
        serializer = UserLoginSerializer()
        return Response(serializer.data)

    if request.method == 'POST':
        # print(request.data)
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.validated_data)
            a = serializer.save()
            responder = Response(a, status=200)
            responder.set_cookie('token', a['token'])
            responder.set_cookie('user_id', a['user_id'])
            return responder
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def registration_view(request):
    if request.method == "GET":
        a = UserRegistrationSerializer()
        return Response(a.data, status=400)

    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            account = serializer.save()
            data = {}
            data['response'] = "Registration Successful!"
            data['email'] = account.email
            data['id'] = account.id

            token, created = Token.objects.get_or_create(user=account)
            data['token'] = token.key

            cookieResponse = Response(data, status=201)
            cookieResponse.set_cookie('token', data['token'])
            cookieResponse.set_cookie('user_id', data['id'])
            return cookieResponse
            
        return Response(serializer.errors, status=400)




@api_view(['POST'])
def merchant_login_view(request):

    if request.method == 'POST':
        serializer = UserMerchantLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            setCookie = Response(user, status=200)
            setCookie.set_cookie('token', user['token'])
            setCookie.set_cookie('user_id', user['user_id'])
            return setCookie
        else:
            return Response(serializer.errors, status=400)


@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def user_view(request, uID):
    
    if request.method == 'GET':
        user = User.objects.get(user_id=uID)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        user = User.objects.get(user_id=uID)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
        user = User.objects.get(user_id=uID)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user = User.objects.get(user_id=uID)
        user.delete()
        if 'user_id' in request.COOKIES and 'token' in request.COOKIES:
            a = Response({'message':'Account Closed Successfully!'}, status=204)
            a.delete_cookie('user_id')
            a.delete_cookie('token')
            return a
        return Response(status=204)

