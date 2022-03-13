from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django.contrib.postgres.search import SearchVector

from pwuDB.models import Categories, Orders, Products
from pwuDB.serializers import CategoriesSerializer, OrderListSerializer, OrderSerializer, ProductSerializer

# Create your views here.

# View for Category Listing
class CategoryAPIView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


# View for Prodcut Listing
class ProductsAPIView(generics.ListAPIView):
    model = Products
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.query_params.get('search', None)
        queryset = Products.objects.annotate(search=SearchVector('name', 'description', 'category')).filter(search=query)
        return queryset    


# View for Product Detail Listing
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = 'id'
    lookup_url_kwarg = 'prod_id'


# View for adding Orders
class OrderAddAPIView(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]   # Token Authentication is required. Must be passed in headers as 'Authorization' 'Token <token_id>


# View for displaying orders against the customer id
class OrderListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        a = Orders.objects.filter(customer=id)
        try:
            serializer = OrderListSerializer(a, many=True)
            return Response(serializer.data)
        except:
            return Response(serializer.errors)

