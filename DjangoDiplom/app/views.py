from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'index.html', context)


def news(request, id):
    news = News.objects.get(id=id)
    context = {
        'news': news
    }
    return render(request, 'news.html', context)