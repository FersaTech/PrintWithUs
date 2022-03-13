from django.http import JsonResponse
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


# View for displaying orders against the customer id
# class OrderListAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderListSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_fields = ['customer']
#     lookup_url_kwarg = 'customer'
    
#     def get_queryset(self):
#         a = Orders.objects.filter(customer=self.kwargs['customer'])
#         return a
    #     # try:
    #         # serializer = OrderListSerializer(a, many=True)
    #         # return Response(serializer.data)
    #     # except:
    #         # return Response(serializer.errors)


class OrderListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        a = Orders.objects.filter(customer=id)
        try:
            serializer = OrderListSerializer(a, many=True)
            return Response(serializer.data)
        except:
            return Response(serializer.errors)
    
    def put(self, request, id):
        a = Orders.objects.filter(customer=id)

        for items in request.data.keys():
            if 'cancellation_status' in items:
                a.update(cancellation_status=request.data['cancellation_status'])
                return Response({'message':'updated the details'}, status=200)
            
            if 'ord_feedback' in items:
                a.update(ord_feedback=request.data['ord_feedback'])
                return Response({'message':'updated the details'}, status=200)
            
            if 'ord_status' in items:
                a.update(ord_status=request.data['ord_status'])
                return Response({'message':'updated the details'}, status=200)
                
            else:
                return Response({'message':'{} does not exist!'.format(items)}, status=400)