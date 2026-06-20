#!/usr/bin/env python3
"""Generate favicon family + OG image from src/assets/logo.png.

Outputs to public/:
  favicon.ico           multi-resolution (16, 32, 48)
  favicon-16x16.png
  favicon-32x32.png
  apple-touch-icon.png  180x180 (filled bg, no transparency per Apple spec)
  icon-192.png          Android / PWA
  icon-512.png          Android / PWA
  og-image.png          1200x630 social card

Re-run after updating the source logo:  python scripts/generate-favicons.py
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "assets" / "logo.png"
OUT = ROOT / "public"

BG = (0x0A, 0x1F, 0x1D)        # Deep Tech Green-Black
TEXT = (0xF0, 0xF4, 0xF4)      # UI Light Background (as text)
ACCENT = (0x1B, 0xC5, 0xBA)    # Teal Accent

# (filename, size, fill_background)
PNG_SIZES = [
    ("favicon-16x16.png", 16, False),
    ("favicon-32x32.png", 32, False),
    ("icon-192.png", 192, False),
    ("icon-512.png", 512, False),
    ("apple-touch-icon.png", 180, True),  # Apple wants opaque
]

ICO_SIZES = [(16, 16), (32, 32), (48, 48)]


def load_logo() -> Image.Image:
    if not SRC.exists():
        raise SystemExit(f"Source logo not found: {SRC}")
    img = Image.open(SRC).convert("RGBA")
    return img


def make_square(img: Image.Image, size: int, fill_bg: bool) -> Image.Image:
    if fill_bg:
        canvas = Image.new("RGBA", (size, size), BG + (255,))
        resized = img.resize((size, size), Image.LANCZOS)
        canvas.alpha_composite(resized)
        return canvas.convert("RGB")
    return img.resize((size, size), Image.LANCZOS)


def load_font(size: int) -> ImageFont.FreeTypeFont | None:
    candidates = [
        "C:/Windows/Fonts/consolab.ttf",   # Consolas Bold (close to JetBrains Mono)
        "C:/Windows/Fonts/seguibl.ttf",    # Segoe UI Black
        "C:/Windows/Fonts/arialbd.ttf",    # Arial Bold
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return None


def make_og_image(logo: Image.Image) -> Image.Image:
    canvas = Image.new("RGB", (1200, 630), BG)
    draw = ImageDraw.Draw(canvas)

    logo_size = 360
    logo_resized = logo.resize((logo_size, logo_size), Image.LANCZOS)
    logo_x = (1200 - logo_size) // 2
    logo_y = 110
    canvas.paste(logo_resized, (logo_x, logo_y), logo_resized)

    title = "CHELYDRA LABS"
    font = load_font(72)
    if font:
        bbox = draw.textbbox((0, 0), title, font=font)
        text_w = bbox[2] - bbox[0]
        text_x = (1200 - text_w) // 2
        text_y = logo_y + logo_size + 40
        draw.text((text_x, text_y), title, font=font, fill=TEXT)

        sub = "Open-source, engineered."
        sub_font = load_font(28)
        if sub_font:
            bbox2 = draw.textbbox((0, 0), sub, font=sub_font)
            sub_w = bbox2[2] - bbox2[0]
            sub_x = (1200 - sub_w) // 2
            draw.text((sub_x, text_y + 95), sub, font=sub_font, fill=ACCENT)

    return canvas


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    logo = load_logo()
    print(f"Source: {SRC} ({logo.size[0]}x{logo.size[1]})")

    for name, size, fill_bg in PNG_SIZES:
        out = make_square(logo, size, fill_bg)
        path = OUT / name
        out.save(path, "PNG", optimize=True)
        print(f"  wrote {path.relative_to(ROOT)}")

    ico_path = OUT / "favicon.ico"
    ico_img = Image.open(SRC).convert("RGBA")
    ico_img.save(ico_path, format="ICO", sizes=ICO_SIZES)
    print(f"  wrote {ico_path.relative_to(ROOT)} (sizes={ICO_SIZES})")

    og = make_og_image(logo)
    og_path = OUT / "og-image.png"
    og.save(og_path, "PNG", optimize=True)
    print(f"  wrote {og_path.relative_to(ROOT)} (1200x630)")


if __name__ == "__main__":
    main()
