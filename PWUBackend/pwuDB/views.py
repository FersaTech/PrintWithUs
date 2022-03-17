from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.postgres.search import SearchVector

from pwuDB.models import Categories, Coupon, Orders, Products
from accounts.models import User
from pwuDB.serializers import CategoriesSerializer, CouponSerializer, OrderListSerializer, OrderSerializer, ProductSerializer

# Create your views here.

# View for Category Listing
class CategoryAPIView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


# View for Prodcut Listing
class ProductsAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['category']
    search_fields = ['@name', '@description', '@category__name']


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


class OrderListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tokenData = request.headers['Authorization'].split()[1]
        id = User.objects.get(email=Token.objects.get(key=tokenData).user).id
        
        a = Orders.objects.filter(customer=id)
        serializer = OrderSerializer(a, many=True)
        return Response(serializer.data)


class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = 'ord_id'
    lookup_url_kwarg = 'ord_id'


class CouponRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    lookup_fields = "id"
    lookup_url_kwarg = "cpn_id"