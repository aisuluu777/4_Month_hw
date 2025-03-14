# Generated by Django 5.1.5 on 2025-02-10 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmodel',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='audi_book',
            field=models.URLField(verbose_name='укажите ссылку с ютуба'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='genre',
            field=models.CharField(choices=[('ROMANCE', 'ROMANCE'), ('FANTASY', 'FANTASY'), ('CLASSIC', 'CLASSIC'), ('MYSTERY', 'MYSTERY'), ('PHSYCOLOGY', 'PHSYCOLOGY'), ('THRILLER', 'THRILLER'), ('DRAMA', 'DRAMA')], default='CLASSIC', max_length=15, verbose_name='Выберите жанр'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='price',
            field=models.PositiveIntegerField(default=250, verbose_name='Введите цену'),
        ),
    ]
