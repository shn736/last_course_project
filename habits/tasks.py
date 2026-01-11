from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_telegram_message
from users.models import User


# Задача для напоминания о привычке
@shared_task
def remind_habit(habit_id):
    habit = Habit.objects.get(id=habit_id)
    user = User.objects.get(id=habit.user.id)  # Получаем пользователя
    message = f"Не забудьте выполнить привычку: {habit.action} в {habit.time.strftime('%H:%M')} в {habit.place}."
    send_telegram_message(user.tg_chat_id, message)


# Задача для планирования напоминаний
@shared_task
def schedule_reminders():
    current_time = timezone.now()
    habits = Habit.objects.all()

    for habit in habits:
        reminder_time = timezone.now().combine(
            current_time.date(), habit.time
        ) - timedelta(hours=1)

        # Планировать только, если время еще не прошло
        if reminder_time > current_time:
            remind_habit.apply_async(args=[habit.id], eta=reminder_time)
