from __future__ import annotations

import screenpy_pyotp


def test_screenpy_pyotp() -> None:
    expected = ("AuthenticateWith2FA",)

    assert sorted(screenpy_pyotp.__all__) == sorted(expected)


def test_abilities() -> None:
    expected = ("AuthenticateWith2FA",)
    assert sorted(screenpy_pyotp.abilities.__all__) == sorted(expected)
