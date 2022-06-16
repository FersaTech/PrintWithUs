from rest_framework import serializers
from .models import Coupon, ProductModel, OrderModel, Gallery

# Create your serializers here.

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = "__all__"



class OrderSerializer(serializers.ModelSerializer):
    # customer = serializers.ReadOnlyField(source='customer.user_id')
    # product = ProductSerializerForOrder()
    class Meta:
        model = OrderModel
        fields = ['ord_id', 'customer', 'product', 'ord_quantity', 'ord_price', 'ord_feedback']


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = "__all__"
        # fields = ('ord_id', 'customer', 'product', 'ord_quantity', 'ord_price', 'ord_status', 'ord_image', 'ord_feedback', 'ca')


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"