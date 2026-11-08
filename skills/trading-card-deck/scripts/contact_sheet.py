#!/usr/bin/env python3
"""Proof sheets for card images.

  python3 contact_sheet.py OUT.jpg card1.png card2.webp ...            # whole cards side by side
  python3 contact_sheet.py --art OUT.jpg cards/*.webp                  # just the art windows, 10 across, labeled
  python3 contact_sheet.py --text OUT.jpg card1.png card2.png          # the bottom (text) half of each card, stacked

Whole cards: compare layouts, colors and consistency across a batch.
--art: work out a deck's visual rules (clothing, poses, backgrounds) from many existing cards at once.
--text: proofread the printed text at a readable size.
The art window is assumed to sit about 10% to 47% down the card; change ART_BOX for other layouts.
"""
import os, sys
from PIL import Image, ImageDraw

ART_BOX = (0.08, 0.10, 0.92, 0.47)


def whole(out, files, w=530):
    h = int(w * 1.4)
    s = Image.new("RGB", (len(files) * (w + 10) - 10, h), "white")
    for k, f in enumerate(files):
        s.paste(Image.open(f).convert("RGB").resize((w, h), Image.LANCZOS), (k * (w + 10), 0))
    s.save(out, quality=88)


def art(out, files, w=300, h=190, cols=10):
    rows = (len(files) + cols - 1) // cols
    s = Image.new("RGB", (w * cols, (h + 16) * rows), "white"); d = ImageDraw.Draw(s)
    for k, f in enumerate(files):
        im = Image.open(f).convert("RGB"); W, H = im.size
        a = im.crop((int(W * ART_BOX[0]), int(H * ART_BOX[1]), int(W * ART_BOX[2]), int(H * ART_BOX[3]))).resize((w, h))
        x, y = (k % cols) * w, (k // cols) * (h + 16)
        s.paste(a, (x, y)); d.text((x + 3, y + h + 2), os.path.basename(f)[:45], fill="black")
    s.save(out, quality=80)


def text(out, files, frac=0.53, w=800):
    parts = []
    for f in files:
        im = Image.open(f).convert("RGB"); W, H = im.size
        c = im.crop((0, int(H * (1 - frac)), W, H)); parts.append(c.resize((w, int(c.height * w / W))))
    s = Image.new("RGB", (w, sum(p.height for p in parts)), "white"); y = 0
    for p in parts: s.paste(p, (0, y)); y += p.height
    s.save(out, quality=88)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--art": art(a[1], a[2:])
    elif a[0] == "--text": text(a[1], a[2:])
    else: whole(a[0], a[1:])
