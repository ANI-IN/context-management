# Claude Code Demo: Managing Context

A hands-on Claude Code exercise for new AI/ML engineers. You get a small Python sentiment-analysis app to explore. While you work in it, you practice keeping Claude's working memory lean with the `/context`, `/compact`, and `/clear` commands.

The demo takes about ten minutes. You fill up the context window while working in the codebase, check what is using the space, and practice the three commands that control it.

## Project Overview

This repository pairs a short lesson on context management with a small, working ML project. The app trains a Naive Bayes classifier on a handful of product reviews and serves predictions through a simple API route. It is written in plain Python with no runtime dependencies.

The code is deliberately small. It only needs to be interesting enough to read. Reading it fills the context window, which gives you something real to manage.

In this demo you will:

- Check how much context you are using and what is taking up space.
- Do some work to fill the context, then summarize it to keep going.
- Clear the context completely before starting an unrelated task.
- Persist a durable fact so it survives across sessions.

## Important Note on Intentional Simplifications

The sample code is intentionally simplified. That is by design.

- Do not fix, refactor, or improve the sample code as part of these exercises. Treat it as read-only material to explore.
- Some comments mark things as deliberate. For example, `src/sentiment_app/training/run_log.py` says that saving runs to disk is not implemented yet. Leave those comments exactly as written. They are part of the lesson, and quietly fixing them would defeat the point of the demo.
- The value of the demo is in practicing the workflow, not in polishing the code.

## Prerequisites

- Python 3.10 or newer.
- Claude Code installed and running. The `claude` command should work in your terminal.
- Basic familiarity with Python and pytest.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ANI-IN/context-management.git
cd context-management
```

2. Create a virtual environment and install the project with its development tools:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

3. Check that everything works:

```bash
pytest
python examples/predict_examples.py
```

4. Launch Claude Code from the project folder:

```bash
claude
```

## Useful Commands

| Task | Command |
|---|---|
| Run the tests | `pytest` |
| Lint and check formatting | `ruff check . && ruff format --check .` |
| Type-check | `mypy` |
| Retrain the model | `python -m sentiment_app.training.train` |
| Try some predictions | `python examples/predict_examples.py` |

The app reads its settings from environment variables:

| Variable | Purpose | Default |
|---|---|---|
| `SENTIMENT_WEIGHTS_PATH` | Path to the trained weights file | `models/sentiment_weights.json` |
| `SENTIMENT_THRESHOLD` | Probability at or above which a review is labeled positive | `0.5` |
| `SENTIMENT_API_KEY` | API key that clients must present | unset, so every key is rejected |

## Project Structure

```
.
├── CLAUDE.md                    Project instructions loaded into every Claude Code session
├── README.md                    This file
├── pyproject.toml               Package metadata, dev dependencies, and tool settings
├── docs/
│   └── context-management.md    The lesson: context window, compaction, commands, tips
├── exercises/                   Step-by-step exercise guides
│   ├── README.md                Index, how to use the guides, and key takeaways
│   └── 01 … 06                  One guide per step
├── data/
│   └── reviews.csv              Labeled product reviews used for training
├── models/
│   └── sentiment_weights.json   Trained model weights
├── examples/
│   └── predict_examples.py      Runs a few reviews through the prediction route
├── src/sentiment_app/           The sample app, used as material to explore
│   ├── api/
│   │   ├── config.py            Loads model settings from environment variables
│   │   └── predict.py           Public prediction route; validates the input text
│   ├── auth/
│   │   └── api_key.py           Checks a client's API key
│   ├── model/
│   │   └── classifier.py        Naive Bayes classifier loaded from JSON weights
│   └── training/
│       ├── train.py             Trains the model from data/reviews.csv
│       └── run_log.py           Tracks the lifecycle of a training run
└── tests/                       pytest suite
```

The three commands you will practice:

| Command | What it does |
|---|---|
| `/context` | Shows how full the window is and what is consuming the most space. |
| `/compact` | Summarizes the conversation so far and keeps the summary, freeing space while preserving memory of what you were doing. |
| `/clear` | Wipes the session entirely for a clean start. `CLAUDE.md` stays loaded. |

Read [docs/context-management.md](docs/context-management.md) first for the background on each one.

## Running the Demo

The demo runs entirely inside Claude Code. Launch `claude` in this folder and follow these steps in order. Each step has a detailed guide in the `exercises/` folder.

1. **Check your starting context.** Run `/context` and note the baseline.
2. **Fill the context with real work.** Ask Claude to read `src/` and trace the prediction flow, then run `/context` again and watch the usage climb.
3. **Compact to keep going.** Run `/compact`, then `/context` to confirm usage dropped.
4. **Clear before an unrelated task.** Run `/clear`, then `/context` to see the window back near baseline.
5. **Persist what should survive.** Ask Claude to add a durable note to `CLAUDE.md`.
6. **Save context space.** Practice specific prompts, MCP server hygiene, and subagents.

## Exercises

Start with the index, [exercises/README.md](exercises/README.md), then work through the guides in order:

1. [Check your starting context](exercises/01-check-your-starting-context.md)
2. [Fill the context with real work](exercises/02-fill-the-context-with-real-work.md)
3. [Compact to keep going](exercises/03-compact-to-keep-going.md)
4. [Clear before an unrelated task](exercises/04-clear-before-an-unrelated-task.md)
5. [Persist what should survive](exercises/05-persist-what-should-survive.md)
6. [Save context space](exercises/06-save-context-space.md)

Each guide tells you what to do, what to observe, what to look for in the code, and what you should learn.

## Additional Notes

- **Persisting memory.** Anything Claude should remember across sessions belongs in `CLAUDE.md`. It survives both compaction and clearing and reloads every session.
- **Saving space.** Write specific prompts, turn off MCP servers you do not need, and delegate lookups to subagents that report back a short answer.
- **Troubleshooting.**

| Symptom | Resolution |
|---|---|
| Context fills surprisingly fast | Run `/context` to find the consumer. Large file reads (such as the weights JSON) or many MCP tools are common causes. |
| Claude forgot something after compaction | It was not durable. Put it in `CLAUDE.md` and it will reload each session. |
| New task feels biased by old work | You compacted when you should have cleared. Use `/clear` when switching to unrelated work. |
| `ModuleNotFoundError: sentiment_app` | Activate the virtual environment and run `pip install -e ".[dev]"`. |
| `FileNotFoundError` for the weights file | Run `python -m sentiment_app.training.train` to regenerate `models/sentiment_weights.json`. |
