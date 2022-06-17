from django.db import models
from django.urls import reverse

class CRUD(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    level = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Create your models here.
