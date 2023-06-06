from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date','count']

        widgets = {
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Название книги'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор' #Анонс статьи#
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание книги'
            }),
            "count": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество',
            })


        }