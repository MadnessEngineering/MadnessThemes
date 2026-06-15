#!/usr/bin/env python3
"""Templar-light voice pass batch 3 — targeted fixes for remaining 274 identical keys.

Many are truly untranslatable (language names, format types, technical labels).
This script only touches ones with meaningful templar-voice alternatives.
"""
import json, copy

THEMES_DIR = "/Users/d.edens/lab/madness_interactive/projects/common/Inventorium/src/locales/themes"

def load(name):
    with open(f"{THEMES_DIR}/{name}.json") as f:
        return json.load(f)

def save(name, data):
    with open(f"{THEMES_DIR}/{name}.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

def set_key(data, path, value):
    """Set a value at a dot-path in nested dict."""
    keys = path.split(".")
    cur = data
    for k in keys[:-1]:
        if k not in cur or not isinstance(cur[k], dict):
            cur[k] = {}
        cur = cur[k]
    if isinstance(cur, dict):
        cur[keys[-1]] = value

templar = load("templar-light")

# Direct key-path patches
patches = {
    # todoList — status/filter synonyms where we can do better
    "todoList.filters.inProgress": "Under Arms",
    "todoList.filters.in_progress": "Under Arms",
    "todoList.project.clearAll": "Clear all",   # keep — no good templar synonym
    "todoList.project.change": "Transfer",
    "todoList.pagination.show": "Display",
    "todoList.pagination.all": "All",
    "todoList.results.matching": " matching \"{{searchText}}\"",  # keep — interpolated
    "todoList.buttons.share": "Share",           # keep — action verb
    "todoList.menu.share": "Share",
    "todoList.dialog.exportFormat": "Format",    # keep — technical label
    "todoList.dialog.variantJSONL": "JSON Lines (Stream)",  # technical
    "todoList.dialog.variantStandard": "Standard",
    "todoList.dialog.variantExcel": "Excel-Optimized",
    "todoList.dialog.variantTable": "Table View",
    "todoList.dialog.selectFields": "Choose Fields",
    "todoList.dialog.renameFields": "Rename Fields",
    "todoList.dialog.calculatedFields": "Computed Fields",
    "todoList.dialog.fieldName": "Field Name",
    "todoList.dialog.addCalculatedField": "Add Computed Field",
    "todoList.dialog.formula.ageInDays": "Age (days)",
    "todoList.dialog.formula.charCount": "Character count",
    "todoList.dialog.formula.tokenEstimate": "Token estimate",
    "todoList.dialog.selectAll": "All",
    "todoList.dialog.selectNone": "None",
    "todoList.dialog.dateRange": "Date Range",
    "todoList.dialog.startDate": "From",
    "todoList.priority.high": "High",
    "todoList.priority.medium": "Medium",
    "todoList.priority.low": "Low",
    "todoList.status.in_progress": "Under Arms",
    "todoList.status.inProgress": "Under Arms",
    "todoList.fields.target": "Target",
    "todoList.fields.source": "Source",
    "todoList.fields.duration": "Duration",
    "todoList.fields.duration_sec": "Duration (seconds)",
    "todoList.fields.complexity": "Complexity",
    "todoList.fields.confidence": "Confidence",
    "todoList.fields.phase": "Phase",
    "todoList.error.unknownError": "Unknown error",
    "todoList.labels.readOnly": "🔒 Read-Only",
    "todoList.actions.archive": "Archive",
    "todoList.actions.reopen": "Reopen",
    "todoList.actions.unarchive": "Restore",
    "todoList.timestamps.due": "Due",
    "todoList.selected": "{{count}} selected",
    "todoList.selectAll": "Select All",
    "todoList.assignee.none": "Unsworn",
    "todoList.assignee.change": "Reassign",
    "todoList.deselectAll": "Deselect All",
    "todoList.loadMore": "Load More",
    "todoList.dropHere": "Drop here",

    # todoEdit
    "todoEdit.fields.dueDate": "Due Date",

    # settings — technical/neutral ones that must stay plain
    "settings.import.error": "Import failed: {{error}}",
    "settings.todoToolbar.copyJiraCommand": "Copy Jira Command",
    "settings.todoToolbar.share": "Share",
    "settings.swarmdesk.orbitalTitle": "Orbital Mode (O key)",
    "settings.swarmdesk.orbitalBaseSpeed": "Base Speed",
    "settings.swarmdesk.orbitalSprintMultiplier": "Sprint Multiplier (Ctrl held)",
    "settings.swarmdesk.fpsTitle": "FPS Mode (F key)",
    "settings.messaging.addRole": "Enlist Role",
    "settings.messaging.roleIdHelper": "Lowercase, alphanumeric, and hyphens only (e.g., 'gpt-4', 'custom-ai')",
    "settings.messaging.coreRole": "Core Role",
    "settings.messaging.hidden": "Hidden",
    "settings.messaging.npcEnabled": "Spawn as SwarmDesk NPC",
    "settings.messaging.npcCount": "NPC Count",
    "settings.messaging.npcCountHelper": "Choose how many clones of this role should appear in SwarmDesk (0-5).",
    "settings.messaging.npcColorHelper": "Used for the NPC body glow and sidebar identity color.",
    "settings.messaging.npcRole": "NPC Role Title",
    "settings.messaging.npcPersonalityHelper": "Controls the default vibe and fallback dialogue for this NPC.",
    "settings.account.title": "Account",
    "settings.account.preferences": "Preferences",
    "settings.about.build": "Build",
    "settings.about.version": "Version",
    "settings.ai.maxTokens": "Max Tokens",
    "settings.display.reducedMotion": "Reduce motion",
    "settings.display.spacious": "Spacious",
    "settings.display.density": "Display Density",
    "settings.display.comfortable": "Comfortable",
    "settings.display.compact": "Compact",
    "settings.advanced.debugMode": "Debug Mode",

    # umlData — mostly technical
    "umlData.viewSwarmDesk.redirect": "Opening in SwarmDesk...",
    "umlData.source.personal": "Personal",
    "umlData.source.shared": "Shared",
    "umlData.table.version": "Version",
    "umlData.table.source": "Source",
    "umlData.table.classes": "Classes",
    "umlData.table.packages": "Packages",
    "umlData.table.actions": "Actions",
    "umlData.actions.view": "View in SwarmDesk",
    "umlData.empty.hint": "Upload a scroll to behold your code in 3D",
    "umlData.compareVersions": "Compare Versions",
    "umlData.filters.recent": "Recent",
    "umlData.success.restored": "Version restored",
    "umlData.metadata.size": "Size",
    "umlData.metadata.nodes": "Nodes",
    "umlData.metadata.framework": "Framework",
    "umlData.versions": "Versions",
    "umlData.depth": "Analysis Depth",
    "umlData.restore": "Restore Version",
    "umlData.branch": "Branch",
    "umlData.repoUrl": "Repository URL",
    "umlData.version": "Version",

    # editableTodoCard
    "editableTodoCard.labels.duration": "Duration",
    "editableTodoCard.labels.enhance": "Invoke",
    "editableTodoCard.labels.enhancing": "Invoking...",
    "editableTodoCard.priority.low": "Low",
    "editableTodoCard.priority.medium": "Medium",
    "editableTodoCard.priority.high": "High",
    "editableTodoCard.status.in_progress": "Under Arms",
    "editableTodoCard.status.initial": "Forming",
    "editableTodoCard.status.inProgress": "Under Arms",
    "editableTodoCard.actions.share": "Share",
    "editableTodoCard.actions.unpin": "Unpin",
    "editableTodoCard.actions.pin": "Pin",
    "editableTodoCard.fields.dueDate": "Due Date",

    # mindMap
    "mindMap.controls.switchToSphere": "Switch to Orb",
    "mindMap.info.nodeCount": "{{count}} Nodes",
    "mindMap.instructions.dragToMove": "Drag to Move",
    "mindMap.instructions.touchAndDrag": "Touch & Drag",
    "mindMap.instructions.doubleTapBurst": "Double-tap for burst!",
    "mindMap.instructions.doubleTapPhysics": "Double-tap for physics!",
    "mindMap.filter.selectAll": "Select All",
    "mindMap.filter.clearAll": "Clear All",
    "mindMap.tooltips.disableStaticMode": "Disable Static Mode",
    "mindMap.tooltips.enableStaticMode": "Enable Static Mode",
    "mindMap.sequence.animateSequence": "Animate Sequence",
    "mindMap.sequence.shuffleSequence": "Vary Sequence",
    "mindMap.selection.multipleNodes": "{{count}} nodes selected (Ctrl+Click to add/remove, max 3)",
    "mindMap.nodes.centerBrain": "⚡ TANGENTRON",
    "mindMap.nodes.centerWorkshop": "🧠 WORKSHOP",
    "mindMap.modes.dynamic": "⚡ Dynamic Mode",
    "mindMap.modes.static": "📖 Scriptorium Mode",
    "mindMap.dialog.nodeText": "Node Inscription",
    "mindMap.nodeInfo.type": "Type",
    "mindMap.filters.all": "All Nodes",
    "mindMap.layout.radial": "Radial Layout",
    "mindMap.layout.force": "Force Layout",
    "mindMap.layout.tree": "Hierarchy Layout",
    "mindMap.layout.grid": "Grid Layout",
    "mindMap.addNode": "Inscribe Node",

    # chatAssistant
    "chatAssistant.suggestedActions.newHighPrio": "New High Prio",
    "chatAssistant.header.refreshTooltip": "Refresh context",
    "chatAssistant.header.settingsTooltip": "Settings",
    "chatAssistant.menu.refreshContext": "Refresh Context",
    "chatAssistant.actions.feedback.bad": "Not Useful",
    "chatAssistant.actions.feedback.good": "Useful",
    "chatAssistant.actions.retry": "Retry",

    # warRoom
    "warRoom.backgroundImage.opacity": "Opacity",
    "warRoom.backgroundImage.fitMode": "Fit Mode",
    "warRoom.backgroundImage.fitCover": "Cover",
    "warRoom.backgroundImage.fitContain": "Contain",
    "warRoom.backgroundImage.fitStretch": "Stretch",
    "warRoom.backgroundImage.fitTile": "Tile",
    "warRoom.backgroundImage.blendWithTerrain": "Blend with Terrain",
    "warRoom.backgroundImage.active": "Active",
    "warRoom.backgroundImage.uploadError": "Upload failed. Please try again.",
    "warRoom.incident.escalate": "Escalate",
    "warRoom.empty.action": "Open Incident",
    "warRoom.filters.active": "Active",

    # swarmDesk
    "swarmDesk.panels.shortcuts.categories.actions.title": "⚔️ Commands",
    "swarmDesk.panels.mcp.debug.authentication": "Authentication: {{status}}",
    "swarmDesk.panels.mcp.debug.apiService": "API Service: {{status}}",
    "swarmDesk.panels.agent.interface.role": "Role: {{role}}",
    "swarmDesk.panels.webllm.compatibility.checkCompatibility": "🔍 Check Compatibility",
    "swarmDesk.panels.webllm.settings.maxTokens": "Max Tokens:",
    "swarmDesk.panels.mqtt.logs.lastMessage": "Last: {{time}}",
    "swarmDesk.panels.mqtt.settings.showTimestamps": "Show timestamps",
    "swarmDesk.panels.insights": "Analytics",
    "swarmDesk.projectData.swarmDesk.visibility": "public repository",
    "swarmDesk.projectData.inventorium.title": "📦 Inventorium",
    "swarmDesk.projectData.swarmonomicon.title": "🐝 Swarmonomicon",
    "swarmDesk.projectData.swarmonomicon.visibility": "public repository",
    "swarmDesk.errors.permissionDenied": "🔒 Access Sealed",
    "swarmDesk.errors.unknownError": "❓ Unknown Error",
    "swarmDesk.controls.zoom": "Zoom",
    "swarmDesk.controls.rotate": "Rotate",
    "swarmDesk.controls.move": "March",
    "swarmDesk.projectPanel.selected": "Active: {{name}}",
    "swarmDesk.hotkeys.space": "Space: Select",
    "swarmDesk.hotkeys.wasd": "WASD: March",
    "swarmDesk.filters.inProgress": "Under Arms",

    # spells
    "spells.results.geomancy.patterns": "Pattern analysis:",
    "spells.results.latest": "Latest",
    "spells.history.result": "Outcome:",
    "spells.history.success": "✅ Fulfilled",
    "spells.history.failed": "❌ Failed",
    "spells.history.duration": "Duration:",
    "spells.accessDenied.title": "Access Sealed",
    "spells.estimatedTime": "Estimated Time",
    "spells.result.confidence": "Confidence",
    "spells.enhanceDescription.result.before": "Before",
    "spells.enhanceDescription.result.after": "After",
    "spells.enhanceDescription.result.improvements": "Improvements",
    "spells.performGeomancy.insights.complexity": "Complexity",
    "spells.performGeomancy.insights.duration": "Estimated Duration",
    "spells.performGeomancy.insights.risks": "Risk Factors",
    "spells.categories.consolidate": "Consolidate",
    "spells.categories.enhance": "Enhance",

    # insights — generic tabs
    "insights.tabs.overview": "Overview",
    "insights.tabs.analytics": "Analytics",

    # admin — keep mostly neutral as it's an admin interface
    "admin.tabs.overview": "Overview",
    "admin.tabs.analytics": "Analytics",
    "admin.overview.fallback": "(showing mock data for development)",
    "admin.overview.activeUsers": "Active (7d)",
    "admin.analytics.title": "Advanced Analytics",
    "admin.analytics.timeframe.day": "Last 24 Hours",
    "admin.analytics.timeframe.week": "Last 7 Days",
    "admin.analytics.timeframe.month": "Last 30 Days",
    "admin.analytics.timeframe.year": "Last 12 Months",
    "admin.logs.fallback": "(showing mock data for development)",
    "admin.logs.columns.timestamp": "Time",
    "admin.logs.columns.level": "Level",
    "admin.logs.severity.error": "ERROR",
    "admin.logs.severity.warning": "WARNING",
    "admin.logs.severity.info": "INFO",
    "admin.featureFlags.fallback": "(showing mock data for development)",
    "admin.featureFlags.flags.api_access": "API Access",
    "admin.featureFlags.flags.analytics": "Analytics",
    "admin.featureFlags.flags.debug_mode": "Debug Mode",
    "admin.users.fallback": "(showing mock data for development)",
    "admin.users.filtered": "filtered from",
    "admin.users.columns.actions": "Actions",

    # queuePane
    "queuePane.incoming.title": "Dispatches",
    "queuePane.stats.total": "Queued",
    "queuePane.stats.high": "Urgent",
    "queuePane.stats.incoming": "Incoming",

    # onboarding
    "onboarding.colors.chipText": "#ffffff",
    "onboarding.steps.add-todo.step1": "Click the floating '+' button again",
    "onboarding.steps.swarmdesk.features.interactive": "Interactive navigation",
    "onboarding.steps.swarmdesk.features.architecture": "Architecture overview",
    "onboarding.steps.swarmdesk.features.dependencies": "Dependency mapping",

    # swarmdesk (lowercase alias)
    "swarmdesk.controls.rotate": "Rotate",
    "swarmdesk.controls.zoom": "Zoom",

    # success
    "success.status.error.title": "RITE FAILED",
    "success.log.session": "Session:",
    "success.log.error": "ERROR:",
    "success.log.verificationFailed": "Verification failed",

    # targetAgent
    "targetAgent.none": "Unsworn",

    # todoDetail
    "todoDetail.tabs.overview": "Overview",
    "todoDetail.tabs.related": "Related",
    "todoDetail.tabs.coordinates": "Coordinates",

    # automationRecipes
    "automationRecipes.tagNormalization.scanned": "Scanned",

    # aiInsights
    "aiInsights.dialog.deselectAll": "None",

    # lessonsViewer
    "lessonsViewer.neighbors.none": "none",
    "lessonsViewer.references.none": "none",

    # questTab
    "questTab.buttons.addChain": "Add Chain",

    # questCard
    "questCard.external": "external",
    "questCard.copiedPrompt": "Copied!",
    "questCard.copiedId": "Copied!",

    # projectNavigator
    "projectNavigator.enterButton.helpText": "Press Enter or #{{number}}",

    # projectSwarmdesk
    "projectSwarmdesk.reviewTab.returnToProgress": "Return to Progress",

    # lessonsLearned — language names are untranslatable
    "lessonsLearned.languages.javascript": "JavaScript",
    "lessonsLearned.languages.typescript": "TypeScript",
    "lessonsLearned.languages.python": "Python",
    "lessonsLearned.languages.rust": "Rust",
    "lessonsLearned.languages.general": "General",
    "lessonsLearned.filters.recent": "Recent (7 days)",
}

for path, value in patches.items():
    set_key(templar, path, value)

save("templar-light", templar)
print("templar-light.json written")

import subprocess
r = subprocess.run(
    ["node", "-e", "require('./templar-light.json'); console.log('templar-light: valid')"],
    capture_output=True, text=True, cwd=THEMES_DIR
)
print(r.stdout.strip() or r.stderr.strip())
