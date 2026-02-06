from django import forms
from .models import Author, Opus

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['abbreviation', 'name',  'praenomen', 'nomen', 'cognomen', 'language']

class WorkForm(forms.ModelForm):
    class Meta:
        model = Opus
        fields = ['abbreviation', 'title', 'dialect', 'author']
