import re

def validate_click_interval(interval):
    """Validates the click interval. Must be a positive float."""
    if not isinstance(interval, (int, float)) or interval <= 0:
        raise ValueError('Click interval must be a positive number.')
    return True


def validate_position(position):
    """Validates mouse position. Must be a tuple of two integers."""
    if not (isinstance(position, tuple) and len(position) == 2 and
            all(isinstance(coord, int) for coord in position)):
        raise ValueError('Position must be a tuple of two integers.')
    return True


def validate_click_count(count):
    """Validates the number of clicks. Must be a positive integer."""
    if not isinstance(count, int) or count <= 0:
        raise ValueError('Click count must be a positive integer.')
    return True

