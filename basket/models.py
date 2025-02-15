from django.db import models
from books.models import BookModel

class BasketModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Введите своё имя')
    address = models.TextField(verbose_name='Введите адрес пункта выдачи')
    gmail = models.EmailField(verbose_name='Введите свой адрес электронной почты')
    product_choice = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return f'{self.name}-{self.product_choice.title}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


