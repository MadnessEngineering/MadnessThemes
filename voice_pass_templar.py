#!/usr/bin/env python3
"""
Voice pass for templar-light.json — scribe-knight/sacred order persona per VOICE_GUIDE.
Lexicon: save=Inscribe, cancel=Withdraw, delete=Expunge, loading=Consulting the Archive…,
create=Pledge, edit-panel=Amend Record, edit-todo=Amend Charge, refresh=Renew,
search=Seek, export=Transcribe Records, complete=Fulfill, close=Seal, review=Examine
Noun-map: Chamber=panel/form, Charge=todo, Roster=ordered work, Archive=data layer,
Passage/Hall=navigation
"""
import json, copy, subprocess

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

templar = load("templar-light")

overrides = {
  "desktop": {
    "deleteBranch": "Dissolve order",
    "discardChanges": "Discard amendments",
    "discardAll": "Discard all amendments",
    "openInTerminal": "Open in terminal",
    "abortMerge": "Abort merge",
    "continueRebase": "Continue rebase",
    "abortRebase": "Abort rebase",
    "discard": "Withdraw",
    "dismiss": "Dismiss"
  },
  "common": {
    "previous": "Previous",
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
    "notes": "Annotations",
    "ticket": "Writ"
  },
  "dashboard": {
    "activityLog": {
      "title": "📜 Chronicle of Deeds",
      "collection": "Archive of deeds",
      "description": "The sacred record of all charges wrought and amended",
      "updates": "Amendments",
      "creates": "Pledges",
      "deletes": "Expungements",
      "completions": "Fulfillments",
      "totalEntries": "Total Inscriptions"
    },
    "recentlyCompleted": {
      "title": "✅ Recently Fulfilled"
    },
    "filters": {
      "allActivity": "All Deeds",
      "todosCreated": "Charges Pledged",
      "todosUpdated": "Charges Amended",
      "todosCompleted": "Charges Fulfilled",
      "todosDeleted": "Charges Expunged",
      "projectsCreated": "Crusades Declared",
      "projectsUpdated": "Crusades Amended",
      "projectsDeleted": "Crusades Dissolved"
    },
    "unifiedView": "Order-wide View",
    "personalView": "Personal Vigil",
    "showingAllDatabases": "Consulting all chapters",
    "showingPersonalOnly": "Showing personal vigil only",
    "filteredByProject": "Filtered by crusade",
    "noLogsFound": "No deeds recorded in the Archive",
    "tryChangingFilter": "Alter thy filter",
    "startCreatingTodos": "Pledge your first charge to begin",
    "failedToLoad": "Archive failed to open: {{error}}",
    "changesMade": "Amendments inscribed",
    "completionNotes": "Fulfillment notes",
    "revertOperation": "Recant {{operation}}",
    "revertSuccess": "{{operation}} recanted successfully",
    "revertFailed": "Recantation failed: {{error}}",
    "revertDeleteNotSupported": "Recanting expungement is not permitted",
    "revertNotSupported": "Recantation not permitted for {{operation}}",
    "confirmRevert": "Confirm Recantation",
    "confirmRevertMessage": "Recant {{operation}} on {{description}}?",
    "confirmRevertAction": "Recant",
    "operationType": "Deed Type",
    "taskDescription": "Charge Description",
    "descriptions": {
      "projectCreated": "Crusade declared: {{projectName}}",
      "projectUpdated": "Crusade amended: {{projectName}}",
      "projectDeleted": "Crusade dissolved: {{projectName}}",
      "projectModified": "Crusade reconfigured: {{projectName}}",
      "unknownTask": "Deed unknown"
    },
    "showingPageStats": "Folio {{currentPage}} of {{totalPages}} ({{totalCount}} inscriptions)",
    "autoRefreshingInterval": "Consulting the Archive every 30 seconds",
    "stats": {
      "totalProjects": "Total Crusades",
      "activeProjects": "Active Crusades",
      "completedTodos": "Charges Fulfilled",
      "archivedProjects": "Archived Crusades"
    },
    "recentActivity": "Recent Deeds"
  },
  "activityLog": {
    "title": "📜 Chronicle of Deeds",
    "autoRefreshOn": "Vigil: ON",
    "autoRefreshOff": "Vigil: OFF",
    "filters": {
      "allActivity": "All Deeds",
      "todosCreated": "Charges Pledged",
      "todosUpdated": "Charges Amended",
      "todosCompleted": "Charges Fulfilled",
      "todosDeleted": "Charges Expunged",
      "projectsCreated": "Crusades Declared",
      "projectsUpdated": "Crusades Amended",
      "projectsDeleted": "Crusades Dissolved",
      "all": "All Deeds",
      "create": "Pledged",
      "update": "Amended",
      "complete": "Fulfilled",
      "delete": "Expunged"
    },
    "unifiedView": "🌐 Order-wide View",
    "personalView": "👤 Personal Vigil",
    "showingAllDatabases": "Consulting all chapter archives",
    "showingPersonalOnly": "Showing your personal vigil only",
    "filteredByProject": "Filtered by crusade:",
    "noLogsFound": "No deeds recorded in the Archive",
    "tryChangingFilter": "Alter thy filter",
    "startCreatingTodos": "Pledge a charge to begin inscribing deeds",
    "failedToLoad": "Chronicle failed to open: {{error}}",
    "changesMade": "Amendments made:",
    "completionNotes": "Fulfillment notes:",
    "revertOperation": "Recant {{operation}}",
    "revertSuccess": "{{operation}} recanted successfully",
    "revertFailed": "Recantation failed: {{error}}",
    "revertDeleteNotSupported": "Recanting expungement is not permitted — inscription is gone",
    "revertNotSupported": "Recantation not permitted for {{operation}}",
    "confirmRevert": "Confirm Recantation",
    "confirmRevertMessage": "Recant {{operation}} on: {{description}}?",
    "confirmRevertAction": "Recant",
    "operationType": "Deed Type",
    "taskDescription": "Charge Description",
    "descriptions": {
      "projectCreated": "Crusade \"{{projectName}}\" declared",
      "projectUpdated": "Crusade \"{{projectName}}\" amended",
      "projectDeleted": "Crusade \"{{projectName}}\" dissolved",
      "projectModified": "Crusade \"{{projectName}}\" reconfigured",
      "unknownTask": "Deed unknown"
    },
    "showingPageStats": "Folio {{currentPage}} of {{totalPages}} ({{totalCount}} total inscriptions)",
    "autoRefreshingInterval": " • Consulting the Archive every 30s",
    "emptyState": {
      "title": "The chronicle stands empty",
      "message": "Begin your vigil — pledge a charge to inscribe the first deed"
    },
    "events": {
      "created": "pledged",
      "updated": "amended",
      "completed": "fulfilled",
      "deleted": "expunged"
    },
    "ago": "ago",
    "stats": {
      "total": "Total Deeds",
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
      "allLessons": "All Chronicles",
      "bookmarked": "Marked",
      "recent": "Recent (7 days)"
    },
    "actions": {
      "starred": "Marked",
      "addStar": "Mark"
    },
    "pagination": {
      "showingRange": "Showing {{start}}-{{end}} of {{total}} chronicles"
    },
    "dialog": {
      "topicLabel": "Subject",
      "lessonLabel": "Chronicle Entry",
      "languageLabel": "Language",
      "tagsLabel": "Seals (comma separated)",
      "tagsPlaceholder": "react, ui, logging",
      "databaseLabel": "Inscribe to Archive",
      "personalDatabase": "👤 Personal Archive",
      "sharedDatabase": "🌐 Chapter Archive (swarmonomicon)",
      "updateLesson": "Amend Chronicle",
      "createLesson": "Inscribe Entry"
    },
    "failedToLoad": "Archive failed to open: {{error}}",
    "confirmDelete": "Expunge this chronicle entry from the Archive?"
  },
  "app": {
    "titleShort": "Madness Interactive",
    "titleLong": "Madness Interactive Workshop"
  },
  "panels": {
    "aiChat": "🤖 Order Oracle",
    "projects": "📂 Crusades",
    "swarmDesk": "🎪 War Council",
    "chatAudit": "📜 Audit",
    "settings": "⚔️ Chapter Config",
    "mindMap": "🗺️ Battle Map"
  },
  "labMaintenance": {
    "tabs": {
      "duplicates": "Duplicate Charges"
    },
    "duplicates": {
      "title": "Duplicate Charge Detection",
      "description": "Find and consolidate near-duplicate charges across crusades.",
      "threshold": "Similarity",
      "scan": "Seek",
      "scanning": "Consulting the Archive…",
      "noResults": "No duplicate charges found at this threshold.",
      "groupsFound": "groups",
      "potentialDuplicates": "charges",
      "analyzeAI": "Seek Counsel",
      "analyzing": "Consulting the Oracle…",
      "aiComplete": "Counsel received. Review recommendations below.",
      "aiUnavailable": "Oracle counsel temporarily unavailable.",
      "recommendations": "Oracle Counsel",
      "keep": "Retain",
      "merge": "Unite",
      "deleteLabel": "Expunge",
      "suggestedDescription": "Proposed",
      "reasoning": "Rationale",
      "apply": "Apply",
      "applyAll": "Apply All",
      "applied": "Counsel applied",
      "selectGroupsFirst": "Select charge groups to examine"
    },
    "sessionResolved": "resolved this vigil"
  },
  "demo": {
    "label": "PILGRIM MODE"
  },
  "menu": {
    "documentation": "Chronicles",
    "replayTutorial": "Replay Rite of Entry",
    "userManagement": "Knight Rolls",
    "github": "GitHub",
    "themeGallery": "Theme Gallery",
    "logout": "Depart",
    "support": "Chapter Support",
    "lessonRefiner": "Chronicle Refiner"
  },
  "notifications": {
    "taskCreated": "🎉 Charge pledged to the roster.",
    "projectCreated": "⚔️ New crusade declared in the Archive."
  },
  "projectNavigator": {
    "subtitle": "Select your crusade • Enter focused vigil environments",
    "cacheStatus": "📜 Cached • Last consulted: {{time}}",
    "keyboardShortcuts": "⌨️ Arrow keys: Navigate • Enter/Space: Select • R: Renew • M: Main War Council • 1-9: Quick select",
    "manageTooltip": {
      "admin": "Manage Crusades (Grand Master)",
      "personal": "Manage Personal Crusades"
    },
    "refreshTooltip": "Renew from Archive",
    "mainSwarmDeskTooltip": "Enter Main War Council",
    "loading": {
      "title": "📜 Consulting the Archive…",
      "subtitle": "Gathering charge tallies and crusade records"
    },
    "stats": {
      "pending": "pending",
      "review": "examination"
    },
    "activity": {
      "title": "Recent Deeds",
      "noActivity": "No recent deeds recorded"
    },
    "enterButton": {
      "selected": "📦 PLEDGED",
      "enter": "⚔️ RIDE FORTH",
      "helpText": "Press Enter or #{{number}}"
    },
    "createCta": {
      "title": "Declare New Crusade",
      "subtitle": "The chapter house awaits — declare a new holy mission"
    },
    "deleteDialog": {
      "title": "Dissolve Crusade",
      "confirm": "Dissolve crusade \"{{projectName}}\"?",
      "graveyardNote": "The crusade shall be archived. You may restore it later if need arises.",
      "hasTodos": "This crusade bears {{count}} charge(s). Shall they be reassigned?",
      "relocateLabel": "Reassign charges to another crusade",
      "selectDestination": "Select destination crusade",
      "cancel": "Withdraw",
      "deleteButton": "Dissolve Crusade"
    },
    "viewInSwarmDesk": "View in War Council"
  },
  "projectSwarmdesk": {
    "title": "⚔️ {{projectName}}",
    "stats": {
      "pendingTasks": "{{count}} pending",
      "completedTasks": "{{count}} fulfilled"
    },
    "loading": "⚔️ Entering {{projectId}} Chapter…",
    "controls": "🎮 WASD: Move | Mouse Drag: Look | ESC: Depart Chapter",
    "workstation": {
      "todoHint": "📜 Click to tend to chapter charges",
      "projectHint": "⚔️ Click to view crusade details"
    },
    "statsPanel": {
      "title": "Crusade Tally",
      "pending": "Pending",
      "completed": "Fulfilled",
      "blocked": "Hindered",
      "review": "Examination"
    },
    "todoPanel": {
      "title": "Charge Roster",
      "empty": "The roster stands empty — no charges pledged.",
      "loading": "Consulting the Archive…",
      "create": "Pledge Charge"
    },
    "exitButton": "Depart Chapter",
    "error": "Failed to enter chapter: {{error}}"
  },
  "projectTab": {
    "noActiveProject": "No active crusade",
    "selectProject": "Select a crusade from the navigator",
    "overview": {
      "description": "No brief inscribed",
      "noRepository": "No archive linked",
      "todos": "Open Charges",
      "completedTodos": "Fulfilled Charges",
      "lessons": "Chronicle Entries",
      "created": "Declared",
      "updated": "Last Amended"
    },
    "actions": {
      "openSwarmDesk": "Open War Council",
      "editProject": "Amend Crusade",
      "deleteProject": "Dissolve Crusade"
    },
    "deleteDialog": {
      "title": "Dissolve Crusade",
      "message": "Dissolve crusade \"{{projectName}}\"? This cannot be undone.",
      "confirm": "Dissolve",
      "cancel": "Withdraw"
    }
  },
  "todoList": {
    "title": "📜 Charge Roster",
    "buttons": {
      "complete": "Fulfill",
      "edit": "Amend Charge",
      "delete": "Expunge",
      "view": "Examine",
      "flag": "Mark",
      "move": "Reassign",
      "clone": "Transcribe",
      "refresh": "Renew",
      "export": "Transcribe Records",
      "saving": "Inscribing…",
      "saveChanges": "Inscribe Changes",
      "discard": "Withdraw",
      "copyId": "Copy Sigil",
      "copyJiraCmd": "Copy Writ",
      "share": "Share",
      "review": "Examine",
      "aiInsights": "Seek Counsel"
    },
    "filters": {
      "all": "All Charges",
      "pending": "Pending",
      "inProgress": "In Progress",
      "completed": "Fulfilled",
      "blocked": "Hindered",
      "review": "Examination",
      "in_progress": "In Progress"
    },
    "sort": {
      "newest": "Newest",
      "oldest": "Oldest",
      "priority": "Priority",
      "alphabetical": "Alphabetical",
      "updated": "Recently Amended",
      "madness": "By Providence"
    },
    "priority": {
      "critical": "Urgent",
      "high": "High",
      "medium": "Medium",
      "low": "Low",
      "none": "Unsworn"
    },
    "status": {
      "pending": "Pending",
      "inProgress": "In Progress",
      "completed": "Fulfilled",
      "blocked": "Hindered",
      "review": "Examination",
      "initial": "Forming",
      "in_progress": "In Progress"
    },
    "empty": {
      "title": "The roster stands empty",
      "message": "No charges pledged. Pledge your first charge to begin.",
      "noResults": "No charges match the current filter.",
      "filtered": "No matching charges",
      "noMatching": "No Matching Charges",
      "workshopClear": "Roster Clear",
      "noMatchingDescription": "No charges match \"{{searchText}}\". Adjust thy search or filters.",
      "workshopClearDescription": "No charges found. The roster is clear and in good order."
    },
    "loading": "Consulting the Archive…",
    "loadingMore": "Consulting further folios…",
    "loadMore": "Load More",
    "count": "{{count}} charge(s)",
    "selected": "{{count}} selected",
    "selectAll": "Select All",
    "deselectAll": "Deselect All",
    "bulkActions": {
      "complete": "Fulfill Selected",
      "delete": "Expunge Selected",
      "move": "Reassign Selected",
      "export": "Transcribe Records"
    },
    "dragHint": "Drag to reorder roster",
    "dropHere": "Drop here",
    "search": {
      "placeholder": "Seek in the Archive…",
      "clear": "Clear Seeking",
      "noResults": "No charges match this seeking"
    },
    "pagination": {
      "showing": "Showing {{start}}-{{end}} of {{total}}",
      "page": "Folio {{current}} of {{total}}",
      "prev": "Previous",
      "next": "Next",
      "show": "Show",
      "perPage": "per folio",
      "all": "All",
      "results": "inscriptions"
    },
    "results": {
      "showing": "Showing {{start}}-{{end}} of {{total}} charges",
      "matching": " matching \"{{searchText}}\"",
      "filteringByProject": "Filtered by crusade: <strong>{{project}}</strong>",
      "filteringByProjects": "Filtered by {{count}} crusade(s)"
    },
    "project": {
      "label": "Crusade",
      "allProjects": "All Crusades ({{count}})",
      "clearFilter": "Clear Filter",
      "clearAll": "Clear all"
    },
    "createFirst": "Pledge your first charge",
    "noTasks": "The roster stands empty — no charges pledged.",
    "actions": {
      "markComplete": "Fulfill",
      "sendToReview": "Send for Examination",
      "reopen": "Reopen",
      "prioritize": "Raise Priority",
      "archive": "Archive",
      "unarchive": "Restore",
      "markPending": "Mark Pending",
      "edit": "Amend Charge",
      "delete": "Expunge Charge"
    },
    "timestamps": {
      "created": "Pledged",
      "updated": "Amended",
      "completed": "Fulfilled",
      "due": "Due"
    },
    "tags": {
      "add": "Add Seal",
      "remove": "Remove Seal",
      "none": "No seals"
    },
    "notes": {
      "add": "Add Annotation",
      "edit": "Amend Annotation",
      "none": "No annotations inscribed"
    },
    "project": {
      "select": "Assign Crusade",
      "change": "Reassign",
      "none": "No crusade assigned"
    },
    "assignee": {
      "select": "Assign Knight",
      "change": "Reassign",
      "none": "Unassigned"
    },
    "dueDate": {
      "set": "Set Due Date",
      "change": "Amend Due Date",
      "none": "No due date",
      "overdue": "Past due",
      "today": "Due today",
      "tomorrow": "Due tomorrow"
    },
    "confirmDelete": {
      "title": "Expunge Charge",
      "message": "Expunge \"{{title}}\" from the Archive? This cannot be undone.",
      "confirm": "Expunge",
      "cancel": "Withdraw"
    },
    "moveDialog": {
      "title": "Reassign Charge",
      "selectProject": "Select destination crusade",
      "confirm": "Reassign",
      "cancel": "Withdraw"
    },
    "completionDialog": {
      "title": "Fulfill Charge",
      "notesLabel": "Fulfillment notes (optional)",
      "confirm": "Fulfill",
      "cancel": "Withdraw"
    },
    "dialog": {
      "completeTitle": "Fulfill Charge: {{description}}",
      "completeDescription": "Add an optional fulfillment note (how the charge was met, time taken, obstacles overcome, etc.)",
      "completePlaceholder": "e.g., Completed the rite by updating the sacred scrolls. Two hours — much deliberation with the council.",
      "cancel": "Withdraw",
      "completeTask": "Fulfill Charge",
      "exportTitle": "Transcribe Charge Records",
      "exportDescription": "Transcribing {{count}} charges",
      "exportFilename": "Scroll Name",
      "exportFilenameHelp": "Name of the transcribed scroll (extension added automatically)",
      "exportFormat": "Format",
      "exportButton": "Transcribe",
      "formatJSON": "JSON — Structured Data",
      "formatJSONDesc": "Complete charge data in JSON format for re-import",
      "formatCSV": "CSV — Tabular Scroll",
      "formatCSVDesc": "Spreadsheet-compatible format for Excel or Google Sheets",
      "formatMarkdown": "Markdown — Readable Scroll",
      "formatMarkdownDesc": "Human-readable format for documentation",
      "formatHTML": "HTML — Web Illumination",
      "formatHTMLDesc": "Styled web page for browser viewing",
      "formatJira": "Jira/Slack Writs",
      "formatJiraDesc": "Ready-to-paste Slack commands for Jira writs",
      "formatVariant": "Scroll Variant",
      "variantPretty": "Illuminated (Readable)",
      "variantMinified": "Compact",
      "variantJSONL": "JSON Lines (Stream)",
      "variantStandard": "Standard",
      "variantExcel": "Excel-Optimized",
      "variantTable": "Table View",
      "selectFields": "Select Fields",
      "customizeFields": "Customize Field Names",
      "renameFields": "Rename Fields",
      "calculatedFields": "Calculated Fields",
      "fieldName": "Field Name",
      "addCalculatedField": "Add Calculated Field",
      "formula": {
        "ageInDays": "Age (days)",
        "daysSinceUpdate": "Days since amendment",
        "charCount": "Character count",
        "tokenEstimate": "Token estimate",
        "timeToComplete": "Time to fulfill"
      },
      "selectAll": "All",
      "selectNone": "None",
      "advancedFilters": "Advanced Filters",
      "dateRange": "Date Range",
      "startDate": "From",
      "priorityFilter": "Priority",
      "statusFilter": "Status"
    },
    "fullEdit": {
      "modeTitle": "Full Amendment Mode"
    },
    "menu": {
      "editTask": "Amend Charge",
      "copyId": "Copy Sigil",
      "copyJiraCmd": "Copy Writ",
      "share": "Share",
      "deleteTask": "Expunge Charge"
    },
    "fields": {
      "description": "Description",
      "project": "Crusade",
      "priority": "Priority",
      "status": "Status",
      "target": "Target",
      "created": "Pledged",
      "updated": "Amended",
      "metadata": "Annotations",
      "source": "Source",
      "notes": "Notes",
      "ticket": "Writ",
      "completed_at": "Fulfilled At",
      "completed_by": "Fulfilled By",
      "completion_comment": "Fulfillment Note",
      "duration": "Duration",
      "duration_sec": "Duration (seconds)",
      "tags": "Seals",
      "complexity": "Complexity",
      "confidence": "Confidence",
      "phase": "Phase",
      "epic": "Epic",
      "blockers": "Hindrances"
    },
    "validation": {
      "descriptionRequired": "Description cannot be empty",
      "descriptionTooLong": "Description must be less than 500 characters",
      "invalidProject": "Please select a valid crusade"
    },
    "error": {
      "failedToLoad": "Archive failed to open",
      "unknownError": "Unknown error",
      "malfunctionMessage": "The Archive encountered an error. Renew the connection or check your scroll."
    },
    "placeholders": {
      "setStatus": "Set status…",
      "editDescription": "Click to amend the charge description…",
      "selectProject": "Select crusade…",
      "setPriority": "Set priority…"
    },
    "tooltip": {
      "unsavedChanges": "You have uninscribed amendments"
    },
    "labels": {
      "readOnly": "🔒 Read-Only",
      "review": "EXAMINATION"
    },
    "aria": {
      "todoActions": "Charge actions"
    },
    "addTodo": "Pledge Charge",
    "emptyState": {
      "title": "The roster stands empty",
      "message": "Pledge your first charge to begin the vigil",
      "action": "Pledge Charge"
    },
    "errorLoading": "Archive failed to open: {{error}}",
    "errorUpdating": "Amendment failed: {{error}}",
    "errorDeleting": "Expungement failed: {{error}}",
    "successComplete": "Charge fulfilled",
    "successDelete": "Charge expunged",
    "successMove": "Charge reassigned",
    "aiEnhance": "Seek Counsel",
    "aiEnhancing": "Consulting the Oracle…",
    "spellsAvailable": "Oracle counsel available",
    "viewDetails": "Examine",
    "hideDetails": "Close Record",
    "expandAll": "Unfurl All",
    "collapseAll": "Fold All"
  },
  "todoEdit": {
    "title": "Amend Charge",
    "createTitle": "Pledge New Charge",
    "fields": {
      "description": "Charge Description",
      "priority": "Priority",
      "status": "Status",
      "notes": "Annotations",
      "tags": "Seals",
      "project": "Crusade",
      "assignee": "Assigned Knight",
      "dueDate": "Due Date"
    },
    "save": "Inscribe",
    "cancel": "Withdraw",
    "delete": "Expunge",
    "saving": "Inscribing…"
  },
  "settings": {
    "title": "⚙️ Chapter Configuration",
    "sections": {
      "appearance": "Appearance",
      "ai": "Oracle Integration",
      "notifications": "Vigil Alerts",
      "privacy": "Access Rites",
      "account": "Knight's Dossier",
      "advanced": "Advanced Rites",
      "about": "Chapter Records",
      "data": "Archive Management",
      "integrations": "Allegiances",
      "security": "Security Rites"
    },
    "theme": {
      "label": "Order Theme",
      "description": "Select the chapter's visual order"
    },
    "language": {
      "label": "Language",
      "description": "Chamber language"
    },
    "notifications": {
      "label": "Vigil Alerts",
      "description": "Enable chapter vigil alerts",
      "email": "Missive Alerts",
      "push": "Herald Alerts",
      "inApp": "In-Chamber Alerts"
    },
    "ai": {
      "label": "Oracle Integration",
      "description": "Configure the Oracle provider",
      "provider": "Provider",
      "apiKey": "Sigil Key",
      "model": "Oracle Model",
      "temperature": "Temperature",
      "maxTokens": "Max Tokens",
      "testConnection": "Test Connexion",
      "testing": "Testing…",
      "connected": "Connexion verified",
      "failed": "Connexion failed"
    },
    "privacy": {
      "label": "Access Rites",
      "description": "Manage access rites",
      "shareAnalytics": "Share usage records",
      "crashReports": "Submit incident reports"
    },
    "advanced": {
      "label": "Advanced Rites",
      "description": "Advanced chapter parameters",
      "debugMode": "Debug Mode",
      "experimentalFeatures": "Experimental Rites",
      "resetSettings": "Restore Covenant",
      "clearCache": "Purge Scriptorium",
      "exportData": "Transcribe Records",
      "importData": "Import Scrolls",
      "dangerZone": "Forbidden Reliquary"
    },
    "save": "Inscribe Config",
    "cancel": "Withdraw",
    "saved": "Configuration inscribed",
    "error": "Inscription failed",
    "reset": "Restore Covenant",
    "confirmReset": "Restore all configuration to the original covenant?",
    "tabs": {
      "general": "General",
      "ai": "Oracle",
      "appearance": "Appearance",
      "data": "Archive",
      "notifications": "Vigil",
      "security": "Security",
      "advanced": "Advanced",
      "profile": "Knight's Dossier",
      "aiConfiguration": "Oracle Config",
      "mcpSetup": "MCP Connexion",
      "messaging": "Missives",
      "apiKeys": "Sigil Keys",
      "mindMap": "Battle Map",
      "umlData": "Sacred Diagrams",
      "privacy": "Access Rites",
      "npcAgents": "Chapter Agents",
      "swarmDesk": "War Council",
      "keyboardShortcuts": "Shortcuts"
    },
    "autoSave": {
      "label": "Auto-inscribe changes",
      "description": "Automatically inscribe configuration changes"
    },
    "display": {
      "density": "Display Density",
      "compact": "Compact",
      "comfortable": "Comfortable",
      "spacious": "Spacious",
      "fontSize": "Font Size",
      "animations": "Animations",
      "reducedMotion": "Reduce motion"
    },
    "data": {
      "exportAll": "Transcribe Full Records",
      "importFile": "Import Scrolls",
      "clearAllData": "Purge All Records",
      "confirmClear": "Purge all records from the Archive? This cannot be undone.",
      "backupFrequency": "Transcription Frequency",
      "autoBackup": "Auto-transcribe"
    },
    "security": {
      "changePassword": "Change Passphrase",
      "twoFactor": "Two-Factor Rite",
      "sessions": "Active Vigils",
      "revokeAll": "Revoke All Vigils",
      "loginHistory": "Entry Chronicle"
    },
    "about": {
      "version": "Version",
      "build": "Build",
      "license": "Charter",
      "documentation": "Chronicles",
      "changelog": "Order Annals",
      "reportBug": "Report Incident",
      "featureRequest": "Request Rite"
    },
    "export": {
      "starting": "Beginning transcription…",
      "success": "Transcription complete! {{todoCount}} charges, {{projectCount}} crusades, and configuration recorded.",
      "error": "Transcription failed: {{error}}"
    },
    "import": {
      "starting": "Beginning import…",
      "confirmDialog": "Import Preview:\n\n{{todoCount}} charges, {{projectCount}} crusades, {{settingsCount}} configuration scrolls\n\nConflicts detected:\n{{conflicts}}\n\nProceed with import?",
      "success": "Import complete! {{importedCount}} inscriptions made. {{skippedCount}} items set aside.",
      "error": "Import failed: {{error}}",
      "fileDialogError": "Failed to open scroll dialog"
    },
    "swarmdesk": {
      "movementTitle": "Movement Speed Controls",
      "movementDescription": "Adjust camera movement in Orbital and FPS modes in the War Council 3D environment.",
      "resetDefaults": "Restore Defaults",
      "orbitalTitle": "Orbital Mode (O key)",
      "orbitalDescription": "Controls camera when using orbital navigation.",
      "orbitalBaseSpeed": "Base Speed",
      "orbitalSprintMultiplier": "Sprint Multiplier (Ctrl held)",
      "fpsTitle": "FPS Mode (F key)",
      "fpsDescription": "Controls camera when using first-person navigation.",
      "fpsBaseSpeed": "Walk Speed",
      "fpsSprintSpeed": "Sprint Speed (Ctrl held)"
    },
    "messaging": {
      "title": "Missive Roles Configuration",
      "subtitle": "Configure which roles are permitted in chapter missives.",
      "allowedRoles": "Permitted Roles",
      "addRole": "Add Role",
      "editRole": "Amend Role",
      "infoMessage": "These roles are available when composing missives. Each role may bear a unique sigil. Core roles can be hidden but not removed.",
      "roleId": "Role Sigil",
      "roleIdHelper": "Lowercase, alphanumeric, and hyphens only (e.g., 'gpt-4', 'custom-ai')",
      "roleIdDisabled": "Role sigil cannot be changed"
    }
  },
  "umlData": {
    "title": "🗺️ Sacred Diagrams",
    "loading": "Consulting the diagrams…",
    "noData": "No diagrams inscribed. Scribe your first diagram.",
    "generate": "Scribe Diagram",
    "generating": "Scribing…",
    "upload": "Present Diagram",
    "uploading": "Presenting…",
    "download": "Transcribe Copy",
    "delete": "Expunge",
    "confirmDelete": "Expunge this diagram from the Archive?",
    "version": "Version",
    "versions": "Versions",
    "noVersions": "No versions inscribed",
    "compareVersions": "Compare Versions",
    "currentVersion": "Present",
    "previousVersion": "Prior",
    "diff": "Compare View",
    "timeline": "Version Chronicle",
    "restore": "Restore Version",
    "confirmRestore": "Restore this version of the diagram?",
    "empty": {
      "title": "No diagrams inscribed",
      "message": "Scribe a diagram to illuminate the project's architecture.",
      "action": "Scribe First Diagram"
    },
    "metadata": {
      "created": "Inscribed",
      "size": "Size",
      "nodes": "Nodes",
      "edges": "Connections",
      "language": "Language",
      "framework": "Framework"
    },
    "filters": {
      "all": "All Diagrams",
      "recent": "Recent",
      "language": "By Language"
    },
    "error": {
      "generate": "Scribing failed: {{error}}",
      "upload": "Presentation failed: {{error}}",
      "load": "Archive failed to open: {{error}}"
    },
    "success": {
      "generated": "Diagram scribed",
      "uploaded": "Diagram presented to Archive",
      "deleted": "Diagram expunged",
      "restored": "Version restored"
    },
    "repoUrl": "Repository URL",
    "branch": "Branch",
    "depth": "Analysis Depth",
    "generateFromRepo": "Scribe from Repository",
    "delete": {
      "confirmTitle": "Expunge Diagram",
      "confirmMessage": "Expunge this diagram from the Archive? This cannot be undone.",
      "success": "Diagram expunged from Archive"
    }
  },
  "editableTodoCard": {
    "placeholder": "Charge description…",
    "saving": "Inscribing…",
    "saved": "Inscribed",
    "error": "Inscription failed",
    "editMode": "Amendment Mode",
    "viewMode": "Examination Mode",
    "actions": {
      "edit": "Amend Charge",
      "save": "Inscribe",
      "cancel": "Withdraw",
      "delete": "Expunge",
      "complete": "Fulfill",
      "move": "Reassign",
      "clone": "Transcribe",
      "flag": "Mark",
      "unflag": "Unmark",
      "pin": "Pin",
      "unpin": "Unpin",
      "share": "Share",
      "view": "Examine"
    },
    "status": {
      "pending": "Pending",
      "inProgress": "In Progress",
      "completed": "Fulfilled",
      "blocked": "Hindered",
      "review": "Examination"
    },
    "priority": {
      "critical": "Urgent",
      "high": "High",
      "medium": "Medium",
      "low": "Low"
    },
    "fields": {
      "description": "Description",
      "notes": "Annotations",
      "tags": "Seals",
      "priority": "Priority",
      "status": "Status",
      "project": "Crusade",
      "dueDate": "Due Date"
    },
    "confirmDelete": {
      "title": "Expunge Charge",
      "message": "Expunge this charge from the Archive?",
      "confirm": "Expunge",
      "cancel": "Withdraw"
    }
  },
  "mindMap": {
    "title": "🗺️ Battle Map",
    "loading": "Consulting the battle map…",
    "empty": {
      "title": "The map stands empty",
      "message": "Pledge charges and declare crusades to illuminate the battle map.",
      "action": "Pledge First Charge"
    },
    "controls": {
      "zoomIn": "Zoom In",
      "zoomOut": "Zoom Out",
      "reset": "Restore View",
      "center": "Center View",
      "fit": "Fit to Chamber",
      "fullscreen": "Full Chamber",
      "exitFullscreen": "Depart Full Chamber"
    },
    "nodes": {
      "todo": "Charge",
      "project": "Crusade",
      "lesson": "Chronicle",
      "tag": "Seal"
    },
    "filters": {
      "all": "All Nodes",
      "todos": "Charges Only",
      "projects": "Crusades Only",
      "tags": "Seals Only"
    },
    "layout": {
      "force": "Force Layout",
      "tree": "Tree Layout",
      "radial": "Radial Layout",
      "grid": "Grid Layout"
    },
    "export": {
      "png": "Transcribe PNG",
      "svg": "Transcribe SVG",
      "json": "Transcribe JSON"
    },
    "error": "Battle map failed to illuminate: {{error}}",
    "refresh": "Renew Battle Map",
    "addNode": "Add Node",
    "editNode": "Amend Node",
    "deleteNode": "Expunge Node",
    "connectNodes": "Link Nodes",
    "disconnectNodes": "Sever Link"
  },
  "chatAssistant": {
    "title": "⚔️ Order Oracle",
    "placeholder": "Seek counsel from the Oracle…",
    "send": "Send",
    "sending": "Conveying…",
    "loading": "Consulting the Archive…",
    "empty": {
      "title": "The Oracle awaits",
      "message": "Pose a question or seek interpretation.",
      "suggestion": "Try: 'What charges are hindered?'"
    },
    "error": {
      "send": "Conveyance failed: {{error}}",
      "load": "Consultation failed: {{error}}"
    },
    "actions": {
      "copy": "Transcribe",
      "retry": "Retry",
      "delete": "Remove",
      "feedback": {
        "good": "Useful",
        "bad": "Not Useful"
      }
    },
    "system": "Order",
    "you": "Knight",
    "ai": "Oracle",
    "typing": "Deliberating…",
    "newConversation": "New Audience",
    "clearHistory": "Purge Chronicle",
    "confirmClear": "Purge all audience chronicles?",
    "history": "Audience Chronicles",
    "noHistory": "No audience chronicles",
    "tools": {
      "listTodos": "List Charges",
      "createTodo": "Pledge Charge",
      "analyzeTodos": "Seek Counsel",
      "searchTodos": "Seek in Archive"
    },
    "suggestions": {
      "listAll": "List all open charges",
      "critical": "Show urgent charges",
      "blocked": "What is hindered?",
      "insights": "Seek counsel on this crusade"
    }
  },
  "mobileChatInterface": {
    "title": "Order Oracle",
    "placeholder": "Seek counsel…",
    "send": "Convey",
    "voiceInput": "Voice Proclamation",
    "stopVoice": "Cease Proclamation",
    "attachFile": "Attach Scroll",
    "loading": "Consulting the Archive…",
    "empty": {
      "title": "The Oracle awaits",
      "message": "Pose a question or seek interpretation."
    },
    "error": "Conveyance failed",
    "newSession": "New Audience",
    "clearHistory": "Purge Chronicles",
    "historyTitle": "Audience Chronicles",
    "noHistory": "No audience chronicles",
    "close": "Seal Chamber",
    "minimize": "Minimize",
    "expand": "Unfurl",
    "connectionStatus": {
      "connected": "Connected",
      "disconnected": "Disconnected",
      "reconnecting": "Reconnecting…"
    }
  },
  "warRoom": {
    "title": "⚔️ War Council",
    "loading": "Consulting the war council…",
    "empty": {
      "title": "The council chamber is peaceful",
      "message": "No active conflicts. The order stands at peace.",
      "action": "Open Incident"
    },
    "incident": {
      "create": "Declare Conflict",
      "resolve": "Resolve Conflict",
      "escalate": "Escalate",
      "assign": "Assign Knight",
      "priority": "Urgency",
      "status": "Status"
    },
    "filters": {
      "all": "All Conflicts",
      "active": "Active",
      "resolved": "Resolved"
    },
    "error": "War council failed to convene: {{error}}",
    "refresh": "Renew"
  },
  "swarmDesk": {
    "title": "⚔️ War Council",
    "loading": "Consulting the Archive…",
    "controls": {
      "move": "Move",
      "rotate": "Rotate",
      "zoom": "Zoom",
      "reset": "Restore View",
      "fullscreen": "Full Chamber",
      "exitFullscreen": "Depart Full Chamber"
    },
    "panels": {
      "todos": "Charge Roster",
      "projects": "Crusades",
      "chat": "Oracle",
      "insights": "Counsel",
      "settings": "Chapter Config"
    },
    "nodes": {
      "create": "Pledge Charge",
      "edit": "Amend Charge",
      "delete": "Expunge",
      "complete": "Fulfill",
      "move": "Reassign",
      "view": "Examine"
    },
    "empty": {
      "title": "The council chamber stands empty",
      "message": "Pledge a charge to populate the war council."
    },
    "error": "War council failed: {{error}}",
    "status": {
      "connected": "Connected to Archive",
      "disconnected": "Archive disconnected",
      "syncing": "Consulting…",
      "synced": "Consulted"
    },
    "hotkeys": {
      "title": "Shortcut Reference",
      "wasd": "WASD: Navigate",
      "mouse": "Mouse: Look",
      "escape": "ESC: Depart",
      "tab": "TAB: Switch Chamber",
      "space": "Space: Select"
    },
    "filters": {
      "all": "All Charges",
      "pending": "Pending",
      "inProgress": "In Progress",
      "blocked": "Hindered",
      "review": "Examination"
    },
    "sort": {
      "priority": "Priority",
      "updated": "Recently Amended",
      "created": "Date Pledged",
      "name": "Alphabetical"
    },
    "createTodo": {
      "title": "Pledge New Charge",
      "placeholder": "Charge description…",
      "submit": "Pledge Charge",
      "cancel": "Withdraw"
    },
    "todoPanel": {
      "title": "Charge Roster",
      "empty": "The roster stands empty.",
      "loading": "Consulting the Archive…"
    },
    "projectPanel": {
      "title": "Active Crusades",
      "empty": "No crusades declared.",
      "loading": "Consulting crusade records…",
      "create": "Declare Crusade",
      "select": "Select Crusade",
      "selected": "Active: {{name}}"
    },
    "agentPanel": {
      "title": "Knight Status",
      "empty": "No knights registered.",
      "loading": "Consulting chapter rolls…",
      "status": {
        "active": "Active",
        "idle": "At Rest",
        "offline": "Absent"
      }
    },
    "chatPanel": {
      "title": "Oracle Counsel",
      "placeholder": "Seek…",
      "send": "Convey",
      "loading": "Consulting…"
    },
    "notifications": {
      "todoCreated": "Charge pledged",
      "todoCompleted": "Charge fulfilled",
      "todoDeleted": "Charge expunged",
      "projectCreated": "Crusade declared",
      "syncComplete": "Archive consulted"
    },
    "tour": {
      "welcome": "Welcome to the War Council",
      "navigation": "WASD to navigate, mouse to look",
      "interaction": "Click nodes to tend to charges",
      "panels": "Use chambers to examine charges and seek counsel",
      "complete": "War council ready"
    },
    "ui": {
      "loading": {
        "entering": "⚔️ Entering Chapter House…",
        "initializing": "⚔️ Preparing War Council…",
        "ready": "✅ Council Ready",
        "connecting": "🔗 Joining the Chapter…",
        "loadingProjects": "📜 Consulting Crusade Records…",
        "title": "⚔️ Assembling War Council…",
        "subtitle": "Preparing the Chapter House"
      },
      "navigation": {
        "controls": "⌨️ Navigation Controls",
        "movement": "⌨️ WASD: Move | Mouse: Look",
        "interaction": "🖱️ Click: Tend | E: Action | Space: Quick Action",
        "escape": "🚪 ESC: Return to Dashboard | M: Menu"
      },
      "status": {
        "connected": "🌐 Chapter: CONNECTED",
        "offline": "⚠️ Chapter: OFFLINE — Local Vigil",
        "syncing": "🔄 Consulting Archive…",
        "ready": "✅ War Council: READY"
      },
      "error": {
        "title": "❌ War Council Error",
        "subtitle": "Consult the chapter scribe for details",
        "initializationFailed": "War Council failed to assemble"
      },
      "controls": {
        "instructions": "⚔️ War Council Active | WASD: Navigate | E: Tend | F4-F7: Open Chambers | Space: Swift Mode"
      }
    },
    "panels": {
      "welcome": {
        "title": "⚔️ Welcome to the War Council",
        "subtitle": "Chapter House Ready",
        "description": "Welcome to the War Council — the 3D chapter house for managing your crusades and charges.",
        "gettingStarted": "Getting started:",
        "features": {
          "title": "🎯 Chapter Features:",
          "draggable": "📱 Draggable chambers with magnetic docking",
          "contextual": "🏷️ Contextual chambers respond to interactions",
          "docking": "🧲 Docking zones at chapter edges",
          "shortcuts": "⌨️ Keyboard shortcuts for swift access",
          "integration": "⚔️ Full War Council 3D integration"
        },
        "actions": {
          "createProject": "📜 Open Crusade Chamber",
          "createAgent": "⚔️ Open Knight Chamber"
        }
      },
      "shortcuts": {
        "title": "⌨️ Keyboard Shortcuts",
        "subtitle": "Quick Reference",
        "categories": {
          "navigation": {
            "title": "🧭 Navigation"
          },
          "panels": {
            "title": "📜 Chamber Controls"
          },
          "actions": {
            "title": "⚡ Actions"
          }
        },
        "f3": "F3 — Toggle Welcome Chamber",
        "f4": "F4 — Toggle Crusade Chamber",
        "f5": "F5 — Toggle Knight Chamber",
        "f6": "F6 — Toggle Chapter Tools",
        "f7": "F7 — Toggle Oracle Chamber",
        "f8": "F8 — Toggle Grimoire Chamber",
        "f9": "F9 — Toggle Herald Monitor",
        "f10": "F10 — Seal All Chambers",
        "f11": "F11 — Close All Chambers",
        "esc": "ESC — Withdraw from current action",
        "drag": "Drag chambers — Click and drag headers",
        "dock": "Dock chambers — Drag near edges to anchor"
      },
      "mcp": {
        "title": "🔗 Oracle Protocol Hub",
        "subtitle": "Service Connexion Layer",
        "description": "The Oracle Protocol enables connexions to external orders and services for enhanced counsel.",
        "gettingStarted": "Setup instructions:",
        "tools": {
          "title": "🛠️ Available Oracle Tools",
          "notAuthenticated": "Authenticate to access Oracle tools.",
          "authRequired": "Authentication required to connect to Oracle services",
          "connecting": "No tools available. Joining the chapter…",
          "serverStatus": "Oracle Status: {{status}}",
          "retryConnection": "🔄 Retry Connexion",
          "connectedAs": "Connected as: {{username}}"
        },
        "history": {
          "title": "📜 Counsel Chronicle",
          "noHistory": "No counsel recorded."
        },
        "debug": {
          "title": "🐛 Chapter Debug",
          "authentication": "Authentication: {{status}}",
          "user": "Knight: {{user}}",
          "authMode": "Mode: {{mode}}",
          "mcpServer": "Oracle Server: {{status}}",
          "activeTools": "Active Oracle Tools: {{count}}",
          "lastPing": "Last Signal: {{time}}",
          "apiService": "API Service: {{status}}",
          "authContext": "Auth Context: {{status}}",
          "refreshAuth": "🔄 Renew Auth"
        }
      },
      "project": {
        "overview": {
          "title": "📜 Crusade Overview",
          "activeProjects": "Active Crusades: 5",
          "pendingTasks": "Pending Charges: 23",
          "completedToday": "Fulfilled Today: 7",
          "actions": {
            "viewAll": "📜 View All Crusades",
            "addTask": "⚔️ Pledge Charge"
          }
        },
        "todos": {
          "title": "✅ Charge Roster",
          "inProgress": "⚔️ Chapter House — In Progress",
          "pending": "📜 Oracle Protocol — Pending",
          "actions": {
            "addTodo": "⚔️ Pledge Charge"
          }
        },
        "files": {
          "title": "📁 Sacred Scrolls",
          "actions": {
            "browse": "📂 Browse the Scriptorium"
          }
        }
      },
      "agent": {
        "chat": {
          "title": "💬 Knight Channel",
          "agentReady": "Knight: Ready for your bidding.",
          "userQuery": "Knight: Aid me with the floating chambers",
          "agentResponse": "Knight: The chamber system is most flexible — drag anywhere and anchor to the walls.",
          "placeholder": "Pose your query…"
        },
        "commands": {
          "title": "⚡ Knight Commands",
          "searchProjects": "🔍 Seek Crusades",
          "listTodos": "📜 List Charges",
          "deployProject": "⚔️ Ride Forth",
          "generateReport": "📜 Generate Chronicle"
        },
        "interface": {
          "title": "💬 {{agentName}} Knight Interface",
          "role": "Role: {{role}}",
          "status": "Status: {{status}}",
          "actions": {
            "startConversation": "💬 Open Channel",
            "executeCommand": "⚔️ Execute Command"
          }
        },
        "capabilities": {
          "title": "⚡ Knight Capabilities",
          "projectManagement": "✅ Crusade Management",
          "codeAnalysis": "✅ Scroll Analysis",
          "mcpIntegration": "✅ Oracle Integration",
          "communication": "✅ Real-time Communication"
        }
      },
      "analytics": {
        "metrics": {
          "title": "📜 Chapter Performance",
          "cpuUsage": "Processing: 42%",
          "memory": "Memory: 68%",
          "activePanels": "Open Chambers: {{count}}",
          "uptime": "Vigil time: 2h 15m"
        },
        "activity": {
          "title": "⚔️ Recent Deeds",
          "panelCreated": "🏷️ Chamber opened: Crusade Management",
          "swarmDeskInteraction": "⚔️ War Council: Station selected",
          "mcpToolExecuted": "📜 Oracle tool invoked: list_projects"
        },
        "insights": {
          "title": "💡 Chapter Insights",
          "mostUsedPanel": "Most used chamber: Crusade Management",
          "peakActivity": "Peak activity: 14:00-15:00",
          "efficiencyScore": "Efficiency: 87%"
        }
      },
      "webllm": {
        "models": {
          "title": "🧠 Available Oracle Models",
          "currentModel": "Present Oracle: {{model}}",
          "loadModel": "Summon Model"
        },
        "compatibility": {
          "title": "✅ Chamber Compatibility",
          "checking": "🔄 Checking compatibility…",
          "checkCompatibility": "🔍 Check Compatibility"
        },
        "status": {
          "title": "⚡ Oracle Status",
          "initialized": "Summoned: {{status}}",
          "currentModel": "Present Oracle: {{model}}",
          "loading": "Summoning: {{status}}",
          "inferencing": "Deliberating: {{status}}",
          "queueLength": "Queue: {{length}}",
          "loadedModels": "Active Oracles: {{count}}",
          "mode": "Mode: {{mode}}",
          "initialize": "⚔️ Summon Oracle"
        },
        "settings": {
          "title": "⚙️ Oracle Configuration",
          "agentModelAssignment": "Knight Model Assignment:",
          "useGlobal": "Use Chapter Oracle",
          "perAgent": "Per-Knight Oracles",
          "temperature": "Temperature:",
          "maxTokens": "Max Tokens:",
          "saveSettings": "📜 Inscribe Config",
          "resetDefaults": "🔄 Restore Defaults"
        }
      },
      "mqtt": {
        "logs": {
          "title": "📜 Herald Feed",
          "noMessages": "No heralds received…",
          "waitingTraffic": "Awaiting herald traffic on port 4140",
          "reconnect": "🔄 Reconnect",
          "messages": "Heralds: {{count}}",
          "lastMessage": "Last: {{time}}",
          "clearLogs": "🗑️ Purge Feed",
          "export": "📜 Transcribe Archive"
        },
        "status": {
          "title": "🔌 Herald Connexion",
          "status": "Connexion: {{status}}",
          "broker": "Herald Post: {{broker}}",
          "clientId": "Sigil ID: swarmdesk_{{id}}",
          "messagesReceived": "Heralds Received: {{count}}",
          "lastActivity": "Last Activity: {{time}}",
          "subscriptions": "📡 Listening:",
          "connect": "🔄 Establish Connexion",
          "disconnect": "🔌 Sever Connexion"
        },
        "settings": {
          "title": "⚙️ Herald Configuration",
          "brokerAddress": "Herald Post Address:",
          "subscribeTopics": "Listen to Topics:",
          "autoReconnect": "Auto-reconnect on severance",
          "showTimestamps": "Show timestamps",
          "saveSettings": "📜 Inscribe Config",
          "resetDefaults": "🔄 Restore Defaults"
        }
      }
    },
    "projectData": {
      "title": "📜 Crusade Registry",
      "subtitle": "Crusade Management Hub",
      "description": "Sacred registry and chapter tools for organizing work and tracking progress.",
      "projectReadmes": {
        "inventorium": {
          "title": "📜 Inventorium — Chapter Dashboard",
          "description": "Charge and crusade management dashboard with integrated tools."
        },
        "omnispindle": {
          "title": "🔗 Omnispindle — Alliance Platform",
          "description": "Communication platform connecting chapter orders and services."
        }
      },
      "swarmDesk": {
        "title": "⚔️ War Council",
        "description": "3D chapter house — the sacred command environment",
        "status": "🔥 Active Development",
        "visibility": "public repository"
      },
      "inventorium": {
        "title": "📦 Inventorium",
        "description": "Charge management — track agents and their work in the sacred registry",
        "status": "⚔️ Active Development (private)",
        "visibility": "private chapter"
      },
      "swarmonomicon": {
        "title": "🐝 Swarmonomicon",
        "description": "Knight swarm coordination for collective intelligence and orchestration",
        "status": "✨ Modularly functional",
        "visibility": "public repository"
      }
    },
    "errors": {
      "connectionFailed": "❌ Connexion Failed",
      "loadingError": "⚠️ Consultation Error",
      "permissionDenied": "🔒 Access Denied",
      "systemUnavailable": "🚫 Chapter Unavailable",
      "unknownError": "❓ Unknown Error",
      "initializationFailed": "War Council failed to assemble within the allotted time",
      "sceneInitFailed": "❌ Scene failed to manifest:",
      "panelSystemFailed": "❌ Failed to erect chamber system:",
      "panelSystemMissing": "⚠️ Chamber system unavailable",
      "controlsInitFailed": "Failed to ready navigation controls:",
      "basicSceneFailed": "❌ Failed to manifest basic scene:"
    },
    "status": {
      "initializing": "⚙️ Assembling Council…",
      "loading": "📜 Consulting Registry…",
      "ready": "✅ Council Ready",
      "error": "❌ Council Error",
      "offline": "⚠️ Offline — Local Vigil",
      "initialized": "✅ War Council assembled",
      "scriptsLoaded": "✅ Council scripts loaded",
      "scriptsTimeout": "⚠️ Council scripts load timeout",
      "containerNotReady": "⚠️ Chapter house not ready",
      "panelSystemExists": "🏷️ Chamber system present — verifying",
      "panelSystemMissing": "⚠️ Chamber system missing — reassembling…",
      "panelSystemCreated": "✅ Chamber system erected"
    },
    "actions": {
      "create": "⚔️ Pledge",
      "view": "👁️ Examine",
      "edit": "📜 Amend Charge",
      "delete": "🗑️ Expunge",
      "refresh": "🔄 Renew",
      "connect": "🔗 Join Order",
      "deploy": "⚔️ Ride Forth",
      "monitor": "📜 Chronicle Progress",
      "optimize": "⚡ Refine Conduct",
      "analyze": "📜 Seek Counsel",
      "configure": "⚙️ Amend Configuration"
    }
  },
  "spells": {
    "title": "⚔️ Sacred Rites",
    "description": "Oracle-powered rites for charge management",
    "available": "Available rites",
    "noTodoSelected": "No charge selected",
    "availableSpells": "Available Rites",
    "keyboardShortcut": "Keyboard Shortcut",
    "estimatedTime": "Estimated Time",
    "accessDenied": {
      "title": "Access Denied",
      "description": "Thou dost not have the authority to perform these rites. Join the order or seek elevation."
    },
    "system": {
      "title": "Sacred Rite System"
    },
    "categories": {
      "enhance": "Enhance",
      "analyze": "Analyze",
      "consolidate": "Consolidate"
    },
    "enhance": {
      "title": "Enhance Charge",
      "description": "Invoke the Oracle to illuminate this charge",
      "button": "Enhance Charge",
      "casting": "Invoking…",
      "success": "Charge illuminated"
    },
    "geomancy": {
      "title": "Seek Patterns",
      "description": "Identify patterns and connexions",
      "button": "Seek Patterns",
      "casting": "Consulting the Oracle…",
      "success": "Patterns revealed"
    },
    "consolidate": {
      "title": "Unite Charges",
      "description": "Identify and unite duplicate charges",
      "button": "Seek Duplicates",
      "casting": "Seeking duplicate charges…",
      "success": "Charges united"
    },
    "effects": {
      "particles": "Sacred rite indicators active",
      "energy": "Rite in motion",
      "casting": "Invocation in progress",
      "complete": "Invocation complete"
    },
    "results": {
      "enhance": {
        "success": "📜 Charge illuminated by Oracle counsel!",
        "improvement": "Illumination applied to charge description",
        "insights": "Key revelations:",
        "suggestions": "Counsel:"
      },
      "geomancy": {
        "success": "🔍 Patterns revealed in crusade!",
        "insights": "Oracle findings:",
        "patterns": "Pattern analysis:",
        "recommendations": "Counsel:",
        "analysis": "Analysis complete"
      },
      "consolidate": {
        "success": "🔗 Duplicate charges united!",
        "merged": "{{count}} charges united",
        "candidates": "Unification candidates:",
        "preview": "Union preview:",
        "confirmation": "Proceed with unification?"
      },
      "title": "Rite Results",
      "latest": "Latest",
      "noResults": "No results yet. Invoke a rite to see results here.",
      "summary": "{{count}} rite results"
    },
    "errors": {
      "castingFailed": "Invocation failed: {{error}}",
      "noDescription": "Charge description required for illumination",
      "rateLimited": "Rite limit reached. Wait: {{timeRemaining}}",
      "aiError": "Oracle system error",
      "networkError": "Herald connexion error",
      "invalidSpell": "Unknown rite requested",
      "unauthorized": "Insufficient authority for this rite"
    },
    "rateLimit": {
      "enhance": "Illumination uses: {{used}}/{{limit}} remaining",
      "geomancy": "Pattern-seeking uses: {{used}}/{{limit}} remaining",
      "consolidate": "Unification uses: {{used}}/{{limit}} remaining",
      "resetTime": "Resets in: {{time}}",
      "depleted": "Rite limit reached"
    },
    "tooltip": {
      "castSpell": "Invoke sacred rite",
      "enhanceDescription": "Illuminate charge (Ctrl+E)",
      "performGeomancy": "Seek patterns (Ctrl+G)",
      "consolidateSimilar": "Find duplicates (Ctrl+C)",
      "spellHistory": "View rite chronicle",
      "clearHistory": "Purge rite chronicle"
    },
    "keyboard": {
      "shortcuts": "⌨️ Keyboard Shortcuts:",
      "enhance": "Ctrl+E — Illuminate Charge",
      "geomancy": "Ctrl+G — Seek Patterns",
      "consolidate": "Ctrl+C — Find Duplicates",
      "cancel": "Esc — Withdraw"
    },
    "history": {
      "timestamp": "Time:",
      "spellType": "Rite type:",
      "target": "Target charge:",
      "result": "Result:",
      "success": "✅ Successful",
      "failed": "❌ Failed",
      "duration": "Duration:",
      "empty": "No rites recorded",
      "toggle": "Toggle rite chronicle"
    },
    "status": {
      "idle": "Rites ready",
      "casting": "Invoking rite…",
      "processing": "Processing…",
      "complete": "Rite complete",
      "failed": "Rite failed",
      "cooldown": "Resting between rites…",
      "success": "Success"
    },
    "enhance_description": {
      "description": "Invoke the Oracle to illuminate this charge description",
      "button": "Illuminate Description",
      "casting": "Illuminating description…"
    },
    "perform_geomancy": {
      "description": "Seek patterns and connexions for this charge",
      "button": "Seek Patterns",
      "casting": "Consulting the Oracle…"
    },
    "consolidate_similar": {
      "description": "Find and unite similar charges to reduce duplication",
      "button": "Seek Similar",
      "casting": "Seeking similar charges…"
    },
    "tip": {
      "castMultiple": "Invoke multiple rites on one charge for deeper counsel"
    },
    "meta": {
      "maxPerHour": "Max invocations per hour",
      "lastCast": "Last invoked"
    },
    "result": {
      "confidence": "Confidence"
    },
    "error": {
      "unknown": "An unknown error occurred"
    },
    "enhanceDescription": {
      "result": {
        "title": "Illuminated Description",
        "before": "Before",
        "after": "After",
        "improvements": "Improvements"
      }
    },
    "performGeomancy": {
      "result": {
        "insights": "Revelations",
        "relatedProjects": "Related Crusades"
      },
      "insights": {
        "complexity": "Complexity",
        "duration": "Estimated Duration",
        "risks": "Risk Factors"
      }
    },
    "consolidateSimilar": {
      "found": "Found {{count}} similar charges",
      "result": {
        "consolidated": "United Description",
        "suggestions": "Union Suggestions"
      }
    }
  },
  "insights": {
    "loading": "Consulting the Oracle…",
    "tabs": {
      "overview": "Overview",
      "analytics": "Analytics",
      "systemLogs": "Chronicle"
    }
  },
  "admin": {
    "tabs": {
      "overview": "Overview",
      "users": "Knights",
      "analytics": "Analytics",
      "featureFlags": "Order Rites",
      "systemLogs": "Chapter Chronicle"
    },
    "overview": {
      "title": "Chapter Overview",
      "loading": "Consulting chapter records…",
      "refresh": "Renew from Archive",
      "fallback": "(showing mock data for development)",
      "totalUsers": "Total Knights",
      "totalUsersSubtitle": "All sworn knights",
      "activeUsers": "Active (7d)",
      "activeUsersSubtitle": "Knights active this week",
      "premiumUsers": "Senior Knights",
      "premiumUsersSubtitle": "Paid memberships",
      "errors": "Errors (24h)",
      "errorsSubtitle": "Chapter errors today",
      "tierDistribution": "Rank Distribution",
      "tier": {
        "free": "Initiate",
        "pro": "Knight",
        "premium": "Paladin",
        "admin": "Grand Master"
      },
      "productivity": "Chapter Productivity",
      "totalTodos": "Total Charges",
      "completedTodos": "Fulfilled",
      "completionRate": "Fulfillment Rate"
    },
    "analytics": {
      "title": "Advanced Analytics",
      "loading": "Consulting the Oracle…",
      "comingSoon": "Analytics Chamber Under Construction",
      "description": "Advanced chronicles and illuminations are being prepared. Check back soon.",
      "timeframe": {
        "day": "Last 24 Hours",
        "week": "Last 7 Days",
        "month": "Last 30 Days",
        "year": "Last 12 Months"
      },
      "futureHint": "Coming soon: Custom date ranges, scroll export, real-time updates, cohort analysis.",
      "charts": {
        "userGrowth": "Knight Growth",
        "userGrowthDesc": "New knight inductions over time",
        "activityHeatmap": "Activity Heatmap",
        "activityHeatmapDesc": "Knight activity by hour/day",
        "featureUsage": "Rite Usage",
        "featureUsageDesc": "Most-invoked rites",
        "performance": "Chapter Performance",
        "performanceDesc": "Response times and error rates"
      }
    },
    "logs": {
      "title": "Chapter Chronicle",
      "loading": "Consulting the chronicle…",
      "refresh": "Renew chronicle",
      "fallback": "(showing mock data for development)",
      "autoRefresh": "Vigil (30s)",
      "showing": "Showing",
      "entries": "inscriptions",
      "empty": "No inscriptions — the chapter stands in good order",
      "columns": {
        "timestamp": "Time",
        "level": "Level",
        "message": "Message",
        "user": "Knight",
        "endpoint": "Passage"
      },
      "severity": {
        "error": "ERROR",
        "warning": "WARNING",
        "info": "INFO"
      }
    },
    "featureFlags": {
      "title": "Order Rites",
      "loading": "Consulting order rites…",
      "refresh": "Renew rites",
      "fallback": "(showing mock data for development)",
      "lastUpdated": "Last updated",
      "unsavedChanges": "Uninscribed changes pending — will affect all knights on inscription.",
      "save": "Inscribe Changes",
      "cancel": "Withdraw",
      "saving": "Inscribing…",
      "confirmSave": "Apply Changes",
      "tiers": {
        "free": "Initiate Rank",
        "pro": "Knight Rank",
        "premium": "Paladin Rank",
        "admin": "Grand Master Rank"
      },
      "flags": {
        "basic_todos": "Basic Charges",
        "chat_interface": "Oracle Interface",
        "theme_selector": "Theme Selector",
        "export_todos": "Transcribe Charges",
        "advanced_search": "Advanced Seeking",
        "unlimited_todos": "Unlimited Charges",
        "mindmap_view": "Battle Map View",
        "custom_themes": "Custom Themes",
        "api_access": "API Access",
        "priority_support": "Priority Counsel",
        "swarmdesk_3d": "War Council 3D",
        "collaborative_editing": "Joint Authorship",
        "ai_copilot": "Oracle Copilot",
        "admin_panel": "Grand Master Panel",
        "user_management": "Knight Management",
        "feature_flags": "Order Rites",
        "system_logs": "Chapter Chronicle",
        "analytics": "Analytics",
        "debug_mode": "Debug Mode"
      },
      "confirm": {
        "title": "Confirm Rite Changes",
        "message": "Apply these rite changes? This will immediately affect all knights.",
        "warning": "Tip: Test on a chapter house first. Disabling core rites may break knight access."
      }
    },
    "users": {
      "title": "Knight Management",
      "loading": "Consulting chapter rolls…",
      "refresh": "Renew rolls",
      "fallback": "(showing mock data for development)",
      "searchPlaceholder": "Seek by missive or name…",
      "showing": "Showing",
      "users": "knights",
      "filtered": "filtered from",
      "empty": "No knights sworn to the order",
      "noResults": "No knights found in this seeking",
      "adminBadge": "GRAND MASTER",
      "edit": {
        "title": "Amend Knight Record",
        "email": "Missive",
        "tier": "Rank",
        "isAdmin": "Grant Grand Master Authority",
        "cancel": "Withdraw",
        "save": "Inscribe",
        "saving": "Inscribing…"
      },
      "columns": {
        "email": "Missive",
        "tier": "Rank",
        "status": "Status",
        "lastLogin": "Last Entry",
        "todos": "Charges",
        "actions": "Actions"
      },
      "confirm": {
        "title": "Confirm Authority Change",
        "grantMessage": "Grant Grand Master authority to this knight? They shall have full access to all chapter records.",
        "revokeMessage": "Revoke Grand Master authority from this knight? They shall lose all elevated access.",
        "cancel": "Withdraw",
        "confirm": "Confirm",
        "saving": "Inscribing…"
      }
    },
    "common": {
      "loading": "Consulting the Archive…",
      "error": "An error occurred",
      "refresh": "Renew",
      "save": "Inscribe",
      "cancel": "Withdraw"
    }
  },
  "queuePane": {
    "allProjects": "All Crusades",
    "incoming": {
      "title": "Incoming",
      "addToTop": "Add to Head of Roster",
      "addToBottom": "Add to Tail of Roster"
    },
    "ordered": {
      "title": "Ordered Roster"
    },
    "stats": {
      "total": "Queued",
      "high": "Urgent",
      "incoming": "Incoming"
    }
  },
  "onboarding": {
    "complete": {
      "message": "Thy oath is sworn. Thou art welcome in the Chapter House."
    },
    "steps": {
      "welcome": {
        "title": "Welcome, Sworn Knight",
        "defaultName": "Knight",
        "description": "Inventorium is thy sacred order for charge management and crusade planning.",
        "subtitle": "Let us walk the rites of initiation so thou art ready for the vigil."
      },
      "create-project": {
        "title": "Declare Thy First Crusade",
        "description": "Declare a crusade to organize thy charges. Crusades group related charges into holy missions.",
        "skipHint": "Thou may skip this and declare a crusade later from the Chapter Create chamber"
      },
      "add-todo": {
        "title": "Pledge a Charge",
        "description": "Now pledge a charge to thy crusade. Charges are the duties thou must fulfill.",
        "guideTitle": "How to pledge a charge:",
        "step1": "Click the floating '+' button again",
        "step2": "Select the 'Charge' tab in the chamber",
        "step3": "Enter thy charge description",
        "step4": "Assign the crusade from the scroll",
        "step5": "Set priority and click 'Pledge Charge'",
        "hint": "Tip: Thou canst pledge charges from anywhere using the '+' button"
      },
      "configure-ai": {
        "title": "Summon the Oracle",
        "description": "Gain the most from Inventorium by summoning an Oracle provider.",
        "whyConfigureTitle": "Why summon the Oracle?",
        "benefits": {
          "suggestions": "Generate wise charge suggestions",
          "enhance": "Illuminate charge descriptions with Oracle counsel",
          "analyze": "Seek patterns and connexions in thy crusades",
          "insights": "Receive counsel and guidance"
        },
        "statusConfigured": "Status: ✅ Oracle summoned and ready.",
        "statusNotConfigured": "Status: ❌ Oracle not yet summoned",
        "configureButton": "Summon Oracle",
        "skipButton": "Withdraw for Now",
        "helpText": "Thou canst summon the Oracle anytime from Settings → Oracle Configuration"
      },
      "ai-assistant": {
        "title": "The Oracle",
        "examplesTitle": "Quick Seekings:",
        "quickActions": {
          "createTodos": "Pledge charges from text",
          "analyzeTasks": "Seek charge patterns",
          "suggestions": "Receive wise counsel",
          "insights": "Crusade insights"
        }
      },
      "swarmdesk": {
        "title": "3D War Council",
        "description": "Explore thy crusades in 3D with the War Council — an immersive chapter environment.",
        "featuresTitle": "War Council Features:",
        "features": {
          "codeViz": "3D sacred diagram view",
          "interactive": "Interactive navigation",
          "architecture": "Architecture overview",
          "dependencies": "Dependency mapping"
        },
        "hint": "💡 Tip: Access the War Council from the crusade view",
        "tabTip": "After the War Council loads, press TAB to move between the dashboard and chapter house"
      },
      "complete": {
        "title": "Thy Vigil Begins",
        "description": "The rites of initiation are complete. Go forth and tend to the order's charges.",
        "nextStepsTitle": "Next Steps:",
        "nextSteps": {
          "createProject": "Declare thy first crusade",
          "addTodos": "Pledge charges to thy crusade",
          "tryAI": "Seek Oracle counsel",
          "checkSwarmDesk": "Explore the War Council 3D"
        },
        "footer": "💡 Thou canst replay these rites of initiation anytime from Settings"
      }
    }
  },
  "lessons": {
    "title": "Chronicles",
    "addLesson": "Inscribe Chronicle",
    "emptyState": {
      "title": "No Chronicles Found",
      "message": "Inscribe learnings to guide the order in future vigils.",
      "action": "Inscribe First Chronicle"
    },
    "fields": {
      "topic": "Subject",
      "language": "Language/Category",
      "lessonLearned": "Chronicle Entry",
      "tags": "Seals"
    },
    "actions": {
      "edit": "Amend",
      "delete": "Expunge",
      "save": "Inscribe Changes"
    }
  },
  "mindmap": {
    "title": "Battle Map",
    "emptyState": {
      "title": "The Map Stands Empty",
      "message": "Pledge charges and declare crusades to illuminate the battle map."
    },
    "controls": {
      "zoomIn": "Zoom In",
      "zoomOut": "Zoom Out",
      "resetView": "Restore View",
      "centerView": "Center View"
    }
  },
  "swarmdesk": {
    "title": "War Council",
    "emptyState": {
      "title": "The Chamber Stands Empty",
      "message": "Initiate components to view the chapter status."
    },
    "controls": {
      "rotate": "Rotate",
      "zoom": "Zoom",
      "pan": "Pan",
      "reset": "Restore View"
    }
  },
  "projectSelector": {
    "title": "Select Crusade",
    "placeholder": "Seek crusades…",
    "noProjects": "No crusades declared",
    "createNew": "Declare New Crusade"
  },
  "success": {
    "status": {
      "verifying": {
        "title": "CONSULTING ARCHIVE…",
        "subtitle": "Verifying payment with the Treasury"
      },
      "success": {
        "title": "ELEVATION COMPLETE",
        "subtitle": "The order confirms thy elevation. Go forth."
      },
      "error": {
        "title": "VERIFICATION FAILED"
      },
      "no_session": {
        "title": "SESSION NOT FOUND",
        "subtitle": "No treasury session detected. Didst thou navigate here directly?"
      }
    },
    "log": {
      "initializing": "Consulting the treasury archive…",
      "connecting": "Contacting the treasury…",
      "session": "Session:",
      "conduitStable": "Payment confirmed: STABLE",
      "tierUpgrade": "Rank elevation:",
      "allSystemsGo": "STATUS: THE ORDER STANDS READY",
      "paymentStatus": "Treasury status:",
      "paymentIncomplete": "WARNING: Payment incomplete",
      "error": "ERROR:",
      "verificationFailed": "Verification failed"
    },
    "tier": "RANK",
    "operator": "KNIGHT",
    "viewManifest": "VIEW TREASURY",
    "errorRetry": "If payment was received by the treasury, thy elevation shall be confirmed shortly.",
    "checkBilling": "Consult the treasury for current status."
  },
  "targetAgent": {
    "user": "Knight",
    "ai": "Oracle",
    "system": "Order",
    "none": "Unassigned"
  },
  "todoDetail": {
    "untitled": "Unnamed Charge",
    "tabs": {
      "overview": "Overview",
      "history": "Chronicle",
      "spells": "Rites",
      "related": "Related",
      "sessions": "Vigils",
      "coordinates": "Coordinates"
    },
    "spells": {
      "empty": "No rites have been invoked upon this charge yet.",
      "hint": "Use the Oracle to illuminate descriptions or seek patterns.",
      "undo": "Withdraw rite"
    },
    "related": {
      "empty": "No related charges found in this crusade.",
      "count": "{{count}} related charges"
    },
    "sessions": {
      "empty": "No vigils linked to this charge.",
      "hint": "Link vigils via the Oracle.",
      "count": "{{count}} linked vigils"
    },
    "coordinates": {
      "empty": "No coordinates assigned to this charge.",
      "hint": "Invoke the geomancy rite to assign spatial coordinates."
    }
  },
  "questTab": {
    "success": "Holy mission \"{{name}}\" declared ({{chains}} chains, {{todos}} charges)",
    "chainsHint": "Optional. {{chains}} chain(s), {{todos}} charge(s) linked.",
    "fields": {
      "name": "Mission Name *",
      "project": "Crusade",
      "tagsInput": "Seals (comma-separated)",
      "quickTags": "Quick Seals:",
      "addCriterion": "Add a fulfillment criterion",
      "chainLabel": "Chain Name",
      "chainTodos": "Charges in chain ({{count}})"
    },
    "buttons": {
      "add": "Add",
      "addChain": "Add Chain",
      "removeChain": "Remove chain",
      "copyId": "Copy Sigil"
    },
    "errors": {
      "nameRequired": "Mission name is required.",
      "projectRequired": "Crusade is required."
    }
  },
  "questCard": {
    "external": "external",
    "briefGenerating": "Composing…",
    "briefSaved": "Inscribed!",
    "briefDismiss": "Dismiss",
    "copiedPrompt": "Copied!",
    "copiedId": "Copied!",
    "deleteFailed": "Expungement failed",
    "save": "Inscribe",
    "saveFailed": "Inscription failed",
    "cancel": "Withdraw",
    "project": "Crusade",
    "projectRequired": "Crusade is required"
  },
  "errors": {
    "serverError": "Internal server error."
  },
  "targetAgent": {
    "user": "Knight",
    "ai": "Oracle",
    "system": "Order",
    "none": "Unassigned"
  }
}

result = deep_merge(templar, overrides)
save("templar-light", result)
print("templar-light.json written")

r = subprocess.run(["node", "-e", "require('./templar-light.json'); console.log('JSON valid')"],
                   capture_output=True, text=True, cwd=THEMES_DIR)
print(r.stdout.strip() or r.stderr.strip())
