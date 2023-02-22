from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    title = models.CharField(
        'Название меню',
        max_length=50,
    )
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
        )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "url",
            kwargs={"url": f'{self.slug}'},
        )
