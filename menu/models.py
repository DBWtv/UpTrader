from django.db import models
from django.urls import reverse


class MainMenu(models.Model):
    title = models.CharField(
        'Название меню',
        max_length=50,
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Основное меню'
        verbose_name_plural = 'Основные меню'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "main_menu_url",
            kwargs={"url": f'{self.slug}'},
        )


class SecondMenu(models.Model):
    title = models.CharField(
        'Название меню',
        max_length=50,
    )
    parent = models.ForeignKey(
        MainMenu,
        on_delete=models.CASCADE,
        related_name='second_menu',
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Меню второго уровня'
        verbose_name_plural = 'Меню второго уровня'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "second_menu_url",
            kwargs={"url": f'{self.slug}'},
        )


class LastMenu(models.Model):
    title = models.CharField(
        'Название меню',
        max_length=50,
    )
    parent = models.ForeignKey(
        SecondMenu,
        on_delete=models.CASCADE,
        related_name='last_menu',
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Последнее меню'
        verbose_name_plural = 'Последние меню'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "last_menu_url",
            kwargs={"url": f'{self.slug}'},
        )
