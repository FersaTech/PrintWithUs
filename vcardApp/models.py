import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from accounts.models import User


# Create your models here.
class Gallery(models.Model):
    first_gallery_image = models.FileField(upload_to='gallery/', blank=True, null=True)
    second_gallery_image = models.FileField(upload_to='gallery/', blank=True, null=True)
    third_gallery_image = models.FileField(upload_to='gallery/', blank=True, null=True)
    fourth_gallery_image = models.FileField(upload_to='gallery/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Gallery'


# Shape choice for the cards
SHAPE_CHOICES = [
    ("rectangle", "Rectangle"),
    ("rounded", "Rounded")
]

# Finish choice for the cards
FINSIH_CHOICES = [
    ("matt", "Matt"),
    ("gloss", "Gloss"),
    ("non lamination", "Non Lamination")
]

# Quality of Paper
QUALITY_CHOICES = [
    ("standard", "Standard"),
    ("premium", "Premium")
]

# Thickness of Paper
THICKNESS_CHOICES = [
    ("250 GSM", "250 GSM"),
    ("300 GSM", "300 GSM")
]


class ProductModel(models.Model):
    id =              models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name =            models.CharField(max_length=50, verbose_name='Name of Product')
    description =     models.TextField(null=True)
    image1 =          models.FileField(upload_to='product_images/', blank=True, default=None)
    image2 =          models.FileField(upload_to='product_images/', blank=True, default=None)
    image3 =          models.FileField(upload_to='product_images/', blank=True, default=None)
    image4 =          models.FileField(upload_to='product_images/', blank=True, default=None)
    shape =           models.CharField(max_length=20, choices=SHAPE_CHOICES, default="rectangle")
    finish =          models.CharField(max_length=20, choices=FINSIH_CHOICES, default="matt")
    quality =         models.CharField(max_length=20, choices=QUALITY_CHOICES, default="premium")
    thickness =       models.CharField(max_length=20, choices=THICKNESS_CHOICES, default="250 GSM")
    price =           models.FloatField(default=0.0)
    feature_flag =    models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Products"


class OrderModel(models.Model):
    ord_id                      = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    customer                    = models.ForeignKey(User, on_delete=models.CASCADE)
    product                     = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    ord_quantity                = models.IntegerField(default=0, blank=False, null=False)
    ord_price                   = models.FloatField(default=0.0, blank=False, null=False)
    ord_date                    = models.DateTimeField(auto_now_add=True)
    ord_status                  = models.CharField(max_length=50, blank=False, null=False, default='Pending')
    ord_feedback                = models.TextField(blank=True, null=True)
    ord_image                   = models.FileField(upload_to='order/customised_images/', blank=True, null=True)
    cancellation_status         = models.CharField(max_length=50, blank=False, null=False, default='No')
    cancellation_date           = models.DateTimeField(blank=True, null=True)
    cancellation_reason         = models.CharField(blank=True, default="None", max_length=50)
    cancellation_description    = models.TextField(blank=True, default="None")
    user_gst_num                = models.CharField(max_length=100, blank=True, default='Not Provided')
    user_refund_cheque          = models.FileField(upload_to='order/OrderRefund/', blank=True)

    def __str__(self):
        return self.customer.email
    
    def save(self, *args, **kwargs):
        gst = (self.product.price*self.ord_quantity) * 0.18
        self.ord_price = (self.product.price*self.ord_quantity) + gst
        super().save()
    
    class Meta:
        verbose_name_plural = "Orders"


class Coupon(models.Model):
    name = models.CharField(verbose_name="Coupon Name", max_length=40, primary_key=True, unique=True)
    discount = models.FloatField(verbose_name="Discount Percent", max_length=40, default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Coupons"


@receiver(post_save, sender=OrderModel)
def send_an_email(sender, created, **kwargs):
    if created:
        orderID = kwargs['instance']
        
        msg =f"Your order for {orderID.product.name} has been placed successfully!\nYour Order Details are ~ \nOrder ID is → {orderID.ord_id}\nProduct Name → {orderID.product.name}\nOrder Price(including GST) → {orderID.ord_price}\nOrder Date → {  orderID.ord_date}\nOrder Status → {orderID.ord_status}"

        send_mail(subject='Order Placed Successfully!', message=msg, from_email='dehimangshu2020@gmail.com', recipient_list=[orderID.customer.email], fail_silently=False)
