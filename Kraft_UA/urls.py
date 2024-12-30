from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Kraft_UA import settings
from main_Kr.views import home
from Kraft_UA import settings

urlpatterns = [
    path('',home, name='home'),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)