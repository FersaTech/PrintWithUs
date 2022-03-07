from django.urls import path

from pwuDB.views import CategoryAPIView, ProductDetailAPIView, ProductsAPIView

urlpatterns = [
    path('', CategoryAPIView.as_view(), name='categories'),
    path('products/', ProductsAPIView.as_view(), name='products'),
    path('products/detail/<prod_id>/', ProductDetailAPIView.as_view(), name='product-detail'),
]
