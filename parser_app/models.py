from django.db import models

class LitresModel(models.Model):
    title = models.CharField(max_length=600)
    author = models.CharField(max_length=600, null=True, blank=True, default='no name')

    def __str__(self):
        return self.title

class RezkaModel(models.Model):
    title = models.CharField(max_length=600)
    image = models.ImageField(upload_to='rezka/', null=True, blank=True)

    def __str__(self):
        return self.title