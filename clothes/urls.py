from django.urls import path
from . import views

urlpatterns = [
    path('all_clothes/', views.all_clothes, name='all_clothes'),
    path('adult_clothes/', views.adult_clothes, name='adult_clothes'),
    path('teenagers_clothes/', views.teenagers_clothes, name='teenagers_clothes'),
    path('children_clothes/', views.children_clothes, name='children_clothes'),
]
