from django.urls import path

from vcardApp.views import (CouponListAPIView,
                            GalleryAPIView,
                            OrderAddAPIView,
                            OrderListAPIView,
                            OrderUpdateAPIView,
                            ProductAPIView, RecommendedAPIView)

urlpatterns = [
    path('', ProductAPIView.as_view(), name='categories'),
    path('orders/add/', OrderAddAPIView.as_view(), name='orders-add'),
    path('orders/list/', OrderListAPIView.as_view(), name='orders-list'),
    path('orders/list/<ord_id>/', OrderUpdateAPIView.as_view(), name='orders-update'),
    path('coupon/', CouponListAPIView.as_view(), name='coupons'),
    path('gallery/', GalleryAPIView.as_view(), name='gallery'),
    path('recommended/', RecommendedAPIView.as_view(), name='recommended'),
]
