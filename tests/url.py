import respx
from httpx import Response
from skolmaten import SchoolFood


@respx.mock
def test_url():
    expected_url = "a8f4b254-6357-4859-a81d-a717a2471274?year=2025&week=10"

    respx.get(f"https://skolmaten.se/api/4/menu/{expected_url}").mock(
        return_value=Response(status_code=200, json={"status": "ok"})
    )

    food = SchoolFood(school="a8f4b254-6357-4859-a81d-a717a2471274")

    assert food.at(2025, 10) == {"status": "ok"}
