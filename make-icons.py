"""Generate PWA icons for simp-timer. One-shot; re-run to refresh."""
from PIL import Image, ImageDraw
from pathlib import Path

OUT = Path(__file__).parent / "icons"
OUT.mkdir(exist_ok=True)

BG = (11, 13, 16)        # var(--bg)
ACCENT = (76, 217, 164)  # var(--accent)
DIM = (138, 148, 163)    # var(--muted)


def draw_icon(size: int, rounded: bool = True) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # Rounded-square background (or full square for apple-touch — iOS masks anyway).
    radius = int(size * 0.22) if rounded else 0
    if rounded:
        d.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=BG)
    else:
        d.rectangle([0, 0, size - 1, size - 1], fill=BG)

    cx, cy = size / 2, size / 2 + size * 0.04  # nudge down for crown

    # Stopwatch crown (top button).
    crown_w = size * 0.16
    crown_h = size * 0.06
    d.rounded_rectangle(
        [cx - crown_w / 2, cy - size * 0.42, cx + crown_w / 2, cy - size * 0.42 + crown_h],
        radius=int(crown_h / 2),
        fill=ACCENT,
    )

    # Face ring.
    r_out = size * 0.34
    ring = max(2, int(size * 0.05))
    d.ellipse(
        [cx - r_out, cy - r_out, cx + r_out, cy + r_out],
        outline=ACCENT,
        width=ring,
    )

    # Tick at 12.
    tick_w = max(2, int(size * 0.025))
    d.rectangle(
        [cx - tick_w / 2, cy - r_out + ring + size * 0.02,
         cx + tick_w / 2, cy - r_out + ring + size * 0.08],
        fill=ACCENT,
    )

    # Hand pointing to ~1 o'clock — gives the "running" feel.
    import math
    angle = math.radians(-60)  # 0 = up, negative = clockwise
    hand_len = r_out * 0.78
    hx = cx + math.sin(angle) * hand_len
    hy = cy - math.cos(angle) * hand_len
    hw = max(3, int(size * 0.04))
    d.line([(cx, cy), (hx, hy)], fill=ACCENT, width=hw)

    # Center dot.
    dot = max(3, int(size * 0.045))
    d.ellipse([cx - dot, cy - dot, cx + dot, cy + dot], fill=BG)
    d.ellipse([cx - dot, cy - dot, cx + dot, cy + dot], outline=ACCENT, width=max(2, int(size * 0.02)))

    return img


def main():
    # Manifest icons (Android / PWA installs)
    for size in (192, 512):
        img = draw_icon(size, rounded=True)
        path = OUT / f"icon-{size}.png"
        img.save(path, "PNG")
        print(f"wrote {path}")

    # Apple touch icon — iOS rounds the corners itself, use full-bleed square.
    apple = draw_icon(180, rounded=False)
    apple_path = OUT / "apple-touch-icon.png"
    apple.save(apple_path, "PNG")
    print(f"wrote {apple_path}")

    # Favicon — tiny, still readable.
    fav = draw_icon(64, rounded=True)
    fav_path = OUT / "favicon.png"
    fav.save(fav_path, "PNG")
    print(f"wrote {fav_path}")


if __name__ == "__main__":
    main()
