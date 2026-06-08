
class ValidationError(Exception):
    """Исключение, вызываемое при ошибках валидации."""
    def __init__(self, value, message="Недопустимое значение"):
        self.value = value
        self.message = message
        super().__init__(f"{self.message}: {self.value}")

def set_percentage(percent):
    if percent < 0 or percent > 100:
        raise ValidationError(percent, "Процент должен быть в диапазоне от 0 до 100")
    return True

# Перехват созданной ошибки
try:
    set_percentage(150)
except ValidationError as error:
    print(f"Перехвачена ошибка! Значение: {error.value}")