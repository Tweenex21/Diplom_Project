from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    short_text = models.TextField()
    image = models.CharField(max_length=170)
    author = models.CharField(max_length=40)
    date = models.DateTimeField()

    def __str__(self):
        return self.title


