from django.urls import path


from . import views
app_name = 'users'

urlpatterns = [
    path('apply/', views.ApplyView.as_view(), name='apply'),
    path('login/', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('employee_list/', views.EmployeeListView.as_view(), name='employee_list'),
]