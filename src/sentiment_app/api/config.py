"""Loads model settings from environment variables, with safe defaults."""

import os
from dataclasses import dataclass
from pathlib import Path

DEFAULT_WEIGHTS_PATH = Path(__file__).resolve().parents[3] / "models" / "sentiment_weights.json"


@dataclass(frozen=True)
class ModelConfig:
    weights_path: Path
    threshold: float


def load_model_config() -> ModelConfig:
    weights_path = Path(os.environ.get("SENTIMENT_WEIGHTS_PATH", DEFAULT_WEIGHTS_PATH))
    threshold = float(os.environ.get("SENTIMENT_THRESHOLD", "0.5"))
    if not 0.0 < threshold < 1.0:
        raise ValueError(f"SENTIMENT_THRESHOLD must be between 0 and 1, got {threshold}")
    return ModelConfig(weights_path=weights_path, threshold=threshold)
