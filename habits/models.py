from django.db import models

from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Пользователь создатель привычки
    action = models.CharField(max_length=255)  # Действие
    time = models.TimeField()  # Время выполнения
    place = models.CharField(max_length=255)  # Место выполнения
    reward = models.CharField(max_length=255, blank=True, null=True)  # Вознаграждение
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, blank=True, null=True
    )  # Связанная привычка
    frequency = models.PositiveIntegerField(
        default=7
    )  # Периодичность (по умолчанию 7 дней)
    duration = models.PositiveIntegerField(
        default=120
    )  # Время на выполнение (в секундах)
    is_public = models.BooleanField(default=False)  # Признак публичности

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return self.action
