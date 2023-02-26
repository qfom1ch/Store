from django.db import models



class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    descriptions = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=256)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)


    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'


# from store.wsgi import *
# from products.models import ProductCategory

# python3 manage.py dumpdata products.ProductCategory > categories.json    это dumpdata
# python3 manage.py loaddata products/fixtures/categories.json             это loaddata
# ctr +alt + l форматирование по PIP