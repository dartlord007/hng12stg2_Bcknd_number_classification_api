from django.urls import path
from .views import number_classifier

urlpatterns = [
    path('', number_classifier, name='number_classifier'),
    path('classify-number/', number_classifier, name='number_classifier'),
]