from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField()

