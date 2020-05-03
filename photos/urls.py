from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index),
    path('subservices/<int:pk>', subservice_example, name = 'subservices')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)