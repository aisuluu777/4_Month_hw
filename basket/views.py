from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import BasketForm
from . import models
from django.views import generic

class CreateBasketView(generic.CreateView):
    template_name = 'basket/create_basket.html'
    form_class = BasketForm
    success_url = '/basket_list_view/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBasketView, self).form_valid(form=form)



class BasketListView(generic.ListView):
    template_name = 'basket/basket_list.html'
    context_object_name = 'basket_list'
    model = models.BasketModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')



class BasketDeleteView(generic.DeleteView):
    template_name = 'basket/delete_basket.html'
    success_url = '/basket_list_view/'

    def get_object(self, *args, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketModel, id=basket_id)


class BasketUpdateView(generic.UpdateView):
    template_name = 'basket/basket_update.html'
    form_class = BasketForm
    success_url = '/basket_list_view/'

    def get_object(self, *args, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketModel, id=basket_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BasketUpdateView, self).form_valid(form=form)





