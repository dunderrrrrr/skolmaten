# read the contents of your README file
from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="Skolmaten",
    version="0.0.6",
    author="dunderrrrrr",
    url="https://github.com/dunderrrrrr/skolmaten/",
    description="Fetch food menu information from skolmaten.se",
    packages=["Skolmaten"],
    install_requires=[
        "feedparser==6.0.10",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
