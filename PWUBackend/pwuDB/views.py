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
class CategoryAPIView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class ProductsAPIView(generics.ListAPIView):
    model = Products
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.query_params.get('search', None)
        queryset = Products.objects.annotate(search=SearchVector('name', 'description', 'category')).filter(search=query)
        return queryset    
    
    
# class ProductsAPIView(generics.ListAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_fields = ['category']
#     search_fields = ['@name', '@description', '@category__name']

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = 'id'
    lookup_url_kwarg = 'prod_id'


class OrderAddAPIView(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticated,)

# class OrderListAPIView(generics.ListAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrderListSerializer
#     permission_classes = (IsAuthenticated,)
#     filter_backends = (DjangoFilterBackend,)
#     filterset_fields = ('customer',)

class OrderListAPIView(APIView):

    def post(self, request, id):
        a = Orders.objects.filter(customer=id)
        try:
            serializer = OrderListSerializer(a, many=True)
            return Response(serializer.data)
        except:
            return Response(serializer.errors)