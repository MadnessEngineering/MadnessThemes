#!/usr/bin/env python3
"""themetool — batch edits and parity checks for the theme string files.

One tool instead of a new one-shot script per voice pass. Everything operates on
the `<theme>.json` personality files in this directory; `*-colors.json` palettes
are left alone.

    ./themetool.py worklist mad-wizard          # strings still identical to standard
    ./themetool.py parity                       # missing/extra keys, every theme
    ./themetool.py get labops settings.tabs.profile
    ./themetool.py set labops settings.tabs.profile "Operator"
    ./themetool.py patch labops patches.json    # {"a.b.c": "value", ...}
    ./themetool.py sync labops standard banana  # copy keys labops has that they lack
    ./themetool.py validate                     # parse + shape check

`patch` is the one that replaces the old voice_pass_*.py scripts: put the
dot-path -> string map in a JSON file and apply it, rather than hand-rolling
load/save/set_key again.
"""
import argparse
import copy
import json
import sys
from pathlib import Path

THEMES_DIR = Path(__file__).resolve().parent
BASELINE = "standard"


# --- io -------------------------------------------------------------------

def theme_path(name):
    return THEMES_DIR / f"{name}.json"


def load(name):
    with open(theme_path(name)) as f:
        return json.load(f)


def save(name, data):
    with open(theme_path(name), "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def all_themes():
    """Personality files only — `*-colors.json` palettes are a different shape."""
    return sorted(
        p.stem for p in THEMES_DIR.glob("*.json")
        if not p.stem.endswith("-colors")
    )


# --- dict helpers ---------------------------------------------------------

def flatten(obj, prefix=""):
    out = {}
    for k, v in obj.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            out.update(flatten(v, key))
        else:
            out[key] = v
    return out


def get_key(data, path, default=None):
    cur = data
    for k in path.split("."):
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


def set_key(data, path, value):
    keys = path.split(".")
    cur = data
    for k in keys[:-1]:
        if not isinstance(cur.get(k), dict):
            cur[k] = {}
        cur = cur[k]
    cur[keys[-1]] = value


def deep_merge(base, overrides):
    result = copy.deepcopy(base)
    for k, v in overrides.items():
        if isinstance(v, dict) and isinstance(result.get(k), dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result


# --- commands -------------------------------------------------------------

def cmd_worklist(args):
    """Strings a theme shares verbatim with standard — the unvoiced backlog."""
    base = flatten(load(BASELINE))
    theme = flatten(load(args.theme))
    hits = [
        (k, v) for k, v in theme.items()
        if isinstance(v, str) and v == base.get(k) and len(v) > args.min_len
    ]
    for k, v in hits:
        print(f"{k} = {json.dumps(v, ensure_ascii=False)}")
    print(f"\n{len(hits)} of {len(theme)} keys still match {BASELINE}", file=sys.stderr)


def cmd_parity(args):
    base = flatten(load(BASELINE))
    names = args.themes or [t for t in all_themes() if t != BASELINE]
    worst = 0
    for name in names:
        theme = flatten(load(name))
        missing = sorted(set(base) - set(theme))
        extra = sorted(set(theme) - set(base))
        worst = max(worst, len(missing) + len(extra))
        print(f"{name}: {len(missing)} missing, {len(extra)} extra")
        if args.verbose:
            for k in missing:
                print(f"  - {k}")
            for k in extra:
                print(f"  + {k}")
    return 1 if (args.strict and worst) else 0


def cmd_get(args):
    value = get_key(load(args.theme), args.key)
    if value is None:
        print(f"{args.key}: not set in {args.theme}", file=sys.stderr)
        return 1
    print(json.dumps(value, ensure_ascii=False, indent=2))
    return 0


def cmd_set(args):
    data = load(args.theme)
    set_key(data, args.key, args.value)
    save(args.theme, data)
    print(f"{args.theme}.{args.key} = {json.dumps(args.value, ensure_ascii=False)}")
    return 0


def cmd_patch(args):
    with open(args.patches) as f:
        patches = json.load(f)
    data = load(args.theme)
    added = changed = same = 0
    for path, value in patches.items():
        prev = get_key(data, path)
        if prev is None:
            added += 1
        elif prev != value:
            changed += 1
        else:
            same += 1
        if not args.dry_run:
            set_key(data, path, value)
    if args.dry_run:
        print(f"dry run — {added} new, {changed} changed, {same} unchanged")
        return 0
    save(args.theme, data)
    print(f"{args.theme}.json: {added} new, {changed} changed, {same} unchanged")
    return 0


def cmd_sync(args):
    """Copy keys the source has that a target lacks, using the source's values."""
    src = flatten(load(args.source))
    for name in args.targets:
        data = load(name)
        flat = flatten(data)
        missing = [k for k in src if k not in flat]
        for k in missing:
            set_key(data, k, src[k])
        if missing and not args.dry_run:
            save(name, data)
        verb = "would add" if args.dry_run else "added"
        print(f"{name}: {verb} {len(missing)} keys from {args.source}")
    return 0


def cmd_validate(args):
    failures = 0
    for name in args.themes or all_themes():
        path = theme_path(name)
        try:
            with open(path) as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"{name}: FAIL — {e}")
            failures += 1
            continue
        if not isinstance(data, dict):
            print(f"{name}: FAIL — top level is {type(data).__name__}, expected object")
            failures += 1
            continue
        print(f"{name}: ok ({len(flatten(data))} keys)")
    return 1 if failures else 0


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    w = sub.add_parser("worklist", help="keys still identical to standard.json")
    w.add_argument("theme")
    w.add_argument("--min-len", type=int, default=2,
                   help="skip strings this short or shorter (default: 2)")
    w.set_defaults(func=cmd_worklist)

    pa = sub.add_parser("parity", help="key coverage against standard.json")
    pa.add_argument("themes", nargs="*")
    pa.add_argument("-v", "--verbose", action="store_true")
    pa.add_argument("--strict", action="store_true", help="exit 1 on any drift")
    pa.set_defaults(func=cmd_parity)

    g = sub.add_parser("get", help="read one dot-path key")
    g.add_argument("theme")
    g.add_argument("key")
    g.set_defaults(func=cmd_get)

    s = sub.add_parser("set", help="write one dot-path key")
    s.add_argument("theme")
    s.add_argument("key")
    s.add_argument("value")
    s.set_defaults(func=cmd_set)

    pt = sub.add_parser("patch", help="apply a {dot.path: value} JSON map")
    pt.add_argument("theme")
    pt.add_argument("patches")
    pt.add_argument("-n", "--dry-run", action="store_true")
    pt.set_defaults(func=cmd_patch)

    sy = sub.add_parser("sync", help="propagate missing keys from one theme to others")
    sy.add_argument("source")
    sy.add_argument("targets", nargs="+")
    sy.add_argument("-n", "--dry-run", action="store_true")
    sy.set_defaults(func=cmd_sync)

    v = sub.add_parser("validate", help="parse + shape check")
    v.add_argument("themes", nargs="*")
    v.set_defaults(func=cmd_validate)

    args = p.parse_args()
    sys.exit(args.func(args) or 0)


if __name__ == "__main__":
    main()
