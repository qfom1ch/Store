from django.urls import path
from .views import IndexView, basket_add, basket_remove, products

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/category/<int:category_id>/', products, name='category'),
    path('products/page/<int:page_number>/', products, name='paginator'),
    path('products/', products, name='products'),
    path('products/baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('products/baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]