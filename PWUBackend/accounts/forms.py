from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm, UserChangeForm
from django.forms import ValidationError
from .models import User

class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
        # fields = ('email', 'password_1', 'password_2')


class UserAdminChangeForm(UserChangeForm):
    
    class Meta:
        model = User
        # fields = ('email',)
        fields = ('email', 'password')
        # fields = ('email', 'password', 'password2')


