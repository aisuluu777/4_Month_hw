from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from . import models, forms
from django.views import generic


class RecipeListView(generic.ListView):
    template_name = 'food/recipe_list.html'
    context_object_name = 'recipe_list'
    model = models.Recipe

    def get_queryset(self):
         return self.model.objects.all()


class RecipeDetailView(generic.DetailView):
    template_name = 'food/recipe_detail.html'
    model = models.Recipe
    context_object_name = 'recipe'

    def get_object(self):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.Recipe, id=recipe_id)


class RecipeCreateView(generic.CreateView):
    template_name = 'food/recipe_create.html'
    model = models.Recipe
    form_class = forms.RecipeForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(RecipeCreateView, self).form_valid(form=form)

    def get_success_url(self):
        return reverse_lazy('add_ingridient')

class IngredientCreateView(generic.CreateView):
    model = models.Ingredient
    form_class = forms.IngredientForm
    template_name = "food/add_ingridient.html"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)

    def get_success_url(self):
        return reverse_lazy("recipe_list")


class UpdateRecipeView(generic.UpdateView):
    template_name = 'food/recipe_update.html'
    form_class = forms.IngredientForm

    def get_object(self):
        obj_id = self.kwargs.get('id')
        return get_object_or_404(models.Recipe, id=obj_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateRecipeView, self).form_valid(form=form)

    def get_success_url(self):
        return reverse_lazy('recipe_list')


class DeleteRecipeView(generic.DeleteView):
    template_name = 'food/recipe_delete.html'

    def get_object(self):
        obj_id = self.kwargs.get('id')
        return get_object_or_404(models.Recipe, id=obj_id)

    def get_success_url(self):
        return reverse_lazy('recipe_list')


