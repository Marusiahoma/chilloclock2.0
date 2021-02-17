from django.contrib import admin
from .models import Task
from django.contrib import admin
from .models import Profile


@admin.register(Profile)  # Регистрация модели профиля на сайте админа
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth']


admin.site.register(Task)
