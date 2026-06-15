#!/usr/bin/env python3
"""Sync 16 new keys added by labops5 voice pass to all other themes."""
import json, subprocess

THEMES_DIR = "/Users/d.edens/lab/madness_interactive/projects/common/Inventorium/src/locales/themes"
THEMES = ["standard", "mad-wizard", "corporate-drone", "corporate-clean", "banana",
          "biomedical", "gunmetal", "labops", "cyan-lab", "dwarf", "templar-light", "debug"]

def load(name):
    with open(f"{THEMES_DIR}/{name}.json") as f:
        return json.load(f)

def save(name, data):
    with open(f"{THEMES_DIR}/{name}.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

def set_key(data, path, value):
    keys = path.split(".")
    cur = data
    for k in keys[:-1]:
        if k not in cur or not isinstance(cur[k], dict):
            cur[k] = {}
        cur = cur[k]
    if isinstance(cur, dict):
        cur[keys[-1]] = value

# New keys: neutral English values for most themes
new_keys = {
    "insights.tabs.performance": "Performance",
    "todoDetail.fields.status": "Status",
    "todoDetail.fields.priority": "Priority",
    "todoDetail.fields.project": "Project",
    "questTab.status.active": "Active",
    "questTab.status.completed": "Completed",
    "questTab.status.pending": "Pending",
    "questTab.filters.all": "All",
    "questTab.filters.active": "Active",
    "questTab.filters.completed": "Completed",
    "questTab.empty.title": "No active quests",
    "questTab.empty.action": "Create Quest",
}

# Per-theme overrides (voiced variants)
theme_overrides = {
    "labops": {
        "todoDetail.fields.project": "Service",
        "questTab.status.completed": "Resolved",
        "questTab.filters.completed": "Resolved",
    },
    "templar-light": {
        "todoDetail.fields.project": "Crusade",
        "questTab.status.completed": "Fulfilled",
        "questTab.status.pending": "Outstanding",
        "questTab.filters.completed": "Fulfilled",
        "questTab.empty.action": "Pledge Quest",
    },
    "debug": {
        # debug gets key-path strings
        "insights.tabs.performance": "insights.tabs.performance",
        "todoDetail.fields.status": "todoDetail.fields.status",
        "todoDetail.fields.priority": "todoDetail.fields.priority",
        "todoDetail.fields.project": "todoDetail.fields.project",
        "questTab.status.active": "questTab.status.active",
        "questTab.status.completed": "questTab.status.completed",
        "questTab.status.pending": "questTab.status.pending",
        "questTab.filters.all": "questTab.filters.all",
        "questTab.filters.active": "questTab.filters.active",
        "questTab.filters.completed": "questTab.filters.completed",
        "questTab.empty.title": "questTab.empty.title",
        "questTab.empty.action": "questTab.empty.action",
    },
}

for theme in THEMES:
    data = load(theme)
    # Apply neutral English defaults
    for path, value in new_keys.items():
        set_key(data, path, value)
    # Apply theme-specific overrides
    if theme in theme_overrides:
        for path, value in theme_overrides[theme].items():
            set_key(data, path, value)
    save(theme, data)
    print(f"  {theme}: updated")

# Validate all
print("\nValidating...")
for theme in THEMES:
    r = subprocess.run(
        ["node", "-e", f"require('./{theme}.json'); console.log('{theme}: valid')"],
        capture_output=True, text=True, cwd=THEMES_DIR
    )
    if r.returncode != 0:
        print(f"  ERROR {theme}: {r.stderr[:100]}")
    else:
        print(f"  {r.stdout.strip()}")
