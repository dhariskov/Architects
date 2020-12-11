from django.db import models


# Create your models here.
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('add_more_details', kwargs={'pk': self.pk})


class MoreProjectDetails(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField()

    def get_absolute_url(self):
        # return reverse('all_project_details', kwargs={'pk': self.pk})
        return reverse('add_more_details', kwargs={'pk': self.pk})

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.TextField()


