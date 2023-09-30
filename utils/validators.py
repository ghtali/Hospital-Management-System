from datetime import datetime


def validate_email(email: str) -> bool:
    """Validate that an email is properly formatted."""
    # This is a basic implementation, a more robust one would be more complex
    if "@" in email and "." in email:
        return True
    return False


def validate_date_string(date_string: str, date_format: str = "%Y-%m-%d") -> bool:
    """Validate that a date string is properly formatted."""
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False
