from django import forms

from projects.models import Project, ProjectDetail


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectProjectDetail(forms.ModelForm):
    class Meta:
        model = ProjectDetail
        fields = '__all__'
