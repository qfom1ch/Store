from django.urls import path
from .views import IndexView, Products

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', Products.as_view(), name='products'),
]