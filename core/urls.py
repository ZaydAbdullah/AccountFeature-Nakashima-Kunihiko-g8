from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.item_list_view, name='item_list'),
    path('items/new/', views.item_create_view, name='item_create'),
    path('items/<int:pk>/edit/', views.item_update_view, name='item_update'),
    path('items/<int:pk>/delete/', views.item_delete_view, name='item_delete'),
]