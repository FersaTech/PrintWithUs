from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Gallery, ProductModel, OrderModel, Coupon

# Register your models here.
admin.site.site_header = "Print With Us Admin"


class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    search_fields = ('name', 'id')
    list_filter = ('feature_flag', 'shape', 'finish', 'quality', 'thickness')
    list_display = ('name', 'shape', 'quality', 'price')


admin.site.register(ProductModel, ProductAdmin)


class OrdersAdmin(ImportExportMixin, admin.ModelAdmin):
    search_fields = ('id', 'customer')
    list_display = ['customer', 'product', 'ord_price','cancellation_status', 'ord_date']
    list_filter = ['cancellation_status']


admin.site.register(OrderModel, OrdersAdmin)
admin.site.register(Gallery)
admin.site.register(Coupon)