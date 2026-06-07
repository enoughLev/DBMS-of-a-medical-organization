def format_date(date_obj):
    if date_obj is None:
        return ""
    return str(date_obj)

def validate_not_empty(value, field_name):
    if not value or not value.strip():
        raise ValueError(f"Поле '{field_name}' не может быть пустым")
    return value.strip()