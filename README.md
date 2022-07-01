### This project will implement

- 📦 A basic [setup.py](setup.py) file to provide installation, packaging and distribution for your project.  
  Template uses setuptools because it's the de-facto standard for Python packages, you can run `make switch-to-poetry` later if you want.
- 🤖 A [Makefile](Makefile) with the most useful commands to install, test, lint, format and release your project.
- 📃 Documentation structure using [mkdocs](http://www.mkdocs.org)
- 💬 Auto generation of change log using **gitchangelog** to keep a HISTORY.md file automatically based on your commit history on every release.
- 🐋 A simple [Containerfile](Containerfile) to build a container image for your project.  
  `Containerfile` is a more open standard for building container images than Dockerfile, you can use buildah or docker with this file.
- 🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/)
- ✅ Code linting using [flake8](https://flake8.pycqa.org/en/latest/)
- 📊 Code coverage reports using [codecov](https://about.codecov.io/sign-up/)
- 🛳️ Automatic release to [PyPI](https://pypi.org) using [twine](https://twine.readthedocs.io/en/latest/) and github actions.
- 🎯 Entry points to execute your program using `python -m <event_segmentation_baldassano>` or `$ event_segmentation_baldassano` with basic CLI argument parsing.
- 🔄 Continuous integration using [Github Actions](.github/workflows/) with jobs to lint, test and release your project on Linux, Mac and Windows environments.


---
### Event Segmentation
It is a reproducibility study for ["Anticipation of temporally structured events in the brain."](https://elifesciences.org/articles/64972)


[![codecov](https://codecov.io/gh/rgbayrak/event_segmentation_baldassano/branch/main/graph/badge.svg?token=event_segmentation_baldassano_token_here)](https://codecov.io/gh/rgbayrak/event_segmentation_baldassano)
[![CI](https://github.com/rgbayrak/event_segmentation_baldassano/actions/workflows/main.yml/badge.svg)](https://github.com/rgbayrak/event_segmentation_baldassano/actions/workflows/main.yml)


## Install it from PyPI

```bash
pip install event_segmentation_baldassano
```

## Usage

```py
from event_segmentation_baldassano import BaseClass
from event_segmentation_baldassano import base_function

BaseClass().base_method()
base_function()
```

```bash
$ python -m event_segmentation_baldassano
#or
$ event_segmentation_baldassano
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
