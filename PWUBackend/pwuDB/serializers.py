from rest_framework import serializers

from pwuDB.models import Categories, Coupon, Orders, Products


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class CategorySerializerForProduct(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('description',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializerForProduct()

    class Meta:
        model = Products
        fields = "__all__"


class ProductSerializerForOrder(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id']
        # read_only_fields = ['id']


class OrderSerializer(serializers.ModelSerializer):
    # customer = serializers.ReadOnlyField(source='customer.user_id')
    # product = ProductSerializerForOrder()
    class Meta:
        model = Orders
        fields = ['ord_id', 'customer', 'product', 'ord_quantity', 'ord_price', 'ord_feedback']


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"
        # fields = ('ord_id', 'customer', 'product', 'ord_quantity', 'ord_price', 'ord_status', 'ord_image', 'ord_feedback', 'ca')


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"