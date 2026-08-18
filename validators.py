import re

def is_valid_email(email):
    """Check if the given email is valid."""
    email_regex = (r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return re.match(email_regex, email) is not None


def is_positive_integer(value):
    """Check if the value is a positive integer."""
    try:
        num = int(value)
        return num > 0
    except (ValueError, TypeError):
        return False


def is_valid_delay(delay):
    """Check if the delay value is a positive integer."""
    return is_positive_integer(delay)


def validate_configuration(config):
    """Validate the provided configuration settings."""
    errors = []
    if not is_valid_email(config.get('email')):
        errors.append('Invalid email address')
    if not is_valid_delay(config.get('delay')):
        errors.append('Delay must be a positive integer')
    if errors:
        raise ValueError('Configuration Errors: ' + ', '.join(errors))
    return True
