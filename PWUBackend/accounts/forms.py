from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm, UserChangeForm
from django.forms import ValidationError
from .models import User

class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ('email',)
        fields = ('email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user=super(UserCreationForm, self).save(commit=False)
        user.set_password(self.clean_password2())
        if commit:
            user.save()
        return user

class UserAdminChangeForm(UserChangeForm):
    
    class Meta:
        model = User
        # fields = ('email',)
        fields = ('email', 'password')
        # fields = ('email', 'password', 'password2')


