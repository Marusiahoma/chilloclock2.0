from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=60)
    task = models.TextField('Описание')
    img = models.ImageField("Картинка", upload_to='article')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"