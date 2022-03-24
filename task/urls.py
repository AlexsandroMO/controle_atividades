
from django.urls import path
from .views import home, listaFunc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home-home'),
    path('Lista_Fun', listaFunc, name='lista-func'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)