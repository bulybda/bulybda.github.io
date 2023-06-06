from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from .forms import RegisterUserForm

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('auth')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/register.html'

