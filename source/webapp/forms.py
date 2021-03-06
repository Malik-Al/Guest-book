from django import forms
from django.forms import widgets


class BookForm(forms.Form):
    author = forms.CharField(max_length=100, label='Author')
    email = forms.CharField(max_length=100, label='Email')
    text = forms.CharField(max_length=2000, label='Текст', widget=widgets.Textarea)
