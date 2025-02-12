from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Выберите котегорию')

    def __str__(self):
        return self.name

class ClothesModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Введите название одежды')
    price = models.FloatField(verbose_name='Введите цену', default=1500)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
      verbose_name = 'Одежда'
      verbose_name_plural = 'Одежды'

