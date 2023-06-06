from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('<int:book_id>/booking',views.booking, name='booking'),
    path('<int:book_id>/booking_delete',views.booking_delete, name='booking_delete'),
    path('mybooks',views.my_books,name='my_books')
]