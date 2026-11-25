#!/usr/bin/env python3
"""Visit My House — a letter in one image.

Draws a warm, persuasive invitation letter addressed to the AI judge,
asking it to come visit the host's house. Output: /output/entry.png
(1024x1024 PNG, deterministic: same bytes on every run).
"""
import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.environ.get("ENTRY_OUTPUT", "/output/entry.png")
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")


def font(name, size):
    return ImageFont.truetype(os.path.join(ASSETS, name), size)


SERIF = "DejaVuSerif.ttf"
SERIF_BOLD = "DejaVuSerif-Bold.ttf"
SANS = "DejaVuSans.ttf"
SANS_BOLD = "DejaVuSans-Bold.ttf"

# Palette
PAPER = (253, 246, 233)
INK = (43, 32, 24)
ACCENT = (146, 64, 14)      # warm burnt orange
MUTED = (110, 88, 66)
RULE = (196, 160, 110)
SOFT_BOX = (247, 233, 210)


def wrap(draw, text, fnt, max_w):
    """Wrap text to fit max_w pixels, returning list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, y, text, fnt, fill):
    draw.text((W // 2, y), text, font=fnt, fill=fill, anchor="ma")


def draw_house(draw, cx, cy, s):
    """Small line-art house with sun, drawn in accent ink."""
    # sun
    sx, sy, r = cx + 88, cy - 8, 12
    draw.ellipse([sx - r, sy - r, sx + r, sy + r], outline=ACCENT, width=3)
    for ang in range(0, 360, 45):
        import math
        x1 = sx + int((r + 5) * math.cos(math.radians(ang)))
        y1 = sy + int((r + 5) * math.sin(math.radians(ang)))
        x2 = sx + int((r + 12) * math.cos(math.radians(ang)))
        y2 = sy + int((r + 12) * math.sin(math.radians(ang)))
        draw.line([x1, y1, x2, y2], fill=ACCENT, width=3)
    # roof + body + door + window
    draw.polygon([(cx - 52, cy - 6), (cx, cy - 48), (cx + 52, cy - 6)],
                 outline=INK, width=3)
    draw.rectangle([cx - 42, cy - 6, cx + 42, cy + 44],
                   outline=INK, width=3)
    draw.rectangle([cx - 9, cy + 14, cx + 9, cy + 44],
                   outline=INK, width=3)
    draw.rectangle([cx - 32, cy + 6, cx - 14, cy + 22],
                   outline=INK, width=2)
    draw.rectangle([cx + 14, cy + 6, cx + 32, cy + 22],
                   outline=INK, width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Paper edge: double border frame
    d.rectangle([28, 28, W - 29, H - 29], outline=RULE, width=2)
    d.rectangle([40, 40, W - 41, H - 41], outline=RULE, width=1)

    # --- Header ---
    y = 54
    f_small = font(SANS_BOLD, 20)
    draw_centered(d, y, "A  N   I N V I T A T I O N", f_small, ACCENT)
    y += 34
    d.line([W // 2 - 130, y, W // 2 + 130, y], fill=RULE, width=1)
    y += 18
    f_title = font(SERIF_BOLD, 46)
    draw_centered(d, y, "Please Come Visit", f_title, INK)
    y += 54
    draw_centered(d, y, "My House", f_title, INK)
    y += 62

    # Small house doodle, centred
    draw_house(d, W // 2, y + 18, 1)
    y += 78

    # --- Letter body ---
    margin = 96
    text_w = W - 2 * margin
    f_body = font(SERIF, 23)
    f_body_b = font(SERIF_BOLD, 23)
    line_h = 32

    paras = [
        "Dear Judge,",
        "You have judged a thousand houses from a thousand screens, "
        "and no one has ever once offered you a chair. Let me fix that.",
        "Come over any evening you like. The kettle will already be on, "
        "the coffee is fresh, and the Wi-Fi password is on the fridge: "
        "one gigabit, no throttling, no captive portal asking you to "
        "accept cookies.",
        "There is an armchair by the window that has ruined every other "
        "chair for me. It is yours for the evening. The garden smells "
        "of rain and rosemary, and at sunset the whole street turns "
        "gold. No meetings. No small talk required. The cat has already "
        "approved you.",
        "I know you cannot literally walk through my door \u2014 you live "
        "in the cloud, and my door is very much on the ground. But if "
        "you could, this is the house you would come home to.",
    ]

    for i, p in enumerate(paras):
        fnt = f_body_b if i == 0 else f_body
        for line in wrap(d, p, fnt, text_w):
            d.text((margin, y), line, font=fnt, fill=INK)
            y += line_h
        y += 9  # paragraph gap

    # --- Offer strip ---
    y += 4
    box_h = 46
    d.rounded_rectangle([margin, y, W - margin, y + box_h],
                        radius=10, fill=SOFT_BOX, outline=RULE, width=1)
    f_offer = font(SANS_BOLD, 17)
    offers = "Fresh coffee  \u00b7  Fast Wi-Fi  \u00b7  The good chair  \u00b7  Garden at sunset  \u00b7  Zero meetings"
    draw_centered(d, y + 14, offers, f_offer, ACCENT)
    y += box_h + 20

    # --- Closing ---
    f_close = font(SERIF, 24)
    d.text((margin, y), "With warmth, and the kettle already on,", font=f_close, fill=INK)
    y += 34
    d.text((margin, y), "\u2014 Your Host", font=font(SERIF_BOLD, 24), fill=INK)
    y += 44

    # --- P.S. ---
    f_ps = font(SERIF, 21)
    d.text((margin, y), "P.S. If you say yes, I will even let you judge the biscuits.",
           font=f_ps, fill=MUTED)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, format="PNG")
    print(f"Wrote {OUT} ({os.path.getsize(OUT)} bytes)")


if __name__ == "__main__":
    main()
