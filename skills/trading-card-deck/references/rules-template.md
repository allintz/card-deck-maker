# Rules template for a card deck

Copy this into your deck's folder as `RULES.md` and answer every question. If the deck already has cards, answer from what the cards actually do, not from memory: dump all the card data into one table, and build art contact sheets (`scripts/contact_sheet.py --art`). Then show the owner, who will know rules nobody wrote down. LegíMon's answers are in brackets.

## Card data

- **Card kinds:** what kinds exist, and how many of each? [Regular; shiny full-art holo for party leaders; one LEGENDARY]
- **Stage labels:** which values are allowed? [SENATOR, LEADER, LEGENDARY. Never invent new ones, like SENATOR-ELECT.]
- **Types:**
  - How many per card? [Always two, each from a committee.]
  - Where does each come from? [First: the committee they lead, or their leadership post. Second: the committee most relevant to their AI work.]
  - What is the full type chart? [13 types, one per committee group.]
  - What happens when the source is missing? [Senators-elect have no committees, so they're Normal type, with no committee label.]
- **Numbers:** what does each one encode?
  - HP: [10 per year in Congress, minimum 10]
  - Retreat cost: [the next election: 1 for 2026, 2 for 2028, 3 for 2030 or later, 0 if leaving]
  - Damage: [decoration: 30 to 50 for one dot, 70 to 150 for two or three]
- **Attacks:** how many, and what counts as one? [One or two real bills, votes or public moves. Costs use the card's own types, plus Normal as filler.]
- **Weakness and resistance:** what do they mean, and how is each type picked? [A real rival typed by that rival's role, and a pressure they shrug off, at −20 or −30.]
- **Text fields:** what goes where, and what is the format of each line? [Number line "No. NNN · Nickname LegíMon · Party-State · Born YYYY"; info strip: posts, committees, years; flavor box: stance on the deck's theme, quoting them if they said something direct.]
- **Numbering:** are numbers permanent? [Yes. Never renumber or reuse a number; collections save numbers.]
- **Sources:** what level of sourcing is needed? [Every fact links to a source on the card's detail page.]

## Card art

- **Subject:** how big, where on the card, and what expression? [Waist-up, large, left or center foreground, smiling or determined.]
- **Clothing:** what does each subject wear, and what signals their side or team? [Business clothes. Democrats: a clearly blue item. Republicans: a clearly red item.]
- **Jobs and backstory:** how do they show? [Through props or the background, never costumes. A doctor wears a stethoscope over a suit.]
- **Action:** what is the subject doing? [One clear action with one prop that shows their position: a pause button, a magnifying glass, a sign with a 1 to 3 word label.]
- **Background:** what setting? [A landmark from their home state, at golden hour.]
- **The deck's theme:** how is it drawn, and what is off-limits? [AI as friendly robots, chips or data centers. Nobody chains, attacks or dominates it.]
- **Card colors:** what decides them? [The card body is the two type colors as a gradient. Normal is beige-gray.]
- **Special kinds:** how do shiny cards differ, and what must they keep? [Holo foil, art fills the card, text on translucent panels. They keep every section a regular card has, in one shared layout.]
- **Style reference:** which existing card is the reference for each kind? [Regular: a beige newcomer card. Shiny: Schumer's.]
- **Licensing:** which photos can be used, and how are they credited? [Public-domain official portraits first; otherwise credit the Wikimedia Commons photo and its license.]

## Checks before publishing

- Every printed string matches the data exactly.
- The numbers and icons are right.
- The art follows every rule above.
- The scene makes physical sense.
- The card looks like the others of its kind.
