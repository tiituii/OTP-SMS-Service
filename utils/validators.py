import re
def validate_phone_number(phone: str) -> bool:
    # Very simple E.164 validation example (adjust as needed)
    pattern = r'^\+855\d{8,9}$' #fixed for cambodia mobile code
    return bool(re.match(pattern, phone))
