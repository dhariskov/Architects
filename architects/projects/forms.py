from django import forms

from projects.models import Project, MoreProjectDetails, Comment


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class MoreProjectDetailsForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput)
    description = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
