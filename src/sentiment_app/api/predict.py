"""Public API route for sentiment predictions. Validates the input text before scoring."""

from dataclasses import dataclass
from typing import Any

from sentiment_app.api.config import load_model_config
from sentiment_app.model.classifier import load_classifier

MAX_TEXT_LENGTH = 1000


@dataclass(frozen=True)
class PredictResponse:
    status: int
    body: dict[str, Any]


def handle_predict(text: str) -> PredictResponse:
    if not text.strip():
        return PredictResponse(status=400, body={"error": "Text must not be empty"})
    if len(text) > MAX_TEXT_LENGTH:
        return PredictResponse(status=400, body={"error": "Text is too long"})
    config = load_model_config()
    classifier = load_classifier(config.weights_path)
    probability = classifier.predict_proba(text)
    label = "positive" if probability >= config.threshold else "negative"
    return PredictResponse(status=200, body={"label": label, "probability": round(probability, 3)})
