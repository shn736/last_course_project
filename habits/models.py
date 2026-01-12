from django.db import models

from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    time = models.TimeField()
    place = models.CharField(max_length=255)
    reward = models.CharField(max_length=255, blank=True, null=True)
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, blank=True, null=True
    )
    frequency = models.PositiveIntegerField(default=7)
    duration = models.PositiveIntegerField(default=120)
    is_public = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return self.action
