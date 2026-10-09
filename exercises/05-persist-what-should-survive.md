# Exercise 5: Persist What Should Survive

## Goal
Save a durable fact so it survives both compaction and clearing, and reloads automatically every session.

## Context
Both `/compact` and `/clear` discard detail. Anything Claude should remember across sessions does not belong in the conversation. It belongs in `CLAUDE.md`.

## Steps
1. Ask Claude to record a durable note. Send this prompt exactly:

```
Add a note to CLAUDE.md: prediction requests must go through
src/sentiment_app/api/predict.py, which validates the input text
and reads the threshold from config.
```

2. Open `CLAUDE.md` and confirm the note is there.

3. Run `/clear`, then ask Claude where prediction requests should go. It answers from `CLAUDE.md` without reading any source files.

## What to observe
The fact is now written into `CLAUDE.md`. From now on it loads every session and never has to be rediscovered. Even after a `/clear`, this note comes back, because `CLAUDE.md` stays loaded.

## What to look for in the code
The note describes real behavior in the project. Open `src/sentiment_app/api/predict.py` and confirm that it:

- rejects empty text and text longer than `MAX_TEXT_LENGTH` before doing anything else,
- loads the model config, including the threshold, from `api/config.py`,
- and only then hands the text to the classifier.

That is why the note is accurate: every prediction goes through this one guarded entry point.

## Outcome
You know where durable memory lives and how to add to it, so important facts survive compaction, clearing, and new sessions.
