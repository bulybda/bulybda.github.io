from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import News,Banner
from .forms import NewsForm

def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def contacts(request):
    return render(request, 'main/contacts.html')

def home(request):
        news = News.objects.all()
        banners = Banner.objects.all()
        return render(request, 'main/index.html', {'news': news, 'banners': banners})


def create_news(request):
    print("aaa")
    error = ''
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка формы'
    form = NewsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/create_news.html', data)