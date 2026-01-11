from rest_framework import serializers

from .models import Habit
from .validators import validate_periodicity, validate_pleasant_habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, attrs):
        validate_pleasant_habit(attrs)
        validate_periodicity(attrs)
        return attrs
