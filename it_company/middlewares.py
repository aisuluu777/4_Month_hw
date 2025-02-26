from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

junior = 600
middle = 1500
senior = 3000


class ExperienceMiddleware(MiddlewareMixin):
    def process_request(self, request):
       if request.path  == '/apply/' and request.method == 'POST':
           experience = int(request.POST.get('experience'))
           if experience == 0:
               return HttpResponseBadRequest('Извините, но мы не принимаем без опыта работы🥲.')
           elif experience >= 1 and experience <= 3:
               request.salary = junior
           elif experience >= 3 and experience <= 5:
               request.salary = middle
           elif experience > 5 and experience <= 30:
               request.salary = senior
           else:
               return HttpResponseBadRequest('Извините, но вы слишком опытны для нас. Спасибо, что прошли регистрацию. Жлаем вам удачи!')
       elif request.path == '/apply/' and request.method == 'GET':
            setattr(request, 'experience', 'Извините что то пошло не так')




