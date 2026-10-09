import pytest

from sentiment_app.auth.api_key import is_valid_api_key


def test_accepts_configured_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SENTIMENT_API_KEY", "s3cret")
    assert is_valid_api_key("s3cret")
    assert not is_valid_api_key("wrong")


def test_rejects_everything_when_no_key_configured(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SENTIMENT_API_KEY", raising=False)
    assert not is_valid_api_key("")
