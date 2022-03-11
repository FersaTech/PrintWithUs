from django.contrib import admin
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin 

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class UserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = UserAdminCreationForm
    form = UserAdminChangeForm
    model = User

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email', 'admin']
    list_filter = ['admin']
    fieldsets = (
        ('Basic Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'mobile', 'address', 'profile_picture')}),
        ('Permissions', {'classes':('collapse',),'fields': ('admin', 'staff', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()

# admin.site.unregister(User)
admin.site.register(User, UserAdmin)