# Context Management in Claude Code

Context is Claude's working memory. Every file it reads, every command it runs, and every message you send takes up space in the context window. This page covers the ideas behind the exercises. Read it once, then work through the guides in [`exercises/`](../exercises/README.md).

## 1. What is the context window?

Think of the context window as the amount of space Claude can hold in its memory. Each prompt you enter, each file Claude reads, each tool call it runs, and each tool result it gets back adds to the context window. That space is finite, so how you use it matters.

## 2. What happens when context fills up

When you approach the limit, Claude Code compacts the context window automatically. Compaction summarizes the important details and drops tool results that are no longer needed, which frees space. A structured summary of the earlier conversation takes the place of the full history.

> **Compaction can lose detail.** If something matters for the long term, don't count on it surviving compaction. Save it somewhere durable, such as your `CLAUDE.md` file.

## 3. Commands

| Command | What it does |
|---|---|
| `/context` | Shows how full the window is, the categories taking up the most space, and a visual breakdown. |
| `/compact` | Summarizes everything up to this point and keeps the summary. Use it to free space while remembering what you were working on. |
| `/clear` | Wipes the session entirely so you can start from a clean slate. `CLAUDE.md` stays loaded. |

## 4. When to use which

| Reach for | When |
|---|---|
| `/compact` | You are working on one feature, you are near the context limit, and you need to keep going. Keep the context focused on what you are building. |
| `/clear` | You are starting a new feature and don't want the previous conversation to bias the new work. |

Anything Claude should remember across sessions belongs in `CLAUDE.md`, so it never has to be rediscovered from scratch.

## 5. Tips for saving context space

- **Be specific.** A vague prompt looks smaller but costs more context over time. Without clear instructions, Claude has to explore your codebase and reason through the gaps, which uses far more space than a detailed prompt.
- **Manage your MCP servers.** By default, each MCP server loads all of its tools into context, including the ones you aren't using. Turn off servers that aren't related to the current project. Skills are a lighter alternative because they don't load everything up front.
- **Use subagents.** A subagent has its own context window, separate from your main session. When you only need an answer, such as "where is the API key checked?", a subagent does the searching and returns just a summary. Your main context stays clean.

## 6. Key takeaways

- Use `/compact` to summarize long sessions and `/clear` to start fresh.
- Write specific prompts so Claude doesn't have to explore to fill in the gaps.
- Check what is consuming your context with `/context`.
- Delegate to subagents when you only need the result.
- Treat context like working memory. Keep it lean, and Claude works better.
