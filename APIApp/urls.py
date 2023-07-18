from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ProductList.as_view(), name='product-list'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
]
