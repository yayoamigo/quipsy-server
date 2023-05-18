#this is a urls file
from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('productDetail/<int:pk>/', views.ProductDetail.as_view()),
]