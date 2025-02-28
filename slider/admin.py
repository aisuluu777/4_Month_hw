from django.contrib import admin
from django import forms
from PIL import Image
from . import models

class ImageForm(forms.ModelForm):
    class Meta:
        model = models.SliderModel
        fields = ['image']

    def clean(self):
        super().clean()
        if self.cleaned_data.get('image'):
            try:
                img = Image.open(self.cleaned_data.get('image'))
                width, height = img.size
                print(width, height)
                if width >= 600 and height >= 900:
                    raise forms.ValidationError('Размер книги должен быть не больше ширина:600 и высота: 900')
            except Exception as e:
                raise forms.ValidationError(f'Ошибки в обработке фотографии{e}')


class SliderForm(admin.ModelAdmin):
    form = ImageForm

admin.site.register(models.SliderModel, SliderForm)

