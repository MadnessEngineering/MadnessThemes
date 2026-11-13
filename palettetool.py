#!/usr/bin/env python3
"""palettetool — terminal colours for the `*-colors.json` palettes.

A terminal needs what a UI palette doesn't carry: a foreground, a cursor and
sixteen ANSI colours. This derives them from the palette's own tokens and
stores them as an optional `terminal` block beside `colors`, so a terminal
(Shellomancy) can wear the theme and the values can be hand-tuned afterwards.

    ./palettetool.py terminal                 # print what would be derived
    ./palettetool.py terminal --write         # add `terminal` to palettes lacking one
    ./palettetool.py terminal --write --force # re-derive over existing blocks
    ./palettetool.py check                    # contrast report for stored blocks
    ./palettetool.py preview out.svg          # swatch sheet of every stored block

Derivation, per palette:
  background  the solid first stop of colors.background.main (the --bg-solid rule)
  foreground  colors.text.primary flattened onto the background
  accent      colors.primary; cursor colors.secondary
  chromatic   primary and secondary first, then text.error / success /
              warning / info, each into the ANSI slot nearest its hue (red is
              reserved for text.error: it means errors and deleted lines); empty
              slots take the nearest other palette colour (accent, status,
              tags), else a hue synthesised at the palette's own lightness
              with saturation capped at 0.6
  black/white             tints between background and foreground
  bright      each colour moved away from the background

Then every colour is nudged in lightness until it clears CONTRAST on the
background. A stored block is never touched without --force: once someone has
tuned a palette by hand, the derivation stops having opinions about it.

The `terminal` block is validated by Inventorium's themeContract.js
(`TERMINAL_FLOORS`); keep CONTRAST below in step with it.
"""

import argparse
import colorsys
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ANSI = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]

# Minimum contrast on the terminal background. The contract enforces the same
# floors, minus the margin the derivation aims above them.
CONTRAST = {
    "foreground": 7.0,
    "chromatic": 4.5,    # red..cyan, normal and bright
    "brightBlack": 3.0,  # comments, dim text
    "white": 4.5,        # dark themes: plain white text (light themes: black)
}

HUES = {"red": 0, "yellow": 50, "green": 125, "cyan": 185, "blue": 220, "magenta": 295}


# ── colour maths ──────────────────────────────────────────────────────────

def parse(value):
    """[r, g, b, a] (0-255, alpha 0-1) from #hex / rgb() / rgba() / a gradient's first stop."""
    if not isinstance(value, str):
        return None
    m = re.search(r"#([0-9a-fA-F]{6})\b", value)
    rgba = re.search(r"rgba?\(([^)]+)\)", value)
    if m and (not rgba or m.start() < rgba.start()):
        h = m.group(1)
        return [int(h[i:i + 2], 16) for i in (0, 2, 4)] + [1.0]
    if rgba:
        parts = [p.strip() for p in rgba.group(1).split(",")]
        r, g, b = (float(p) for p in parts[:3])
        a = float(parts[3]) if len(parts) > 3 else 1.0
        return [r, g, b, a]
    return None


def flatten(c, ground):
    a = c[3]
    return tuple(round(c[i] * a + ground[i] * (1 - a)) for i in range(3))


def solid(value, ground=(128, 128, 128)):
    c = parse(value)
    return None if c is None else flatten(c, ground)


def hexof(rgb):
    return "#%02x%02x%02x" % tuple(max(0, min(255, round(v))) for v in rgb)


def luminance(rgb):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def to_hls(rgb):
    return colorsys.rgb_to_hls(*(v / 255 for v in rgb))


def from_hls(h, l, s):
    return tuple(v * 255 for v in colorsys.hls_to_rgb(h, max(0, min(1, l)), max(0, min(1, s))))


def mix(a, b, t):
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(3))


def hue_distance(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


def nearest_slot(hue):
    return min(HUES, key=lambda name: hue_distance(hue, HUES[name]))


def reach(rgb, ground, floor, dark):
    """Move rgb's lightness away from the ground until it clears floor."""
    h, l, s = to_hls(rgb)
    step = 0.01 if dark else -0.01
    out = rgb
    for _ in range(100):
        if contrast(out, ground) >= floor:
            return out
        l += step
        out = from_hls(h, l, s)
    return out


# ── derivation ────────────────────────────────────────────────────────────

def get(obj, path):
    for k in path.split("."):
        if not isinstance(obj, dict):
            return None
        obj = obj.get(k)
    return obj


def candidates(colors, bg):
    """Saturated palette colours, as (rgb, hue°)."""
    paths = ["primary", "secondary", "accent", "success", "warning", "error",
             "text.success", "text.warning", "text.error", "text.info",
             "text.critical", "text.high", "text.medium"]
    for group in ("status", "tags"):
        node = colors.get(group)
        if isinstance(node, dict):
            for k, v in node.items():
                paths.append(f"{group}.{k}.text" if isinstance(v, dict) else f"{group}.{k}")
    out = []
    for p in paths:
        v = get(colors, p)
        if isinstance(v, dict):
            v = v.get("main") or v.get("text")
        rgb = solid(v, bg) if v else None
        if rgb is None:
            continue
        h, l, s = to_hls(rgb)
        if s > 0.35 and 0.2 < l < 0.85:
            out.append((rgb, h * 360))
    return out


def derive(theme):
    colors = theme["colors"]
    dark = theme.get("mode", "dark") == "dark"
    bg = solid(get(colors, "background.main"), (0, 0, 0) if dark else (255, 255, 255))
    fg = reach(solid(get(colors, "text.primary"), bg), bg, CONTRAST["foreground"], dark)
    accent = solid(colors.get("primary"), bg) or fg
    cursor = solid(colors.get("secondary"), bg) or accent

    pool = candidates(colors, bg)
    sats = sorted(to_hls(rgb)[2] for rgb, _ in pool) or [0.7]
    lights = sorted(to_hls(rgb)[1] for rgb, _ in pool) or [0.6]
    sat, light = sats[len(sats) // 2], lights[len(lights) // 2]

    normal = {}
    # A colour serves the ANSI slot whose hue it is nearest, so a cyan-ish
    # "info" never ends up as blue beside a cyan primary. The theme's own
    # primary and secondary claim their slots before the status colours do:
    # they are what makes the terminal look like this theme.
    for path in ("primary", "secondary",
                 "text.error", "text.success", "text.warning", "text.info"):
        rgb = solid(get(colors, path), bg)
        if rgb is None or to_hls(rgb)[2] < 0.35 or not 0.2 < to_hls(rgb)[1] < 0.85:
            continue
        slot = nearest_slot(to_hls(rgb)[0] * 360)
        # Red means errors and deleted lines; only the theme's error colour gets it.
        if slot == "red" and path != "text.error":
            continue
        normal.setdefault(slot, rgb)
    used = set(map(hexof, normal.values()))
    for name in ("red", "yellow", "green", "cyan", "blue", "magenta"):
        if name in normal:
            continue
        near = [(hue_distance(hue, HUES[name]), rgb) for rgb, hue in pool
                if hexof(rgb) not in used and nearest_slot(hue) == name
                and hue_distance(hue, HUES[name]) <= 30]
        if near:
            normal[name] = min(near)[1]
        else:
            # Synthesised: the palette's own lightness, saturation capped so a
            # missing hue reads as part of the theme rather than a neon guest.
            normal[name] = from_hls(HUES[name] / 360, min(0.7, max(0.55, light)), min(0.6, sat))
        used.add(hexof(normal[name]))
    for name in HUES:
        normal[name] = reach(normal[name], bg, CONTRAST["chromatic"], dark)

    if dark:
        normal["black"] = mix(bg, fg, 0.18)
        normal["white"] = reach(mix(bg, fg, 0.78), bg, CONTRAST["white"], dark)
        bright_black = reach(mix(bg, fg, 0.45), bg, CONTRAST["brightBlack"], dark)
        bright_white = fg
    else:
        normal["black"] = fg
        normal["white"] = mix(bg, fg, 0.12)
        bright_black = reach(mix(bg, fg, 0.55), bg, CONTRAST["brightBlack"], dark)
        bright_white = mix(bg, fg, 0.04)

    bright = {"black": bright_black, "white": bright_white}
    for name in HUES:
        h, l, s = to_hls(normal[name])
        moved = from_hls(h, l + (0.12 if dark else -0.12), min(1, s + 0.05))
        bright[name] = reach(moved, bg, CONTRAST["chromatic"], dark)

    return {
        "background": hexof(bg),
        "foreground": hexof(fg),
        "accent": hexof(accent),
        "cursor": hexof(cursor),
        "details": "darker" if dark else "lighter",
        "normal": {k: hexof(normal[k]) for k in ANSI},
        "bright": {k: hexof(bright[k]) for k in ANSI},
    }


# ── checks and preview ────────────────────────────────────────────────────

def problems(block, dark=True):
    """Contrast failures for a stored block, as strings."""
    bg = solid(block["background"])
    out = []

    def need(label, value, floor):
        ratio = contrast(solid(value), bg)
        if ratio < floor:
            out.append(f"{label} {value} is {ratio:.2f}:1, needs {floor}")

    need("foreground", block["foreground"], CONTRAST["foreground"])
    for tier in ("normal", "bright"):
        for name in HUES:
            need(f"{tier}.{name}", block[tier][name], CONTRAST["chromatic"] - 1.5)
    need("bright.black", block["bright"]["black"], CONTRAST["brightBlack"])
    readable = "white" if dark else "black"
    need(f"normal.{readable}", block["normal"][readable], CONTRAST["white"] - 1.5)
    return out


def palettes():
    return sorted(HERE.glob("*-colors.json"))


def load(path):
    return json.loads(path.read_text())


def save(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def cmd_terminal(args):
    for path in palettes():
        data = load(path)
        if "terminal" in data and not args.force:
            print(f"{path.name}: has a terminal block (use --force to re-derive)")
            continue
        block = derive(data)
        if args.write:
            # Keep `terminal` right after `colors` so the file reads top-down.
            ordered = {}
            for k, v in data.items():
                if k != "terminal":
                    ordered[k] = v
                if k == "colors":
                    ordered["terminal"] = block
            save(path, ordered)
        bad = problems(block, data.get("mode", "dark") == "dark")
        flag = "  ! " + "; ".join(bad) if bad else ""
        print(f"{path.name}: bg {block['background']} fg {block['foreground']} "
              f"{' '.join(block['normal'][k] for k in ANSI)}{flag}")


def cmd_check(args):
    failed = 0
    for path in palettes():
        data = load(path)
        block = data.get("terminal")
        if not block:
            print(f"--    {path.name} (no terminal block)")
            continue
        bad = problems(block, data.get("mode", "dark") == "dark")
        print(f"{'FAIL' if bad else 'ok':5} {path.name}")
        for b in bad:
            print(f"        {b}")
        failed += bool(bad)
    return 1 if failed else 0


def cmd_preview(args):
    rows = [(p.stem.replace("-colors", ""), load(p)["terminal"])
            for p in palettes() if "terminal" in load(p)]
    w, rh = 1180, 96
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{rh * len(rows)}" '
           'font-family="Menlo, monospace" font-size="15">']
    for i, (name, t) in enumerate(rows):
        y = i * rh
        svg.append(f'<rect x="0" y="{y}" width="{w}" height="{rh}" fill="{t["background"]}"/>')
        svg.append(f'<text x="14" y="{y + 26}" fill="{t["foreground"]}">{name} '
                   f'<tspan fill="{t["bright"]["black"]}"># {t["background"]}</tspan> '
                   f'<tspan fill="{t["accent"]}">accent</tspan> '
                   f'<tspan fill="{t["cursor"]}">▌cursor</tspan></text>')
        for tier, dy in (("normal", 56), ("bright", 82)):
            for j, k in enumerate(ANSI):
                svg.append(f'<text x="{14 + j * 144}" y="{y + dy}" '
                           f'fill="{t[tier][k]}">{tier[0]}.{k}</text>')
    svg.append("</svg>")
    Path(args.out).write_text("\n".join(svg))
    print(f"wrote {args.out} ({len(rows)} palettes)")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("terminal", help="derive terminal blocks")
    t.add_argument("--write", action="store_true", help="write them into the palettes")
    t.add_argument("--force", action="store_true", help="re-derive existing blocks too")
    t.set_defaults(func=cmd_terminal)
    c = sub.add_parser("check", help="contrast report for stored terminal blocks")
    c.set_defaults(func=cmd_check)
    v = sub.add_parser("preview", help="SVG swatch sheet of stored terminal blocks")
    v.add_argument("out")
    v.set_defaults(func=cmd_preview)
    args = p.parse_args()
    sys.exit(args.func(args) or 0)


if __name__ == "__main__":
    main()
