from django.db import models
from django.contrib.auth.models import User

junior = 600
middle = 1500
senior = 3000

class EmployeeModel(User):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    age = models.PositiveIntegerField(verbose_name='Укажите ваш возраст')
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True)
    it_direction = models.CharField(max_length=700, verbose_name='Укажите ваше направление в айти')
    skills = models.TextField(verbose_name='Укажите ваши навыки')
    experience = models.PositiveIntegerField(verbose_name='Укажите опыт работы')
    any_projects = models.TextField(verbose_name='Укажите проекты в которых вы участвовали')
    linkedin = models.CharField(max_length=700, verbose_name='Укажите ссылку вашего Linkedin')
    salary = models.PositiveIntegerField()


    def save(self, *args, **kwargs):
        if self.experience == 0:
            self.message = 'Извините, но мы не принимаем без опыта работы🥲.'
            self.salary = 0
        elif 1 >= self.experience < 3:
            self.salary = junior
        elif 3 >= self.experience < 5:
            self.salary = middle
        elif 5 >= self.experience < 30:
            self.salary = senior
        else:
            self.message = 'Извините, но вы слишком опытны для нас. Спасибо, что прошли регистрацию. Жлаем вам удачи!'
            self.salary = 0

        super().save(*args, **kwargs)



