from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from pwuDB.models import Categories, Orders, Products
from pwuDB.serializers import CategoriesSerializer, OrderListSerializer, OrderSerializer, ProductSerializer

# Create your views here.
class CategoryAPIView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class ProductsAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = 'id'
    lookup_url_kwarg = 'prod_id'


class OrderAddAPIView(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticated,)

class OrderListAPIView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('customer',)