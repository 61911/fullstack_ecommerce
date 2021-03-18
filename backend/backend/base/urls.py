from django.urls import path
from .views import getRoutes, getProducts, getProduct


urlpatterns = [
    path('', getRoutes, name='routers'),
    path('products/', getProducts, name='products'),
    path('products/<str:pk>/', getProduct, name='product'),
]
