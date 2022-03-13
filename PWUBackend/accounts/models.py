import uuid
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

from .managers import UserManager

# Create your models here.

# User Model for data storage
class User(AbstractBaseUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    address= models.CharField(max_length=100, blank=True)
    profile_picture = models.FileField(upload_to="accountStorage/profile_pictures/", blank=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # merchant = models.BooleanField(default=False)

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    # This manages this User Model. Its functionality is reflected in admin
    objects = UserManager() 

    def get_full_name(self):
        # The user is identified by their first name and last name including a space in between.
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        # The user is identified by their first name.
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin



class CartDataModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField(default=dict)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = "Cart Data"

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)