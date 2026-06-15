#!/usr/bin/env python3
"""
Voice pass for labops.json — SRE/ops persona per VOICE_GUIDE.
Lexicon: save=Commit, cancel=Discard, delete=Decommission, loading=Querying…,
create=Provision, edit-panel=Reconfigure, edit-todo=Edit Ticket,
refresh=Resync, search=Query, export=Export Snapshot, complete=Resolve,
close=Dismiss, review=Triage, AI=Run Diagnostics
Noun-map: Console=panel/form, Ticket=todo, Queue=ordered work, Datastore=data layer
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

def deep_merge(base, overrides):
    result = copy.deepcopy(base)
    for k, v in overrides.items():
        if isinstance(v, dict) and isinstance(result.get(k), dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result

labops = load("labops")

overrides = {
  "desktop": {
    "commitTo": "Commit to {branch}",
    "amend": "Amend last commit",
    "committing": "Committing…",
    "fetch": "Fetch origin",
    "publishBranch": "Publish branch",
    "fetching": "Fetching…",
    "pushing": "Pushing…",
    "pulling": "Pulling…",
    "newBranch": "New branch",
    "deleteBranch": "Decommission branch",
    "renameBranch": "Rename branch",
    "switchBranch": "Switch branch",
    "branchName": "Branch name",
    "noBranches": "No branches on record",
    "discardChanges": "Discard changes",
    "discardAll": "Discard all changes",
    "stashChanges": "Stash changes",
    "cloneRepository": "Clone repository",
    "addRepository": "Register repository",
    "removeRepository": "Deregister repository",
    "openInTerminal": "Open terminal session",
    "viewOnGitHub": "View on GitHub",
    "noHistory": "No commit history",
    "resolveConflicts": "Resolve conflicts",
    "abortMerge": "Abort merge",
    "continueRebase": "Continue rebase",
    "abortRebase": "Abort rebase",
    "cancel": "Discard",
    "discard": "Discard",
    "continue": "Continue",
    "dismiss": "Dismiss"
  },
  "tabs": {
    "sessions": "Sessions"
  },
  # validation stays plain per Part A
  "common": {
    "confirm": "Confirm",
    "collapse": "Collapse",
    "expand": "Expand",
    "dismiss": "Dismiss"
  },
  "forms": {
    "name": "Project Name",
    "displayName": "Display Name",
    "description": "Description",
    "type": "Project Type",
    "visibility": "Visibility",
    "repository": "Repository",
    "language": "Language",
    "framework": "Framework",
    "priority": "Priority",
    "status": "Status",
    "notes": "Notes",
    "ticket": "Ticket"
  },
  "dashboard": {
    "activityLog": {
      "title": "📊 Ops Event Log",
      "collection": "event_logs collection",
      "description": "Telemetry stream — all ticket state changes and ops events",
      "updates": "Updates",
      "creates": "Provisions",
      "deletes": "Decommissions",
      "completions": "Resolutions",
      "totalEntries": "Total Events"
    },
    "recentlyCompleted": {
      "title": "✅ Recently Resolved"
    },
    "filters": {
      "allActivity": "All Events",
      "todosCreated": "Tickets Opened",
      "todosUpdated": "Tickets Updated",
      "todosCompleted": "Tickets Resolved",
      "todosDeleted": "Tickets Decommissioned",
      "projectsCreated": "Projects Provisioned",
      "projectsUpdated": "Projects Updated",
      "projectsDeleted": "Projects Decommissioned"
    },
    "unifiedView": "Unified View",
    "personalView": "Personal View",
    "showingAllDatabases": "Querying all datastores",
    "showingPersonalOnly": "Showing personal queue only",
    "filteredByProject": "Filtered by project",
    "noLogsFound": "No events in telemetry log",
    "tryChangingFilter": "Adjust filter parameters",
    "startCreatingTodos": "Open your first ticket to begin",
    "failedToLoad": "Query failed: {{error}}",
    "changesMade": "Changes committed",
    "completionNotes": "Resolution notes",
    "revertOperation": "Roll back {{operation}}",
    "revertSuccess": "{{operation}} rolled back successfully",
    "revertFailed": "Roll back failed: {{error}}",
    "revertDeleteNotSupported": "Reverting decommission ops is not supported",
    "revertNotSupported": "Roll back not supported for {{operation}}",
    "confirmRevert": "Confirm Roll Back",
    "confirmRevertMessage": "Roll back {{operation}} on {{description}}?",
    "confirmRevertAction": "Roll Back",
    "operationType": "Event Type",
    "taskDescription": "Ticket Description",
    "descriptions": {
      "projectCreated": "Project provisioned: {{projectName}}",
      "projectUpdated": "Project updated: {{projectName}}",
      "projectDeleted": "Project decommissioned: {{projectName}}",
      "projectModified": "Project reconfigured: {{projectName}}",
      "unknownTask": "Unknown event"
    },
    "showingPageStats": "Page {{currentPage}} of {{totalPages}} ({{totalCount}} events)",
    "autoRefreshingInterval": "Auto-syncing every 30 seconds",
    "stats": {
      "totalProjects": "Total Projects",
      "activeProjects": "Active Projects",
      "completedTodos": "Resolved Tickets",
      "archivedProjects": "Archived Projects"
    },
    "recentActivity": "Recent Events"
  },
  "activityLog": {
    "title": "📋 Ops Event Log",
    "autoRefreshOn": "Auto-sync ON",
    "autoRefreshOff": "Auto-sync OFF",
    "filters": {
      "allActivity": "All Events",
      "todosCreated": "Tickets Opened",
      "todosUpdated": "Tickets Updated",
      "todosCompleted": "Tickets Resolved",
      "todosDeleted": "Tickets Decommissioned",
      "projectsCreated": "Projects Provisioned",
      "projectsUpdated": "Projects Updated",
      "projectsDeleted": "Projects Decommissioned",
      "all": "All Events",
      "create": "Opened",
      "update": "Updated",
      "complete": "Resolved",
      "delete": "Decommissioned"
    },
    "unifiedView": "🌐 Unified View",
    "personalView": "👤 Personal View",
    "showingAllDatabases": "Querying all datastores",
    "showingPersonalOnly": "Showing your personal queue only",
    "filteredByProject": "Filtered by project:",
    "noLogsFound": "No events in telemetry log",
    "tryChangingFilter": "Adjust filter parameters",
    "startCreatingTodos": "Open a ticket to begin generating telemetry",
    "failedToLoad": "Query failed: {{error}}",
    "changesMade": "Changes committed:",
    "completionNotes": "Resolution notes:",
    "revertOperation": "Roll back {{operation}}",
    "revertSuccess": "{{operation}} rolled back successfully",
    "revertFailed": "Roll back failed: {{error}}",
    "revertDeleteNotSupported": "Cannot roll back decommission — resource is gone",
    "revertNotSupported": "Roll back not supported for {{operation}}",
    "confirmRevert": "Confirm Roll Back",
    "confirmRevertMessage": "Roll back {{operation}} on: {{description}}?",
    "confirmRevertAction": "Roll Back",
    "operationType": "Event Type",
    "taskDescription": "Ticket Description",
    "descriptions": {
      "projectCreated": "Project \"{{projectName}}\" provisioned",
      "projectUpdated": "Project \"{{projectName}}\" updated",
      "projectDeleted": "Project \"{{projectName}}\" decommissioned",
      "projectModified": "Project \"{{projectName}}\" reconfigured",
      "unknownTask": "Unknown event"
    },
    "showingPageStats": "Page {{currentPage}} of {{totalPages}} ({{totalCount}} total events)",
    "autoRefreshingInterval": " • Auto-syncing every 30s",
    "emptyState": {
      "title": "Queue clear",
      "message": "No events recorded yet. Open a ticket to begin."
    },
    "events": {
      "created": "opened",
      "updated": "updated",
      "completed": "resolved",
      "deleted": "decommissioned"
    },
    "ago": "ago",
    "stats": {
      "total": "Total Events",
      "today": "Today",
      "thisWeek": "This Week"
    }
  },
  "lessonsLearned": {
    "languages": {
      "allLanguages": "All Languages",
      "javascript": "JavaScript",
      "typescript": "TypeScript",
      "python": "Python",
      "rust": "Rust",
      "general": "General"
    },
    "filters": {
      "allLessons": "All Runbooks",
      "bookmarked": "Flagged",
      "recent": "Recent (7 days)"
    },
    "actions": {
      "starred": "Flagged",
      "addStar": "Flag"
    },
    "pagination": {
      "showingRange": "Showing {{start}}-{{end}} of {{total}} runbooks"
    },
    "dialog": {
      "topicLabel": "Topic",
      "lessonLabel": "Runbook Entry",
      "languageLabel": "Language",
      "tagsLabel": "Tags (comma separated)",
      "tagsPlaceholder": "react, ui, logging",
      "databaseLabel": "Commit to Datastore",
      "personalDatabase": "👤 Personal Datastore",
      "sharedDatabase": "🌐 Shared Datastore (swarmonomicon)",
      "updateLesson": "Update Runbook",
      "createLesson": "Log Runbook"
    },
    "failedToLoad": "Query failed: {{error}}",
    "confirmDelete": "Decommission this runbook entry?"
  },
  "app": {
    "titleShort": "Madness Interactive",
    "titleLong": "Madness Interactive Workshop"
  },
  "panels": {
    "aiChat": "🤖 Diagnostics",
    "projects": "📂 Projects",
    "swarmDesk": "🎪 SwarmDesk",
    "chatAudit": "📊 Audit",
    "quests": "⚔️ Objectives"
  },
  "labMaintenance": {
    "duplicates": {
      "title": "Duplicate Ticket Detection",
      "description": "Identify and consolidate near-duplicate tickets across projects.",
      "threshold": "Similarity",
      "scan": "Scan",
      "scanning": "Querying…",
      "noResults": "No duplicate tickets detected at this threshold. Lower the sensitivity to broaden the scan.",
      "groupsFound": "groups",
      "potentialDuplicates": "tickets",
      "analyzeAI": "Run Diagnostics",
      "analyzing": "Running diagnostics…",
      "aiComplete": "Diagnostic complete. Review recommendations below.",
      "aiUnavailable": "Diagnostics temporarily unavailable.",
      "recommendations": "Diagnostic Recommendations",
      "keep": "Keep",
      "merge": "Merge",
      "deleteLabel": "Decommission",
      "suggestedDescription": "Suggested",
      "reasoning": "Rationale",
      "apply": "Apply",
      "applyAll": "Apply All",
      "applied": "Recommendation applied",
      "selectGroupsFirst": "Select ticket groups to analyze"
    },
    "sessionResolved": "resolved this session"
  },
  "demo": {
    "label": "OBSERVATION MODE"
  },
  "menu": {
    "documentation": "Runbooks",
    "replayTutorial": "Replay Onboarding",
    "userManagement": "User Management",
    "github": "GitHub",
    "themeGallery": "Theme Gallery",
    "logout": "Log Out",
    "support": "Operations Support",
    "lessonRefiner": "Runbook Refiner"
  },
  "projectNavigator": {
    "subtitle": "Select active project • Enter focused ops environment",
    "cacheStatus": "🏪 Cached • Last synced: {{time}}",
    "keyboardShortcuts": "⌨️ Arrow keys: Navigate • Enter/Space: Select • R: Resync • M: Main Swarmdesk • 1-9: Quick select",
    "manageTooltip": {
      "admin": "Manage Projects (Admin)",
      "personal": "Manage Personal Projects"
    },
    "refreshTooltip": "Resync Project Data",
    "mainSwarmDeskTooltip": "Open Main Swarmdesk",
    "loading": {
      "title": "🔍 Querying projects…",
      "subtitle": "Pulling ticket data and project metrics"
    },
    "stats": {
      "pending": "pending",
      "review": "triage"
    },
    "activity": {
      "title": "Recent Events",
      "noActivity": "No recent events"
    },
    "enterButton": {
      "selected": "📦 STAGED",
      "enter": "🚀 DEPLOY",
      "helpText": "Press Enter or #{{number}}"
    },
    "createCta": {
      "title": "Provision New Project",
      "subtitle": "Resources available — stand up a new environment"
    },
    "deleteDialog": {
      "title": "Decommission Project",
      "confirm": "Decommission project \"{{projectName}}\"?",
      "graveyardNote": "Project will be archived. You can restore it later if needed.",
      "hasTodos": "This project has {{count}} open ticket(s). Relocate them?",
      "relocateLabel": "Relocate tickets to another project",
      "selectDestination": "Select destination project",
      "cancel": "Discard",
      "deleteButton": "Decommission Project"
    },
    "viewInSwarmDesk": "View in SwarmDesk"
  },
  "projectSwarmdesk": {
    "title": "🎪 {{projectName}}",
    "stats": {
      "pendingTasks": "{{count}} pending",
      "completedTasks": "{{count}} resolved"
    },
    "loading": "🎪 Loading {{projectId}} environment…",
    "controls": "🎮 WASD: Move | Mouse Drag: Look | ESC: Exit Project",
    "workstation": {
      "todoHint": "📋 Click to manage project tickets",
      "projectHint": "🎪 Click to view project details"
    }
  },
  "projectTab": {
    "noActiveProject": "No active project",
    "selectProject": "Select a project from the navigator",
    "overview": {
      "description": "No description on record",
      "noRepository": "No repository linked",
      "todos": "Open Tickets",
      "completedTodos": "Resolved Tickets",
      "lessons": "Runbook Entries",
      "created": "Provisioned",
      "updated": "Last Updated"
    },
    "actions": {
      "openSwarmDesk": "Open SwarmDesk",
      "editProject": "Reconfigure Project",
      "deleteProject": "Decommission Project"
    },
    "deleteDialog": {
      "title": "Decommission Project",
      "message": "Decommission project \"{{projectName}}\"? This cannot be undone.",
      "confirm": "Decommission",
      "cancel": "Discard"
    }
  },
  "todoList": {
    "title": "🔬 Ticket Queue",
    "buttons": {
      "complete": "Resolve",
      "edit": "Edit Ticket",
      "delete": "Decommission",
      "view": "View",
      "flag": "Flag",
      "move": "Reassign",
      "clone": "Duplicate"
    },
    "filters": {
      "all": "All Tickets",
      "pending": "Pending",
      "inProgress": "In Progress",
      "completed": "Resolved",
      "blocked": "Blocked",
      "review": "Triage"
    },
    "sort": {
      "newest": "Newest",
      "oldest": "Oldest",
      "priority": "Priority",
      "alphabetical": "Alphabetical",
      "updated": "Recently Updated"
    },
    "priority": {
      "critical": "Critical",
      "high": "High",
      "medium": "Medium",
      "low": "Low",
      "none": "Unset"
    },
    "status": {
      "pending": "Pending",
      "inProgress": "In Progress",
      "completed": "Resolved",
      "blocked": "Blocked",
      "review": "Triage",
      "initial": "Initializing"
    },
    "empty": {
      "title": "Queue clear",
      "message": "No open tickets. Provision a new ticket to begin.",
      "noResults": "No tickets match the current filter.",
      "filtered": "No matching tickets"
    },
    "loading": "Querying…",
    "loadingMore": "Pulling more tickets…",
    "loadMore": "Load More",
    "count": "{{count}} ticket(s)",
    "selected": "{{count}} selected",
    "selectAll": "Select All",
    "deselectAll": "Deselect All",
    "bulkActions": {
      "complete": "Resolve Selected",
      "delete": "Decommission Selected",
      "move": "Reassign Selected",
      "export": "Export Snapshot"
    },
    "dragHint": "Drag to reorder queue",
    "dropHere": "Drop here",
    "search": {
      "placeholder": "Query tickets…",
      "clear": "Clear Query",
      "noResults": "No tickets match this query"
    },
    "pagination": {
      "showing": "Showing {{start}}-{{end}} of {{total}}",
      "page": "Page {{current}} of {{total}}",
      "prev": "Previous",
      "next": "Next"
    },
    "createFirst": "Open your first ticket",
    "noTasks": "Board is clear — no open tickets.",
    "actions": {
      "markComplete": "Resolve",
      "sendToReview": "Send to Triage",
      "reopen": "Reopen",
      "prioritize": "Prioritize",
      "archive": "Archive",
      "unarchive": "Restore"
    },
    "timestamps": {
      "created": "Opened",
      "updated": "Updated",
      "completed": "Resolved",
      "due": "Due"
    },
    "tags": {
      "add": "Add Tag",
      "remove": "Remove Tag",
      "none": "No tags"
    },
    "notes": {
      "add": "Add Note",
      "edit": "Edit Note",
      "none": "No notes on record"
    },
    "project": {
      "select": "Assign Project",
      "change": "Reassign",
      "none": "No project assigned"
    },
    "assignee": {
      "select": "Assign Operator",
      "change": "Reassign",
      "none": "Unassigned"
    },
    "dueDate": {
      "set": "Set Due Date",
      "change": "Adjust Due Date",
      "none": "No due date",
      "overdue": "Overdue",
      "today": "Due today",
      "tomorrow": "Due tomorrow"
    },
    "confirmDelete": {
      "title": "Decommission Ticket",
      "message": "Decommission \"{{title}}\"? This cannot be undone.",
      "confirm": "Decommission",
      "cancel": "Discard"
    },
    "moveDialog": {
      "title": "Reassign Ticket",
      "selectProject": "Select destination project",
      "confirm": "Reassign",
      "cancel": "Discard"
    },
    "completionDialog": {
      "title": "Resolve Ticket",
      "notesLabel": "Resolution notes (optional)",
      "confirm": "Resolve",
      "cancel": "Discard"
    },
    "errorLoading": "Failed to query tickets: {{error}}",
    "errorUpdating": "Failed to update ticket: {{error}}",
    "errorDeleting": "Failed to decommission ticket: {{error}}",
    "successComplete": "Ticket resolved",
    "successDelete": "Ticket decommissioned",
    "successMove": "Ticket reassigned",
    "aiEnhance": "Run Diagnostics",
    "aiEnhancing": "Running diagnostics…",
    "spellsAvailable": "Diagnostics available",
    "viewDetails": "View Details",
    "hideDetails": "Hide Details",
    "expandAll": "Expand All",
    "collapseAll": "Collapse All"
  },
  "todoEdit": {
    "title": "Edit Ticket",
    "createTitle": "Open New Ticket",
    "fields": {
      "description": "Ticket Description",
      "priority": "Priority",
      "status": "Status",
      "notes": "Notes",
      "tags": "Tags",
      "project": "Project",
      "assignee": "Assignee",
      "dueDate": "Due Date"
    },
    "save": "Commit",
    "cancel": "Discard",
    "delete": "Decommission",
    "saving": "Committing…"
  },
  "settings": {
    "title": "⚙️ System Configuration",
    "sections": {
      "appearance": "Display Config",
      "ai": "AI Integration",
      "notifications": "Alert Config",
      "privacy": "Access Control",
      "account": "Operator Profile",
      "advanced": "Advanced Ops",
      "about": "System Info",
      "data": "Data Management",
      "integrations": "Integrations",
      "security": "Security Config"
    },
    "theme": {
      "label": "Interface Theme",
      "description": "Select the console display theme"
    },
    "language": {
      "label": "Language",
      "description": "Interface language"
    },
    "notifications": {
      "label": "Alert Notifications",
      "description": "Enable system alerts",
      "email": "Email Alerts",
      "push": "Push Alerts",
      "inApp": "In-Console Alerts"
    },
    "ai": {
      "label": "AI Integration",
      "description": "Configure AI diagnostic provider",
      "provider": "Provider",
      "apiKey": "API Key",
      "model": "Model",
      "temperature": "Temperature",
      "maxTokens": "Max Tokens",
      "testConnection": "Test Connection",
      "testing": "Testing…",
      "connected": "Connection verified",
      "failed": "Connection failed"
    },
    "privacy": {
      "label": "Access Control",
      "description": "Manage data access settings",
      "shareAnalytics": "Share usage telemetry",
      "crashReports": "Submit crash reports"
    },
    "advanced": {
      "label": "Advanced Ops",
      "description": "Advanced configuration parameters",
      "debugMode": "Debug Mode",
      "experimentalFeatures": "Experimental Features",
      "resetSettings": "Reset to Defaults",
      "clearCache": "Purge Cache",
      "exportData": "Export Snapshot",
      "importData": "Import Data",
      "dangerZone": "Restricted Zone"
    },
    "save": "Commit Config",
    "cancel": "Discard",
    "saved": "Configuration committed",
    "error": "Configuration commit failed",
    "reset": "Reset to Defaults",
    "confirmReset": "Reset all configuration to factory defaults?",
    "tabs": {
      "general": "General",
      "ai": "AI",
      "appearance": "Display",
      "data": "Data",
      "notifications": "Alerts",
      "security": "Security",
      "advanced": "Advanced"
    },
    "autoSave": {
      "label": "Auto-commit changes",
      "description": "Automatically commit configuration changes"
    },
    "display": {
      "density": "Display Density",
      "compact": "Compact",
      "comfortable": "Comfortable",
      "spacious": "Spacious",
      "fontSize": "Font Size",
      "animations": "UI Animations",
      "reducedMotion": "Reduce motion"
    },
    "data": {
      "exportAll": "Export Full Snapshot",
      "importFile": "Import Data File",
      "clearAllData": "Purge All Data",
      "confirmClear": "Purge all data? This cannot be undone.",
      "backupFrequency": "Snapshot Frequency",
      "autoBackup": "Auto-snapshot"
    },
    "security": {
      "changePassword": "Change Password",
      "twoFactor": "Two-Factor Auth",
      "sessions": "Active Sessions",
      "revokeAll": "Revoke All Sessions",
      "loginHistory": "Login Log"
    },
    "about": {
      "version": "Version",
      "build": "Build",
      "license": "License",
      "documentation": "Runbooks",
      "changelog": "Release Notes",
      "reportBug": "Report Incident",
      "featureRequest": "Request Feature"
    }
  },
  "umlData": {
    "title": "🗂️ Code Map Archive",
    "loading": "Querying code maps…",
    "noData": "No code maps on record. Generate your first map.",
    "generate": "Generate Map",
    "generating": "Generating…",
    "upload": "Upload Map",
    "uploading": "Uploading…",
    "download": "Download",
    "delete": "Decommission",
    "confirmDelete": "Decommission this code map?",
    "version": "Version",
    "versions": "Versions",
    "noVersions": "No versions on record",
    "compareVersions": "Compare Versions",
    "currentVersion": "Current",
    "previousVersion": "Previous",
    "diff": "Diff View",
    "timeline": "Version Timeline",
    "restore": "Restore Version",
    "confirmRestore": "Restore this version?",
    "metadata": {
      "created": "Generated",
      "size": "Size",
      "nodes": "Nodes",
      "edges": "Edges",
      "language": "Language",
      "framework": "Framework"
    },
    "filters": {
      "all": "All Maps",
      "recent": "Recent",
      "language": "By Language"
    },
    "empty": {
      "title": "No code maps on record",
      "message": "Generate a code map to visualize project architecture.",
      "action": "Generate First Map"
    },
    "error": {
      "generate": "Map generation failed: {{error}}",
      "upload": "Upload failed: {{error}}",
      "load": "Query failed: {{error}}"
    },
    "success": {
      "generated": "Code map generated",
      "uploaded": "Map uploaded to archive",
      "deleted": "Map decommissioned",
      "restored": "Version restored"
    },
    "repoUrl": "Repository URL",
    "branch": "Branch",
    "depth": "Analysis Depth",
    "generateFromRepo": "Generate from Repository"
  },
  "editableTodoCard": {
    "placeholder": "Ticket description…",
    "saving": "Committing…",
    "saved": "Committed",
    "error": "Commit failed",
    "editMode": "Edit Mode",
    "viewMode": "View Mode",
    "actions": {
      "edit": "Edit Ticket",
      "save": "Commit",
      "cancel": "Discard",
      "delete": "Decommission",
      "complete": "Resolve",
      "move": "Reassign",
      "clone": "Duplicate",
      "flag": "Flag",
      "unflag": "Unflag",
      "pin": "Pin",
      "unpin": "Unpin",
      "share": "Share",
      "view": "View Details"
    },
    "status": {
      "pending": "Pending",
      "inProgress": "In Progress",
      "completed": "Resolved",
      "blocked": "Blocked",
      "review": "Triage"
    },
    "priority": {
      "critical": "Critical",
      "high": "High",
      "medium": "Medium",
      "low": "Low"
    },
    "fields": {
      "description": "Description",
      "notes": "Notes",
      "tags": "Tags",
      "priority": "Priority",
      "status": "Status",
      "project": "Project",
      "dueDate": "Due Date"
    },
    "confirmDelete": {
      "title": "Decommission Ticket",
      "message": "Decommission this ticket?",
      "confirm": "Decommission",
      "cancel": "Discard"
    }
  },
  "mindMap": {
    "title": "🗺️ Project Topology",
    "loading": "Querying topology…",
    "empty": {
      "title": "Topology empty",
      "message": "Add tickets and projects to map the system topology.",
      "action": "Open First Ticket"
    },
    "controls": {
      "zoomIn": "Zoom In",
      "zoomOut": "Zoom Out",
      "reset": "Reset View",
      "center": "Center View",
      "fit": "Fit to Window",
      "fullscreen": "Full Screen",
      "exitFullscreen": "Exit Full Screen"
    },
    "nodes": {
      "todo": "Ticket",
      "project": "Project",
      "lesson": "Runbook",
      "tag": "Tag"
    },
    "filters": {
      "all": "All Nodes",
      "todos": "Tickets Only",
      "projects": "Projects Only",
      "tags": "Tags Only"
    },
    "layout": {
      "force": "Force Layout",
      "tree": "Tree Layout",
      "radial": "Radial Layout",
      "grid": "Grid Layout"
    },
    "export": {
      "png": "Export PNG",
      "svg": "Export SVG",
      "json": "Export JSON"
    },
    "error": "Topology query failed: {{error}}",
    "refresh": "Resync Topology",
    "addNode": "Add Node",
    "editNode": "Edit Node",
    "deleteNode": "Remove Node",
    "connectNodes": "Link Nodes",
    "disconnectNodes": "Unlink Nodes"
  },
  "chatAssistant": {
    "title": "🤖 Lab Diagnostics",
    "placeholder": "Query the diagnostic system…",
    "send": "Send",
    "sending": "Transmitting…",
    "loading": "Querying…",
    "empty": {
      "title": "Diagnostics ready",
      "message": "Ask a question or request an analysis.",
      "suggestion": "Try: 'What tickets are blocked?'"
    },
    "error": {
      "send": "Transmission failed: {{error}}",
      "load": "Query failed: {{error}}"
    },
    "actions": {
      "copy": "Copy",
      "retry": "Retry",
      "delete": "Remove",
      "feedback": {
        "good": "Useful",
        "bad": "Not Useful"
      }
    },
    "system": "System",
    "you": "Operator",
    "ai": "Diagnostics",
    "typing": "Processing…",
    "newConversation": "New Session",
    "clearHistory": "Purge History",
    "confirmClear": "Purge all chat history?",
    "history": "Chat History",
    "noHistory": "No session history",
    "tools": {
      "listTodos": "List Tickets",
      "createTodo": "Open Ticket",
      "analyzeTodos": "Run Diagnostics",
      "searchTodos": "Query Tickets"
    },
    "suggestions": {
      "listAll": "List all open tickets",
      "critical": "Show critical tickets",
      "blocked": "What is blocked?",
      "insights": "Run project diagnostics"
    }
  },
  "mobileChatInterface": {
    "title": "Lab Diagnostics",
    "placeholder": "Query the diagnostic system…",
    "send": "Send",
    "voiceInput": "Voice Input",
    "stopVoice": "Stop Voice",
    "attachFile": "Attach File",
    "loading": "Querying…",
    "empty": {
      "title": "Diagnostics ready",
      "message": "Run a query or request an analysis."
    },
    "error": "Transmission failed",
    "newSession": "New Session",
    "clearHistory": "Purge History",
    "historyTitle": "Chat History",
    "noHistory": "No session history",
    "close": "Dismiss",
    "minimize": "Minimize",
    "expand": "Expand",
    "connectionStatus": {
      "connected": "Connected",
      "disconnected": "Disconnected",
      "reconnecting": "Reconnecting…"
    }
  },
  "warRoom": {
    "title": "🚨 Incident Command",
    "loading": "Querying incident data…",
    "empty": {
      "title": "All clear",
      "message": "No active incidents. All systems nominal.",
      "action": "Open Incident"
    },
    "incident": {
      "create": "Open Incident",
      "resolve": "Resolve Incident",
      "escalate": "Escalate",
      "assign": "Assign",
      "priority": "Severity",
      "status": "Status"
    },
    "filters": {
      "all": "All Incidents",
      "active": "Active",
      "resolved": "Resolved"
    },
    "error": "Incident query failed: {{error}}",
    "refresh": "Resync"
  },
  "swarmDesk": {
    "title": "🎪 SwarmDesk Ops Center",
    "loading": "Querying…",
    "controls": {
      "move": "Move",
      "rotate": "Rotate",
      "zoom": "Zoom",
      "reset": "Reset View",
      "fullscreen": "Full Screen",
      "exitFullscreen": "Exit Full Screen"
    },
    "panels": {
      "todos": "Ticket Queue",
      "projects": "Projects",
      "chat": "Diagnostics",
      "insights": "Analytics",
      "settings": "Config"
    },
    "nodes": {
      "create": "Open Ticket",
      "edit": "Edit Ticket",
      "delete": "Decommission",
      "complete": "Resolve",
      "move": "Reassign",
      "view": "View Details"
    },
    "empty": {
      "title": "No nodes in view",
      "message": "Open a ticket to populate the ops center."
    },
    "error": "SwarmDesk query failed: {{error}}",
    "status": {
      "connected": "Connected to datastore",
      "disconnected": "Datastore disconnected",
      "syncing": "Syncing…",
      "synced": "Synced"
    },
    "hotkeys": {
      "title": "Hotkey Reference",
      "wasd": "WASD: Navigate",
      "mouse": "Mouse: Look",
      "escape": "ESC: Exit",
      "tab": "TAB: Switch Panel",
      "space": "Space: Select"
    },
    "filters": {
      "all": "All Tickets",
      "pending": "Pending",
      "inProgress": "In Progress",
      "blocked": "Blocked",
      "review": "Triage"
    },
    "sort": {
      "priority": "Priority",
      "updated": "Recently Updated",
      "created": "Date Opened",
      "name": "Alphabetical"
    },
    "createTodo": {
      "title": "Open New Ticket",
      "placeholder": "Ticket description…",
      "submit": "Open Ticket",
      "cancel": "Discard"
    },
    "todoPanel": {
      "title": "Ticket Queue",
      "empty": "Board is clear.",
      "loading": "Querying tickets…"
    },
    "projectPanel": {
      "title": "Active Projects",
      "empty": "No projects provisioned.",
      "loading": "Querying projects…",
      "create": "Provision Project",
      "select": "Select Project",
      "selected": "Active: {{name}}"
    },
    "agentPanel": {
      "title": "Agent Status",
      "empty": "No agents registered.",
      "loading": "Querying agents…",
      "status": {
        "active": "Active",
        "idle": "Idle",
        "offline": "Offline"
      }
    },
    "chatPanel": {
      "title": "Diagnostics",
      "placeholder": "Query…",
      "send": "Send",
      "loading": "Querying…"
    },
    "notifications": {
      "todoCreated": "Ticket opened",
      "todoCompleted": "Ticket resolved",
      "todoDeleted": "Ticket decommissioned",
      "projectCreated": "Project provisioned",
      "syncComplete": "Datastore synced"
    },
    "tour": {
      "welcome": "Welcome to SwarmDesk Ops Center",
      "navigation": "WASD to navigate, mouse to look",
      "interaction": "Click nodes to manage tickets",
      "panels": "Use panels to query tickets and run diagnostics",
      "complete": "Ops center ready"
    }
  },
  "spells": {
    "title": "🔬 Diagnostic Tools",
    "description": "AI-powered analytics for ticket management",
    "available": "Available diagnostics",
    "noTodoSelected": "No ticket selected",
    "availableSpells": "Available Diagnostics",
    "keyboardShortcut": "Keyboard Shortcut",
    "estimatedTime": "Estimated Time",
    "accessDenied": {
      "title": "Access Denied",
      "description": "Insufficient access level to run diagnostics. Upgrade your account or log in."
    },
    "system": {
      "title": "Diagnostic System"
    },
    "categories": {
      "enhance": "Enhance",
      "analyze": "Analyze",
      "consolidate": "Consolidate"
    },
    "enhance": {
      "title": "Enhance Ticket",
      "description": "Use AI to improve ticket description",
      "button": "Enhance Ticket",
      "casting": "Enhancing…",
      "success": "Ticket enhanced"
    },
    "geomancy": {
      "title": "Pattern Analysis",
      "description": "Identify patterns and dependencies",
      "button": "Analyze Patterns",
      "casting": "Running analysis…",
      "success": "Analysis complete"
    },
    "consolidate": {
      "title": "Consolidate Tickets",
      "description": "Identify and merge duplicate tickets",
      "button": "Find Duplicates",
      "casting": "Scanning for duplicates…",
      "success": "Consolidation complete"
    },
    "effects": {
      "particles": "Diagnostic indicators active",
      "energy": "System processing",
      "casting": "Enhancement in progress",
      "complete": "Enhancement completed"
    },
    "results": {
      "enhance": {
        "success": "🔬 Ticket enhanced with AI diagnostics!",
        "improvement": "Improvement applied to ticket description",
        "insights": "Key findings:",
        "suggestions": "Recommendations:"
      },
      "geomancy": {
        "success": "🔍 Patterns identified in project!",
        "insights": "Analysis findings:",
        "patterns": "Pattern analysis:",
        "recommendations": "Recommendations:",
        "analysis": "Analysis complete"
      },
      "consolidate": {
        "success": "🔗 Duplicate tickets consolidated!",
        "merged": "{{count}} tickets merged",
        "candidates": "Consolidation candidates:",
        "preview": "Merge preview:",
        "confirmation": "Proceed with consolidation?"
      },
      "title": "Diagnostic Results",
      "latest": "Latest",
      "noResults": "No results yet. Run a diagnostic to see results here.",
      "summary": "{{count}} diagnostic results"
    },
    "errors": {
      "castingFailed": "Diagnostic failed: {{error}}",
      "noDescription": "Ticket description required for enhancement",
      "rateLimited": "Rate limit reached. Wait: {{timeRemaining}}",
      "aiError": "AI system error",
      "networkError": "Network error",
      "invalidSpell": "Unknown diagnostic requested",
      "unauthorized": "Insufficient access level"
    },
    "rateLimit": {
      "enhance": "Enhancement uses: {{used}}/{{limit}} remaining",
      "geomancy": "Analysis uses: {{used}}/{{limit}} remaining",
      "consolidate": "Consolidation uses: {{used}}/{{limit}} remaining",
      "resetTime": "Resets in: {{time}}",
      "depleted": "Rate limit reached"
    },
    "tooltip": {
      "castSpell": "Run diagnostic",
      "enhanceDescription": "Enhance ticket (Ctrl+E)",
      "performGeomancy": "Analyze patterns (Ctrl+G)",
      "consolidateSimilar": "Find duplicates (Ctrl+C)",
      "spellHistory": "View diagnostic history",
      "clearHistory": "Purge diagnostic history"
    },
    "keyboard": {
      "shortcuts": "⌨️ Keyboard Shortcuts:",
      "enhance": "Ctrl+E - Enhance Ticket",
      "geomancy": "Ctrl+G - Pattern Analysis",
      "consolidate": "Ctrl+C - Find Duplicates",
      "cancel": "Esc - Cancel"
    },
    "history": {
      "timestamp": "Timestamp:",
      "spellType": "Diagnostic type:",
      "target": "Target ticket:",
      "result": "Result:",
      "success": "✅ Successful",
      "failed": "❌ Failed",
      "duration": "Duration:",
      "empty": "No diagnostics logged",
      "toggle": "Toggle diagnostic history"
    },
    "status": {
      "idle": "Diagnostics ready",
      "casting": "Applying diagnostic…",
      "processing": "Processing…",
      "complete": "Diagnostic complete",
      "failed": "Diagnostic failed",
      "cooldown": "Rate limit cooling down…",
      "success": "Success"
    },
    "enhance_description": {
      "description": "Use AI to enhance and clarify this ticket description",
      "button": "Enhance Description",
      "casting": "Enhancing description…"
    },
    "perform_geomancy": {
      "description": "Analyze patterns and relationships for this ticket",
      "button": "Analyze Patterns",
      "casting": "Analyzing patterns…"
    },
    "consolidate_similar": {
      "description": "Find and merge similar tickets to reduce duplication",
      "button": "Find Similar",
      "casting": "Scanning for similar tickets…"
    },
    "tip": {
      "castMultiple": "Run multiple diagnostics on the same ticket for comprehensive analysis"
    },
    "meta": {
      "maxPerHour": "Max runs per hour",
      "lastCast": "Last run"
    },
    "result": {
      "confidence": "Confidence"
    },
    "error": {
      "unknown": "An unknown error occurred"
    },
    "enhanceDescription": {
      "result": {
        "title": "Enhanced Description",
        "before": "Before",
        "after": "After",
        "improvements": "Improvements"
      }
    },
    "performGeomancy": {
      "result": {
        "insights": "Insights",
        "relatedProjects": "Related Projects"
      },
      "insights": {
        "complexity": "Complexity",
        "duration": "Estimated Duration",
        "risks": "Risk Factors"
      }
    },
    "consolidateSimilar": {
      "found": "Found {{count}} similar tickets",
      "result": {
        "consolidated": "Consolidated Description",
        "suggestions": "Merge Suggestions"
      }
    }
  },
  "insights": {
    "loading": "Querying analytics…",
    "tabs": {
      "overview": "Overview",
      "analytics": "Analytics",
      "systemLogs": "System Logs"
    }
  },
  "admin": {
    "tabs": {
      "overview": "Overview",
      "users": "Users",
      "analytics": "Analytics",
      "featureFlags": "Feature Flags",
      "systemLogs": "System Logs"
    },
    "overview": {
      "title": "Operations Overview",
      "loading": "Querying ops metrics…",
      "refresh": "Resync metrics",
      "fallback": "(showing mock data for development)",
      "totalUsers": "Total Users",
      "totalUsersSubtitle": "All registered operators",
      "activeUsers": "Active (7d)",
      "activeUsersSubtitle": "Operators active this week",
      "premiumUsers": "Premium Operators",
      "premiumUsersSubtitle": "Paid subscriptions",
      "errors": "Errors (24h)",
      "errorsSubtitle": "System errors today",
      "tierDistribution": "Tier Distribution",
      "tier": {
        "free": "Free",
        "pro": "Pro",
        "premium": "Premium",
        "admin": "Admin"
      },
      "productivity": "Productivity Metrics",
      "totalTodos": "Total Tickets",
      "completedTodos": "Resolved",
      "completionRate": "Resolution Rate"
    },
    "analytics": {
      "title": "Advanced Analytics",
      "loading": "Querying analytics…",
      "comingSoon": "Analytics Under Construction",
      "description": "Advanced charts and data visualization are being calibrated. Check back soon.",
      "timeframe": {
        "day": "Last 24 Hours",
        "week": "Last 7 Days",
        "month": "Last 30 Days",
        "year": "Last 12 Months"
      },
      "futureHint": "Coming soon: Custom date ranges, CSV export, real-time updates, cohort analysis.",
      "charts": {
        "userGrowth": "User Growth",
        "userGrowthDesc": "New operator registrations over time",
        "activityHeatmap": "Activity Heatmap",
        "activityHeatmapDesc": "Operator activity by hour/day",
        "featureUsage": "Feature Usage",
        "featureUsageDesc": "Most-used features",
        "performance": "System Performance",
        "performanceDesc": "API response times and error rates"
      }
    },
    "logs": {
      "title": "System Logs",
      "loading": "Querying logs…",
      "refresh": "Resync logs",
      "fallback": "(showing mock data for development)",
      "autoRefresh": "Auto-sync (30s)",
      "showing": "Showing",
      "entries": "entries",
      "empty": "No log entries — systems nominal",
      "columns": {
        "timestamp": "Time",
        "level": "Level",
        "message": "Message",
        "user": "Operator",
        "endpoint": "Endpoint"
      },
      "severity": {
        "error": "ERROR",
        "warning": "WARNING",
        "info": "INFO"
      }
    },
    "featureFlags": {
      "title": "Feature Flags",
      "loading": "Querying flags…",
      "refresh": "Resync flags",
      "fallback": "(showing mock data for development)",
      "lastUpdated": "Last updated",
      "unsavedChanges": "Uncommitted changes pending — will affect all operators on commit.",
      "save": "Commit Changes",
      "cancel": "Discard",
      "saving": "Committing…",
      "confirmSave": "Apply Changes",
      "tiers": {
        "free": "Free Tier",
        "pro": "Pro Tier",
        "premium": "Premium Tier",
        "admin": "Admin Tier"
      },
      "flags": {
        "basic_todos": "Basic Tickets",
        "chat_interface": "Chat Interface",
        "theme_selector": "Theme Selector",
        "export_todos": "Export Tickets",
        "advanced_search": "Advanced Query",
        "unlimited_todos": "Unlimited Tickets",
        "mindmap_view": "Topology View",
        "custom_themes": "Custom Themes",
        "api_access": "API Access",
        "priority_support": "Priority Support",
        "swarmdesk_3d": "SwarmDesk 3D",
        "collaborative_editing": "Collaborative Editing",
        "ai_copilot": "AI Copilot",
        "admin_panel": "Admin Panel",
        "user_management": "User Management",
        "feature_flags": "Feature Flags",
        "system_logs": "System Logs",
        "analytics": "Analytics",
        "debug_mode": "Debug Mode"
      },
      "confirm": {
        "title": "Confirm Flag Changes",
        "message": "Apply these changes? This will immediately affect all operators.",
        "warning": "Tip: Test changes on staging first. Disabling core flags may break operator workflows."
      }
    },
    "users": {
      "title": "Operator Management",
      "loading": "Querying operator roster…",
      "refresh": "Resync roster",
      "fallback": "(showing mock data for development)",
      "searchPlaceholder": "Query by email or name…",
      "showing": "Showing",
      "users": "operators",
      "filtered": "filtered from",
      "empty": "No operators registered",
      "noResults": "No operators match this query",
      "adminBadge": "ADMIN",
      "edit": {
        "title": "Edit Operator",
        "email": "Email",
        "tier": "Tier",
        "isAdmin": "Grant Admin Access",
        "cancel": "Discard",
        "save": "Commit",
        "saving": "Committing…"
      },
      "columns": {
        "email": "Email",
        "tier": "Tier",
        "status": "Status",
        "lastLogin": "Last Login",
        "todos": "Tickets",
        "actions": "Actions"
      },
      "confirm": {
        "title": "Confirm Access Change",
        "grantMessage": "Grant admin access to this operator? They will have full access to all admin panels.",
        "revokeMessage": "Revoke admin access from this operator? They will lose all admin access.",
        "cancel": "Discard",
        "confirm": "Confirm",
        "saving": "Committing…"
      }
    },
    "common": {
      "loading": "Querying…",
      "error": "An error occurred",
      "refresh": "Resync",
      "save": "Commit",
      "cancel": "Discard"
    }
  },
  "queuePane": {
    "allProjects": "All Projects",
    "incoming": {
      "title": "Incoming",
      "addToTop": "Push to Top",
      "addToBottom": "Enqueue"
    },
    "ordered": {
      "title": "Ordered Queue"
    },
    "stats": {
      "total": "Queued",
      "high": "Urgent",
      "incoming": "Incoming"
    }
  },
  "onboarding": {
    "colors": {
      "chipText": "#ffffff"
    },
    "complete": {
      "message": "Operator account provisioned. Access your ops dashboard now."
    },
    "steps": {
      "welcome": {
        "title": "Welcome, Operator",
        "defaultName": "Operator",
        "description": "Inventorium is your AI-powered ticket management and project ops platform.",
        "subtitle": "Let's run a quick orientation to get you operational."
      },
      "create-project": {
        "title": "Provision Your First Project",
        "description": "Let's provision a project to organize your tickets. Projects group related work into manageable environments.",
        "skipHint": "You can skip this and provision a project later from the Create console"
      },
      "add-todo": {
        "title": "Open a Ticket",
        "description": "Now let's open a ticket in your project. Tickets are the actionable items you track and resolve.",
        "guideTitle": "How to open a ticket:",
        "step1": "Click the floating '+' button again",
        "step2": "Select the 'Ticket' tab in the dialog",
        "step3": "Enter your ticket description",
        "step4": "Assign the project from the dropdown",
        "step5": "Set priority and click 'Open Ticket'",
        "hint": "Tip: You can open tickets from anywhere in the console using the '+' button"
      },
      "configure-ai": {
        "title": "Configure AI Diagnostics",
        "description": "Get the most from Inventorium by connecting an AI provider like Google Gemini or OpenAI.",
        "whyConfigureTitle": "Why configure AI?",
        "benefits": {
          "suggestions": "Generate smart ticket suggestions",
          "enhance": "Enhance ticket descriptions with AI analysis",
          "analyze": "Analyze project patterns and dependencies",
          "insights": "Get ops insights and recommendations"
        },
        "statusConfigured": "Status: ✅ AI diagnostics configured and ready.",
        "statusNotConfigured": "Status: ❌ AI diagnostics not configured",
        "configureButton": "Configure AI Now",
        "skipButton": "Skip for Now",
        "helpText": "You can configure AI anytime from Settings → AI Configuration"
      },
      "ai-assistant": {
        "title": "AI Diagnostics",
        "examplesTitle": "Quick Queries:",
        "quickActions": {
          "createTodos": "Open tickets from text",
          "analyzeTasks": "Analyze ticket patterns",
          "suggestions": "Get smart suggestions",
          "insights": "Project analytics"
        }
      },
      "swarmdesk": {
        "title": "3D Ops Center",
        "description": "Visualize your codebase in 3D with SwarmDesk — an immersive ops environment.",
        "featuresTitle": "SwarmDesk Features:",
        "features": {
          "codeViz": "3D code visualization",
          "interactive": "Interactive navigation",
          "architecture": "Architecture overview",
          "dependencies": "Dependency mapping"
        },
        "hint": "💡 Tip: Access SwarmDesk from the project view",
        "tabTip": "After SwarmDesk loads, press TAB to switch between dashboard and 3D ops center"
      },
      "complete": {
        "title": "Operator Online",
        "description": "You're ready. Explore the console and tune it to your workflow.",
        "nextStepsTitle": "Next Steps:",
        "nextSteps": {
          "createProject": "Provision your first project",
          "addTodos": "Open tickets in your project",
          "tryAI": "Run AI diagnostics",
          "checkSwarmDesk": "Explore SwarmDesk 3D"
        },
        "footer": "💡 You can replay this orientation anytime from Settings"
      }
    }
  },
  "lessons": {
    "title": "Runbooks",
    "addLesson": "Add Runbook",
    "emptyState": {
      "title": "No Runbooks Found",
      "message": "Document findings to improve future ops workflows.",
      "action": "Add First Runbook"
    },
    "fields": {
      "topic": "Topic",
      "language": "Language/Category",
      "lessonLearned": "Runbook Entry",
      "tags": "Tags"
    },
    "actions": {
      "edit": "Edit",
      "delete": "Decommission",
      "save": "Commit Changes"
    }
  },
  "mindmap": {
    "title": "Project Topology",
    "emptyState": {
      "title": "Topology Empty",
      "message": "Add tickets and projects to map the system topology."
    },
    "controls": {
      "zoomIn": "Zoom In",
      "zoomOut": "Zoom Out",
      "resetView": "Reset View",
      "centerView": "Center View"
    }
  },
  "swarmdesk": {
    "title": "Ops Overview",
    "emptyState": {
      "title": "No Data Available",
      "message": "Initialize components to view system status."
    },
    "controls": {
      "rotate": "Rotate",
      "zoom": "Zoom",
      "pan": "Pan",
      "reset": "Reset View"
    }
  },
  "projectSelector": {
    "title": "Select Project",
    "placeholder": "Query projects…",
    "noProjects": "No projects provisioned",
    "createNew": "Provision New Project"
  },
  "errors": {
    "serverError": "Internal server error."
  },
  "success": {
    "status": {
      "verifying": {
        "title": "VERIFYING…",
        "subtitle": "Verifying payment with Stripe"
      },
      "success": {
        "title": "UPGRADE COMPLETE",
        "subtitle": "All systems nominal. Account upgraded."
      },
      "error": {
        "title": "VERIFICATION FAILED"
      },
      "no_session": {
        "title": "SESSION NOT FOUND",
        "subtitle": "No checkout session detected. Did you navigate here directly?"
      }
    },
    "log": {
      "initializing": "Initializing payment verification…",
      "connecting": "Connecting to Stripe…",
      "session": "Session:",
      "conduitStable": "Payment confirmed: STABLE",
      "tierUpgrade": "Tier upgrade:",
      "allSystemsGo": "STATUS: ALL SYSTEMS GO",
      "paymentStatus": "Payment status:",
      "paymentIncomplete": "WARNING: Payment incomplete",
      "error": "ERROR:",
      "verificationFailed": "Verification failed"
    },
    "tier": "TIER",
    "operator": "ACCOUNT",
    "viewManifest": "VIEW BILLING",
    "errorRetry": "If payment was processed, your upgrade will activate shortly.",
    "checkBilling": "Check billing for current status."
  },
  "targetAgent": {
    "user": "Operator",
    "ai": "Diagnostic AI",
    "system": "System",
    "none": "Unassigned"
  },
  "todoDetail": {
    "untitled": "Untitled Ticket",
    "tabs": {
      "overview": "Overview",
      "history": "Changelog",
      "spells": "Diagnostics",
      "related": "Related",
      "sessions": "Sessions",
      "coordinates": "Coordinates"
    },
    "spells": {
      "empty": "No diagnostics run on this ticket yet.",
      "hint": "Use the AI chat to enhance descriptions or run analysis.",
      "undo": "Undo diagnostic"
    },
    "related": {
      "empty": "No related tickets found in this project.",
      "count": "{{count}} related tickets"
    },
    "sessions": {
      "empty": "No sessions linked to this ticket.",
      "hint": "Link sessions via the AI chat.",
      "count": "{{count}} linked sessions"
    },
    "coordinates": {
      "empty": "No coordinates assigned to this ticket.",
      "hint": "Run a geomancy diagnostic to assign spatial coordinates."
    }
  },
  "automationRecipes": {
    "tagNormalization": {
      "scanned": "Scanned",
      "modified": "Modified"
    }
  },
  "constellation": {
    "contextMenu": {
      "openInSwarmDesk": "Open in SwarmDesk"
    },
    "controls": {
      "recenter": "Recenter",
      "fullscreen": "Fullscreen"
    }
  },
  "shareReceiver": {
    "cancel": "Discard"
  },
  "lessonsViewer": {
    "bench": {
      "run": "Execute"
    },
    "neighbors": {
      "none": "none"
    },
    "references": {
      "none": "none"
    }
  },
  "questTab": {
    "success": "Objective \"{{name}}\" registered ({{chains}} chains, {{todos}} tickets)",
    "chainsHint": "Optional. {{chains}} chain(s), {{todos}} ticket(s) linked.",
    "fields": {
      "name": "Objective Name *",
      "project": "Project",
      "tagsInput": "Tags (comma-separated)",
      "quickTags": "Quick Tags:",
      "addCriterion": "Add a success criterion",
      "chainLabel": "Chain Label",
      "chainTodos": "Tickets in chain ({{count}})"
    },
    "buttons": {
      "add": "Add",
      "addChain": "Add Chain",
      "removeChain": "Remove chain",
      "copyId": "Copy ID"
    },
    "errors": {
      "nameRequired": "Objective name is required.",
      "projectRequired": "Project is required."
    }
  },
  "questCard": {
    "external": "external",
    "briefGenerating": "Generating…",
    "briefSaved": "Committed",
    "briefDismiss": "Dismiss",
    "copiedPrompt": "Copied!",
    "copiedId": "Copied!",
    "deleteFailed": "Decommission failed",
    "save": "Commit",
    "saveFailed": "Commit failed",
    "cancel": "Discard",
    "project": "Project",
    "projectRequired": "Project is required"
  }
}

result = deep_merge(labops, overrides)
save("labops", result)
print("labops.json written")

# Validate
import subprocess
r = subprocess.run(["node", "-e", "require('./labops.json'); console.log('JSON valid')"],
                   capture_output=True, text=True, cwd=THEMES_DIR)
print(r.stdout.strip() or r.stderr.strip())
