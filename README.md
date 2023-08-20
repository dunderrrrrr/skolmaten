# Skolmaten

The `skolmaten` python package provides a convenient way to fetch school food menu information for Swedish schools connected to [skolmaten.se](https://skolmaten.se/).


## Installation
```
pip install skolmaten
```
[View Skolmaten at pypi](https://pypi.org/project/Skolmaten/)

## Usage

If you want food menu information for `https://skolmaten.se/atlas-skolan/`, use `SchoolFood` like this.

```py
>>> from Skolmaten import SchoolFood
>>> food = SchoolFood(school="atlas-skolan")
```

### get_weeks(weeks)
`get_weeks` will output current week including number of weeks provided.
```py
food.get_weeks(2)
```

### get_days(limit, offset)
`limit` sets the number of total results
`offset` can be adjusted to fetch days back in time

```py
food.get_days(3) # today and 3 days ahead of time
food.get_days(3, 1) # yesterday, today and tomorrow
```

## Example

```py
>>> pip install skolmaten
>>> ...
>>> from Skolmaten import SchoolFood
>>> school_food = SchoolFood(school="vilbergsskolan")
>>> for food in school_food.get_weeks(2): food.verbose_week, food.food, food.datetime
...
('Måndag - Vecka 33', 'Sommarlov', datetime.datetime(2023, 8, 14, 0, 0))
('Tisdag - Vecka 33', 'Sommarlov', datetime.datetime(2023, 8, 15, 0, 0))
('Onsdag - Vecka 33', 'Panerad fisk serveras med kall sås och potatis', datetime.datetime(2023, 8, 16, 0, 0))
('Torsdag - Vecka 33', 'Korvstroganoff serveras med ris', datetime.datetime(2023, 8, 17, 0, 0))
('Fredag - Vecka 33', 'Köttbullar serveras med pasta', datetime.datetime(2023, 8, 18, 0, 0))
('Måndag - Vecka 34', 'Carbonara serveras med pasta', datetime.datetime(2023, 8, 21, 0, 0))
('Tisdag - Vecka 34', 'Fiskgratäng med tacosmak serveras med kokt potatis', datetime.datetime(2023, 8, 22, 0, 0))
('Onsdag - Vecka 34', 'Chili con carne serveras med bulgur', datetime.datetime(2023, 8, 23, 0, 0))
('Torsdag - Vecka 34', 'Broccolisoppa serveras med mjuk smörgås och pålägg', datetime.datetime(2023, 8, 24, 0, 0))
('Fredag - Vecka 34', 'Pastagratäng med mozzarella och spenat', datetime.datetime(2023, 8, 25, 0, 0))
```

# License
This package is not in any way related to the makers of skolmaten.se and is licensed under the `WTFPL` license.
