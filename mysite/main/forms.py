from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task', 'img']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'введите текст'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'введите '
            })
        }


class LoginForm(forms.Form):  # Аутентификация пользователей через базу данных
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):  # Регистрация
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class UserEditForm(forms.ModelForm):  # Редактирование имени, фамилии и мейла
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):  # Редактирование даты рождения
    class Meta:
        model = Profile
        fields = ('date_of_birth',)