#!/usr/bin/env python3
"""
Voice pass labops - batch 2: swarmDesk, remaining todoList/settings/admin/etc.
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
  "swarmDesk": {
    "ui": {
      "loading": {
        "entering": "🖥️ Connecting to Ops Environment…",
        "initializing": "⚙️ Initializing SwarmDesk…",
        "ready": "✅ System Nominal",
        "connecting": "🔗 Linking to Services…",
        "loadingProjects": "📊 Querying Project Data…",
        "title": "🖥️ Standing Up SwarmDesk Workspace…",
        "subtitle": "Preparing Ops Console"
      },
      "navigation": {
        "controls": "⌨️ Navigation Controls",
        "movement": "⌨️ WASD: Move Camera | Mouse: Look Around",
        "interaction": "🖱️ Click: Interact | E: Action | Space: Quick Action",
        "escape": "🚪 ESC: Return to Dashboard | M: Menu"
      },
      "status": {
        "connected": "🌐 Network: CONNECTED",
        "offline": "⚠️ Network: OFFLINE — Local Mode",
        "syncing": "🔄 Syncing datastore…",
        "ready": "✅ SwarmDesk: NOMINAL"
      },
      "error": {
        "title": "❌ SwarmDesk System Error",
        "subtitle": "Check ops console for technical details",
        "initializationFailed": "SwarmDesk workspace initialization failed"
      },
      "controls": {
        "instructions": "🖥️ SwarmDesk Active | WASD: Navigate | E: Primary Action | F4-F7: Open Panels | Space: Performance Mode"
      }
    },
    "panels": {
      "welcome": {
        "title": "🖥️ SwarmDesk Ops Center",
        "subtitle": "Ops Console Ready",
        "description": "Welcome to the SwarmDesk ops environment. Use navigation controls to move through the 3D space and interact with project nodes.",
        "gettingStarted": "Getting started:",
        "features": {
          "title": "🎯 Console Features:",
          "draggable": "📱 Draggable console panels with magnetic docking",
          "contextual": "🏷️ Contextual tabs respond to workspace interactions",
          "docking": "🧲 Docking zones at workspace edges and corners",
          "shortcuts": "⌨️ Keyboard shortcuts for rapid access",
          "integration": "🖥️ Full SwarmDesk 3D environment integration"
        },
        "actions": {
          "createProject": "📋 Open Project Panel",
          "createAgent": "🤖 Open Agent Panel"
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
            "title": "📊 Panel Controls"
          },
          "actions": {
            "title": "⚡ Actions"
          }
        },
        "f3": "F3 — Toggle Welcome Panel",
        "f4": "F4 — Toggle Project Panel",
        "f5": "F5 — Toggle Agent Panel",
        "f6": "F6 — Toggle System Tools",
        "f7": "F7 — Toggle Analytics Panel",
        "f8": "F8 — Toggle WebLLM Panel",
        "f9": "F9 — Toggle MQTT Monitor",
        "f10": "F10 — Minimize All Panels",
        "f11": "F11 — Close All Panels",
        "esc": "ESC — Cancel current operation",
        "drag": "Drag panels — Click and drag panel headers",
        "dock": "Dock panels — Drag near workspace edges to anchor"
      },
      "mcp": {
        "title": "🔗 MCP Integration Hub",
        "subtitle": "Service Integration Layer",
        "description": "The Model Context Protocol (MCP) connects to external tools and services for enhanced automation and ops functionality.",
        "gettingStarted": "Setup instructions:",
        "tools": {
          "title": "🛠️ Available MCP Tools",
          "notAuthenticated": "Authenticate to access MCP tools.",
          "authRequired": "Authentication required to connect to MCP services",
          "connecting": "No tools available. Connecting to service…",
          "serverStatus": "Service Status: {{status}}",
          "retryConnection": "🔄 Retry Connection",
          "connectedAs": "Connected as: {{username}}"
        },
        "history": {
          "title": "📜 Command History",
          "noHistory": "No command history."
        },
        "debug": {
          "title": "🐛 Debug Info",
          "authentication": "Authentication: {{status}}",
          "user": "User: {{user}}",
          "authMode": "Mode: {{mode}}",
          "mcpServer": "MCP Server: {{status}}",
          "activeTools": "Active Tools: {{count}}",
          "lastPing": "Last Ping: {{time}}",
          "apiService": "API Service: {{status}}",
          "authContext": "Auth Context: {{status}}",
          "refreshAuth": "🔄 Refresh Auth"
        }
      },
      "project": {
        "overview": {
          "title": "📊 Project Overview",
          "activeProjects": "Active Projects: 5",
          "pendingTasks": "Pending Tickets: 23",
          "completedToday": "Resolved Today: 7",
          "actions": {
            "viewAll": "📋 View All Projects",
            "addTask": "➕ Open Ticket"
          }
        },
        "todos": {
          "title": "✅ Ticket Queue",
          "inProgress": "🖥️ Dashboard Integration — In Progress",
          "pending": "🔧 MCP Enhancement — Pending",
          "actions": {
            "addTodo": "➕ Open Ticket"
          }
        },
        "files": {
          "title": "📁 System Files",
          "actions": {
            "browse": "📂 Browse File Archive"
          }
        }
      },
      "agent": {
        "chat": {
          "title": "💬 Agent Channel",
          "agentReady": "Agent: Ready for ops tasks.",
          "userQuery": "Operator: Help with the floating panels",
          "agentResponse": "Agent: The panel system is flexible — drag anywhere and dock to edges.",
          "placeholder": "Enter query…"
        },
        "commands": {
          "title": "⚡ Agent Commands",
          "searchProjects": "🔍 Query Projects",
          "listTodos": "📋 List Tickets",
          "deployProject": "🚀 Deploy Project",
          "generateReport": "📊 Generate Report"
        },
        "interface": {
          "title": "💬 {{agentName}} Agent Interface",
          "role": "Role: {{role}}",
          "status": "Status: {{status}}",
          "actions": {
            "startConversation": "💬 Open Channel",
            "executeCommand": "⚡ Execute Command"
          }
        },
        "capabilities": {
          "title": "⚡ Agent Capabilities",
          "projectManagement": "✅ Project Management",
          "codeAnalysis": "✅ Code Analysis",
          "mcpIntegration": "✅ MCP Integration",
          "communication": "✅ Real-time Communication"
        }
      },
      "analytics": {
        "metrics": {
          "title": "📈 System Performance Metrics",
          "cpuUsage": "CPU Usage: 42%",
          "memory": "Memory: 68%",
          "activePanels": "Active Panels: {{count}}",
          "uptime": "Uptime: 2h 15m"
        },
        "activity": {
          "title": "🚀 Recent Activity",
          "panelCreated": "🏷️ Panel created: Project Management",
          "swarmDeskInteraction": "🖥️ SwarmDesk: Workstation selected",
          "mcpToolExecuted": "🔧 MCP tool executed: list_projects"
        },
        "insights": {
          "title": "💡 Ops Insights",
          "mostUsedPanel": "Most used panel: Project Management",
          "peakActivity": "Peak activity: 14:00-15:00",
          "efficiencyScore": "Efficiency score: 87%"
        }
      },
      "webllm": {
        "models": {
          "title": "🧠 Available LLM Models",
          "currentModel": "Current Model: {{model}}",
          "loadModel": "Load Model"
        },
        "compatibility": {
          "title": "✅ Browser Compatibility",
          "checking": "🔄 Checking compatibility…",
          "checkCompatibility": "🔍 Check Compatibility"
        },
        "status": {
          "title": "⚡ WebLLM Status",
          "initialized": "Initialized: {{status}}",
          "currentModel": "Current Model: {{model}}",
          "loading": "Loading: {{status}}",
          "inferencing": "Inference: {{status}}",
          "queueLength": "Queue Length: {{length}}",
          "loadedModels": "Loaded Models: {{count}}",
          "mode": "Mode: {{mode}}",
          "initialize": "🚀 Initialize WebLLM"
        },
        "settings": {
          "title": "⚙️ WebLLM Config",
          "agentModelAssignment": "Agent Model Assignment:",
          "useGlobal": "Use Global Model",
          "perAgent": "Per-Agent Models",
          "temperature": "Temperature:",
          "maxTokens": "Max Tokens:",
          "saveSettings": "💾 Commit Config",
          "resetDefaults": "🔄 Reset to Defaults"
        }
      },
      "mqtt": {
        "logs": {
          "title": "📋 MQTT Live Feed",
          "noMessages": "No messages received…",
          "waitingTraffic": "Waiting for MQTT traffic on port 4140",
          "reconnect": "🔄 Reconnect",
          "messages": "Messages: {{count}}",
          "lastMessage": "Last: {{time}}",
          "clearLogs": "🗑️ Purge Feed",
          "export": "💾 Export Archive"
        },
        "status": {
          "title": "🔌 MQTT Connection",
          "status": "Connection: {{status}}",
          "broker": "Broker: {{broker}}",
          "clientId": "Client ID: swarmdesk_{{id}}",
          "messagesReceived": "Messages Received: {{count}}",
          "lastActivity": "Last Activity: {{time}}",
          "subscriptions": "📡 Subscriptions:",
          "connect": "🔄 Connect",
          "disconnect": "🔌 Disconnect"
        },
        "settings": {
          "title": "⚙️ MQTT Config",
          "brokerAddress": "Broker Address:",
          "subscribeTopics": "Subscribe Topics:",
          "autoReconnect": "Auto-reconnect on disconnect",
          "showTimestamps": "Show timestamps",
          "saveSettings": "💾 Commit Config",
          "resetDefaults": "🔄 Reset to Defaults"
        }
      }
    },
    "projectData": {
      "title": "📂 Project Registry",
      "subtitle": "Project Management Hub",
      "description": "Project registry and ops tooling for organizing work and tracking progress.",
      "projectReadmes": {
        "inventorium": {
          "title": "📊 Inventorium — Ops Dashboard",
          "description": "Ticket management and project ops dashboard with integrated tools and analytics."
        },
        "omnispindle": {
          "title": "🔗 Omnispindle — Integration Platform",
          "description": "Communication and coordination platform connecting tools and services for streamlined ops."
        }
      },
      "swarmDesk": {
        "title": "🖥️ SwarmDesk",
        "description": "3D interactive ops command center — the ops interface for the Madness Interactive environment",
        "status": "🔥 Active Development",
        "visibility": "public repository"
      },
      "inventorium": {
        "title": "📦 Inventorium",
        "description": "Ticket management system — track agents at speed, edit their tasks as they process and execute",
        "status": "🚀 Active Development (private repository)",
        "visibility": "private environment"
      },
      "swarmonomicon": {
        "title": "🐝 Swarmonomicon",
        "description": "AI agent swarm coordination system for centralized orchestration and collective intelligence",
        "status": "✨ Modularly functional",
        "visibility": "public repository"
      }
    },
    "errors": {
      "connectionFailed": "❌ Connection Failed",
      "loadingError": "⚠️ Query Error",
      "permissionDenied": "🔒 Access Denied",
      "systemUnavailable": "🚫 System Unavailable",
      "unknownError": "❓ Unknown Error",
      "initializationFailed": "SwarmDesk scripts failed to load within timeout",
      "sceneInitFailed": "❌ Scene initialization failed:",
      "panelSystemFailed": "❌ Failed to create panel system:",
      "panelSystemMissing": "⚠️ FloatingPanelSystem unavailable",
      "controlsInitFailed": "Failed to initialize controls:",
      "basicSceneFailed": "❌ Failed to initialize Three.js scene:"
    },
    "status": {
      "initializing": "⚙️ Initializing…",
      "loading": "📊 Loading config…",
      "ready": "✅ System Nominal",
      "error": "❌ System Error",
      "offline": "⚠️ Offline Mode — Limited Features",
      "initialized": "✅ SwarmDesk initialized",
      "scriptsLoaded": "✅ SwarmDesk scripts loaded",
      "scriptsTimeout": "⚠️ SwarmDesk scripts load timeout",
      "containerNotReady": "⚠️ Container not ready",
      "panelSystemExists": "🏷️ Panel system exists — verifying state",
      "panelSystemMissing": "⚠️ Panel system missing keyboard handler — reinitializing…",
      "panelSystemCreated": "✅ Panel system created"
    },
    "actions": {
      "create": "🆕 Provision",
      "view": "👁️ View Details",
      "edit": "✏️ Edit Ticket",
      "delete": "🗑️ Decommission",
      "refresh": "🔄 Resync",
      "connect": "🔗 Connect Service",
      "deploy": "🚀 Deploy Project",
      "monitor": "📊 Monitor Metrics",
      "optimize": "⚡ Optimize Allocation",
      "analyze": "📈 Run Analysis",
      "configure": "⚙️ Configure Parameters"
    }
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
  "todoList": {
    "aiEnhance": "Run Diagnostics",
    "aiEnhancing": "Running diagnostics…",
    "spellsAvailable": "Diagnostics available",
    "viewDetails": "View Details",
    "hideDetails": "Hide Details",
    "expandAll": "Expand All",
    "collapseAll": "Collapse All",
    "errorLoading": "Query failed: {{error}}",
    "errorUpdating": "Update failed: {{error}}",
    "errorDeleting": "Decommission failed: {{error}}",
    "successComplete": "Ticket resolved",
    "successDelete": "Ticket decommissioned",
    "successMove": "Ticket reassigned"
  },
  "settings": {
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
    "repoUrl": "Repository URL",
    "branch": "Branch",
    "depth": "Analysis Depth",
    "generateFromRepo": "Generate from Repository",
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
    "error": {
      "generate": "Generation failed: {{error}}",
      "upload": "Upload failed: {{error}}",
      "load": "Query failed: {{error}}"
    },
    "success": {
      "generated": "Code map generated",
      "uploaded": "Map uploaded to archive",
      "deleted": "Map decommissioned",
      "restored": "Version restored"
    }
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
    "error": "Topology query failed: {{error}}",
    "refresh": "Resync Topology",
    "addNode": "Add Node",
    "editNode": "Edit Node",
    "deleteNode": "Remove Node",
    "connectNodes": "Link Nodes",
    "disconnectNodes": "Unlink Nodes"
  },
  "chatAssistant": {
    "newConversation": "New Session",
    "clearHistory": "Purge History",
    "confirmClear": "Purge all session history?",
    "history": "Session History",
    "noHistory": "No session history"
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
    "historyTitle": "Session History",
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
  "admin": {
    "overview": {
      "productivity": "Productivity Metrics",
      "totalTodos": "Total Tickets",
      "completedTodos": "Resolved",
      "completionRate": "Resolution Rate"
    },
    "analytics": {
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
    "featureFlags": {
      "flags": {
        "basic_todos": "Basic Tickets",
        "export_todos": "Export Tickets",
        "unlimited_todos": "Unlimited Tickets",
        "mindmap_view": "Topology View",
        "advanced_search": "Advanced Query"
      }
    },
    "users": {
      "title": "Operator Management",
      "loading": "Querying operator roster…",
      "refresh": "Resync roster",
      "searchPlaceholder": "Query by email or name…",
      "users": "operators",
      "empty": "No operators registered",
      "noResults": "No operators match this query",
      "edit": {
        "title": "Edit Operator",
        "cancel": "Discard",
        "save": "Commit",
        "saving": "Committing…"
      },
      "columns": {
        "todos": "Tickets"
      },
      "confirm": {
        "cancel": "Discard",
        "saving": "Committing…"
      }
    }
  },
  "notifications": {
    "taskCreated": "🎉 Ticket provisioned.",
    "projectCreated": "🔬 New project provisioned."
  },
  "success": {
    "status": {
      "no_session": {
        "title": "SESSION NOT FOUND",
        "subtitle": "No checkout session detected. Did you navigate here directly?"
      }
    },
    "log": {
      "initializing": "Initializing payment verification…",
      "connecting": "Connecting to Stripe…",
      "conduitStable": "Payment confirmed: STABLE",
      "allSystemsGo": "STATUS: ALL SYSTEMS GO",
      "paymentIncomplete": "WARNING: Payment incomplete",
      "verificationFailed": "Verification failed"
    },
    "errorRetry": "If payment was processed, your upgrade will activate shortly.",
    "checkBilling": "Check billing for current status."
  },
  "questTab": {
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
  }
}

result = deep_merge(labops, overrides)
save("labops", result)
print("labops.json written (batch 2)")

import subprocess
r = subprocess.run(["node", "-e", "require('./labops.json'); console.log('JSON valid')"],
                   capture_output=True, text=True, cwd=THEMES_DIR)
print(r.stdout.strip() or r.stderr.strip())
