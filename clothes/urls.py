from django.urls import path
from . import views

urlpatterns = [
    path('all_clothes/', views.ClothesListView.as_view(), name='all_clothes'),
    path('adult_clothes/', views.AdultClothesView.as_view(), name='adult_clothes'),
    path('teenagers_clothes/', views.TeenClothesView.as_view(), name='teenagers_clothes'),
    path('children_clothes/', views.KidClothesView.as_view(), name='children_clothes'),
]
