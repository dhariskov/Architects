from django.db import models

# Create your models here.
from django.urls import reverse

from architects.authentication.models import Profile, UserModel


class Project(models.Model):
    """Model Project, contains all projects"""
    title = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('add_more_details', kwargs={'pk': self.pk})


class MoreProjectDetails(models.Model):
    """Contains project details, FK to project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField()

    def get_absolute_url(self):
        # return reverse('all_project_details', kwargs={'pk': self.pk})
        return reverse('add_more_details', kwargs={'pk': self.pk})


class Comment(models.Model):
    """Comments to projects, FK to Project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.TextField()
