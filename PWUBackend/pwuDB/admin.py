from django.contrib import admin
from .models import UserModel, Categories, Products, OrderModel

# Register your models here.

admin.site.register(UserModel)
admin.site.register(Categories)
admin.site.register(Products)
@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('ord_user', 'ord_prod', 'ord_id')