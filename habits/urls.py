from django.urls import path
from rest_framework.routers import SimpleRouter

from .apps import HabitsConfig
from .views import HabitViewSet, PublicHabitList

app_name = HabitsConfig.name


router = SimpleRouter()
router.register("", HabitViewSet, "habits")

urlpatterns = [
    path("public-habits/", PublicHabitList.as_view(), name="public_habits"),
]

urlpatterns += router.urls
