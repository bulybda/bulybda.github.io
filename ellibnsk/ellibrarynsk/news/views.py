from django.shortcuts import render, redirect
from .models import Articles,CartUser
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    filter_query = request.GET
    try:
        sort_query = request.GET['sort']
    except:
        sort_query = "-date"
    if (sort_query == "названию"):
        sort_query = '-title'
    elif (sort_query == "жанру"):
        sort_query = '-anons'
    elif (sort_query == "дате"):
        sort_query = '-date'
    search_query = request.GET.get('search', '')
    news = Articles.objects.filter(title__icontains=search_query).order_by(sort_query)
    cartuser = CartUser.objects.filter(user=request.user.id)
    return render(request, 'news/news_home.html', {'news': news,'cartuser': cartuser})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/news-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
       form = ArticlesForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('home')
       else:
           error = 'Ошибка формы'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)

def booking(request,book_id):
    try:
        if (CartUser.objects.filter(user=request.user.id) != None):
            if (CartUser.objects.filter(user=request.user.id,books=book_id)):
                pass
            else:
                print("sadas")
                book = CartUser.objects.create(user=request.user.id,books=book_id)
                book.books = book_id
                book.save()
        else:
            book = CartUser.objects.create(user=request.user.id,books=book_id)
            book.books = book_id
            book.save()
    except:
        book = CartUser.objects.create(user=request.user.id,books=book_id)
        book.books = book_id
        book.save()
    count = Articles.objects.get(id=book_id)
    count.count -= 1
    count.save()
    news = Articles.objects.all()
    cartuser = CartUser.objects.filter(user=request.user.id)
    return render(request, 'news/news_home.html', {'news': news,'cartuser': cartuser})

def booking_delete(request,book_id):
    try:
        CartUser.objects.filter(books=book_id).delete()
    except:
        pass
    count = Articles.objects.get(id=book_id)
    count.count += 1
    count.save()
    news = Articles.objects.all()
    cartuser = CartUser.objects.filter(user=request.user.id)
    return render(request, 'news/news_home.html', {'news': news,'cartuser': cartuser})

def my_books(request):
    user_books = CartUser.objects.filter(user=request.user.id)
    books = Articles.objects.none()
    for user_book in user_books:
        new_book = Articles.objects.get(id=user_book.books)
        books |= Articles.objects.filter(id=new_book.id)

    return render(request,'news/my_books.html',{'books':books})
