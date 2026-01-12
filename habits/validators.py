from rest_framework.exceptions import ValidationError


def validate_pleasant_habit(attrs):
    if attrs.get("is_pleasant_habit") and (
        attrs.get("reward") or attrs.get("related_habit")
    ):
        raise ValidationError(
            "Приятные привычки не могут иметь вознаграждений или связанных с ними привычек."
        )
    if attrs.get("reward") and attrs.get("related_habit"):
        raise ValidationError(
            "Вы можете использовать только вознаграждение или связанную с ним привычку, но не то и другое вместе."
        )


def validate_periodicity(attrs):
    if attrs.get("frequency") < 1 or attrs.get("frequency") > 7:
        raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
