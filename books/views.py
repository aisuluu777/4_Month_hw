from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

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