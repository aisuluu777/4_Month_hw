# Generated by Django 5.1.5 on 2025-02-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_company', '0003_employeemodel_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='message',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
