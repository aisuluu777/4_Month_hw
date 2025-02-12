from django.shortcuts import render
from . import models
# Create your views here.

def all_clothes(request):
    if request.method == "GET":
        query = models.ClothesModel.objects.all().order_by('-id')
        context_object_name = {
            'clothes' : query,
        }
        return render(request, template_name='clothes/all_clothes.html', context=context_object_name)

def adult_clothes(request):
    if request.method == "GET":
        query = models.ClothesModel.objects.filter(tags__name='Взрослая').order_by('-id')
        context_object_name = {
            'adults' : query,
        }
        return render(request, template_name='clothes/for_adults.html', context=context_object_name)

def teenagers_clothes(request):
    if request.method == "GET":
        query = models.ClothesModel.objects.filter(tags__name='Подростковая').order_by('-id')
        context_object_name = {
            'teenagers' : query,
        }
        return render(request, template_name='clothes/for_teenagers.html', context=context_object_name)


def children_clothes(request):
    if request.method == "GET":
        query = models.ClothesModel.objects.filter(tags__name='Детская').order_by('-id')
        context_object_name = {
            'children': query,
        }
        return render(request, template_name='clothes/for_children.html', context=context_object_name)




