#!/usr/bin/env python3
"""
Voice pass labops - batch 3: todoList deep keys, settings, remaining sections.
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

labops = load("labops")

overrides = {
  "todoList": {
    "filters": {
      "pending": "Pending",
      "inProgress": "In Progress",
      "blocked": "Blocked",
      "in_progress": "In Progress"
    },
    "sort": {
      "madness": "Random Order"
    },
    "project": {
      "label": "Project",
      "allProjects": "All Projects ({{count}})",
      "clearFilter": "Clear Filter",
      "clearAll": "Clear all"
    },
    "pagination": {
      "show": "Show",
      "perPage": "per page",
      "all": "All",
      "results": "results"
    },
    "results": {
      "showing": "Showing {{start}}-{{end}} of {{total}} tickets",
      "matching": " matching \"{{searchText}}\"",
      "filteringByProject": "Filtered by project: <strong>{{project}}</strong>",
      "filteringByProjects": "Filtered by {{count}} project(s)"
    },
    "empty": {
      "noMatching": "No Matching Tickets",
      "workshopClear": "Queue Clear",
      "noMatchingDescription": "No tickets match \"{{searchText}}\". Adjust your query or filters.",
      "workshopClearDescription": "No tickets found. The queue is clear."
    },
    "buttons": {
      "refresh": "Resync",
      "export": "Export Snapshot",
      "saving": "Committing…",
      "saveChanges": "Commit Changes",
      "discard": "Discard",
      "copyId": "Copy ID",
      "copyJiraCmd": "Copy Jira Cmd",
      "share": "Share",
      "review": "Triage",
      "aiInsights": "Run Diagnostics"
    },
    "fullEdit": {
      "modeTitle": "Full Edit Mode"
    },
    "menu": {
      "editTask": "Edit Ticket",
      "copyId": "Copy ID",
      "copyJiraCmd": "Copy Jira Cmd",
      "share": "Share",
      "deleteTask": "Decommission Ticket"
    },
    "dialog": {
      "completeTitle": "Resolve Ticket: {{description}}",
      "completeDescription": "Add an optional resolution note (solution details, time taken, blockers resolved, etc.)",
      "completePlaceholder": "e.g., Fixed CSS issue by updating responsive breakpoints. 2 hours — browser compat testing.",
      "cancel": "Discard",
      "completeTask": "Resolve Ticket",
      "exportTitle": "Export Ticket Snapshot",
      "exportDescription": "Exporting {{count}} tickets",
      "exportFilename": "Filename",
      "exportFilenameHelp": "Export file name (extension added automatically)",
      "exportFormat": "Format",
      "exportButton": "Export",
      "formatJSON": "JSON — Structured Data",
      "formatJSONDesc": "Complete ticket data in JSON format for reimport",
      "formatCSV": "CSV — Spreadsheet",
      "formatCSVDesc": "Spreadsheet-compatible format for Excel or Google Sheets",
      "formatMarkdown": "Markdown — Documentation",
      "formatMarkdownDesc": "Human-readable format for documentation",
      "formatHTML": "HTML — Web Page",
      "formatHTMLDesc": "Styled web page for browser viewing",
      "formatJira": "Jira/Slack Commands",
      "formatJiraDesc": "Ready-to-paste Slack commands for Jira tickets",
      "formatVariant": "Format Variant",
      "variantPretty": "Pretty (Readable)",
      "variantMinified": "Minified (Compact)",
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
        "daysSinceUpdate": "Days since update",
        "charCount": "Character count",
        "tokenEstimate": "Token estimate",
        "timeToComplete": "Time to resolve"
      },
      "selectAll": "All",
      "selectNone": "None",
      "advancedFilters": "Advanced Filters",
      "dateRange": "Date Range",
      "startDate": "From",
      "priorityFilter": "Priority",
      "statusFilter": "Status"
    },
    "priority": {
      "high": "High",
      "medium": "Medium",
      "low": "Low",
      "critical": "Critical"
    },
    "status": {
      "pending": "Pending",
      "in_progress": "In Progress",
      "blocked": "Blocked"
    },
    "fields": {
      "description": "Description",
      "project": "Project",
      "priority": "Priority",
      "status": "Status",
      "target": "Target",
      "created": "Opened",
      "updated": "Updated",
      "metadata": "Metadata",
      "source": "Source",
      "notes": "Notes",
      "ticket": "Ticket",
      "completed_at": "Resolved At",
      "completed_by": "Resolved By",
      "completion_comment": "Resolution Comment",
      "duration": "Duration",
      "duration_sec": "Duration (seconds)",
      "tags": "Tags",
      "complexity": "Complexity",
      "confidence": "Confidence",
      "phase": "Phase",
      "epic": "Epic",
      "blockers": "Blockers"
    },
    "validation": {
      "descriptionRequired": "Description cannot be empty",
      "descriptionTooLong": "Description must be less than 500 characters",
      "invalidProject": "Please select a valid project"
    },
    "error": {
      "failedToLoad": "Query failed",
      "unknownError": "Unknown error",
      "malfunctionMessage": "The system encountered an error. Resync or check your connection."
    },
    "placeholders": {
      "setStatus": "Set status…",
      "editDescription": "Click to edit ticket description…",
      "selectProject": "Select project…",
      "setPriority": "Set priority…"
    },
    "tooltip": {
      "unsavedChanges": "You have uncommitted changes"
    },
    "labels": {
      "readOnly": "🔒 Read-Only",
      "review": "TRIAGE"
    },
    "aria": {
      "todoActions": "Ticket actions"
    },
    "addTodo": "Open Ticket",
    "emptyState": {
      "title": "Queue clear",
      "message": "Open your first ticket to get started",
      "action": "Open Ticket"
    },
    "actions": {
      "markPending": "Mark Pending",
      "edit": "Edit Ticket",
      "delete": "Decommission Ticket"
    }
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
    "tabs": {
      "general": "General",
      "ai": "AI",
      "appearance": "Display",
      "data": "Data",
      "notifications": "Alerts",
      "security": "Security",
      "advanced": "Advanced"
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
    "confirmReset": "Reset all configuration to factory defaults?"
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
    "confirmRestore": "Restore this version?"
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
    }
  },
  "chatAssistant": {
    "title": "🤖 Diagnostic Console",
    "placeholder": "Query the diagnostic system…",
    "send": "Send",
    "sending": "Transmitting…",
    "loading": "Querying…",
    "empty": {
      "title": "Diagnostics ready",
      "message": "Enter a query or request an analysis.",
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
      "users": "Operators",
      "analytics": "Analytics",
      "featureFlags": "Feature Flags",
      "systemLogs": "System Logs"
    },
    "overview": {
      "title": "Operations Overview",
      "loading": "Querying ops metrics…",
      "refresh": "Resync metrics",
      "fallback": "(showing mock data for development)",
      "totalUsers": "Total Operators",
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
      "productivity": "Throughput Metrics",
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
        "userGrowth": "Operator Growth",
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
        "user_management": "Operator Management",
        "feature_flags": "Feature Flags",
        "system_logs": "System Logs",
        "analytics": "Analytics",
        "debug_mode": "Debug Mode"
      },
      "confirm": {
        "title": "Confirm Flag Changes",
        "message": "Apply these changes? This will immediately affect all operators.",
        "warning": "Tip: Test on staging first. Disabling core flags may break operator workflows."
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
  "projectSwarmdesk": {
    "statsPanel": {
      "title": "Project Metrics",
      "pending": "Pending",
      "completed": "Resolved",
      "blocked": "Blocked",
      "review": "Triage"
    },
    "todoPanel": {
      "title": "Ticket Queue",
      "empty": "Board clear — no open tickets.",
      "loading": "Querying tickets…",
      "create": "Open Ticket"
    },
    "exitButton": "Exit Ops Environment",
    "error": "Failed to load ops environment: {{error}}"
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
  "desktop": {
    "deleteBranch": "Decommission branch",
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
  "labMaintenance": {
    "duplicates": {
      "title": "Duplicate Ticket Detection",
      "description": "Identify and consolidate near-duplicate tickets across projects.",
      "threshold": "Similarity",
      "scan": "Scan",
      "scanning": "Querying…",
      "noResults": "No duplicate tickets detected at this threshold.",
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
    }
  },
  "menu": {
    "documentation": "Runbooks",
    "replayTutorial": "Replay Onboarding",
    "lessonRefiner": "Runbook Refiner"
  },
  "projectNavigator": {
    "subtitle": "Select active project • Enter focused ops environment",
    "refreshTooltip": "Resync Project Data",
    "mainSwarmDeskTooltip": "Open Main Swarmdesk",
    "stats": {
      "pending": "pending",
      "review": "triage"
    },
    "activity": {
      "title": "Recent Events",
      "noActivity": "No recent events"
    },
    "createCta": {
      "title": "Provision New Project",
      "subtitle": "Resources available — stand up a new environment"
    }
  },
  "onboarding": {
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
        "description": "Let's provision a project to organize your tickets.",
        "skipHint": "You can skip this and provision a project later from the Create console"
      },
      "add-todo": {
        "title": "Open a Ticket",
        "description": "Now let's open a ticket in your project.",
        "guideTitle": "How to open a ticket:",
        "step1": "Click the floating '+' button again",
        "step2": "Select the 'Ticket' tab in the dialog",
        "step3": "Enter your ticket description",
        "step4": "Assign the project from the dropdown",
        "step5": "Set priority and click 'Open Ticket'",
        "hint": "Tip: You can open tickets from anywhere using the '+' button"
      },
      "configure-ai": {
        "title": "Configure AI Diagnostics",
        "description": "Connect an AI provider to unlock advanced analytics.",
        "statusConfigured": "Status: ✅ AI diagnostics configured and ready.",
        "statusNotConfigured": "Status: ❌ AI diagnostics not configured",
        "configureButton": "Configure AI Now",
        "skipButton": "Skip for Now",
        "helpText": "You can configure AI anytime from Settings → AI Configuration"
      },
      "swarmdesk": {
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
  "lessonsLearned": {
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
    "briefSaved": "Committed",
    "deleteFailed": "Decommission failed",
    "save": "Commit",
    "saveFailed": "Commit failed",
    "cancel": "Discard",
    "projectRequired": "Project is required"
  },
  "constellation": {
    "contextMenu": {
      "openInSwarmDesk": "Open in SwarmDesk"
    },
    "controls": {
      "recenter": "Recenter",
      "fullscreen": "Fullscreen"
    }
  }
}

result = deep_merge(labops, overrides)
save("labops", result)
print("labops.json written (batch 3)")

r = subprocess.run(["node", "-e", "require('./labops.json'); console.log('JSON valid')"],
                   capture_output=True, text=True, cwd=THEMES_DIR)
print(r.stdout.strip() or r.stderr.strip())
