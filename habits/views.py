from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habits.serializers import HabitSerializer

from .models import Habit
from .paginations import CustomPagination


class HabitViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = HabitSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Habit.objects.filter(user=self.request.user)
        return Habit.objects.none()


class PublicHabitList(ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = CustomPagination
