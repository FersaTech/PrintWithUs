from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import CategoryModel, Gallery, ProductModel, OrderModel, Coupon

# Register your models here.
admin.site.site_header = "Print With Us Admin"
admin.site.register(CategoryModel)
admin.site.register(ProductModel)
class OrdersAdmin(ImportExportMixin, admin.ModelAdmin):
    search_fields = ('id', 'customer')
    list_display = ['customer', 'product', 'ord_price','cancellation_status', 'ord_date']
    list_filter = ['cancellation_status']
admin.site.register(OrderModel, OrdersAdmin)
admin.site.register(Gallery)
admin.site.register(Coupon)