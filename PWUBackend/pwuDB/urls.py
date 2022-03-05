from django.urls import path
from .views import UserModelDetailView, CategoriesListView, ProductsListView, OrderModelListView, OrderModelUpdateView, UserModelRegistrationView

# Create your urlpatterns here.


urlpatterns = [
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('products/', ProductsListView.as_view(), name='products'),
    # path('account/',UserModelDetailView.as_view(), name='user'),
    path('register/', UserModelRegistrationView.as_view(), name='register'),
]

