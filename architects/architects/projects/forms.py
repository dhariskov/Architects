from django import forms

# from architects.projects.models import Project


# class ProjectCreateForm(forms.ModelForm):
#     """project creation from"""
#     class Meta:
#         model = Project
#         fields = '__all__'


class MoreProjectDetailsForm(forms.Form):
    """form used to add more details to project"""
    image = forms.ImageField(widget=forms.FileInput)
    description = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.Form):
    """for used to all comments to project"""
    comment = forms.CharField(widget=forms.Textarea)


class FilterForm(forms.Form):
    """form used to add search criteria"""
    SEARCH_BY_TITLE = 'title'
    SEARCH_BY_TYPE = 'type'

    ORDER_CHOICES = (
        (SEARCH_BY_TITLE, 'Project title'),
        (SEARCH_BY_TYPE, 'Project type'),
    )

    text = forms.CharField(
        required=False,
    )
    order = forms.ChoiceField(
        choices=ORDER_CHOICES,
        required=False,
    )
