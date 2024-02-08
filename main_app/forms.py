from django import forms
from django.forms import TextInput
from .models import Journal, Comment, Entry

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['title', 'description', 'date', 'location']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title','text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'margin: 20px 0 0 0;'
            })
        }