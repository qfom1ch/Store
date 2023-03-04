from django.urls import path
from .views import IndexView, Products, basket_add, basket_remove

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', Products.as_view(), name='products'),
    path('products/baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('products/baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]