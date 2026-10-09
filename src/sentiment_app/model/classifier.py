"""Scores text with a Naive Bayes sentiment model loaded from a JSON weights file."""

import json
import math
import re
from dataclasses import dataclass
from pathlib import Path


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z']+", text.lower())


@dataclass(frozen=True)
class SentimentClassifier:
    log_prior: float
    word_log_ratios: dict[str, float]

    def predict_proba(self, text: str) -> float:
        """Return the probability that ``text`` is positive."""
        score = self.log_prior + sum(self.word_log_ratios.get(word, 0.0) for word in tokenize(text))
        return 1.0 / (1.0 + math.exp(-score))


def load_classifier(weights_path: Path) -> SentimentClassifier:
    weights = json.loads(weights_path.read_text(encoding="utf-8"))
    return SentimentClassifier(
        log_prior=weights["log_prior"],
        word_log_ratios=weights["word_log_ratios"],
    )
