from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import BasketForm
from . import models

def create_basket(request):
    if request.method == 'POST':
        form = BasketForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            order_id = order.product_choice.id
            return redirect('book_detail', id=order_id)
        else:
            return HttpResponse('Корзина успешно обработана')
    form = BasketForm()
    return render(request, 'basket/create_basket.html', {'form': form})


def basket_list_view(request):
    if request.method == 'GET':
        query = models.BasketModel.objects.all()
        context_object_name = {
            'basket_list': query,
        }
        return render(request, template_name='basket/basket_list.html', context=context_object_name)

def delete_basket_view(request, id):
    product_id = get_object_or_404(models.BasketModel, id=id)
    product_id.delete()
    return redirect('basket_list')

def update_basket_view(request, id):
    product_id =get_object_or_404(models.BasketModel, id=id)
    if request.method == 'POST':
        form = BasketForm(request.POST, instance=product_id)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
        else:
            return HttpResponse('')
    form = BasketForm()
    return render(request, 'basket/basket_update.html', {'form': form})





