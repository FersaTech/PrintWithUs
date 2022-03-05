from django.contrib import admin
from .models import UserModel, Categories, Products, OrderModel

# Register your models here.

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('c_id', 'c_name', 'c_email')

admin.site.register(Categories)
admin.site.register(Products)
@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('ord_user', 'ord_prod', 'ord_id')