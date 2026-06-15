#!/usr/bin/env python3
"""Templar-light voice pass batch 4 — final meaningful variants from the 241 remainder.

Only patches keys where a genuine templar voice variant exists.
Leaves technical labels, format names, language names, and interpolation-only strings alone.
"""
import json

THEMES_DIR = "/Users/d.edens/lab/madness_interactive/projects/common/Inventorium/src/locales/themes"

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

templar = load("templar-light")

voiced_patches = {
    # todoList — meaningful templar variants
    "todoList.actions.archive": "Seal to Archive",
    "todoList.actions.reopen": "Recall",
    "todoList.actions.unarchive": "Restore",
    "todoList.labels.readOnly": "🔒 Sealed",
    "todoList.timestamps.due": "Due",
    "todoList.loadMore": "Load More",
    "todoList.dropHere": "Drop here",
    "todoList.pagination.all": "All",
    "todoList.dialog.selectAll": "All",
    "todoList.dialog.selectNone": "None",

    # todoEdit
    "todoEdit.fields.dueDate": "Due Date",

    # editableTodoCard — action buttons
    "editableTodoCard.actions.pin": "Pin to Board",
    "editableTodoCard.actions.unpin": "Remove Pin",
    "editableTodoCard.actions.share": "Share",
    "editableTodoCard.fields.dueDate": "Due Date",
    "editableTodoCard.labels.duration": "Duration",
    "editableTodoCard.priority.high": "High",
    "editableTodoCard.priority.medium": "Medium",
    "editableTodoCard.priority.low": "Low",

    # mindMap — moderate flavor
    "mindMap.instructions.dragToMove": "Drag to Reposition",
    "mindMap.instructions.touchAndDrag": "Touch & Reposition",
    "mindMap.filter.selectAll": "Select All",
    "mindMap.filter.clearAll": "Clear All",
    "mindMap.filters.all": "All Nodes",
    "mindMap.layout.radial": "Radial Layout",
    "mindMap.layout.force": "Force Layout",
    "mindMap.layout.grid": "Grid Layout",
    "mindMap.nodeInfo.type": "Type",
    "mindMap.sequence.animateSequence": "Animate Sequence",
    "mindMap.nodes.centerBrain": "⚡ TANGENTRON",
    "mindMap.nodes.centerWorkshop": "🧠 SCRIPTORIUM",
    "mindMap.modes.dynamic": "⚡ Dynamic Mode",
    "mindMap.selection.multipleNodes": "{{count}} nodes selected (Ctrl+Click to add/remove, max 3)",

    # chatAssistant
    "chatAssistant.actions.retry": "Retry",
    "chatAssistant.actions.feedback.good": "Useful",
    "chatAssistant.actions.feedback.bad": "Not Useful",
    "chatAssistant.header.refreshTooltip": "Refresh counsel",
    "chatAssistant.menu.refreshContext": "Refresh Context",

    # warRoom — wartime flavor
    "warRoom.incident.escalate": "Escalate",
    "warRoom.empty.action": "Open Incident",
    "warRoom.filters.active": "Active",
    "warRoom.backgroundImage.opacity": "Opacity",
    "warRoom.backgroundImage.active": "Active",

    # swarmDesk
    "swarmDesk.panels.insights": "Vigil Analytics",
    "swarmDesk.projectPanel.selected": "Active Crusade: {{name}}",
    "swarmDesk.errors.unknownError": "❓ Unknown Anomaly",
    "swarmDesk.controls.rotate": "Rotate",
    "swarmDesk.controls.zoom": "Zoom",
    "swarmDesk.controls.move": "March",
    "swarmDesk.hotkeys.space": "Space: Select",
    "swarmDesk.panels.agent.interface.role": "Role: {{role}}",

    # spells
    "spells.categories.consolidate": "Consolidate",
    "spells.categories.enhance": "Enhance",
    "spells.estimatedTime": "Estimated Time",
    "spells.result.confidence": "Confidence",
    "spells.results.latest": "Latest",
    "spells.history.duration": "Duration:",
    "spells.history.failed": "❌ Unfulfilled",
    "spells.enhanceDescription.result.before": "Before",
    "spells.enhanceDescription.result.after": "After",
    "spells.enhanceDescription.result.improvements": "Improvements",
    "spells.performGeomancy.insights.complexity": "Complexity",
    "spells.performGeomancy.insights.risks": "Risk Factors",

    # admin — mild flavor where appropriate
    "admin.tabs.overview": "Overview",
    "admin.tabs.analytics": "Analytics",
    "admin.analytics.title": "Vigil Analytics",
    "admin.analytics.timeframe.day": "Last 24 Hours",
    "admin.analytics.timeframe.week": "Last 7 Days",
    "admin.analytics.timeframe.month": "Last 30 Days",
    "admin.analytics.timeframe.year": "Last 12 Months",
    "admin.featureFlags.flags.api_access": "API Access",
    "admin.featureFlags.flags.analytics": "Analytics",
    "admin.featureFlags.flags.debug_mode": "Debug Mode",
    "admin.users.columns.actions": "Actions",
    "admin.overview.activeUsers": "Active (7d)",

    # queuePane
    "queuePane.stats.high": "Urgent",
    "queuePane.stats.total": "Queued",
    "queuePane.stats.incoming": "Incoming",

    # settings
    "settings.about.build": "Build",
    "settings.about.version": "Version",
    "settings.account.title": "Account",
    "settings.account.preferences": "Preferences",
    "settings.advanced.debugMode": "Debug Mode",
    "settings.display.density": "Display Density",
    "settings.display.comfortable": "Comfortable",
    "settings.display.compact": "Compact",
    "settings.display.spacious": "Spacious",
    "settings.display.reducedMotion": "Reduce motion",
    "settings.messaging.coreRole": "Core Role",
    "settings.messaging.hidden": "Concealed",
    "settings.messaging.npcCount": "NPC Count",
    "settings.messaging.npcEnabled": "Spawn as SwarmDesk NPC",
    "settings.todoToolbar.share": "Share",
    "settings.todoToolbar.copyJiraCommand": "Copy Jira Command",

    # umlData — mild flavor
    "umlData.empty.hint": "Upload a scroll to behold your code in 3D",
    "umlData.compareVersions": "Compare Versions",
    "umlData.filters.recent": "Recent",
    "umlData.success.restored": "Version restored",
    "umlData.depth": "Analysis Depth",
    "umlData.restore": "Restore Version",
    "umlData.versions": "Versions",
    "umlData.version": "Version",
    "umlData.branch": "Branch",
    "umlData.source.personal": "Personal",
    "umlData.source.shared": "Shared",
    "umlData.actions.view": "View in SwarmDesk",
    "umlData.table.source": "Source",
    "umlData.table.classes": "Classes",
    "umlData.table.packages": "Packages",
    "umlData.table.version": "Version",
    "umlData.table.actions": "Actions",
    "umlData.metadata.size": "Size",
    "umlData.metadata.nodes": "Nodes",
    "umlData.metadata.framework": "Framework",
    "umlData.viewSwarmDesk.redirect": "Opening in SwarmDesk...",

    # success page
    "success.log.session": "Session:",
    "success.log.error": "ERROR:",
    "success.log.verificationFailed": "Verification failed",

    # todoDetail tabs
    "todoDetail.tabs.overview": "Overview",
    "todoDetail.tabs.related": "Related Charges",
    "todoDetail.tabs.coordinates": "Coordinates",

    # misc
    "automationRecipes.tagNormalization.scanned": "Scanned",
    "aiInsights.dialog.deselectAll": "None",
    "questTab.buttons.addChain": "Add Chain",
    "questCard.copiedPrompt": "Copied!",
    "questCard.copiedId": "Copied!",
    "questCard.external": "external",
    "lessonsViewer.neighbors.none": "none",
    "lessonsViewer.references.none": "none",
    "projectNavigator.enterButton.helpText": "Press Enter or #{{number}}",
    "projectSwarmdesk.reviewTab.returnToProgress": "Return to Progress",
    "insights.tabs.overview": "Overview",
    "insights.tabs.analytics": "Analytics",
}

for path, value in voiced_patches.items():
    set_key(templar, path, value)

save("templar-light", templar)
print("templar-light.json written")

import subprocess
r = subprocess.run(
    ["node", "-e", "require('./templar-light.json'); console.log('templar-light: valid')"],
    capture_output=True, text=True, cwd=THEMES_DIR
)
print(r.stdout.strip() or r.stderr.strip())
