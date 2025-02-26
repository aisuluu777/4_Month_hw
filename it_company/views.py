
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic
from . import models, forms

class ApplyView(generic.CreateView):
    form_class = forms.CustomRegisterForm
    template_name = 'apply/apply_form.html'

    def get_success_url(self):
        return reverse_lazy('users:login')

class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'apply/login.html'

    def get_success_url(self):
        return reverse_lazy('users:employee_list')

class AuthLogoutView(LogoutView):
    form_class = AuthenticationForm
    template_name = 'apply/login.html'

    def get_success_url(self):
        return reverse_lazy('users:login')


class EmployeeListView(generic.ListView):
    model = models.EmployeeModel
    template_name = 'apply/employees_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return models.EmployeeModel.objects.all().order_by('-id')








