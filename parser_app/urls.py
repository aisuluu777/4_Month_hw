from django.urls import path
from .views import LitreslistView, LitresFormview, RezkaListView


urlpatterns = [
    path('litres_list', LitreslistView.as_view(), name='litres_list'),
    path('litres_form', LitresFormview.as_view(), name='litres_form'),
    path('rezka_list', RezkaListView.as_view(), name='rezka_list'),
]