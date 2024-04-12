from django.conf import settings
from django.contrib import admin
from django.urls import path
from apps.common.views import *
from apps.users.views import *
from apps.users.views import *

urlpatterns = [
    path("product-info/", ProductInfoView.as_view()),
    path("product-list/", ProductView.as_view()),
    path('create-product-info/', CreateProductInfoView.as_view()),
    path('create-product/', CreateProductView.as_view()),
    path('update-product-info/<int:pk>', UpdateProductInfoView.as_view()),
    path('update-product/<int:pk>', UpdateProductView.as_view()),
    path('korzinka/<int:pk>', KorzinkaListView.as_view()),
    path('add-product-korzinka/', AddProductKorzinkaView.as_view()),
    path('update-korzinka/<int:pk>', UpdateProductKorzinkaView.as_view()),
    path('sign-up/', SignupView.as_view()),
    path('login/', SignInView.as_view()),
]

