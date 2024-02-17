from django.db import models
from project01.settings import GROUPS

class Contact(models.Model):
    name = models.CharField(
        'Имя',
        max_length=30
    )
    second_name = models.CharField(
        'Фамилия',
        max_length=30
    )
    email = models.CharField(
        'Почта',
        max_length=30
    )
    phone = models.CharField(
        'Телефон',
        max_length=30
    )
    text = models.TextField(
        'Текст'
    )

    date = models.DateTimeField(
        'Время отправки',
        auto_now_add=True,
        db_index=True
    )
    def __str__(self):
        return self.name[:50]

    class Meta:
        app_label = 'main'
        ordering = ('-date',)
        verbose_name = 'Письмо от пользователя'
        verbose_name_plural = 'Письма от пользователей'

class Dish(models.Model):
    name = models.CharField(
        'Название',
        max_length=20
    )
    price = models.CharField(
        'Цена',
        max_length=10
    )
    pub_date = models.DateTimeField(
        'Время публикации',
        auto_now_add=True,
        db_index=True
    )
    group = models.CharField(
        choices = GROUPS,
        verbose_name='Тип',
        max_length=20
    )
    image = models.ImageField(
        'Картинка',
        upload_to='img/',
        blank=True
    )
    q = models.CharField(
        'Количество',
        max_length=20
    )
    is_published = models.BooleanField(
        'Публикация',
        default=True
    )
    is_published_main = models.BooleanField(
        'На главной странице',
        default=False
    )

    def __str__(self):
        return self.name[:50]
    class Meta:
        app_label = 'main'
        ordering = ('group',)
        verbose_name = 'Позиция'
        verbose_name_plural = 'Ассортимент'