from django.urls import path, include
from product import views

urlpatterns = [
    path('latest-products/', views.LatesProductsList.as_view()),
]