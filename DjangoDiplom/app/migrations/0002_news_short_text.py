# Generated by Django 4.2.16 on 2024-11-21 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='short_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]