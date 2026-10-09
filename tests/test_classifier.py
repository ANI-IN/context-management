from sentiment_app.model.classifier import SentimentClassifier, tokenize


def test_tokenize_lowercases_and_drops_punctuation() -> None:
    assert tokenize("Great, GREAT product!") == ["great", "great", "product"]


def test_unknown_words_fall_back_to_prior() -> None:
    classifier = SentimentClassifier(log_prior=0.0, word_log_ratios={"good": 2.0})
    assert classifier.predict_proba("zebra") == 0.5
    assert classifier.predict_proba("good") > 0.5
