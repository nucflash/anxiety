#!/usr/bin/env python3
"""Overlay Greek text on anxiety sprite/thumbnail PNGs."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parents[1]
OUT = REPO.parent / "anxiety-el"
FONT_HAND = "/System/Library/Fonts/Supplemental/Chalkduster.ttf"
FONT_BOLD = "/Library/Fonts/Arial Unicode.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def cover(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], color=(0, 0, 0, 255)) -> None:
    draw.rectangle(box, fill=color)


def draw_centered(
    draw: ImageDraw.ImageDraw,
    text: str,
    box: tuple[int, int, int, int],
    fnt: ImageFont.FreeTypeFont,
    fill: str | tuple,
) -> None:
    x0, y0, x1, y1 = box
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = x0 + (x1 - x0 - tw) // 2
    y = y0 + (y1 - y0 - th) // 2
    draw.text((x, y), text, font=fnt, fill=fill)


def translate_fear_captions(path: Path) -> None:
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    f = font(FONT_HAND, 28)
    rows = [("βλάβη", 0), ("μόνος", h // 3), ("κακός", 2 * h // 3)]
    for text, y in rows:
        cover(draw, (0, y, w, y + h // 3 - 4))
        draw_centered(draw, text, (0, y, w, y + h // 3), f, "#ff4040")
    img.save(path)


def translate_preloader(path: Path) -> None:
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    cover(draw, (0, 0, w, 55))
    draw_centered(draw, "ΦΟΡΤΩΣΗ...", (0, 0, w, 55), font(FONT_HAND, 22), "white")
    # Three GO buttons stacked
    for y in (70, 145, 220):
        cover(draw, (w // 2 - 55, y, w // 2 + 55, y + 40), (0, 0, 0, 255))
        draw_centered(draw, "ΠΑΜΕ!", (w // 2 - 55, y, w // 2 + 55, y + 40), font(FONT_HAND, 20), "white")
    img.save(path)


def translate_thumb(path: Path, base: Path) -> None:
    img = Image.open(base).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    title = font(FONT_HAND, 42)
    sub = font(FONT_HAND, 28)
    draw.text((24, h - 120), "ΠΕΡΙΠΕΤΕΙΕΣ", font=title, fill="#ff4040")
    draw.text((24, h - 72), "ΜΕ ΑΓΧΟΣ!", font=title, fill="#ff4040")
    draw.text((24, h - 28), "παίζεις ως το άγχος", font=sub, fill="white")
    img.save(path)


def translate_intro_logo(path: Path) -> None:
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    cover(draw, (0, 0, w - 10, h - 80))
    t = font(FONT_HAND, 34)
    draw.text((20, 20), "ΠΕΡΙΠΕΤΕΙΕΣ", font=t, fill="#ff4040")
    draw.text((20, 58), "με", font=font(FONT_HAND, 22), fill="#ff4040")
    draw.text((60, 52), "ΑΓΧΟΣ", font=t, fill="#ff4040")
    s = font(FONT_HAND, 16)
    draw.text((w - 210, h - 95), "ΔΙΑΡΚΕΙΑ: 30 ΛΕΠ", font=s, fill="#888888")
    draw.text((w - 210, h - 72), "του NICKY CASE", font=s, fill="#888888")
    draw.text((w - 210, h - 49), "& MONPLAISIR", font=s, fill="#888888")
    draw.text((w - 210, h - 26), "μεταφ.: el fork", font=font(FONT_HAND, 12), fill="#666666")
    img.save(path)


def translate_cc0(path: Path) -> None:
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    cover(draw, (40, 0, w, h))
    draw.text((40, 8), "ΔΗΜΟΣΙΟ ΚΤΗΜΑ", font=font(FONT_HAND, 22), fill="white")
    img.save(path)


def translate_replay(path: Path) -> None:
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    for x in (0, w // 3, 2 * w // 3):
        cover(draw, (x + 5, 0, x + w // 3 - 5, 45))
        draw_centered(draw, "ΞΑΝΑ", (x, 0, x + w // 3, 45), font(FONT_HAND, 18), "#ff4040")
    img.save(path)


def translate_youwin(path: Path) -> None:
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    f_big = font(FONT_HAND, 36)
    cover(draw, (0, 0, w, h // 2))
    draw_centered(draw, "ΝΙΚΗΣΕΣ!", (0, 10, w, h // 2 - 10), f_big, "#ff4040")
    cover(draw, (0, h // 2, w, h))
    draw.text((w // 2 - 90, h // 2 + 10), "Εσύ,", font=font(FONT_HAND, 20), fill="#ff4040")
    draw.text((w // 2 - 30, h // 2 + 35), "νίκησες...", font=f_big, fill="#ff4040")
    img.save(path)


def translate_callback(path: Path) -> None:
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    cover(draw, (10, 15, 95, 75))
    draw.text((18, 22), "RIP", font=font(FONT_HAND, 16), fill="#333333")
    draw.text((14, 42), "ΚΙΝΗΤΟ", font=font(FONT_HAND, 12), fill="#333333")
    cover(draw, (img.size[0] - 95, img.size[1] - 45, img.size[0] - 5, img.size[1] - 5))
    draw.text((img.size[0] - 88, img.size[1] - 38), "ΛΙΜΝΗ", font=font(FONT_HAND, 11), fill="white")
    draw.text((img.size[0] - 88, img.size[1] - 24), "ΔΑΚΡΥΩΝ", font=font(FONT_HAND, 10), fill="white")
    img.save(path)


def translate_starring(path: Path) -> None:
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, _ = img.size
    cover(draw, (0, 0, w, 45))
    draw_centered(draw, "ΠΡΩΤΑΓΩΝΙΣΤΟΥΝ:", (0, 0, w, 45), font(FONT_HAND, 22), "#ff4040")
    img.save(path)


def translate_thanks(path: Path) -> None:
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, _ = img.size
    cover(draw, (0, 0, w, 55))
    draw.text((20, 8), "ΤΕΡΑΣΤΙΕΣ ΕΥΧΑΡΙΣΤΙΕΣ σε όσους με στήριξαν στο Patreon <3", font=font(FONT_HAND, 14), fill="white")
    cover(draw, (0, 520, w, 560))
    draw.text((20, 525), "& ΕΙΔΙΚΕΣ ΕΥΧΑΡΙΣΤΙΕΣ στους playtesters μου:", font=font(FONT_HAND, 14), fill="white")
    cover(draw, (0, img.size[1] - 35, w, img.size[1]))
    draw_centered(draw, "& ευχαριστώ, beebee", (0, img.size[1] - 35, w, img.size[1]), font(FONT_HAND, 14), "white")
    img.save(path)


def translate_screens(path: Path) -> None:
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    cover(draw, (0, 0, 280, 90))
    t = font(FONT_HAND, 24)
    draw.text((10, 10), "ΠΕΡΙΠΕΤΕΙΕΣ", font=t, fill="#ff4040")
    draw.text((10, 40), "με ΑΓΧΟΣ", font=t, fill="#ff4040")
    cover(draw, (300, 55, 520, 95))
    draw.text((305, 58), "δημιουργία:", font=font(FONT_HAND, 14), fill="white")
    cover(draw, (300, 130, 420, 155))
    draw.text((305, 132), "(και τον λύκο του)", font=font(FONT_HAND, 11), fill="#888888")
    cover(draw, (530, 55, 720, 95))
    draw.text((535, 58), "μουσική:", font=font(FONT_HAND, 14), fill="white")
    cover(draw, (530, 130, 680, 155))
    draw.text((535, 132), "(και το περιστέρι του)", font=font(FONT_HAND, 11), fill="#888888")
    cover(draw, (10, 175, 200, 200))
    draw.text((12, 177), "επιπλέον κώδικας:", font=font(FONT_HAND, 12), fill="white")
    cover(draw, (10, 230, 120, 255))
    draw.text((12, 232), "ηχητικά εφέ:", font=font(FONT_HAND, 12), fill="#ff4040")
    cover(draw, (w // 2 - 60, h - 40, w // 2 + 60, h - 10))
    draw_centered(draw, "ό,τι νά 'ναι,", (w // 2 - 60, h - 40, w // 2 + 60, h - 10), font(FONT_HAND, 14), "white")
    img.save(path)


def translate_end_message(path: Path) -> None:
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    msg = (
        "Αν σου άρεσε αυτό,\n"
        "μοιράσου το με έναν φίλο\n"
        "που μπορεί να το χρειάζεται.\n"
        "Και ξαναπαίξε το\n"
        "για άλλα τέλη!"
    )
    draw.multiline_text((w // 2 - 140, h // 2 - 80), msg, font=font(FONT_HAND, 18), fill="white", align="center")
    img.save(path)


def main() -> None:
    translate_fear_captions(OUT / "sprites/ui/fear_captions.png")
    translate_preloader(OUT / "sprites/ui/preloader.png")
    translate_thumb(OUT / "sharing/thumb.png", OUT / "sharing/thumb_no_words.png")
    translate_intro_logo(OUT / "sprites/intro/intro_logo.png")
    translate_cc0(OUT / "sprites/about/cc0.png")
    translate_replay(OUT / "sprites/about/replay.png")
    translate_youwin(OUT / "sprites/intermission/youwin.png")
    translate_callback(OUT / "sprites/act4/callback.png")
    translate_starring(OUT / "sprites/credits/starring.png")
    translate_thanks(OUT / "sprites/credits/thanks.png")
    translate_screens(OUT / "sprites/credits/screens.png")
    translate_end_message(OUT / "sprites/credits/end_message.png")
    print("Translated 13 images in", OUT)


if __name__ == "__main__":
    main()
