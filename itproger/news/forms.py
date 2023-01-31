from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form_control',
                'placeholder': 'Name of news'
            }),
            "anons": TextInput(attrs={
                'class': 'form_control',
                'placeholder': 'Name of anons'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form_control',
                'placeholder': 'date of publishing'

            }),
            "full_text": Textarea(attrs={
                'class': 'form_control',
                'placeholder': 'Text of news'
            }),
        }
