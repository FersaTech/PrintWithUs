from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView

from .models import UserModel, Categories, Products, OrderModel
from .serializers import UserModelSerializer, CategoriesSerializer, ProductsSerializer, OrderModelSerializer
# Create your views here.

class UserModelDetailView(RetrieveUpdateDestroyAPIView):
    pass
    # queryset = UserModel.objects.all()
    # serializer_class = UserModelSerializer
class UserModelRegistrationView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

class CategoriesListView(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class ProductsListView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class OrderModelListView(ListCreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelSerializer

class OrderModelUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelSerializer