# Project
Sentiment-analysis app. Python backend that trains a small Naive Bayes
model on product reviews and serves predictions through an API route.
Use this project to practise context management with /context, /compact,
and /clear.

# Map
- src/sentiment_app/api/       public prediction API route and model config
- src/sentiment_app/model/     the sentiment classifier
- src/sentiment_app/auth/      client API key check
- src/sentiment_app/training/  model training and training-run tracking
- data/reviews.csv             labeled training data
- models/                      trained model weights (JSON)
- tests/                       pytest suite

# Commands
- Install: pip install -e ".[dev]"
- Train:   python -m sentiment_app.training.train
- Test:    pytest
- Lint:    ruff check . && ruff format --check .
- Types:   mypy

# Code Style
- PEP 8, 4-space indentation, type hints on every function.
- Absolute imports from the sentiment_app package.
- Never hardcode secrets or settings; read them from environment variables.
