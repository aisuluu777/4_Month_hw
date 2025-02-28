from django.urls import path

from . import views

urlpatterns = [
    path('recipe_list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe_detail/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe_create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('add_ingridient/', views.IngredientCreateView.as_view(), name='add_ingridient'),
    path('recipe_list/<int:id>/delete/', views.DeleteRecipeView.as_view(), name='recipe_delete'),
    path('recipe_list/<int:id>/update/', views.UpdateRecipeView.as_view(), name='recipe_update'),
]