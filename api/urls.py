from django.urls import path
from .views import NumberClassifierView 

urlpatterns = [
    path('number-classifier/', NumberClassifierView.as_view(), name='number-classifier'),
]