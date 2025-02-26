
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class CustomRegisterForm(UserCreationForm):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    email = forms.EmailField(required=True, label='Укажите ваш email')
    age = forms.IntegerField(required=True,label='Укажите ваш возраст')
    gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES)
    it_direction = forms.CharField(required=True, label='Укажите ваше направление в айти')
    skills = forms.CharField(required=True,label='Укажите ваши навыки')
    experience = forms.IntegerField(required=True,  label='Укажите опыт работы')
    any_projects = forms.CharField(required=True, label='Укажите проекты в которых вы участвовали')
    linkedin = forms.CharField(required=True, label='Укажите ссылку вашего Linkedin')

    class Meta:
        model = models.EmployeeModel
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'age',
            'gender',
            'it_direction',
            'skills',
            'experience',
            'any_projects',
            'linkedin',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        employee = super().save(commit=False)
        employee.first_name = self.cleaned_data['first_name']
        employee.email = self.cleaned_data['email']
        employee.age = self.cleaned_data['age']
        employee.gender = self.cleaned_data['gender']
        employee.it_direction = self.cleaned_data['it_direction']
        employee.skills = self.cleaned_data['skills']
        employee.experience = self.cleaned_data['experience']
        employee.any_projects = self.cleaned_data['any_projects']
        employee.linkedin = self.cleaned_data['linkedin']

        if commit:
            employee.save()
        return employee



