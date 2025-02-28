from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import BasketForm
from . import models
from django.views import generic
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from .models import BasketModel


@method_decorator(cache_page(60 * 15), name='dispatch')
class CreateBasketView(generic.CreateView):
    template_name = 'basket/create_basket.html'
    form_class = BasketForm
    success_url = '/basket_list_view/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBasketView, self).form_valid(form=form)


@method_decorator(cache_page(60 * 15), name='dispatch')
class BasketListView(generic.ListView):
    template_name = 'basket/basket_list.html'
    context_object_name = 'basket_list'
    model = models.BasketModel

    def get_queryset(self):
        baskets = cache.get('baskets')
        if not baskets:
            baskets = self.model.objects.all().order_by('-id')
            cache.set('baskets', baskets,60 * 15)
        return baskets


class BasketDeleteView(generic.DeleteView):
    template_name = 'basket/delete_basket.html'
    success_url = '/basket_list_view/'

    def get_object(self, *args, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketModel, id=basket_id)

        # delete_obj = cache.get('delete_obj')
        # if not delete_obj:
        #     delete_obj = self.kwargs.get('id')
        #     delete_obj = get_object_or_404(models.BasketModel, id=delete_obj)
        #     cache.set('delete_obj', delete_obj, 60 * 15)
        # return delete_obj


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

    # def get_object(self, *args, **kwargs):
    #     update_obj = cache.get('update_obj')
    #     if not update_obj:
    #         update_obj = self.kwargs.get('id')
    #         update_obj = get_object_or_404(models.BasketModel, id=update_obj)
    #         cache.set('update_obj', update_obj)
    #     return update_obj
    #
    # @receiver(post_save, sender=BasketModel)
    # def clean_cache(sender, instance, **kwargs):
    #     cache.delete('update_obj')


