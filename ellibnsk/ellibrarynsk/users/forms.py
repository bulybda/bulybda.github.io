from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea,Select,CharField,PasswordInput,ChoiceField

class RegisterUserForm(UserCreationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class' : 'form-input'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input'}))
    password2 = CharField(label='Повтор пароля', widget=PasswordInput(attrs={'class': 'form-input'}))
    is_staff = ChoiceField(label = 'Роль', widget=Select, choices=(('0','Читатель'),('1','Библиотекарь')))
    class Meta:
        model = User
        fields = ('username','password1','password2','is_staff')
        widgets = {
            "username": TextInput(attrs={
                'class':'form-input',
            }),
            "password1": TextInput(attrs={
                'class': 'form-input',
            }),
            "password2": TextInput(attrs={
                'class': 'form-input',
            }),
            "is_staff": Select(attrs={
                'class': 'form-control',
            })

        }