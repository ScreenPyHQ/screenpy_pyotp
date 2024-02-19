ScreenPy PyOTP
==============

[![Build Status](../../actions/workflows/tests.yml/badge.svg)](../../actions/workflows/tests.yml)
[![Build Status](../../actions/workflows/lint.yml/badge.svg)](../../actions/workflows/lint.yml)

[![Supported Versions](https://img.shields.io/pypi/pyversions/screenpy_pyotp.svg)](https://pypi.org/project/screenpy_pyotp)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

```
TITLE CARD:
                                "ScreenPy PyOTP"
TITLE DISAPPEARS.
                                                                      FADE IN:
EXT. DOCUMENTATION - MIDNIGHT

AUDIENCE continues walking, guided by the mysterious voice of the NARRATOR.
AUDIENCE winds through a garden of large hedges, twisting past brambles,
until they arrive at a single large, glowing lock upon a pedestal.


                              NARRATOR (V.O.)
            ... and you have arrived at ScreenPy PyOTP, an
            extension which enables using One Time Passwords.

                              AUDIENCE
            Wait, how long has it been since I met you? How is this
            pedestal glowing like that? And what, there's only one
            tchotchke this time?

                              NARRATOR (V.O.)
            Extensions do not need to be all that large to enable
            great things. This library provides only the Ability
            an Actor needs for two-factor authentication.

                              AUDIENCE
            You always seem to ignore the questions I most want the
            answers to.

                              NARRATOR (V.O.)
            Continuing along, to your left...

                                                                      FADE OUT
```


Installation
------------
    pip install screenpy_pyotp

or

    pip install screenpy[pyotp]


Documentation
-------------
Please check out the [Read The Docs documentation](https://screenpy-pyotp-docs.readthedocs.io/en/latest/) for the latest information about this module!

You can also read the [ScreenPy Docs](https://screenpy-docs.readthedocs.io/en/latest/) for more information about ScreenPy in general.


Contributing
------------
You want to contribute? Great! Here are the things you should do before submitting your PR:

1. Fork the repo and git clone your fork.
1. `dev` install the project package:
    1. `pip install -e .[dev]`
    1. Optional (poetry users):
        1. `poetry install --extras dev`
1. Run `pre-commit install` once.
1. Run `tox` to perform tests frequently.
1. Create pull-request from your branch.

That's it! :)
