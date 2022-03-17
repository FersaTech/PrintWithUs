from django.contrib import admin
from .models import Coupon, Products, Categories, Orders
# Register your models here.

admin.site.site_header = "Print With Us Admin"

admin.site.register(Products)
admin.site.register(Categories)


class OrdersAdmin(admin.ModelAdmin):
    search_fields = ('id', 'customer')
    list_display = ['customer', 'product', 'ord_price','cancellation_status', 'ord_date']
    list_filter = ['cancellation_status']
admin.site.register(Orders, OrdersAdmin)

admin.site.register(Coupon)