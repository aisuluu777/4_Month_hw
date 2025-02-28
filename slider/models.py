from django.db import models

class SliderModel(models.Model):
    image = models.ImageField(upload_to='sliders/')

