# card-deck-maker

A Claude Code plugin with one skill, `trading-card-deck`. It's the process behind LegíMon (https://legimon.pages.dev), a Pokémon-style deck of US senators and their AI records, written so you can reuse it for any deck about real people or things.

Start with `skills/trading-card-deck/SKILL.md`. To make a new deck, copy `examples/legimon/`, rewrite its `RULES.md` and `deck.json`, and follow the steps.

Generating images needs the Codex CLI signed in with a ChatGPT account (`npm i -g @openai/codex`, then `codex login`). Without it, paste the generated prompts into ChatGPT by hand.
