from django import forms
from . import models, parser_litres, parser_rezka

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
         ('litres.ru', 'litres.ru'),
         ('rezka.ag', 'rezka.ag'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ['media_type']


    def parser_data(self):
        if self.data['media_type'] == 'litres.ru':
            litres_books = parser_litres.parsing_litres()
            for i in litres_books:
                models.LitresModel.objects.create(**i)
        elif self.data['media_type'] == 'rezka.ag':
            rezka_films = parser_rezka.parsing_rezka()
            for i in rezka_films:
                models.RezkaModel.objects.create(**i)


