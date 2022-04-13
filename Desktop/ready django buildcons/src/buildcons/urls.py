from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import home, about, contact, interdesign, building, exdesign, renovation, projection


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('interdesign/', interdesign, name='interdesign'),
    path('building/', building, name='building'),
    path('exdesign/', exdesign, name='exdesign'),
    path('projection/', projection, name='projection'),
    path('renovation/', renovation, name='renovation'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)