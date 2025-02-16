# Skolmaten

[![PyPI version](https://img.shields.io/pypi/v/skolmaten?style=for-the-badge)](https://pypi.org/project/skolmaten/) [![License](https://img.shields.io/badge/license-WTFPL-green?style=for-the-badge)](https://github.com/dunderrrrrr/skolmaten/blob/main/LICENSE) [![Python versions](https://img.shields.io/pypi/pyversions/skolmaten?style=for-the-badge)](https://pypi.org/project/skolmaten/)


The `skolmaten` python package provides a convenient way to fetch school food menu information for Swedish schools connected to [skolmaten.se](https://skolmaten.se/).


## Installation
```
pip install skolmaten
```
[View Skolmaten at pypi](https://pypi.org/project/Skolmaten/)

## Usage

If you want food menu information for `https://skolmaten.se/atlas-skolan/`, use `SchoolFood` like this.

Provide `year` and `week` as parameters to `at`.

```py
>>> from Skolmaten import SchoolFood
>>> food = SchoolFood(school="atlas-skolan")
>>> food.at(2025, 10) # returns skolmaten json data
```


# License
This package is not in any way related to the makers of skolmaten.se and is licensed under the `WTFPL` license.
