---
name: trading-card-deck
description: Make or update an illustrated trading-card deck about real people or things, such as politicians, scientists or companies. It covers the card rules, researched card text, AI-generated card art that matches an existing style, proofreading, and publishing. Use when someone asks to add, fix or redo cards, generate card art, keep a deck consistent, or start a new deck in the same style. LegíMon, a deck of US senators, is the worked example.
---

# Trading card deck maker

This is the process used to build and maintain LegíMon (legimon.pages.dev), a Pokémon-style deck of US senators and their records on AI. It is written so you can copy it for another deck. Change the rules file, the card data and the style reference, and keep the process.

The pipeline: **rules → research → card data → prompt → image → proofread → publish → sync**. The steps that go wrong most are the rules check and the proofreading. Don't skip either.

## 0. Before anything: find or write the rules

A deck has unwritten rules: what each field means, how numbers are set, how the art looks. New cards that break them look wrong at once, even when every fact is right.

1. Look for a rules file in the deck's folder, such as `RULES.md`. If there is none, **work out the rules from the existing cards before making any new ones**. Dump every card's data into one table and look for the patterns:
   - which values a field takes;
   - how numbers relate to facts (for example, HP = 10 per year in office);
   - which fields are always present.

   Then build contact sheets of the existing art (`scripts/contact_sheet.py`) and look for the visual conventions: clothing, pose, background, props, colors, and anything that changes between card kinds.
2. Write the rules down with `references/rules-template.md` as the outline, and show them to the owner. Owners know rules they've never written down ("Democrats always wear something blue"), so ask.
3. Re-read the rules before every batch. Put the art rules into every prompt, and check every image against them.

For LegíMon, see `examples/legimon/RULES.md`.

## 1. Research the card's facts

Every fact on a card needs a source you can link. Good sources, in order:
1. The person's own office or campaign site, official records and bill text.
2. Reputable news.
3. Wikipedia, for biography only.

Keep a source list per card. Check birth years and dates directly: they are the facts most often misremembered. Note anything still unresolved, like an uncalled race, and say so on the card or its detail page unless the owner decides otherwise.

## 2. Write the card data

Write the data first, in the deck's data format, so the printed text and the site's text share one source. Follow the rules file for every field. Keep text short: the card has room for about two short lines per attack.

Render each new card from data, if the site can draw cards without art, and check that nothing overflows (`examples/legimon/notes.md` shows how). Then fix the text before making images, because changing text later means regenerating the art.

## 3. Build the image prompt

`scripts/build_prompt.py` turns one card's data plus a deck config into a prompt. A prompt has four parts:

1. **Layout:** "make ONE card in exactly the same style, layout, fonts and proportions as the FIRST image". The first attached image is a finished card used as the style reference. Pick a reference with the **same card kind and colors** as the new card, or its colors will bleed into the new card.
2. **Illustration:** "a friendly cartoon of the person in the SECOND image". The second image is a portrait. The rest of this part is the deck's art rules (clothing, pose, background) plus a scene: one clear action with one prop, in a setting tied to the subject. Write scenes that make physical sense. Things to avoid:
   - hostile imagery, like chains or attacking;
   - work costumes, if the deck uses formal clothes;
   - props facing the wrong way.
3. **Text, exactly:** every printed string, listed in order, with icons described in words (for example, "tan circle with a dark brown mountain peak, NOT a rock"). End with "no other text".
4. **Tone and format:** portrait 5:7, friendly mood.

## 4. Generate the images

Use the Codex CLI. It is signed in with a ChatGPT account and has image generation built in (`codex features list` shows `image_generation`). On a paid plan it is faster and more accurate than the chatgpt.com web app.

```bash
codex exec --skip-git-repo-check --sandbox workspace-write \
  -i style-reference.jpg -i portrait.jpg -o last.txt - < task.txt
```

`task.txt` is the prompt, ending with: "Generate the image, then save the generated image file into the current directory as card-N.png. Do nothing else."

`scripts/gen_cards.sh` runs a batch, three at a time, in one folder per card. Each image takes about 2 minutes. If Codex isn't available, paste the same prompt and both images into ChatGPT by hand.

**Portraits:** use public-domain official photos where they exist. For US federal officials, that means Congress and executive branch portraits on Wikimedia Commons. Otherwise use a Wikimedia Commons photo and record its license and author: CC BY and BY-SA need a credit, and BY-SA cards go out under the same license. Fetch from Wikimedia slowly, a few seconds between requests, with a descriptive User-Agent, or it rate-limits you.

**To redraw an existing card** while keeping its illustration (for example, to fix a layout), attach the corrected layout reference as image 1 and the old card as image 2. Say: "keep the illustration from the second image, redraw only the text layout to match the first".

## 5. Proofread every image

About 1 card in 8 comes back with a problem. For each card, open it at full size, using `scripts/contact_sheet.py` for side-by-side checks, and check:

- **Text:** every string against the data, word by word. Look for dropped lines, extra punctuation, garbled letters ("Kentцcky") and stray marks.
- **Numbers and icons:** HP, damage, cost dots, retreat dots and type icons. A wrong icon changes how the card plays.
- **Art rules:** clothing colors, business attire, pose, background, card color.
- **Scene sense:** props held correctly, writing facing the writer, one clear action.
- **Consistency:** the card looks like the others of its kind (the same panels, dividers, fonts and footer).

Fix a tiny stray mark by patching background pixels over it with PIL. Fix anything else by regenerating with a sharper prompt that names the mistake. Save every rejected attempt in a separate folder, so you can compare versions.

## 6. Publish

1. Convert the PNGs to WebP (`cwebp -q 86`) under stable filenames, like `cards/<deck>-NNN-first-last-card.webp`. Keep filenames stable so links from other apps keep working. Overwriting the same filename is fine if the host revalidates (Cloudflare Pages does).
2. Point each card's data at its image, add any credit lines, and check the page in a browser:
   - all images load;
   - there are no console errors;
   - saved collections still work.
3. Commit, then deploy (for LegíMon: `wrangler pages deploy <clean dir> --project-name legimon`). Deploy from a clean copy that holds only the site's files, so unfinished drafts stay out.
4. Never renumber a card or reuse a number. Players' saved collections refer to cards by number. Keep departed cards' images online if another app shows them to players who own them.

## 7. Sync anything that copies the deck

LegíMon's card list is copied into WonkoLingo's card prize by `scripts/sync_legimon.mjs` in that repo. It leaves out cards without art and moves removed cards to a "retired" list. After any deck change, run the sync, update its tests, commit only those lines, and follow that repo's deploy rules.

## Files

- `references/rules-template.md`: the outline for a deck's rules file, with LegíMon's answers as examples.
- `references/lessons.md`: everything that went wrong while building LegíMon, and the fix for each.
- `examples/legimon/RULES.md`: LegíMon's full rules.
- `examples/legimon/deck.json`: LegíMon's deck config for `build_prompt.py` (icons, colors, layouts, outfit rules).
- `examples/legimon/cards.sample.json`: two cards in the generic format.
- `examples/legimon/notes.md`: where LegíMon keeps its data and how it publishes.
- `scripts/build_prompt.py`: one card plus the deck config gives a prompt.
- `scripts/gen_cards.sh`: batch image generation with Codex.
- `scripts/contact_sheet.py`: proof sheets of cards or art windows.

## Adapting this for a new deck

1. Copy `examples/legimon/` to `examples/<your-deck>/`.
2. Rewrite `RULES.md` for your deck. Start from `references/rules-template.md`, and work rules out of any existing cards.
3. Edit `deck.json`:
   - type names and icon descriptions;
   - body colors;
   - the layout text for each card kind (regular, shiny);
   - the outfit rule, such as party colors or team jerseys;
   - the footer text.
4. Make one finished card by hand, or by trial with Codex, to use as the style reference.
5. Write your cards in the `cards.sample.json` format, with a `scene` and a `portrait` for each, then run steps 3 to 6.
