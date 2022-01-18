from django import forms
from django.forms import fields, widgets

from .models import Headline, Post

class HeadlineForm(forms.ModelForm):
    class Meta:
        model = Headline
        fields = ['text']
        labels = {'text' : ''}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
