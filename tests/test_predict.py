import pytest

from sentiment_app.api.predict import MAX_TEXT_LENGTH, handle_predict


@pytest.mark.parametrize("text", ["", "   ", "x" * (MAX_TEXT_LENGTH + 1)])
def test_rejects_invalid_text(text: str) -> None:
    assert handle_predict(text).status == 400


def test_predicts_positive_review() -> None:
    response = handle_predict("Excellent quality, I love it")
    assert response.status == 200
    assert response.body["label"] == "positive"
    assert response.body["probability"] > 0.5


def test_predicts_negative_review() -> None:
    response = handle_predict("Terrible, it broke and I want a refund")
    assert response.status == 200
    assert response.body["label"] == "negative"


def test_threshold_comes_from_config(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SENTIMENT_THRESHOLD", "0.999")
    assert handle_predict("Good product").body["label"] == "negative"
