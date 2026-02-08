import re

def normalize_phone(phone_number):
    phone = phone_number.strip()

    phone = re.sub(r"[^\d+]", "", phone)

    if phone.startswith("+380"):
        return phone
    elif phone.startswith("380"):
        return "+" + phone
    elif phone.startswith("0"):
        return "+38" + phone
    else:
        return "+38" + phone
