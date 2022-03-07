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
    class Meta:
        model = Orders
        fields = "__all__"