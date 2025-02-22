from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models, forms
from django.views import generic


class SearchView(generic.ListView):
    template_name = 'book.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return models.BookModel.objects.filter(title__icontains=query)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context



class BookListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book'
    model = models.BookModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'
    model = models.BookModel

    def get_object(self, *args, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.BookModel, id=book_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = forms.ReviewForm()
        return context


class CreateReviewView(generic.edit.CreateView):
    template_name = 'book_detail.html'
    form_class = forms.ReviewForm
    success_url = '/book_detail/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewView, self).form_valid(form=form)


















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