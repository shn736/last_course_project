from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        null=True,
        help_text="Введите номер телефона",
    )
    country = models.CharField(
        max_length=50, verbose_name="Страна", null=True, help_text="Введите свою страну"
    )
    tg_nick = models.CharField(
        max_length=50,
        verbose_name="Телеграм ник",
        null=True,
        help_text="Введите свой телеграм ник",
    )

    tg_chat_id = models.CharField(
        max_length=50,
        verbose_name="Телеграм chat-id",
        null=True,
        help_text="Введите свой телеграм chat-id",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
