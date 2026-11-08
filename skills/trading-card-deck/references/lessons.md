# Lessons from building LegíMon

Every problem here actually happened, along with the fix.

## Rules

- **New cards ignored rules nobody had written down.** The first batch of new cards had one type instead of two, an invented stage (SENATOR-ELECT), an invented retreat value (4), and outfits that broke the party-color rule. The owner had to point all of it out.
  - Fix: work the rules out of the existing deck before making anything (SKILL.md step 0), and write them in `RULES.md`.
- **Shiny cards were missing sections and didn't match each other.** Some had no info strip or flavor box. Thune's said "HP 270" instead of "270 HP" and had no Ability tag.
  - Fix: one shared layout for all shiny cards, with every section a regular card has. Redraw old ones by attaching the corrected layout as image 1 and the old card as image 2.

## Art

- **Domination imagery.** "Holding a giant AI robot on a chain leash" read as enslaving AI.
  - Fix: show the person's actual position (pressing a pause button), and add "nobody chains, attacks or dominates anyone" to every prompt.
- **Scenes that make no sense.** A senator wrote on a clipboard that faced away from him.
  - Fix: ask for props "held the right way round, facing the person using it", and look at every scene, not just the text.
- **Costumes.** Lab coats, scrubs and a flannel shirt broke the business-clothes look.
  - Fix: "No lab coats, scrubs or work clothes; show their job through a prop or the background" (a stethoscope over a suit).
- **Colors bleeding from the reference card.** An orange and purple reference card turned beige cards orange and purple.
  - Fix: use a reference card of the same kind and color, and say "copy the first image's background color exactly, with no orange or purple tint".
- **Wrong icons.** "Tan circle with a brown mountain" sometimes came back as a rock.
  - Fix: describe icons so they can't be mistaken: "dark brown mountain peak (a triangle mountain, NOT a rock)". Check icons during proofreading, because they change how the game plays.
- **Layout drift.** Some generations added boxes around attacks, dividers in the weakness row, or a thin border.
  - Fix: "Match the first image's layout exactly: no extra boxes around attacks and no vertical divider lines". Compare cards side by side.

## Text

- Roughly 1 card in 8 had a text problem: "Kentцcky", "Oct. 2026: plan:", a dropped flavor line, a stray apostrophe, or "~30" in place of "−30". Proofread every card at full size.
- Patching background pixels with PIL fixed a stray mark faster than regenerating, and without new errors.
- ChatGPT's web app edits drifted more than fresh Codex generations: fixing one thing broke another, like a retreat cost dropping from 4 to 3. Prefer a fresh generation with a sharper prompt over a chain of edits.

## Tools and accounts

- The chatgpt.com account in the browser was a different, Free-plan account; the Pro plan was on the desktop app's account. The Codex CLI uses the desktop login and has image generation, so it is the better route.
- If chatgpt.com looks logged out on the first load, reload before telling anyone.
- Wikimedia's API rate-limits fast requests (HTTP 429). Wait 2 seconds between requests, back off on 429, and send a descriptive User-Agent.
- Generated text can be off even when the prompt is right. Check birth years and dates independently: two of four guesses were wrong.

## Data and publishing

- Saved collections stored list positions, so removing cards would have scrambled every binder.
  - Fix: store card numbers, with a one-time migration from the old positions. Never renumber or reuse numbers.
- The site had an empty `404.html`. A redeploy without it made every unknown URL serve the home page.
  - Fix: download every file the live site serves before the first redeploy.
- Another app (WonkoLingo) copies the card list and links to the images.
  - Fix: keep departed cards' images online, sync after every change, and commit only your own lines in a repo where other sessions are working.
