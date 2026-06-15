#!/usr/bin/env python3
"""Fix structural mismatches between labops and other themes."""
import json, copy, subprocess

THEMES_DIR = "/Users/d.edens/lab/madness_interactive/projects/common/Inventorium/src/locales/themes"

def load(name):
    with open(f"{THEMES_DIR}/{name}.json") as f:
        return json.load(f)

def save(name, data):
    with open(f"{THEMES_DIR}/{name}.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

# Fix labops: umlData.upload should be a string, umlData.empty should be an object,
# editableTodoCard.confirmDelete should be an object
labops = load("labops")

# Fix umlData.upload (should be string "Upload Map")
if isinstance(labops.get("umlData", {}).get("upload"), dict):
    labops["umlData"]["upload"] = "Upload Map"

# Fix umlData.empty (should be object with title/message/action)
if isinstance(labops.get("umlData", {}).get("empty"), str):
    labops["umlData"]["empty"] = {
        "title": "No code maps on record",
        "message": "Generate a code map to visualize project architecture.",
        "action": "Generate First Map"
    }

# Fix editableTodoCard.confirmDelete (should be object)
if isinstance(labops.get("editableTodoCard", {}).get("confirmDelete"), str):
    labops["editableTodoCard"]["confirmDelete"] = {
        "title": "Decommission Ticket",
        "message": "Decommission this ticket? This cannot be undone.",
        "confirm": "Decommission",
        "cancel": "Discard"
    }

save("labops", labops)
print("labops fixed")

# Fix templar-light similarly if needed
templar = load("templar-light")
if isinstance(templar.get("umlData", {}).get("upload"), dict):
    templar["umlData"]["upload"] = "Upload Map"
if isinstance(templar.get("umlData", {}).get("empty"), str):
    templar["umlData"]["empty"] = {
        "title": "No code maps on record",
        "message": "Generate a code map to visualize project architecture.",
        "action": "Generate First Map"
    }
if isinstance(templar.get("editableTodoCard", {}).get("confirmDelete"), str):
    templar["editableTodoCard"]["confirmDelete"] = {
        "title": "Expunge Record",
        "message": "Expunge this charge from the record? This cannot be undone.",
        "confirm": "Expunge",
        "cancel": "Withdraw"
    }
save("templar-light", templar)
print("templar-light fixed")

# Now fix the umlData.upload.* keys that check-themes sees in the master
# but not in other themes. Let's check which theme has the upload sub-keys.
# check-themes complains about umlData.upload.button etc - these must be in debug.json
debug = load("debug")
print("debug umlData.upload:", json.dumps(debug.get("umlData", {}).get("upload")))

# If debug has upload as an object, we need all themes to have the same structure
# But standard has it as a string - this is a structural conflict.
# The right fix: check-themes uses the UNION of all keys. If debug has upload.button
# as a key-path string, other themes need it too OR debug needs to match standard.

# For now, if debug.umlData.upload is an object, convert to match standard (string)
if isinstance(debug.get("umlData", {}).get("upload"), dict):
    debug["umlData"]["upload"] = "umlData.upload"
    save("debug", debug)
    print("debug umlData.upload fixed to string")

# Validate all
for name in ["labops", "templar-light", "debug"]:
    r = subprocess.run(["node", "-e", f"require('./{name}.json'); console.log('{name}: valid')"],
                       capture_output=True, text=True, cwd=THEMES_DIR)
    print(r.stdout.strip() or r.stderr.strip())
