from django.db import models
from django.urls import reverse


class MainMenu(models.Model):
    title = models.CharField(
        'Название меню',
        max_length=50,
    )

    class Meta:
        verbose_name = 'Основное меню'
        verbose_name_plural = 'Основные меню'

    def __str__(self):
        return self.title


class SecondMenu(models.Model):
    title = models.CharField(
        'Название меню',
        max_length=50,
    )
    parent = models.ForeignKey(
        MainMenu,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Меню второго уровня'
        verbose_name_plural = 'Меню второго уровня'

    def __str__(self):
        return self.title


class LastMenu(models.Model):
    title = models.CharField(
        'Название меню',
        max_length=50,
    )
    parent = models.ForeignKey(
        SecondMenu,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Последнее меню'
        verbose_name_plural = 'Последние меню'

    def __str__(self):
        return self.title
