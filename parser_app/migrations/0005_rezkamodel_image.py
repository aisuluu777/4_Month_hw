# Generated by Django 5.1.5 on 2025-02-22 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0004_remove_litresmodel_cover_litresmodel_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='rezkamodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='rezka/'),
        ),
    ]
