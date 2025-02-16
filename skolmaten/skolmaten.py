from dataclasses import dataclass
from datetime import datetime

import httpx


class SkolmatenHttpError(Exception): ...


SKOLMATEN_BASE_URL = "https://skolmaten.se/api/4"


@dataclass
class Food:
    verbose_week: str
    food: str
    datetime: datetime


@dataclass
class SkolmatenAPI:
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://skolmaten.se/",
    }

    def get(self, endpoint: str) -> dict:
        try:
            response = httpx.get(
                f"{SKOLMATEN_BASE_URL}/{endpoint}", headers=self.headers
            )
            response.raise_for_status()
        except Exception as E:
            raise SkolmatenHttpError(E)
        return response.json()


@dataclass
class SchoolFood:
    school: str
    api = SkolmatenAPI()

    def at(self, year: int, week: int) -> dict:
        return self.api.get(f"menu/{self.school}?year={year}&week={week}")
