from django.urls import path
from . import views



urlpatterns = [
    path('create_basket/', views.CreateBasketView.as_view(), name='create_basket'),
    path('basket_list_view/', views.BasketListView.as_view(), name='basket_list'),
    path('basket_list_view/<int:id>/delete/', views.BasketDeleteView.as_view(), name='delete_basket'),
    path('basket_list_view/<int:id>/update/', views.BasketUpdateView.as_view(), name='update_basket'),
]

