# Exercise 6: Save Context Space

## Goal
Practice three habits that keep the context window lean, so Claude stays sharp and fast. This exercise turns the lesson's tips into things you can try directly.

## Habit 1: Be specific
A vague prompt can look smaller, but it usually costs more context in the long run. Without clear instructions, Claude has to explore your codebase and reason to fill the gaps, which takes far more space than a detailed prompt would.

Try it. Run `/clear`, send each prompt below, and run `/context` after each one to compare:

- Vague: `explain the prediction stuff`
- Specific: `In src/sentiment_app/api/predict.py, explain what handle_predict validates before calling the classifier.`

The specific version points Claude straight at the answer, so it reads less and reasons less. Notice also that a vague prompt might lead Claude to open `models/sentiment_weights.json`, a large file that fills the window quickly while adding little to the answer.

## Habit 2: Manage your MCP servers
By default, each connected MCP server loads all of its tools into context, even the ones you are not using. Run `/context` and look at how much space tools take. If some servers are unrelated to the current task, turn them off. Skills are a lighter alternative, because they do not load everything up front.

## Habit 3: Use subagents
A subagent runs with its own separate context window and returns just a summary, which keeps your main window clean. Reach for one when you only need the answer to a lookup, not the whole search.

For example, to find the authentication code without loading every file into your main context, ask a subagent:

```
Use a subagent to find where the client API key is checked.
```

The subagent does the searching and reports back a short answer. In this project that answer points at `src/sentiment_app/auth/api_key.py`. Run `/context` afterwards and notice that your main window barely grew.

## Outcome
You have three concrete habits for keeping context lean: write specific prompts, prune MCP servers you do not need, and delegate lookups to subagents.
