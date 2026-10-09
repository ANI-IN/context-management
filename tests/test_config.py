from pathlib import Path

import pytest

from sentiment_app.api.config import DEFAULT_WEIGHTS_PATH, load_model_config


def test_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SENTIMENT_WEIGHTS_PATH", raising=False)
    monkeypatch.delenv("SENTIMENT_THRESHOLD", raising=False)
    config = load_model_config()
    assert config.weights_path == DEFAULT_WEIGHTS_PATH
    assert config.threshold == 0.5


def test_reads_environment(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("SENTIMENT_WEIGHTS_PATH", str(tmp_path / "w.json"))
    monkeypatch.setenv("SENTIMENT_THRESHOLD", "0.7")
    config = load_model_config()
    assert config.weights_path == tmp_path / "w.json"
    assert config.threshold == 0.7


@pytest.mark.parametrize("value", ["0", "1", "1.5"])
def test_rejects_out_of_range_threshold(monkeypatch: pytest.MonkeyPatch, value: str) -> None:
    monkeypatch.setenv("SENTIMENT_THRESHOLD", value)
    with pytest.raises(ValueError):
        load_model_config()
