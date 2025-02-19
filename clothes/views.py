from django.shortcuts import render
from . import models
from django.views import generic


class ClothesListView(generic.ListView):
    template_name = 'clothes/all_clothes.html'
    context_object_name = 'clothes'
    model = models.ClothesModel

    def get_queryset(self):
        return  self.model.objects.all().order_by('-id')



class AdultClothesView(generic.ListView):
    template_name = 'clothes/for_adults.html'
    context_object_name = 'adults'
    model = models.ClothesModel

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Взрослая').order_by('-id')



class TeenClothesView(generic.ListView):
    template_name = 'clothes/for_teenagers.html'
    context_object_name = 'teenagers'
    model = models.ClothesModel

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Подростковая').order_by('-id')



class KidClothesView(generic.ListView):
    template_name = 'clothes/for_children.html'
    context_object_name = 'children'
    model = models.ClothesModel

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Детская').order_by('-id')
