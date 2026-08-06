from pathlib import Path
from PIL import Image

path = Path('images/couple.jpg')
if not path.exists():
    raise FileNotFoundError(f"Image not found: {path}")

with Image.open(path) as img:
    print('format', img.format)
    print('size', img.size)
    print('mode', img.mode)
    width, height = img.size
    # Crop to a centered square focusing on faces, with a safe margin for both people.
    target_size = min(width, height)
    left = max(0, (width - target_size) // 2)
    top = max(0, (height - target_size) // 2)
    right = left + target_size
    bottom = top + target_size
    cropped = img.crop((left, top, right, bottom))
    out_path = Path('images/couple_cropped.jpg')
    cropped.save(out_path, quality=95)
    print('saved', out_path, 'cropped_size', cropped.size)
