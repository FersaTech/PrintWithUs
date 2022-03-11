import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Categories(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name          = models.CharField(max_length=50, blank=False, null=False)
    description   = models.JSONField(blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    id                  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image               = models.FileField(upload_to='product/product_images/', blank=False, null=False)
    name                = models.CharField(max_length=50, blank=False, null=False)
    description         = models.TextField(blank=False, null=False)
    category            = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price               = models.FloatField(default=0.0, blank=False, null=False)
    merchant_price      = models.IntegerField(default=0.0, blank=False, null=False)

    def __str__(self):
        return self.name


class Orders(models.Model):
    ord_id               = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    customer             = models.ForeignKey(User, on_delete=models.CASCADE)
    product              = models.ForeignKey(Products, on_delete=models.CASCADE)
    ord_quantity         = models.IntegerField(default=0, blank=False, null=False)
    ord_price            = models.FloatField(default=0.0, blank=False, null=False)
    ord_date             = models.DateTimeField(auto_now_add=True)
    ord_status           = models.CharField(max_length=50, blank=False, null=False, default='Pending')
    ord_feedback         = models.TextField(blank=True, null=True)
    cancellation_status  = models.CharField(max_length=50, blank=False, null=False, default='No')
    user_gst_num         = models.CharField(max_length=100, blank=True, default='Not Provided')
    user_refund_cheque   = models.FileField(upload_to='OrderRefund/', blank=True)

    def __str__(self):
        return self.customer.email
    
    def save(self):
        gst = (self.order_product.product_price*self.order_quantity) * 0.18
        self.order_price = (self.order_product.product_price*self.order_quantity) + gst
        super().save()