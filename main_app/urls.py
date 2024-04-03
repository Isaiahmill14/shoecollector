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
]