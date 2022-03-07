from django.shortcuts import render
from rest_framework import generics

from pwuDB.models import Categories, Products
from pwuDB.serializers import CategoriesSerializer, ProductSerializer

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

