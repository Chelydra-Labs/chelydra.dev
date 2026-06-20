#!/usr/bin/env python3
import sys
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "assets" / "logo.png"

def main():
    if not SRC.exists():
        print(f"Error: {SRC} does not exist", file=sys.stderr)
        sys.exit(1)
        
    print(f"Loading {SRC}...")
    img = Image.open(SRC).convert("RGBA")
    width, height = img.size
    
    # We will perform flood fill from the four corners to make the dark background transparent.
    # The background has some noise (values around RGB 15 to 40). A threshold of 55 is safe
    # because the mascot has a bright teal border (#1BC5BA) that will block the fill.
    corners = [
        (0, 0),
        (width - 1, 0),
        (0, height - 1),
        (width - 1, height - 1)
    ]
    
    print("Performing flood fill from corners...")
    for x, y in corners:
        ImageDraw.floodfill(img, (x, y), (0, 0, 0, 0), thresh=55)
        
    # Also check if we should clear the bottom/top middle edge points just in case of non-contiguous noise blocks
    additional_seeds = [
        (width // 2, 0),
        (width // 2, height - 1),
        (0, height // 2),
        (width - 1, height // 2)
    ]
    for x, y in additional_seeds:
        # Check if the pixel is still somewhat opaque and dark
        pixel = img.getpixel((x, y))
        if pixel[3] > 0 and sum(pixel[:3]) / 3 < 50:
            ImageDraw.floodfill(img, (x, y), (0, 0, 0, 0), thresh=55)
            
    print("Saving transparent logo...")
    img.save(SRC, "PNG")
    print("Success!")

if __name__ == "__main__":
    main()
