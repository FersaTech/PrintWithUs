import uuid
from django.db import models

# Create your models here.
class Categories(models.Model): # GET
    cat_id = models.UUIDField(verbose_name='Category ID', default=uuid.uuid4, editable=False, primary_key=True)
    cat_name = models.CharField(verbose_name='Category Name', default=None, max_length=100)
    cat_desc = models.JSONField(verbose_name='Category Description (in JSON)')

    def __str__(self) -> str:
        return self.cat_name
    
    class Meta:
        verbose_name_plural = 'Categories'


class UserModel(models.Model): # GET, POST, PUT, DELETE
    c_id = models.UUIDField(verbose_name='Customer ID', default=uuid.uuid4, editable=False, primary_key=True)
    c_img = models.FileField(verbose_name='Customer Image', default=None, blank=True, upload_to='media/customer_images')
    c_name = models.CharField(verbose_name='Customer Name', default=None, max_length=100)
    c_email = models.EmailField(verbose_name='Customer Email', default=None, max_length=100)
    c_password = models.CharField(verbose_name='Customer Password', default=None, max_length=100)
    c_phone = models.CharField(verbose_name='Customer Phone', default=None, max_length=100)
    c_address = models.CharField(verbose_name='Customer Address', default=None, max_length=100)

    def __str__(self) -> str:
        return self.c_name
    
    class Meta:
        verbose_name_plural = 'Users'


class Products(models.Model): # GET
    prod_id = models.UUIDField(verbose_name='Product ID', default=uuid.uuid4, editable=False, primary_key=True)
    prod_name = models.CharField(verbose_name='Product Name', default=None, max_length=100)
    prod_img = models.FileField(verbose_name='Product Image', default=None, upload_to='media/product_images')
    prod_desc = models.TextField(verbose_name='Product Description')
    prod_price = models.FloatField(verbose_name='Product Price', default=None)
    prod_cat = models.ForeignKey(Categories, verbose_name='Product Category', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.prod_name
    
    class Meta:
        verbose_name_plural = 'Products'


class OrderModel(models.Model): # GET, POST, PUT, DELETE
    ord_id = models.UUIDField(verbose_name='Order ID', default=uuid.uuid4, editable=False, primary_key=True)
    ord_status = models.CharField(verbose_name='Cancellation Status', default="False", max_length=100)
    ord_delivery_status = models.CharField(verbose_name='Delivery Status', default='7 days', max_length=100)
    ord_date = models.DateTimeField(verbose_name='Order Date', auto_now_add=True)
    ord_user = models.ForeignKey(UserModel, verbose_name='Customer Name', on_delete=models.CASCADE)
    ord_prod = models.ForeignKey(Products, verbose_name='Product Name', on_delete=models.CASCADE)
    ord_price = models.FloatField(verbose_name='Order Price', default=None, blank=True)
    ord_gst = models.CharField(verbose_name='GST No.', default="null", max_length=100)
    ord_qty = models.IntegerField(verbose_name='Quantity', default=None)
    ord_refund_type = models.CharField(verbose_name='Order Refund Status', default='False', max_length=100)
    ord_refund_img = models.FileField(verbose_name='Passbook Image', blank=True, default=None, upload_to='media/order_refund_images')
    ord_feedback = models.TextField(verbose_name='Feedback', default=None, max_length=100)
    ord_bill = models.FileField(verbose_name='Generated Bill', default=None, upload_to='media/order_bills')
    
    def __str__(self) -> str:
        return f"{self.ord_id}"
    
    def save(self, *args, **kwargs):
        self.ord_price = (self.ord_prod.prod_price * self.ord_qty) * (18/100) + (self.ord_prod.prod_price * self.ord_qty)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Orders'

