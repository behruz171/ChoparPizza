from django.db import models
from apps.users.models import User
SMALL, MEDIUM, LARGE = 'small', 'medium', 'large'

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name


class ProductInfo(BaseModel):
    img = models.ImageField(upload_to='./images')
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product_name


class Product(BaseModel):
    CHOICES_TYPE =(
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large')
    )

    product = models.ForeignKey(ProductInfo, related_name='products', on_delete=models.CASCADE)
    
    weight = models.DecimalField(max_digits=20, decimal_places=2)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return self.product.product_name



class MakePizza(BaseModel):
    CHOICES_TYPE =(
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large')
    )

    first_pizza = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='make_first_pizza')
    last_pizza = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='make_last_pizza')
    type = models.CharField(max_length=255, choices=CHOICES_TYPE, default=MEDIUM)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return self.type



class Korzinka(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='korzinkalar')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user
