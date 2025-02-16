# Skolmaten

[![PyPI version](https://img.shields.io/pypi/v/skolmaten?style=for-the-badge)](https://pypi.org/project/skolmaten/) [![License](https://img.shields.io/badge/license-WTFPL-green?style=for-the-badge)](https://github.com/dunderrrrrr/skolmaten/blob/main/LICENSE) [![Python versions](https://img.shields.io/pypi/pyversions/skolmaten?style=for-the-badge)](https://pypi.org/project/skolmaten/)


The `skolmaten` python package provides a convenient way to fetch school food menu information for Swedish schools connected to [skolmaten.se](https://skolmaten.se/).


## Installation
```
pip install skolmaten
```
[View Skolmaten at pypi](https://pypi.org/project/Skolmaten/)

## Usage

Provide `year` and `week` as parameters to `at`.

```py
>>> from skolmaten import SchoolFood
>>> food = SchoolFood(school="0b4d4d77-7b27-4591-a03e-28309e039b1e")
>>> food.at(2025, 10) # returns skolmaten json data
```

You school `id` can be found in the URL of the school's page on skolmaten.se. For example, the school with id `0b4d4d77-7b27-4591-a03e-28309e039b1e` has the URL `https://skolmaten.se/menu/fbcb1b38-978c-42b9-a1ef-71798654e1d9?school=0b4d4d77-7b27-4591-a03e-28309e039b1e`.

# License
This package is not in any way related to the makers of skolmaten.se and is licensed under the `WTFPL` license.
