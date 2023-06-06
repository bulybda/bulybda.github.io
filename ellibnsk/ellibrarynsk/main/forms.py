from .models import News
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Название новости'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),
        }