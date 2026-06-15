#!/usr/bin/env python3
"""Templar-light voice pass batch 2 — remaining 603 identical keys."""
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

templar = load("templar-light")

overrides = {
    # desktop — quick terminal & merge gestures; short labels
    "desktop": {
        "openInTerminal": "Open in Scriptorium",
        "abortMerge": "Abort Binding",
        "continueRebase": "Continue Alignment",
        "abortRebase": "Abort Alignment",
        "dismiss": "Seal",
    },

    # common
    "common": {
        "previous": "Prior",
        "dismiss": "Seal",
    },

    # forms — field labels; keep factual, mild flavor
    "forms": {
        "name": "Crusade Name",
        "displayName": "Heraldic Title",
        "description": "Chronicle",
        "type": "Crusade Type",
        "visibility": "Visibility Edict",
        "repository": "Codex Repository",
        "language": "Tongue",
        "framework": "Order Framework",
        "priority": "Precedence",
        "status": "Standing",
    },

    # activityLog
    "activityLog": {
        "ago": "past",
        "stats": {
            "today": "This Day",
            "thisWeek": "This Sennight",
        },
    },

    # lessonsLearned
    "lessonsLearned": {
        "languages": {
            "allLanguages": "All Tongues",
            "javascript": "JavaScript",
            "typescript": "TypeScript",
            "python": "Python",
            "rust": "Rust",
            "general": "General",
        },
        "filters": {
            "recent": "Recent (7 days)",
        },
        "dialog": {
            "languageLabel": "Tongue",
            "tagsPlaceholder": "rite, rune, passage",
        },
    },

    # app
    "app": {
        "titleShort": "The Order",
        "titleLong": "The Sacred Order Workshop",
    },

    # labMaintenance duplicates subsection
    "labMaintenance": {
        "duplicates": {
            "threshold": "Accord",
            "groupsFound": "clusters",
            "apply": "Bind",
            "applyAll": "Bind All",
        },
    },

    # menu
    "menu": {
        "github": "Codex Repository",
        "themeGallery": "Vestment Gallery",
    },

    # notifications
    "notifications": {
        "aiConfigured": "✅ Oracle bound successfully!",
    },

    # projectNavigator
    "projectNavigator": {
        "stats": {
            "pending": "outstanding",
        },
        "enterButton": {
            "helpText": "Press Enter or #{{number}}",
        },
    },

    # projectSwarmdesk
    "projectSwarmdesk": {
        "stats": {
            "pendingTasks": "{{count}} outstanding",
        },
        "statsPanel": {
            "totalTasks": "Total Charges",
            "pending": "Outstanding",
        },
        "reviewTab": {
            "title": "Examination Queue",
            "approveButton": "Sanction",
            "requestChanges": "Request Revision",
            "returnToProgress": "Return to Progress",
            "emptyState": "No charges under examination",
        },
    },

    # projectTab
    "projectTab": {
        "title": "Crusade Founding",
        "sections": {
            "basicInfo": "Core Chronicle",
            "configuration": "Charter",
            "technicalDetails": "Technical Scrolls (Optional)",
        },
        "projectTypes": {
            "web": "Web Citadel",
            "mobile": "Mobile Envoy",
            "desktop": "Desktop Stronghold",
            "library": "Tome/Grimoire",
            "api": "API Conduit",
            "general": "General Crusade",
        },
        "buttons": {
            "creating": "Founding...",
            "demoMode": "Witness Mode",
            "createProject": "FOUND CRUSADE",
        },
    },

    # todoList — the big one
    "todoList": {
        "filters": {
            "pending": "Outstanding",
            "inProgress": "In Progress",
            "in_progress": "In Progress",
        },
        "sort": {
            "alphabetical": "By Inscription",
        },
        "project": {
            "label": "Crusade",
            "allProjects": "All Crusades ({{count}})",
            "clearFilter": "Clear Edict",
            "clearAll": "Clear all",
            "change": "Reassign",
        },
        "pagination": {
            "show": "Show",
            "all": "All",
            "next": "Advance",
            "prev": "Retreat",
            "showing": "Displaying {{start}}-{{end}} of {{total}}",
        },
        "results": {
            "matching": " matching \"{{searchText}}\"",
        },
        "buttons": {
            "share": "Share",
            "move": "Transfer",
        },
        "menu": {
            "share": "Share",
        },
        "dialog": {
            "exportFormat": "Format",
            "formatCSVDesc": "Parchment-compatible format for scrolls or ledgers",
            "formatMarkdownDesc": "Human-readable format for chronicles",
            "variantJSONL": "JSON Lines (Stream)",
            "variantStandard": "Standard",
            "variantExcel": "Excel-Optimized",
            "variantTable": "Table View",
            "selectFields": "Select Fields",
            "customizeFields": "Customise Field Names",
            "renameFields": "Rename Fields",
            "calculatedFields": "Calculated Fields",
            "fieldName": "Field Name",
            "addCalculatedField": "Add Calculated Field",
            "formula": {
                "ageInDays": "Age (days)",
                "charCount": "Character count",
                "tokenEstimate": "Token estimate",
            },
            "selectAll": "All",
            "selectNone": "None",
            "advancedFilters": "Advanced Edicts",
            "dateRange": "Date Range",
            "startDate": "From",
            "priorityFilter": "Precedence",
            "statusFilter": "Standing",
        },
        "priority": {
            "high": "High",
            "medium": "Medium",
            "low": "Low",
        },
        "status": {
            "pending": "Outstanding",
            "in_progress": "In Progress",
            "inProgress": "In Progress",
        },
        "fields": {
            "description": "Chronicle",
            "priority": "Precedence",
            "status": "Standing",
            "target": "Target",
            "source": "Source",
            "notes": "Marginalia",
            "duration": "Duration",
            "duration_sec": "Duration (seconds)",
            "complexity": "Complexity",
            "confidence": "Confidence",
            "phase": "Phase",
            "epic": "Crusade",
            "description_preview": "Chronicle Preview",
            "created_at": "Inscribed At",
            "updated_at": "Revised At",
        },
        "validation": {
            "descriptionRequired": "Chronicle cannot be empty",
            "descriptionTooLong": "Chronicle must be less than 500 characters",
        },
        "error": {
            "unknownError": "Unknown error",
        },
        "labels": {
            "readOnly": "🔒 Read-Only",
        },
        "actions": {
            "markPending": "Mark Outstanding",
            "archive": "Archive",
            "reopen": "Reopen",
            "unarchive": "Restore",
        },
        "timestamps": {
            "due": "Due",
        },
        "dueDate": {
            "none": "No date set",
            "set": "Set Date",
            "today": "Due this day",
            "tomorrow": "Due on the morrow",
        },
        "moveDialog": {
            "confirm": "Transfer",
        },
        "selected": "{{count}} selected",
        "bulkActions": {
            "move": "Transfer Selected",
        },
        "selectAll": "Select All",
        "assignee": {
            "none": "Unassigned",
            "change": "Reassign",
        },
        "deselectAll": "Deselect All",
        "loadMore": "Load More",
        "dropHere": "Drop here",
    },

    # todoEdit
    "todoEdit": {
        "loading": {
            "text": "Consulting the Archive...",
        },
        "header": {
            "editTodo": "Amend Charge",
            "createNewTodo": "Inscribe New Charge",
        },
        "buttons": {
            "backToDashboard": "Return to Chamber",
        },
        "error": {
            "todoNotFound": "Charge not found. It may have been expunged or the seal is incorrect.",
        },
        "workshop": {
            "modeTitle": "⚒️ Scriptorium Mode - Full Edit Access",
        },
        "tips": {
            "title": "📜 Edit Scrolls:",
            "description": "• Click any field to amend in-place • Use the Amend button for full form • ESC to withdraw • Ctrl+Enter to inscribe • Purple sparkle for Oracle enhancement",
        },
        "fields": {
            "dueDate": "Due Date",
            "priority": "Precedence",
            "status": "Standing",
        },
    },

    # settings
    "settings": {
        "import": {
            "error": "Import failed: {{error}}",
        },
        "todoToolbar": {
            "complete": "Fulfill",
            "edit": "Amend",
            "copyId": "Copy Seal",
            "copyJiraCommand": "Copy Jira Command",
            "share": "Share",
            "review": "Examine",
            "aiInsights": "Oracle Insights",
        },
        "tabs": {
            "appearance": "Vestments",
            "advanced": "Advanced Rites",
            "keyboardShortcuts": "Rune Bindings",
            "security": "Ward Seals",
            "general": "General Edicts",
        },
        "swarmdesk": {
            "movementTitle": "Movement Speed Edicts",
            "orbitalTitle": "Orbital Mode (O key)",
            "orbitalBaseSpeed": "Base Speed",
            "orbitalSprintMultiplier": "Sprint Multiplier (Ctrl held)",
            "fpsTitle": "FPS Mode (F key)",
            "fpsBaseSpeed": "March Speed",
            "fpsSprintSpeed": "Charge Speed (Ctrl held)",
        },
        "messaging": {
            "addRole": "Add Role",
            "roleIdHelper": "Lowercase, alphanumeric, and hyphens only (e.g., 'gpt-4', 'custom-ai')",
            "displayLabel": "Heraldic Label",
            "displayLabelHelper": "Human-readable name shown in chamber",
            "emoji": "Emblem",
            "emojiHelper": "Single emblem character for visual identification",
            "coreRole": "Core Role",
            "hidden": "Hidden",
            "showRole": "Reveal role",
            "hideRole": "Conceal role",
            "saveChanges": "Inscribe Changes",
            "cancel": "Withdraw",
            "npcConfig": "SwarmDesk NPC Charter",
            "npcEnabled": "Spawn as SwarmDesk NPC",
            "npcCount": "NPC Count",
            "npcCountHelper": "Choose how many clones of this role should appear in SwarmDesk (0-5).",
            "npcColor": "NPC Livery",
            "npcColorHelper": "Used for the NPC body glow and sidebar identity color.",
            "npcRole": "NPC Role Title",
            "npcRoleHelper": "Shown above the NPC in SwarmDesk. Leave blank to use the heraldic label.",
            "npcPersonality": "NPC Disposition",
            "npcPersonalityHelper": "Controls the default vibe and fallback dialogue for this NPC.",
            "npcPersonalities": {
                "helpful_assistant": "Faithful Squire",
                "chaotic_genius": "Errant Knight",
                "methodical_precise": "Scribe-Knight",
                "curious_explorer": "Wandering Pilgrim",
                "zen_creative": "Contemplative Friar",
                "welcoming_efficient": "Hospitable Steward",
                "organized_visionary": "Grand Visionary",
            },
            "duplicateRoleId": "A role bearing this seal already exists.",
            "duplicateAgentId": "An agent bearing this seal already exists.",
        },
        "theme": {
            "title": "Vestments",
            "colorTheme": "Heraldic Colors",
            "textTheme": "Script Style",
        },
        "account": {
            "title": "Account",
            "profile": "Profile Scrolls",
            "preferences": "Preferences",
        },
        "about": {
            "build": "Build",
            "reportBug": "Report Anomaly",
            "version": "Version",
        },
        "ai": {
            "provider": "Oracle Provider",
            "temperature": "Fervor",
            "maxTokens": "Max Tokens",
            "testing": "Consulting…",
        },
        "language": {
            "label": "Tongue",
        },
        "display": {
            "reducedMotion": "Reduce motion",
            "spacious": "Spacious",
            "density": "Display Density",
            "comfortable": "Comfortable",
            "compact": "Compact",
            "fontSize": "Script Size",
        },
        "advanced": {
            "debugMode": "Debug Mode",
        },
    },

    # umlData — keep technical, mild templar flavor
    "umlData": {
        "description": "Manage architectural scrolls for the 3D code citadel in SwarmDesk",
        "errors": {
            "loadFailed": "Failed to retrieve architectural scrolls",
            "uploadFailed": "Failed to upload scroll",
            "deleteFailed": "Failed to expunge scroll",
        },
        "viewSwarmDesk": {
            "redirect": "Opening in SwarmDesk...",
        },
        "source": {
            "personal": "Personal",
            "shared": "Shared",
        },
        "instructions": {
            "title": "How to inscribe:",
            "step1": "Install the cartographer: npm install -g @madnessengineering/cartogomancy",
            "step2": "Map your codebase: cartogomancy /path/to/project -o project-uml.json",
            "step3": "Upload the generated JSON scroll using the button above",
        },
        "storage": {
            "info": "You hold {{count}} visualisation(s). Storage edict: {{limit}}",
            "limit": "10 scrolls per order member (10MB each)",
        },
        "table": {
            "name": "Crusade Name",
            "linkedProject": "Bound Crusade",
            "version": "Version",
            "lastUpdated": "Last Revised",
            "source": "Source",
            "classes": "Classes",
            "packages": "Packages",
            "created": "Inscribed",
            "actions": "Actions",
        },
        "actions": {
            "view": "View in SwarmDesk",
            "delete": "Expunge",
        },
        "empty": {
            "hint": "Upload a scroll to behold your code in 3D",
        },
        "compareVersions": "Compare Versions",
        "filters": {
            "recent": "Recent",
            "language": "By Tongue",
        },
        "success": {
            "restored": "Version restored",
        },
        "metadata": {
            "size": "Size",
            "nodes": "Nodes",
            "framework": "Framework",
            "language": "Tongue",
        },
        "versions": "Versions",
        "depth": "Analysis Depth",
        "restore": "Restore Version",
        "branch": "Branch",
        "repoUrl": "Repository URL",
        "version": "Version",
    },

    # auth
    "auth": {
        "errors": {
            "demoLoginFailed": "Witness login failed",
            "tokenInvalid": "Access seal has expired",
        },
    },

    # editableTodoCard
    "editableTodoCard": {
        "confirmCancel": "You bear unsaved revisions. Are you sure you wish to withdraw?",
        "sections": {
            "metadata": "Annotations (Optional)",
        },
        "errors": {
            "descriptionRequired": "Chronicle is required for Oracle enhancement",
            "aiEnhancementFailed": "Oracle enhancement failed: {{error}}",
            "saveFailed": "Failed to inscribe changes",
        },
        "placeholders": {
            "description": "Enter charge chronicle...",
            "clickToAdd": "Click to add chronicle...",
            "enhancedDescription": "Oracle-enhanced chronicle will appear here...",
            "notes": "Additional marginalia...",
            "ticket": "Seal reference...",
        },
        "labels": {
            "enhancedDescription": "Enhanced Chronicle",
            "aiEnhanced": "🧠 Oracle Enhanced Chronicle:",
            "completionNotes": "✅ Fulfilment Notes:",
            "completed": "Fulfilled",
            "duration": "Duration",
            "autoEnhanceOnSave": "Auto-enhance on inscribe",
            "enhance": "Enhance",
            "enhancing": "Enhancing...",
        },
        "priority": {
            "low": "Low",
            "medium": "Medium",
            "high": "High",
        },
        "status": {
            "pending": "Outstanding",
            "in_progress": "In Progress",
            "initial": "Initial",
            "cancelled": "Withdrawn",
            "inProgress": "In Progress",
        },
        "menu": {
            "editTask": "Amend Charge",
            "deleteTask": "Expunge Charge",
        },
        "messages": {
            "noEnhancedDescription": "No enhanced chronicle yet. Invoke the Oracle to generate one.",
        },
        "tooltips": {
            "enhance": "Oracle enhances chronicle, suggests tags and complexity",
        },
        "actions": {
            "share": "Share",
            "unpin": "Unpin",
            "pin": "Pin",
            "move": "Transfer",
        },
        "fields": {
            "description": "Chronicle",
            "status": "Standing",
            "priority": "Precedence",
            "dueDate": "Due Date",
        },
    },

    # mindMap
    "mindMap": {
        "controls": {
            "switchToWorldMap": "Open War Room",
            "switchToSphere": "Switch to Sphere",
            "chaos": "Discord",
            "center": "Centre View",
            "zoomOut": "Withdraw View",
            "zoomIn": "Advance View",
        },
        "info": {
            "nodeCount": "{{count}} Nodes",
        },
        "instructions": {
            "dragToMove": "Drag to Move",
            "dragging": "Moving!",
            "touchAndDrag": "Touch & Drag",
            "doubleTapBurst": "Double-tap for burst!",
            "doubleTapPhysics": "Double-tap for physics!",
        },
        "filter": {
            "title": "Crusade Filter",
            "allProjects": "All Crusades",
            "projectCount": "{{selected}}/{{total}} Crusades",
            "selectAll": "Select All",
            "clearAll": "Clear All",
            "selectProjects": "Select Crusades",
            "projectsSelected": "{{count}} crusades selected",
            "selectedProjects": "Selected Crusades ({{count}})",
        },
        "tooltips": {
            "disableStaticMode": "Disable Static Mode",
            "enableStaticMode": "Enable Static Mode",
            "cleanUpEffects": "Cleanse Visual Effects",
        },
        "sequence": {
            "hideSequence": "Conceal Task Sequence",
            "showSequence": "Reveal Oracle Sequence",
            "analyzeSequences": "Analyse Sequences",
            "stopAnimation": "Halt Animation",
            "animateSequence": "Animate Sequence",
            "shuffleSequence": "Shuffle Sequence Type",
        },
        "selection": {
            "multipleNodes": "{{count}} nodes selected (Ctrl+Click to add/remove, max 3)",
        },
        "nodes": {
            "centerBrain": "⚡ TANGENTRON",
            "centerWorkshop": "🧠 WORKSHOP",
        },
        "modes": {
            "dynamic": "⚡ Dynamic Mode",
            "static": "📖 Static Mode",
        },
        "dialog": {
            "createNode": "📜 Inscribe New Node",
            "nodeText": "Node Text",
        },
        "nodeInfo": {
            "type": "Type",
            "priority": "Precedence",
            "energy": "Vigour",
        },
        "filters": {
            "all": "All Nodes",
        },
        "layout": {
            "radial": "Radial Layout",
            "force": "Force Layout",
            "tree": "Tree Layout",
            "grid": "Grid Layout",
        },
        "connectNodes": "Bind Nodes",
        "addNode": "Add Node",
    },

    # chatAssistant
    "chatAssistant": {
        "errors": {
            "demoUserRestricted": "🚫 Oracle counsel is unavailable for witness users. Please enlist to access the Oracle.",
        },
        "quickActions": {
            "listPending": "List my outstanding charges",
            "createHighPriority": "Inscribe a new high-precedence charge",
            "summarizeProject": "Chronicle the {{project}} crusade",
            "filterHighPriority": "Show me high-precedence charges in this crusade",
        },
        "suggestedActions": {
            "listPending": "List Outstanding",
            "newHighPrio": "New High Prio",
            "summarize": "Chronicle",
        },
        "status": {
            "typing": "Oracle is composing",
        },
        "emptyState": {
            "title": "Sacred Order Oracle",
            "demoMessage": "Oracle counsel is unavailable for witness users. Enlist for a free account to access the Oracle!",
            "description": "Your personal Oracle to help manage charges, crusades, and more.",
        },
        "notConfigured": {
            "title": "Oracle Not Bound",
            "description": "To invoke the Oracle, please bind your provider in the Settings.",
            "configureButton": "Bind Oracle Provider",
        },
        "header": {
            "title": "Sacred Oracle",
            "refreshTooltip": "Refresh context",
            "settingsTooltip": "Settings",
        },
        "menu": {
            "refreshContext": "Refresh Context",
            "aiSettings": "Oracle Settings (Go to Settings)",
            "aiSettingsRedirect": "Oracle configuration has been moved to Settings → Oracle Configuration",
        },
        "input": {
            "placeholder": "Seek counsel from the Oracle...",
            "demoPlaceholder": "Oracle counsel is unavailable for witness users. Enlist for a free account!",
        },
        "send": "Dispatch",
        "thinking": "Consulting...",
        "suggestions": {
            "searchLessons": "Search the Archive",
            "listTodos": "List active charges",
            "createProject": "Found new crusade",
            "summarize": "Generate chronicle",
        },
        "actions": {
            "feedback": {
                "bad": "Not Useful",
                "good": "Useful",
            },
            "retry": "Retry",
            "delete": "Expunge",
        },
    },

    # mobileChatInterface
    "mobileChatInterface": {
        "quickActions": {
            "createTodo": "Inscribe Charge",
            "listTodos": "List Charges",
            "projectStatus": "Crusade Status",
            "help": "Seek Aid",
            "prioritize": "Set Precedence",
            "summarize": "Chronicle",
        },
        "actionMessages": {
            "createTodo": "Help me inscribe a new charge",
            "listTodos": "Show me my current charges",
            "projectStatus": "Give me a status on my crusades",
            "help": "What counsel can you offer?",
            "prioritize": "What should I address today?",
            "summarize": "Give me a quick chronicle of my current crusade",
        },
        "header": {
            "title": "Sacred Oracle",
            "statusListening": "Hearkening...",
            "statusTyping": "Composing...",
            "statusOnline": "Vigilant",
        },
        "emptyState": {
            "greeting": "Hail! I am your Sacred Oracle",
            "description": "I can help you manage charges, navigate crusades, and answer questions about your order.",
        },
        "status": {
            "thinking": "Oracle is deliberating...",
        },
        "input": {
            "placeholder": "Speak your query...",
        },
        "minimize": "Withdraw",
        "connectionStatus": {
            "disconnected": "Severed",
            "connected": "Bound",
            "reconnecting": "Rebinding…",
        },
    },

    # warRoom
    "warRoom": {
        "backgroundImage": {
            "noUploads": "No custom banners yet",
            "opacity": "Opacity",
            "fitMode": "Fit Mode",
            "fitCover": "Cover",
            "fitContain": "Contain",
            "fitStretch": "Stretch",
            "fitTile": "Tile",
            "blendWithTerrain": "Blend with Terrain",
            "remove": "Remove Banner",
            "active": "Active",
            "uploadError": "Upload failed. Please try again.",
            "fileTooLarge": "Banner must be under 5MB",
            "invalidType": "Only JPEG, PNG, and WebP banners are supported",
        },
        "incident": {
            "escalate": "Escalate",
            "status": "Standing",
        },
        "empty": {
            "action": "Open Incident",
        },
        "filters": {
            "active": "Active",
        },
    },

    # swarmDesk
    "swarmDesk": {
        "ui": {
            "navigation": {
                "controls": "⌨️ Navigation Edicts",
                "escape": "🚪 ESC: Return to Chamber | M: Menu",
            },
        },
        "panels": {
            "shortcuts": {
                "title": "⌨️ Rune Bindings",
                "categories": {
                    "navigation": {
                        "title": "🧭 Pathfinding",
                    },
                    "actions": {
                        "title": "⚡ Actions",
                    },
                },
            },
            "mcp": {
                "tools": {
                    "connectedAs": "Bound as: {{username}}",
                },
                "debug": {
                    "authentication": "Authentication: {{status}}",
                    "apiService": "API Service: {{status}}",
                },
            },
            "agent": {
                "interface": {
                    "role": "Role: {{role}}",
                    "status": "Standing: {{status}}",
                },
                "capabilities": {
                    "communication": "✅ Real-time Communion",
                },
            },
            "analytics": {
                "insights": {
                    "peakActivity": "Peak vigil: 14:00-15:00",
                },
            },
            "webllm": {
                "compatibility": {
                    "checkCompatibility": "🔍 Check Compatibility",
                },
                "settings": {
                    "temperature": "Fervor:",
                    "maxTokens": "Max Tokens:",
                },
            },
            "mqtt": {
                "logs": {
                    "lastMessage": "Last: {{time}}",
                },
                "status": {
                    "lastActivity": "Last Vigil: {{time}}",
                },
                "settings": {
                    "showTimestamps": "Show timestamps",
                },
            },
            "settings": "Charter",
            "chat": "Oracles",
            "insights": "Analytics",
            "projects": "Crusades",
            "todos": "Charge Queue",
        },
        "projectData": {
            "swarmDesk": {
                "status": "🔥 Active Crusade",
                "visibility": "public repository",
            },
            "inventorium": {
                "title": "📦 Inventorium",
            },
            "swarmonomicon": {
                "title": "🐝 Swarmonomicon",
                "visibility": "public repository",
            },
        },
        "errors": {
            "permissionDenied": "🔒 Access Denied",
            "unknownError": "❓ Unknown Error",
        },
        "status": {
            "disconnected": "Archive severed",
            "connected": "Bound to Archive",
            "synced": "Synchronised",
            "syncing": "Synchronising…",
        },
        "controls": {
            "zoom": "Zoom",
            "rotate": "Rotate",
            "move": "Move",
        },
        "tour": {
            "navigation": "WASD to navigate, mouse to survey",
        },
        "agentPanel": {
            "status": {
                "active": "Vigilant",
            },
        },
        "projectPanel": {
            "selected": "Active: {{name}}",
        },
        "hotkeys": {
            "mouse": "Mouse: Survey",
            "space": "Space: Select",
            "wasd": "WASD: Navigate",
        },
        "nodes": {
            "move": "Transfer",
        },
        "filters": {
            "inProgress": "In Progress",
            "pending": "Outstanding",
        },
        "sort": {
            "name": "By Inscription",
            "priority": "By Precedence",
        },
    },

    # spells
    "spells": {
        "interface": {
            "title": "⚔️ Charge Enhancement Rites",
            "subtitle": "Employ Oracle-powered rites to improve your charge management",
            "selectSpell": "Choose Enhancement Rite",
            "castSpell": "Invoke Rite",
            "cancelSpell": "Withdraw",
            "casting": "Invoking Rite...",
            "resultsTitle": "✨ Rite Results",
            "historyTitle": "📜 Rite Chronicle",
            "clearHistory": "Clear Chronicle",
            "noHistory": "No rites have been invoked",
            "placeholder": "Select a rite to enhance your charges...",
        },
        "results": {
            "geomancy": {
                "patterns": "Pattern analysis:",
            },
            "latest": "Latest",
        },
        "history": {
            "result": "Result:",
            "success": "✅ Successful",
            "failed": "❌ Failed",
            "duration": "Duration:",
        },
        "status": {
            "success": "Fulfilled",
        },
        "accessDenied": {
            "title": "Access Denied",
        },
        "keyboardShortcut": "Rune Binding",
        "estimatedTime": "Estimated Time",
        "result": {
            "confidence": "Confidence",
        },
        "error": {
            "unknown": "An unknown error transpired",
        },
        "enhanceDescription": {
            "result": {
                "before": "Before",
                "after": "After",
                "improvements": "Improvements",
            },
        },
        "performGeomancy": {
            "insights": {
                "complexity": "Complexity",
                "duration": "Estimated Duration",
                "risks": "Risk Factors",
            },
        },
        "categories": {
            "consolidate": "Consolidate",
            "analyze": "Analyse",
            "enhance": "Enhance",
        },
    },

    # insights
    "insights": {
        "tabs": {
            "overview": "Overview",
            "analytics": "Analytics",
        },
    },

    # admin
    "admin": {
        "tabs": {
            "overview": "Overview",
            "analytics": "Analytics",
        },
        "overview": {
            "fallback": "(showing mock data for development)",
            "activeUsers": "Active (7d)",
            "errors": "Anomalies (24h)",
        },
        "analytics": {
            "title": "Advanced Analytics",
            "timeframe": {
                "day": "Last 24 Hours",
                "week": "Last 7 Days",
                "month": "Last 30 Days",
                "year": "Last 12 Months",
            },
            "charts": {
                "activityHeatmap": "Vigil Heatmap",
            },
        },
        "logs": {
            "fallback": "(showing mock data for development)",
            "showing": "Displaying",
            "columns": {
                "timestamp": "Time",
                "level": "Level",
                "message": "Inscription",
            },
            "severity": {
                "error": "ERROR",
                "warning": "WARNING",
                "info": "INFO",
            },
        },
        "featureFlags": {
            "fallback": "(showing mock data for development)",
            "lastUpdated": "Last revised",
            "flags": {
                "theme_selector": "Vestment Selector",
                "custom_themes": "Custom Vestments",
                "api_access": "API Access",
                "analytics": "Analytics",
                "debug_mode": "Debug Mode",
            },
        },
        "users": {
            "fallback": "(showing mock data for development)",
            "showing": "Displaying",
            "filtered": "filtered from",
            "columns": {
                "status": "Standing",
                "actions": "Actions",
            },
        },
        "common": {
            "error": "An anomaly occurred",
        },
    },

    # queuePane
    "queuePane": {
        "incoming": {
            "title": "Incoming",
        },
        "stats": {
            "total": "Queued",
            "high": "Urgent",
            "incoming": "Incoming",
        },
    },

    # onboarding
    "onboarding": {
        "colors": {
            "chipText": "#ffffff",
        },
        "steps": {
            "add-todo": {
                "step1": "Click the floating '+' button again",
            },
            "ai-assistant": {
                "examplePromptsTitle": "Seek counsel:",
            },
            "swarmdesk": {
                "features": {
                    "interactive": "Interactive navigation",
                    "architecture": "Architecture overview",
                    "dependencies": "Dependency mapping",
                },
            },
            "complete": {
                "nextStepsTitle": "Forthcoming Rites:",
            },
        },
    },

    # version
    "version": "1.0.0",

    # lessons
    "lessons": {
        "fields": {
            "language": "Tongue/Category",
        },
    },

    # mindmap (lower-case alias)
    "mindmap": {
        "controls": {
            "zoomIn": "Advance View",
            "zoomOut": "Withdraw View",
            "centerView": "Centre View",
        },
    },

    # swarmdesk (lower-case alias)
    "swarmdesk": {
        "controls": {
            "rotate": "Rotate",
            "zoom": "Zoom",
            "pan": "Survey",
        },
    },

    # errors
    "errors": {
        "serverError": "Internal sanctum error.",
    },

    # success
    "success": {
        "status": {
            "error": {
                "title": "VERIFICATION FAILED",
                "subtitle": "The verification rite encountered an anomaly.",
            },
        },
        "log": {
            "session": "Session:",
            "conduitStable": "Tithe confirmed: STABLE",
            "unlocking": "Unlocking elevated privileges...",
            "paymentIncomplete": "WARNING: Tithe incomplete",
            "error": "ERROR:",
            "verificationFailed": "Verification failed",
            "containment": "Containment protocols engaged",
        },
    },

    # targetAgent
    "targetAgent": {
        "none": "Unassigned",
    },

    # todoDetail
    "todoDetail": {
        "tabs": {
            "overview": "Overview",
            "related": "Related",
            "coordinates": "Coordinates",
        },
    },

    # automationRecipes
    "automationRecipes": {
        "tagNormalization": {
            "scanned": "Scanned",
            "modified": "Revised",
        },
    },

    # aiInsights
    "aiInsights": {
        "dialog": {
            "deselectAll": "None",
        },
    },

    # lessonsViewer
    "lessonsViewer": {
        "bench": {
            "sectionLessons": "Scrolls",
        },
        "neighbors": {
            "none": "none",
        },
        "references": {
            "none": "none",
        },
    },

    # questTab
    "questTab": {
        "buttons": {
            "add": "Enlist",
            "addChain": "Add Chain",
            "removeChain": "Remove Chain",
        },
    },

    # questCard
    "questCard": {
        "external": "external",
        "briefDismiss": "Seal",
        "copiedPrompt": "Copied!",
        "copiedId": "Copied!",
    },
}

result = deep_merge(templar, overrides)
save("templar-light", result)
print("templar-light.json written")

# Validate
import subprocess
r = subprocess.run(
    ["node", "-e", "require('./templar-light.json'); console.log('templar-light: valid')"],
    capture_output=True, text=True, cwd=THEMES_DIR
)
print(r.stdout.strip() or r.stderr.strip())
