"""Makes small square JPG thumbnails of every fabric PNG.

Usage (run inside the folder that holds your fabric PNGs, i.e. your repo folder):
    pip install pillow
    python make_thumbs.py

It creates a "thumbs" folder with one 256x256 JPG per PNG (center-cropped, not stretched).
Commit and push the thumbs folder along with the rest of the repo.
"""
from pathlib import Path
from PIL import Image

SIZE = 256
out = Path("thumbs")
out.mkdir(exist_ok=True)

for png in sorted(Path(".").glob("*.png")):
    with Image.open(png) as im:
        im = im.convert("RGB")
        side = min(im.size)
        left, top = (im.width - side) // 2, (im.height - side) // 2
        im = im.crop((left, top, left + side, top + side)).resize((SIZE, SIZE), Image.LANCZOS)
        im.save(out / (png.stem + ".jpg"), quality=82, optimize=True)
        print("made", png.stem + ".jpg")
