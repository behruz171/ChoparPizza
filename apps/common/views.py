from . import serializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from . import models
from rest_framework.views import Response, APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.db.models import Sum


class ProductInfoView(ListAPIView):
    queryset = models.ProductInfo.objects.all()
    serializer_class = serializers.ProductInfoSerializer

class ProductView(ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class CreateProductInfoView(CreateAPIView):
    queryset = models.ProductInfo.objects.all()
    serializer_class = serializers.CreateProductInfoSerializer

class CreateProductView(CreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.CreateProduct


class UpdateProductInfoView(RetrieveUpdateDestroyAPIView):
    queryset = models.ProductInfo.objects.all()
    serializer_class = serializers.UpdateProductInfoSerializer


class UpdateProductView(RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.UpdateProductSerializer


class KorzinkaListView(ListAPIView):
    serializer_class = serializers.KorzinkaListSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return models.Korzinka.objects.filter(user__id=pk)


class AddProductKorzinkaView(CreateAPIView):
    queryset = models.Korzinka
    serializer_class = serializers.AddProductKorzinkaSerializer

