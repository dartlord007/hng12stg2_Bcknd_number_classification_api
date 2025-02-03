from django.db import models

# Create your models here.

from django.db import models

class Number(models.Model):
    number = models.IntegerField()
    is_prime = models.BooleanField()
    is_perfect = models.BooleanField()
    properties = models.CharField(max_length=255)
    digit_sum = models.IntegerField()
    fun_fact = models.TextField()
