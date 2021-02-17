from django.db import models
from django.conf import settings


class Task(models.Model):
    title = models.CharField('Название', max_length=60)
    task = models.TextField('Описание')
    img = models.ImageField("Картинка", upload_to='article')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"


class Profile(models.Model):  # Модель профиля
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, verbose_name='Пользователь')
    date_of_birth = models.DateField(verbose_name='Дата рождения', blank=True, null=True)

    def __str__(self):
        return 'Профиль для пользователя {}'.format(self.user.username)

    class Meta:
        verbose_name = 'Дата рождения'
        verbose_name_plural = 'Даты рождения'
