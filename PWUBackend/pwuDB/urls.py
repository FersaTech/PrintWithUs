from django.urls import path

from pwuDB.views import CategoryAPIView, CouponRetrieveAPIView, OrderAddAPIView, OrderListAPIView, OrderUpdateAPIView, ProductDetailAPIView, ProductsAPIView

urlpatterns = [
    path('', CategoryAPIView.as_view(), name='categories'),
    path('products/', ProductsAPIView.as_view(), name='products'),
    path('products/detail/<prod_id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('orders/add/', OrderAddAPIView.as_view(), name='orders'),
    # path('orders/list/<customer>/', OrderListAPIView.as_view(), name='order-list'),
    path('orders/list/', OrderListAPIView.as_view(), name='order-list'),
    path('orders/list/<ord_id>/', OrderUpdateAPIView.as_view(), name='order-list'),
    path('coupon/<cpn_id>/', CouponRetrieveAPIView.as_view(), name="coupon-list"),
]
