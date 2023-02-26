from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, ProductCategory

class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Store'
        return context


class Products(TemplateView):
    template_name = 'products/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Store - Каталог'
        context['products']= Product.objects.all()
        context['categories']= ProductCategory.objects.all()
        return context