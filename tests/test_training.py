import json
from pathlib import Path

from sentiment_app.api.config import DEFAULT_WEIGHTS_PATH
from sentiment_app.training.run_log import end_run, start_run
from sentiment_app.training.train import DEFAULT_DATA_PATH, load_rows, train


def test_train_learns_word_direction() -> None:
    rows = [("good great", "positive"), ("bad awful", "negative")]
    weights = train(rows)
    ratios = weights["word_log_ratios"]
    assert isinstance(ratios, dict)
    assert ratios["good"] > 0 > ratios["bad"]


def test_committed_weights_match_training_data() -> None:
    saved = json.loads(Path(DEFAULT_WEIGHTS_PATH).read_text(encoding="utf-8"))
    assert saved == train(load_rows(DEFAULT_DATA_PATH))


def test_start_and_end_run() -> None:
    run = start_run("baseline")
    assert run.experiment == "baseline"
    assert end_run(run.id)
    assert not end_run(run.id)
