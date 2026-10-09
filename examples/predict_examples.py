"""Send a few reviews through the prediction route and print the results.

Run from the project root after installing the package:

    python examples/predict_examples.py
"""

from sentiment_app.api.predict import handle_predict

REVIEWS = [
    "Excellent quality, I love it",
    "Terrible, it broke and I want a refund",
    "",
]


def main() -> None:
    for review in REVIEWS:
        response = handle_predict(review)
        print(f"{review!r:45} -> {response.status} {response.body}")


if __name__ == "__main__":
    main()
