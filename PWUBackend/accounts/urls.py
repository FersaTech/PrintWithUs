from django.urls import path
from .views import *
from rest_framework.authtoken import views

urlpatterns = [
    path('<uuid:uID>/', user_view, name='account'),
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='account'),
    path('login/merchant/', merchant_login_view, name='merchant_login'),
    path('logout/', logout_view, name='logout'),
]
