from django.db.models.functions import Upper
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from taggit.models import Tag
from .models import *

# Create your views here.


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


