from django.urls import path
from . import views
from .views import RegisterUser, LoginUser

urlpatterns = [
    path('', LoginUser.as_view(), name='auth'),
    path('register/', RegisterUser.as_view(), name = 'register'),
]