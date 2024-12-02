from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.


# Регистрация модели News в административной панели
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'main_text', 'shortened_text', 'display_image', 'author', 'date')

    # Метод для отображения первых 30 символов текста новости
    def main_text(self, obj):
        return obj.text if len(obj.text) <= 30 else obj.text[:30] + '...'

    main_text.short_description = 'Text'

    # Метод для отображения первых 30 символов краткого текста новости
    def shortened_text(self, obj):
        return obj.short_text if len(obj.short_text) <= 30 else obj.short_text[:30] + '...'

    shortened_text.short_description = 'Text'

    # Метод для отображения изображения новости
    def display_image(self, obj):
        html = '<img width="100" src="{img}">'
        if obj.image:
            return format_html(html, img=obj.image.url)
        return format_html('<strong>Изображения нет<strong>')


admin.site.register(News, NewsAdmin)
