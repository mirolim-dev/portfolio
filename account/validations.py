from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
import re


def validate_phone(phone:str):
    pattern = re.compile(r'^\+?[1-9]\d{1,14}$')
    print("Phone validation is working")
    if not pattern.fullmatch(phone):
        raise ValidationError(_("Enter a valid phone number. The number must start with a country code and contain 1 to 14 digits."))
    
# invalid_phones = ["123", "abc1234567", "+12345", "+12345678901234567890"]

# count = 0
# for phone in invalid_phones:
#     if validate_phone(phone):
#         print(f"{phone} is valid")
