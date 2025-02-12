from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from .models import Review


def book_list_view(request):
    if request.method == 'GET':
        query = models.BookModel.objects.all().order_by('-id')
        context_object_name = {
            'book' : query,
        }
        return render(request, template_name='book.html',
                      context=context_object_name)


def book_detail_view(request, id):
    if request.method == 'GET':
        query = get_object_or_404(models.BookModel, id=id)
        context_object_name = {
            'book_id' : query,
        }
        return render(request, template_name='book_detail.html',
                      context=context_object_name)






# Create your views here.
def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Name: Aisuluu\n'
                            'Age: 16\n'
                            'Type: introvert')

def text_and_photo(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Ice cream</h1>'
            '<img src="https://www.foodandwine.com/thmb/QnTrAIt3aY1g4ToQEk-jULmKMsQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/vanilla-ice-cream-FT-RECIPE0324-cebca493f53c4431a0049ea65bfb4796.jpg" />')


def system_time(request):
    if request.method == 'GET':
        current_time = datetime.now()
        return HttpResponse(current_time)