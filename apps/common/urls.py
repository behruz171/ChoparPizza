from django.conf import settings
from django.contrib import admin
from django.urls import path
from apps.common.views import *
from . import views

urlpatterns = [
    path("product-info/", views.ProductInfoView.as_view()),
    path("product-list/", views.ProductView.as_view()),
    path('create-product-info/', views.CreateProductInfoView.as_view()),
    path('create-product/', views.CreateProductView.as_view()),
    path('update-product-info/<int:pk>', views.UpdateProductInfoView.as_view()),
    path('update-product/<int:pk>', views.UpdateProductView.as_view()),
    path('korzinka/<int:pk>', views.KorzinkaListView.as_view()),
    path('add-product-korzinka/', views.AddProductKorzinkaView.as_view()),
]

