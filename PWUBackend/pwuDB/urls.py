from django.urls import path

from pwuDB.views import CategoryAPIView, OrderAddAPIView, OrderListAPIView, ProductDetailAPIView, ProductsAPIView

urlpatterns = [
    path('', CategoryAPIView.as_view(), name='categories'),
    path('products/', ProductsAPIView.as_view(), name='products'),
    path('products/detail/<prod_id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('orders/add/', OrderAddAPIView.as_view(), name='orders'),
    path('orders/list/<uuid:id>/', OrderListAPIView.as_view(), name='order-list'),
]
