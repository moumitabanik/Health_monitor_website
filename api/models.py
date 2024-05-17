from django.db import models


class UserHealthData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    symptoms = models.TextField()
    recommendations = models.TextField(blank=True, null=True)