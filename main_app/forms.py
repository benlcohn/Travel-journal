from django import forms
from .models import Journal, Comment, Entry

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['title', 'description', 'date', 'content', 'location']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title','text']