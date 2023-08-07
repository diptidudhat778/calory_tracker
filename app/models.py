from django.db import models

class Food(models.Model):
    class Meta:
        app_label = 'app'
    name = models.CharField(max_length=10)
    calories = models.PositiveIntegerField()
