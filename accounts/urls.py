from django.urls import path
from .views import *

urlpatterns = [
    path('user/<uuid:uID>/', user_view, name='account'),
    path('user/cart/<uuid:uID>/', cart_view,name='cart'),
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='account'),
    path('login/merchant/', merchant_login_view, name='merchant_login'),
    path('logout/', logout_view, name='logout'),
]