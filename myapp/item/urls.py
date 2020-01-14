from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.item_list),
    path('product/<int:item_pk>/', views.item_detail),
]