from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('', include('clothes.urls')),
    path('', include('basket.urls')),
    path('', include('parser_app.urls')),
    path('', include('it_company.urls')),
    path('', include('slider.urls')),
    path('', include('food.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

