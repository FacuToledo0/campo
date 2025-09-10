from django.contrib import admin  # 👈 IMPORTANTE
from django.urls import path
from propiedades import views  # 👈 Importá tus vistas

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # 👈 Usás admin.site.urls
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('lista_campos', views.lista_campos, name='lista_campos'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
