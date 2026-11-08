#!/usr/bin/env python3
"""Build an image-generation prompt for one card from card data plus a deck config.

Usage:
  python3 build_prompt.py DECK.json CARDS.json NUMBER > task.txt

DECK.json describes the deck once: type icons, body colors, the layout text for each card kind, the outfit rule and the
footer. CARDS.json is a list of cards in the generic format (see examples/legimon/cards.sample.json). Each card can carry
a "scene" (the illustration's one action and setting) and a "kind" ("regular" by default, or "shiny").

The prompt follows the recipe in SKILL.md: layout from the first attached image, person from the second, the art rules,
the scene, then every printed string spelled out, with "no other text".
"""
import json, sys


def icons(deck, types):
    return ", ".join(deck["icons"][t] for t in types) or "none"


def outfit(deck, card):
    rule = deck.get("outfit", {})
    for key, text in rule.items():          # e.g. {"R": "...red...", "D": "...blue...", "I": "...blue..."}
        if card.get("faction", "").startswith(key):
            return text
    return rule.get("default", "")


def text_lines(deck, c, kind):
    L = ["Use this text exactly, spelled exactly as written, and no other text except any short prop label mentioned above:",
         f"- Top left, small caps: {c['stage']}",
         f"- Name, big bold: {c['name']}",
         f"- Top right: {c['hp']} HP in red, then the type icons: {icons(deck, c['types'])}",
         f"- {deck['layouts'][kind]['number_line_place']}: " + deck["number_line"].format(**c),
         f"- Silver strip: {c['strip']}"]
    if c.get("ability"):
        L.append(f"- Red 'Ability' tag, then '{c['ability']['name']}' in bold; below it: {c['ability']['text']}")
    for a in c["attacks"]:
        L.append(f"- Attack: cost icons on the left ({icons(deck, a['cost'])}), name '{a['name']}' in bold, "
                 f"damage {a['damage']} on the right; below it: {a['text']}")
    w, r = c.get("weakness"), c.get("resistance")
    star = deck["icons"][deck.get("colorless", "normal")]
    L += ["- weakness: " + (f"{deck['icons'][w['type']]} icon + '{w['text']}'" if w else "a dash"),
          "- resistance: " + (f"{deck['icons'][r['type']]} icon + '{r['text']}'" if r else "a dash"),
          "- retreat cost: " + (f"{c['retreat']} {star} icons" if c.get("retreat") else "a dash"),
          f"- Flavor box, italic serif: {c['flavor']}",
          "- Footer: " + deck["footer"].format(**c)]
    return L


def prompt(deck, c):
    kind = c.get("kind", "regular")
    lay = deck["layouts"][kind]
    head = [lay["intro"]]
    if kind == "regular":
        body = " and ".join(dict.fromkeys(deck["body_colors"][t] for t in c["types"]))
        head.append(" ".join([deck["illustration"], c["scene"] + ".", outfit(deck, c), deck.get("art_rules", ""),
                              f"The card body background is {body}, matching the card's type; copy the first image's background color exactly."]))
    else:
        head.append(lay["keep_art"])
    return "\n".join(head + text_lines(deck, c, kind) + [deck["closing"]])


if __name__ == "__main__":
    deck = json.load(open(sys.argv[1], encoding="utf-8"))
    cards = json.load(open(sys.argv[2], encoding="utf-8"))
    n = int(sys.argv[3])
    print(prompt(deck, next(c for c in cards if c["number"] == n)))
