def to_uppercase(value: str) -> str:
    if not value:
        return value

    if not type(value) == str:
        return value

    return value.upper()


def to_lowercase(value: str) -> str:
    if not value:
        return value

    if not type(value) == str:
        return value

    return value.lower()


def capitalize(value: str) -> str:
    if not value:
        return value

    if not type(value) == str:
        return value

    return value.capitalize()


def truncate(value: str, n_char: int) -> str:
    if not value:
        return value

    if not type(value) == str:
        return value

    if len(value) < n_char:
        return value

    return value[:n_char] + '...'


