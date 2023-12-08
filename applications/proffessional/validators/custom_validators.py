from django.core.exceptions import ValidationError
from django.utils import timezone
    

class CustomFieldValidator:
    def __call__(self, value):
        if not value.replace(" ", "").isalpha():
            raise ValidationError("Should contain alphabets only")


class CustomDateValidator:
    
    def __call__(self, date ):
        if date and date > timezone.now().date():
            raise ValidationError("Invalid date input")
