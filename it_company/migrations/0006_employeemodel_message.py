# Generated by Django 5.1.5 on 2025-02-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_company', '0005_remove_employeemodel_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='message',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
