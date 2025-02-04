from django.urls import path
from .views import NumberClassifierView 

urlpatterns = [
   
 path('', NumberClassifierView.as_view(), name='number-classifier'),
]