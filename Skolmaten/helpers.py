from datetime import datetime


def str_to_dt(str_date: str) -> datetime:
    return datetime.strptime(str_date, "%a, %d %b %Y %H:%M:%S %Z")
