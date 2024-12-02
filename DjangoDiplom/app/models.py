from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


# Create your models here.

# Модель для новостей
class News(models.Model):
    title = models.CharField(max_length=100) # Заголовок новости
    short_text = models.TextField() # Краткое описание новости
    text = models.TextField() # Полный текст новости
    image = models.ImageField(default="", upload_to='static/image') # Изображение новости
    author = models.CharField(max_length=40) # Автор новости
    date = models.DateTimeField(auto_now_add=True) # Дата создания новости
    tags = TaggableManager(blank=True) # Теги новости

    def __str__(self):
        return self.title  # Возвращает заголовок новости как строковое представление объекта

# Модель для профиля пользователя
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Связь с моделью User
    age = models.PositiveIntegerField() # Возраст пользователя

    def __str__(self):
        return self.user.username  # Возвращает имя пользователя как строковое представление объекта