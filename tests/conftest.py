from __future__ import annotations

from unittest import mock

import pyotp
import pytest


@pytest.fixture()
def mocked_pyotp() -> mock.Mock:
    return mock.create_autospec(pyotp.TOTP, instance=True)
