import uuid
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class UserData(User):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_address = models.CharField(max_length=100, blank=True, default='Not Provided')
    user_phone = models.CharField(max_length=100, blank=True, default='Not Provided')
    user_profile_pic = models.FileField(upload_to='accountStorage/profile_pics/', blank=True, null=True)
    is_merchant = models.BooleanField(default=False, verbose_name='Merchant', help_text="Check if you are a merchant")

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = 'User Data'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)