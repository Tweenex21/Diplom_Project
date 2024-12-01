from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100)
    short_text = models.TextField()
    text = models.TextField()
    image = models.ImageField(default="", upload_to='static/image')
    author = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username