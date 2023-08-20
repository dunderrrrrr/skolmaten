from dataclasses import dataclass
from datetime import datetime

import feedparser

from .constants import SKOLMATEN_BASE_URL
from .helpers import str_to_dt


class SkolmatenHttpError(Exception):
    ...


@dataclass
class Food:
    verbose_week: str
    food: str
    datetime: datetime


@dataclass
class SkolmatenAPI:
    def get(self, endpoint: str):
        result = feedparser.parse(f"{SKOLMATEN_BASE_URL}/{endpoint}")
        if result.status != 200:
            raise SkolmatenHttpError(result.status, result)
        return result.entries


@dataclass
class SchoolFood:
    school: str
    api = SkolmatenAPI()

    def get_weeks(self, limit: int) -> list[Food]:
        result = self.api.get(f"{self.school}/rss/weeks/?limit={limit}")
        return [Food(r.title, r.summary, str_to_dt(r.id)) for r in result]

    def get_days(self, limit: int, offset: int = None) -> list[Food]:
        params = (
            f"?offset=-{offset}&limit={limit}"
            if offset is not None
            else f"?limit={limit}"
        )
        result = self.api.get(f"{self.school}/rss/days/{params}")
        return [Food(r.title, r.summary, str_to_dt(r.id)) for r in result]
