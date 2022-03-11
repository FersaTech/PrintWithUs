from rest_framework import serializers

from pwuDB.models import Categories, Orders, Products


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



class OrderSerializer(serializers.ModelSerializer):
    # customer = serializers.ReadOnlyField(source='customer.user_id')
    # product = serializers.ReadOnlyField(source='product.id')
    class Meta:
        model = Orders
        fields = ('ord_id', 'customer', 'product', 'ord_quantity', 'ord_feedback',)


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('ord_id', 'customer', 'product', 'ord_quantity', 'ord_price', 'ord_status', 'ord_feedback',)