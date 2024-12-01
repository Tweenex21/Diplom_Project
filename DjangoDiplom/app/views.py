from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from taggit.models import Tag
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import *

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            age = form.cleaned_data.get('age')

            # Проверка на существование пользователя
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Пользователь с таким именем уже существует.')
                return render(request, 'registration_page.html', {'form': form})

            # Проверка возраста
            if age < 18:
                form.add_error('age', 'Вы должны быть старше 18 лет.')
                return render(request, 'registration_page.html', {'form': form})

            # Сохранение пользователя и профиля
            user = form.save()
            profile = Profile.objects.create(user=user, age=age)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'registration_page.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def index(request):
    news = News.objects.all()
    paginator = Paginator(news, 4)  # Показывать 4 новостей на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)


def news(request, id):
    news = News.objects.get(id=id)
    context = {
        'news': news
    }
    return render(request, 'news.html', context)


def tags(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    newsQuerySet = News.objects.filter(tags__in=[tag])
    paginator = Paginator(newsQuerySet, 4)  # Показывать 4 новостей на странице
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    context = {
        'tag': tag,
        'news': news
    }
    return render(request, 'tags.html', context)


def search(request):
    q = request.GET.get('q')
    newsQuerySet = News.objects.filter(text__icontains=q)
    paginator = Paginator(newsQuerySet, 4)  # Показывать 4 новостей на странице
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    context = {
        'news': news,
        'q': q,
    }
    return render(request, 'search.html', context)


def contact(request):
    context = {
        'phone': 'phone',
        'email': 'email',
    }
    return render(request, 'contact.html', context)


