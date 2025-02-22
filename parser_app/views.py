from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from . import models, forms


class LitreslistView(generic.ListView):
    template_name = 'parser/litres_list.html'
    context_object_name = 'litres'
    model = models.LitresModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class LitresFormview(generic.FormView):
    template_name = 'parser/litres_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            if form.cleaned_data['media_type'] == 'litres.ru':
                return redirect('litres_list')
            else:
                return redirect('rezka_list')


        else:
            return super(LitresFormview, self).post(request, *args, **kwargs)


class RezkaListView(generic.ListView):
    template_name = 'parser/rezka_list.html'
    context_object_name = 'rezka'
    model = models.RezkaModel


    def get_queryset(self):
        return self.model.objects.all().order_by('id')

