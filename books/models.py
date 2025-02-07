from django.db import models

class BookModel(models.Model):
    GENRE_CHOICES = (
        ('ROMANCE', 'ROMANCE'),
        ('FANTASY', 'FANTASY'),
        ('CLASSIC', 'CLASSIC'),
        ('MYSTERY', 'MYSTERY'),
        ('PHSYCOLOGY', 'PHSYCOLOGY'),
        ('THRILLER', 'THRILLER'),
        ('DRAMA', 'DRAMA'),
    )
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите фотографию')
    title = models.CharField(max_length=100, verbose_name='Введите название книги')
    description = models.TextField(verbose_name='Введите краткое описания книги', blank=True)
    price = models.PositiveIntegerField(verbose_name='Введите название', default=250)
    released_date = models.DateField(verbose_name='Укажите дату выпуска')
    genre = models.CharField(max_length=15 ,choices=GENRE_CHOICES, default='CLASSIC',
                             verbose_name='Выберите жанр')
    gmail = models.TextField(verbose_name='Введите почту автора', blank=True)
    author = models.CharField(max_length=100, verbose_name='Введите имя автора', default='No name')
    audi_book = models.URLField(verbose_name='укажите ссылку с ютуба', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'