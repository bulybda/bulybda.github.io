from django.urls import path
from . import views
#ccылки на вкладки#
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('logout/',views.logout_user, name='logout'),
    path('contacts/',views.contacts, name='contacts'),
    path('create_news/',views.create_news, name='create_news')
    ]