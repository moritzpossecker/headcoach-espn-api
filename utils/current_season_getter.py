from datetime import datetime


def get_current_season() -> int:
    date = datetime.now()
    current_year = date.year

    if date.month < 8:
        return current_year - 1

    return current_year
