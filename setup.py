"""Python setup.py for event_segmentation_baldassano package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("event_segmentation_baldassano", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="event_segmentation_baldassano",
    version=read("event_segmentation_baldassano", "VERSION"),
    description="Awesome event_segmentation_baldassano created by rgbayrak",
    url="https://github.com/rgbayrak/event_segmentation_baldassano/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="rgbayrak",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["event_segmentation_baldassano = event_segmentation_baldassano.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
