from django.urls import path
from . import views
from .models import Shoe

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shoes/', views.shoes_index, name='index'),
    # shoes/:id/
    path('shoes/<int:shoe_id>/', views.shoes_detail, name='detail'),
    # shoes/create/
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
    # shoes/:id/update
    path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoes_update'),
    # shoes/:id/delete
    path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoes_delete'),
    path('shoes/<int:shoe_id>/add_history/', views.add_history, name='add_history'),
    # associate a cleaning product with a shoe (M:M)
    path('shoes/<int:shoe_id>/assoc_cleaning_product/<int:cleaning_product_id>', views.assoc_cleaning_product, name='assoc_cleaning_product'),
    path('shoes/<int:shoe_id>/unassoc_cleaning_product/<int:cleaning_product_id>', views.unassoc_cleaning_product, name='unassoc_cleaning_product'),
    path('cleaning_products/', views.Cleaning_ProductList.as_view(), name='cleaning_products_index'),
    path('cleaning_products/<int:pk>/', views.Cleaning_ProductDetail.as_view(), name='cleaning_products_detail'),
    path('cleaning_products/create/', views.Cleaning_ProductCreate.as_view(), name='cleaning_products_create'),
    path('cleaning_products/<int:pk>/update/', views.Cleaning_ProductUpdate.as_view(), name='cleaning_products_update'),
    path('cleaning_products/<int:pk>/delete/', views.Cleaning_ProductDelete.as_view(), name='cleaning_products_delete'),
]