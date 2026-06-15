#!/usr/bin/env python3
"""
Sync new keys from labops.json to all other theme files.
Labops got new keys added during voice pass that standard + others don't have.
We propagate using the standard.json values as defaults, but first need to
figure out what the standard values should be.

Strategy: For each key in labops that's missing from other themes,
use the labops value as the default for all themes (standard English).
Then debug.json gets key-path strings.
"""
import json, copy, os, subprocess

THEMES_DIR = "/Users/d.edens/lab/madness_interactive/projects/common/Inventorium/src/locales/themes"

# Theme files to update (all except debug which is handled separately, and labops which is source)
THEMES = ["standard", "mad-wizard", "corporate-drone", "corporate-clean", "banana",
          "biomedical", "gunmetal", "labops", "cyan-lab", "dwarf", "templar-light"]
DEBUG_THEME = "debug"

def load(name):
    with open(f"{THEMES_DIR}/{name}.json") as f:
        return json.load(f)

def save(name, data):
    with open(f"{THEMES_DIR}/{name}.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

def flatten(obj, prefix=""):
    result = {}
    for k, v in obj.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            result.update(flatten(v, key))
        else:
            result[key] = v
    return result

def set_nested(obj, key_path, value):
    """Set a value in a nested dict using a dot-separated key path."""
    keys = key_path.split(".")
    current = obj
    for k in keys[:-1]:
        if k not in current or not isinstance(current[k], dict):
            current[k] = {}
        current = current[k]
    if isinstance(current, dict):
        current[keys[-1]] = value

def deep_merge(base, overrides):
    result = copy.deepcopy(base)
    for k, v in overrides.items():
        if isinstance(v, dict) and isinstance(result.get(k), dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result

# Load all themes
themes = {name: load(name) for name in THEMES + [DEBUG_THEME]}

# Flatten all themes to find keys
flat_themes = {name: flatten(data) for name, data in themes.items()}

# Find all unique keys across all themes
all_keys = set()
for flat in flat_themes.values():
    all_keys.update(flat.keys())

print(f"Total unique keys across all themes: {len(all_keys)}")

# Find keys missing from standard.json (these are "new" keys added in labops)
standard_keys = set(flat_themes["standard"].keys())
labops_keys = set(flat_themes["labops"].keys())
new_keys = labops_keys - standard_keys
print(f"Keys in labops not in standard: {len(new_keys)}")

# Also find keys in any theme but not in labops
for name in THEMES + [DEBUG_THEME]:
    missing_from_labops = set(flat_themes[name].keys()) - labops_keys
    if missing_from_labops:
        print(f"Keys in {name} not in labops: {len(missing_from_labops)}")

# For each new key: determine the "standard English" value
# Use the labops value as a starting point, but we should map back to neutral English
# Since the labops voice pass changed values, use the ORIGINAL standard values where possible,
# or a neutral version of the labops value.

# Actually, the right approach: check if these keys exist in check-themes "master".
# The check-themes script uses debug.json as master checklist. Let's see debug.json.
debug_keys = set(flat_themes[DEBUG_THEME].keys())
new_in_labops_not_debug = new_keys - debug_keys
print(f"New labops keys NOT in debug.json: {len(new_in_labops_not_debug)}")
if new_in_labops_not_debug:
    for k in sorted(list(new_in_labops_not_debug))[:20]:
        print(f"  {k}")

# Keys in debug but missing from standard/other themes
missing_from_standard = debug_keys - standard_keys
print(f"\nKeys in debug not in standard: {len(missing_from_standard)}")

# The check-themes says 530 keys are missing from most themes.
# These must be keys that exist in labops (and debug) but not others.
# Find them:
present_in_labops_missing_from_others = {}
for name in THEMES:
    if name == "labops":
        continue
    missing = labops_keys - set(flat_themes[name].keys())
    if missing:
        present_in_labops_missing_from_others[name] = missing

sample_name = next(iter(present_in_labops_missing_from_others))
sample_missing = present_in_labops_missing_from_others[sample_name]
print(f"\nSample: {sample_name} is missing {len(sample_missing)} keys from labops")
for k in sorted(sample_missing)[:10]:
    print(f"  {k} = {flat_themes['labops'].get(k, 'N/A')[:60]}")

# Now propagate: for each theme that's missing keys,
# add those keys using the labops value as a neutral/standard fallback.
# For debug.json: use the key path string as value.

# But wait - we need to map labops-voiced values back to standard English.
# Let's check what value standard.json has for the non-new keys first.
# Better approach: use check-themes to find the master set, then
# for keys only in labops: add them to all other themes with standard English text.

# The labops values are in SRE voice. We need to add neutral values to other themes.
# Since we can't run gemini reliably, use the labops VALUE as a "close enough" default
# for now - these are new keys that other themes didn't have at all.
# Each theme will inherit the labops value (which may be ops-voiced) as a fallback.
# This is not ideal but keeps parity. The other theme voice passes can override later.

# ACTUALLY: re-read the situation. These 530 keys are missing from ALL themes including standard.
# This means they were ONLY added to labops by my voice pass scripts.
# The correct fix: propagate them to all other themes with neutral English values.
# The labops values are ops-voiced; standard should get neutral English.

# Map: labops-voiced -> neutral English (for standard and others)
# We'll use a simple mapping for common transformations, otherwise use as-is.
def neutralize(value):
    """Convert common labops-voiced terms back to neutral English for standard."""
    replacements = [
        ("Querying…", "Loading…"),
        ("Querying...", "Loading..."),
        ("Commit", "Save"),
        ("Committing…", "Saving…"),
        ("Discard", "Cancel"),
        ("Decommission", "Delete"),
        ("Decommissioned", "Deleted"),
        ("Provision", "Create"),
        ("Provisioned", "Created"),
        ("Provisioning", "Creating"),
        ("Ticket", "Todo"),
        ("Tickets", "Todos"),
        ("ticket", "todo"),
        ("tickets", "todos"),
        ("Runbook", "Lesson"),
        ("Runbooks", "Lessons"),
        ("Resync", "Refresh"),
        ("Triage", "Review"),
        ("Resolve", "Complete"),
        ("Resolved", "Completed"),
        ("Operator", "User"),
        ("Deregister", "Remove"),
        ("Topology", "Mind Map"),
        ("Export Snapshot", "Export"),
        ("Run Diagnostics", "AI Insights"),
        ("Diagnostics ready", "Chat ready"),
        ("diagnostic system", "assistant"),
        ("Diagnostic", "AI"),
        ("analytics", "analytics"),
        ("Ops", ""),
    ]
    result = value
    for ops_term, neutral in replacements:
        result = result.replace(ops_term, neutral)
    return result.strip()

# For each missing key in all themes, add it
updates_by_theme = {name: {} for name in THEMES + [DEBUG_THEME]}

for name in THEMES:
    if name == "labops":
        continue
    missing = labops_keys - set(flat_themes[name].keys())
    for key in missing:
        labops_val = flat_themes["labops"][key]
        if name == "standard":
            updates_by_theme[name][key] = neutralize(labops_val)
        else:
            # For voiced themes: use standard (neutral) as fallback - they'll get voiced later
            updates_by_theme[name][key] = neutralize(labops_val)

# Debug gets key-path strings
for key in labops_keys - debug_keys:
    updates_by_theme[DEBUG_THEME][key] = key

# Also handle keys missing from labops that exist in other themes
# (the check said labops is missing 6 umlData keys)
for name in THEMES + [DEBUG_THEME]:
    if name == "labops":
        continue
    missing_from_labops = set(flat_themes[name].keys()) - labops_keys
    for key in missing_from_labops:
        val = flat_themes[name][key]
        updates_by_theme["labops"][key] = val  # carry over to labops

print("\nApplying updates...")
for name in THEMES + [DEBUG_THEME]:
    if not updates_by_theme[name]:
        print(f"  {name}: no changes needed")
        continue
    data = themes[name]
    for key, value in updates_by_theme[name].items():
        set_nested(data, key, value)
    save(name, data)
    print(f"  {name}: added {len(updates_by_theme[name])} keys")

# Validate all
print("\nValidating JSON...")
for name in THEMES + [DEBUG_THEME]:
    r = subprocess.run(["node", "-e", f"require('./{name}.json'); console.log('{name}: valid')"],
                       capture_output=True, text=True, cwd=THEMES_DIR)
    if r.returncode != 0:
        print(f"  ERROR in {name}: {r.stderr[:200]}")
    else:
        print(f"  {r.stdout.strip()}")
