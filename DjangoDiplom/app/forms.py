from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Форма для регистрации пользователя
class UserRegisterForm(UserCreationForm):
    age = forms.IntegerField(label='Введите свой возраст:', required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'age']