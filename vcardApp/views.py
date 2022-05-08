from rest_framework import generics
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.models import Token

from accounts.models import User
from .serializers import CategorySerializer, CouponSerializer, GallerySerializer, OrderListSerializer, ProductSerializer, OrderSerializer
from .models import CategoryModel, Coupon, ProductModel, OrderModel, Gallery
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Create your views here.

class CategoryAPIView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class ProductAPIView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['category']
    search_fields = ['@name', '@description', '@category__name']


# View for Product Detail Listing
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = 'id'
    lookup_url_kwarg = 'prod_id'


# View for adding Orders
class OrderAddAPIView(generics.CreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]   # Token Authentication is required. Must be passed in headers as 'Authorization' 'Token <token_id>


class OrderListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tokenData = request.headers['Authorization'].split()[1]
        id = User.objects.get(email=Token.objects.get(key=tokenData).user).id
        
        a = OrderModel.objects.filter(customer=id)
        serializer = OrderSerializer(a, many=True)
        return Response(serializer.data)


class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = 'ord_id'
    lookup_url_kwarg = 'ord_id'


class CouponListAPIView(generics.ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class GalleryAPIView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer