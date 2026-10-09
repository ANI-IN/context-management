# Exercise 2: Fill the Context with Real Work

## Goal
Do enough real work to grow the context noticeably, then watch the usage climb. This shows that every file Claude reads has a cost.

## Steps
1. Ask Claude to read the source files and trace the prediction flow. Send this prompt exactly:

```
Read the files in src/ and explain how a sentiment prediction request flows
from the API route through to the model.
```

2. Let Claude open the files under `src/sentiment_app/api/`, `src/sentiment_app/model/`, `src/sentiment_app/auth/`, and `src/sentiment_app/training/` and describe the path.

3. Check the context again:

```
/context
```

## What to observe
Usage has climbed compared to your Exercise 1 baseline, and the conversation and file reads now take a visible slice of the window. This is normal. It is the cost of the exploration you asked for. Every file Claude opened is now sitting in your context.

## What to look for in the code
A good explanation from Claude should trace this path:

- `api/predict.py` receives the text, rejects it if it is empty or longer than `MAX_TEXT_LENGTH`, then loads the config and the classifier.
- `api/config.py` reads the weights path and the decision threshold from environment variables instead of hardcoding them.
- `model/classifier.py` loads the Naive Bayes weights from `models/sentiment_weights.json`, splits the text into words, and turns the summed word scores into a probability.
- `predict.py` compares that probability with the threshold and returns `positive` or `negative`.
- `training/train.py` is where the weights came from. It learns them from `data/reviews.csv`.
- `auth/api_key.py` and `training/run_log.py` are not on the prediction path. Claude should say so.

The code is intentionally small so it is easy to read. Explore it, but do not change it for these exercises.

## Outcome
You have seen for yourself that reading files consumes context, and you can measure the increase with `/context`. This sets up the next exercise, where you free the space back up.
