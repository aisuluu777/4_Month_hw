from django.urls import path
from . import views



urlpatterns = [
    path('create_basket/', views.create_basket, name='create_basket'),
    path('basket_list_view/', views.basket_list_view, name='basket_list'),
    path('basket_list_view/<int:id>/delete/', views.delete_basket_view, name='delete_basket'),
    path('basket_list_view/<int:id>/update/', views.update_basket_view, name='update_basket'),
]

