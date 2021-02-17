from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})


def shop(request):
    return render(request, 'main/shop.html')


def Log_in(request):
    return render(request, 'main/Log in.html')


def reg(request):
    return render(request, 'main/reg.html')


def account(request):
    return render(request, 'main/account.html')


def change(request):
    return render(request, 'main/change.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'error'

    form = TaskForm()
    context = {
        'form' : form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Форма с данными
        if form.is_valid():  # Проверка валидности формы
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])  # Поиск в базе данных по пользователю
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Успешная авторизация')
                else:
                    return HttpResponse('Нет такого аккаунта')  # Disabled account
            else:
                return HttpResponse('Недействительный логин')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():  # Проверка валидности
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно обновлен')
        else:
            messages.error(request, 'Ошибка в обновление профиля')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'main/edit.html',
                  {'user_form': user_form, 'profile_form': profile_form})


def dashboard(request):
    return render(request, 'main/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создаем нового пользователя, но пока не сохраняем в базу данных.
            new_user = user_form.save(commit=False)
            # Задаем пользователю зашифрованный пароль.
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохраняем пользователя в базе данных
            new_user.save()
            Profile.objects.create(user=new_user)
            new_user.save()
            return render(request, 'main/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/register.html', {'user_form': user_form})