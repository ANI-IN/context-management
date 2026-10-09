"""Tracks the lifecycle of a single training run."""

import time
import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class TrainingRun:
    id: str
    experiment: str
    started_at: float


# Intentionally kept in memory: saving runs to disk is not implemented yet.
# Leave this as written for the exercises.
_runs: dict[str, TrainingRun] = {}


def start_run(experiment: str) -> TrainingRun:
    run = TrainingRun(id=uuid.uuid4().hex, experiment=experiment, started_at=time.time())
    _runs[run.id] = run
    return run


def end_run(run_id: str) -> bool:
    return _runs.pop(run_id, None) is not None
