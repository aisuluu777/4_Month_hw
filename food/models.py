from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=500, verbose_name='Укажите название')
    description = models.TextField(verbose_name='Укажите описание')

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=500, verbose_name='Укажите название ингредиента')
    quantity = models.PositiveIntegerField(verbose_name='Укажите количество')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")




