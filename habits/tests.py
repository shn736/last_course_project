from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@sky.pro")
        self.habit = Habit.objects.create(action="Спорт", time="18:00:00", place="Дом",user=self.user, frequency=5)
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("action"), self.habit.action
        )

    def test_habit_create(self):
        url = reverse("habits:habits-list")
        data = {
            "action": "Спорт",
            "time": "19:00:00",
            "place": "Дом",
            "user": self.user.pk,
            "frequency": 4
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
