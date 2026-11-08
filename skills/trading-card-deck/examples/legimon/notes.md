# LegíMon: where things live

- **Live site:** https://legimon.pages.dev, the Cloudflare Pages project `legimon`.
- **Source:** `~/Documents/legimon`, a local git repo on Alex's Mac. All card data is inline in `index.html`:
  - `var CARDS`: JS literals for the old cards, JSON objects for cards 102 and up;
  - `var DETAILS`: the detail pages (about, AI record, stance, election, sources), keyed by name;
  - `var LEVELS`: each senator's AI-risk stance on a 1 to 5 scale.
- **Card images:** `cards/legimon-NNN-first-last-card.webp`. The shinies are full-art; Thune's and Cotton's are `.jpg`.
- **Rules:** `RULES.md`, also copied here.
- **Tools** (in `~/Documents/legimon/tools/`):
  - `card_prompts.py`: the LegíMon-specific prompt builder, which reads `index.html` directly;
  - `add_art.py`: adds art for new cards (PNG to WebP, sets `cardImage`, adds credit lines);
  - `replace_art.py`: overwrites an existing card's image in place;
  - `newcomers.py`, `colom.py`, `midterm_update.py`: the November 2026 roster changes, kept for reference.
- **Checking a card without art:** the page's `makeSlot(card, index)` draws any card from data. In the browser, put the slots in a fixed overlay and check each `.panel` for overflow (`scrollHeight > clientHeight`).
- **Deploy:** copy `index.html`, `favicon.svg`, `404.html` (empty) and `cards/` into a clean folder, then run `wrangler pages deploy <folder> --project-name legimon --branch main`. Leave out drafts like `rulebook.html`.
- **Sync after any change:** in `~/Documents/wonkolingo`, pull first, then run `node scripts/sync_legimon.mjs`, then `./build.sh`, then `node tests/legimon.test.mjs`. Commit only the `LEGI_CARDS`/`LEGI_RETIRED` lines and the tests. The deploy follows that repo's skill.
