from django.contrib import admin

# Register your models here.
from architects.projects.models import Project, MoreProjectDetails, Comment

admin.site.register(Project)
admin.site.register(MoreProjectDetails)
admin.site.register(Comment)

