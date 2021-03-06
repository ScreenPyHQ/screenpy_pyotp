from unittest import mock

from screenpy_pyotp.abilities import AuthenticateWith2FA


class TestAuthenticateWith2FA:
    def test_can_be_instantiated(self):
        a1 = AuthenticateWith2FA.using_secret("")
        a2 = AuthenticateWith2FA.using(None)

        assert isinstance(a1, AuthenticateWith2FA)
        assert isinstance(a2, AuthenticateWith2FA)

    @mock.patch("screenpy_pyotp.abilities.authenticate_with_2fa.pyotp")
    def test_using_secret(self, mocked_pyotp):
        secret = "the macguffin"
        AuthenticateWith2FA.using_secret(secret)

        mocked_pyotp.TOTP.assert_called_once_with(secret)
