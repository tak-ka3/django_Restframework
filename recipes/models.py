from django.db import models
from django.utils import timezone

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    making_time = models.CharField(max_length=100)
    serves = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=300)
    cost = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)