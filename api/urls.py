from django.urls import path
from django.conf.urls.static import static

from number_classification_api import settings
from .views import number_classifier

urlpatterns = [
    path('', number_classifier, name='number_classifier'),
    path('classify-number/', number_classifier, name='number_classifier'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)