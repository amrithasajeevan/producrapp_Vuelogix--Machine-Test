from django.urls import path
from .views import *
urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register-api'),
    path('login/', usersigninview.as_view(), name='login-api'),
    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('orders/', OrderAPIView.as_view(), name='order-list'),
    path('highest-ordered-products/', ProductOrderListView.as_view(), name='highest_ordered_products'),
   

]