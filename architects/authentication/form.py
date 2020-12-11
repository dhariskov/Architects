import unicodedata

from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from django.contrib.auth.models import User


class FirstName(forms.CharField):
    """those are form extensions """
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            'autocapitalize': 'none',
            'autocomplete': 'first_name',
        }


class LastName(forms.CharField):
    """those are form extensions """
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            'autocapitalize': 'none',
            'autocomplete': 'last_name',
        }


class UserCreationAddForm(UserCreationForm):
    """Extended  user creation from with first and last names"""
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")
        field_classes = {
            'username': UsernameField,
            'first_name': FirstName,
            'last_name': LastName,
        }
