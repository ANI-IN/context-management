"""Trains the Naive Bayes sentiment model from a labeled CSV and saves its weights.

Run from the project root:

    python -m sentiment_app.training.train
"""

import csv
import json
import math
from collections import Counter
from pathlib import Path

from sentiment_app.api.config import DEFAULT_WEIGHTS_PATH
from sentiment_app.model.classifier import tokenize

DEFAULT_DATA_PATH = Path(__file__).resolve().parents[3] / "data" / "reviews.csv"


def train(rows: list[tuple[str, str]]) -> dict[str, object]:
    """Fit word log-likelihood ratios with Laplace smoothing.

    Each row is ``(text, label)`` where label is "positive" or "negative".
    """
    word_counts: dict[str, Counter[str]] = {"positive": Counter(), "negative": Counter()}
    doc_counts = Counter(label for _, label in rows)
    for text, label in rows:
        word_counts[label].update(tokenize(text))

    vocabulary = set(word_counts["positive"]) | set(word_counts["negative"])
    pos_total = sum(word_counts["positive"].values()) + len(vocabulary)
    neg_total = sum(word_counts["negative"].values()) + len(vocabulary)
    word_log_ratios = {
        word: math.log((word_counts["positive"][word] + 1) / pos_total)
        - math.log((word_counts["negative"][word] + 1) / neg_total)
        for word in sorted(vocabulary)
    }
    log_prior = math.log(doc_counts["positive"] / doc_counts["negative"])
    return {"log_prior": log_prior, "word_log_ratios": word_log_ratios}


def load_rows(data_path: Path) -> list[tuple[str, str]]:
    with data_path.open(newline="", encoding="utf-8") as handle:
        return [(row["text"], row["label"]) for row in csv.DictReader(handle)]


def main() -> None:
    rows = load_rows(DEFAULT_DATA_PATH)
    weights = train(rows)
    DEFAULT_WEIGHTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    DEFAULT_WEIGHTS_PATH.write_text(json.dumps(weights, indent=2) + "\n", encoding="utf-8")
    print(f"Trained on {len(rows)} reviews. Saved weights to {DEFAULT_WEIGHTS_PATH}")


if __name__ == "__main__":
    main()
