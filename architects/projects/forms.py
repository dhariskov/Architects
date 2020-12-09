from django import forms

from projects.models import Project, MoreProjectDetails


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class MoreProjectDetailsForm(forms.Form):
    image = forms.ImageField(required=False, widget=forms.FileInput)
    description = forms.CharField(required=False, widget=forms.Textarea)
