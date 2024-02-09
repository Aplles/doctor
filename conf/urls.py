from django.contrib import admin
from django.urls import path
from django.urls import include
from conf.settings import django as settings
from django.conf.urls.static import static
from conf.yasg import urlpatterns as doc_urls

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('api.urls')),
              ] + doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
