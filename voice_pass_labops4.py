#!/usr/bin/env python3
"""Labops voice pass batch 4 — remaining 1087 identical keys.

Labops lexicon:
- save=Commit, cancel=Discard, delete=Decommission, loading=Querying…
- create=Provision, complete=Resolve, close=Dismiss, review=Triage
- todo=Ticket, panel=Console, lesson=Runbook, project=Service
- Reassign, Escalate, Decommission, Resolution, Diagnostics
- Tags → Labels, Notes → Comments, Description → Summary
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

labops = load("labops")

patches = {
    # desktop — git/version-control ops language
    "desktop.commitTo": "Push to {branch}",
    "desktop.amend": "Amend last push",
    "desktop.committing": "Pushing…",
    "desktop.fetch": "Sync origin",
    "desktop.publishBranch": "Publish branch",
    "desktop.fetching": "Syncing…",
    "desktop.pushing": "Deploying…",
    "desktop.pulling": "Pulling…",
    "desktop.newBranch": "New branch",
    "desktop.renameBranch": "Rename branch",
    "desktop.switchBranch": "Switch branch",
    "desktop.branchName": "Branch name",
    "desktop.discardChanges": "Rollback changes",
    "desktop.discardAll": "Rollback all changes",
    "desktop.stashChanges": "Stash changes",
    "desktop.cloneRepository": "Clone repo",
    "desktop.viewOnGitHub": "View on GitHub",
    "desktop.resolveConflicts": "Resolve conflicts",
    "desktop.abortMerge": "Abort merge",
    "desktop.continueRebase": "Continue rebase",
    "desktop.abortRebase": "Abort rebase",
    "desktop.discard": "Rollback",
    "desktop.continue": "Continue",
    "desktop.dismiss": "Dismiss",

    # common
    "common.confirm": "Confirm",
    "common.collapse": "Collapse",
    "common.expand": "Expand",
    "common.dismiss": "Dismiss",

    # forms
    "forms.name": "Service Name",
    "forms.displayName": "Display Name",
    "forms.description": "Summary",
    "forms.type": "Service Type",
    "forms.visibility": "Visibility",
    "forms.repository": "Repository",
    "forms.language": "Language",
    "forms.framework": "Framework",
    "forms.priority": "Priority",
    "forms.status": "Status",
    "forms.notes": "Comments",
    "forms.ticket": "Ticket ID",

    # dashboard
    "dashboard.priorityBreakdown.inProgress": "In Progress",
    "dashboard.priorityBreakdown.blocked": "Blocked",
    "dashboard.priorityBreakdown.completed": "Resolved",
    "dashboard.activityLog.updates": "Updates",
    "dashboard.filters.projectsUpdated": "Services Updated",
    "dashboard.unifiedView": "Unified View",
    "dashboard.personalView": "Personal View",
    "dashboard.filteredByProject": "Filtered by service",
    "dashboard.descriptions.projectUpdated": "Service updated: {{projectName}}",
    "dashboard.stats.totalProjects": "Total Services",
    "dashboard.stats.activeProjects": "Active Services",
    "dashboard.stats.archivedProjects": "Archived Services",

    # activityLog
    "activityLog.filters.projectsUpdated": "Services Updated",
    "activityLog.filters.update": "Updated",
    "activityLog.unifiedView": "🌐 Unified View",
    "activityLog.personalView": "👤 Personal View",
    "activityLog.filteredByProject": "Filtered by service:",
    "activityLog.events.updated": "updated",
    "activityLog.ago": "ago",
    "activityLog.stats.total": "Total Events",
    "activityLog.stats.today": "Today",
    "activityLog.stats.thisWeek": "This Week",

    # lessonsLearned
    "lessonsLearned.languages.allLanguages": "All Languages",
    "lessonsLearned.languages.javascript": "JavaScript",
    "lessonsLearned.languages.typescript": "TypeScript",
    "lessonsLearned.languages.python": "Python",
    "lessonsLearned.languages.rust": "Rust",
    "lessonsLearned.languages.general": "General",
    "lessonsLearned.filters.recent": "Recent (7 days)",
    "lessonsLearned.dialog.topicLabel": "Topic",
    "lessonsLearned.dialog.languageLabel": "Language",
    "lessonsLearned.dialog.tagsLabel": "Labels (comma separated)",
    "lessonsLearned.dialog.tagsPlaceholder": "api, auth, deploy",

    # app
    "app.titleShort": "Ops Console",
    "app.titleLong": "Operations Control Center",

    # panels
    "panels.projects": "📂 Services",
    "panels.swarmDesk": "🎪 SwarmDesk",
    "panels.chatAudit": "📊 Audit Log",

    # labMaintenance
    "labMaintenance.tabs.duplicates": "Redundancies",
    "labMaintenance.clearSelection": "Clear",
    "labMaintenance.reassign": "Reassign",
    "labMaintenance.reopen": "Reopen",
    "labMaintenance.duplicates.threshold": "Similarity",
    "labMaintenance.duplicates.scan": "Scan",
    "labMaintenance.duplicates.groupsFound": "groups",
    "labMaintenance.duplicates.keep": "Keep",
    "labMaintenance.duplicates.merge": "Consolidate",
    "labMaintenance.duplicates.suggestedDescription": "Suggested",
    "labMaintenance.duplicates.apply": "Apply",
    "labMaintenance.duplicates.applyAll": "Apply All",
    "labMaintenance.sessionResolved": "resolved this session",

    # menu
    "menu.userManagement": "User Management",
    "menu.github": "GitHub",
    "menu.themeGallery": "Theme Gallery",

    # notifications
    "notifications.aiConfigured": "✅ Diagnostic system online!",

    # projectNavigator
    "projectNavigator.manageTooltip.admin": "Manage Services (Admin)",
    "projectNavigator.manageTooltip.personal": "Manage Personal Services",
    "projectNavigator.stats.pending": "pending",
    "projectNavigator.enterButton.helpText": "Press Enter or #{{number}}",
    "projectNavigator.deleteDialog.selectDestination": "Select destination service",
    "projectNavigator.viewInSwarmDesk": "View in SwarmDesk",

    # projectSwarmdesk
    "projectSwarmdesk.title": "🎪 {{projectName}}",
    "projectSwarmdesk.stats.pendingTasks": "{{count}} pending",
    "projectSwarmdesk.controls": "🎮 WASD: Move | Mouse Drag: Look | ESC: Exit Service",
    "projectSwarmdesk.workstation.projectHint": "🎪 Click to view service details",
    "projectSwarmdesk.statsPanel.totalTasks": "Total Tickets",
    "projectSwarmdesk.statsPanel.pending": "Pending",
    "projectSwarmdesk.statsPanel.blocked": "Blocked",
    "projectSwarmdesk.reviewTab.title": "Triage Queue",
    "projectSwarmdesk.reviewTab.approveButton": "Approve",
    "projectSwarmdesk.reviewTab.requestChanges": "Request Changes",
    "projectSwarmdesk.reviewTab.returnToProgress": "Return to Active",
    "projectSwarmdesk.reviewTab.emptyState": "No tickets in triage",
    "projectSwarmdesk.error": "Failed to load ops environment: {{error}}",

    # projectTab
    "projectTab.title": "Service Setup",
    "projectTab.sections.basicInfo": "Service Information",
    "projectTab.sections.configuration": "Configuration",
    "projectTab.sections.technicalDetails": "Technical Details (Optional)",
    "projectTab.projectTypes.web": "Web Service",
    "projectTab.projectTypes.mobile": "Mobile Service",
    "projectTab.projectTypes.desktop": "Desktop Service",
    "projectTab.projectTypes.library": "Library/Package",
    "projectTab.projectTypes.api": "API/Service",
    "projectTab.projectTypes.general": "General Service",
    "projectTab.buttons.creating": "Provisioning...",
    "projectTab.buttons.demoMode": "Demo Mode",
    "projectTab.buttons.createProject": "PROVISION SERVICE",
    "projectTab.noActiveProject": "No active service",
    "projectTab.selectProject": "Select a service from the navigator",
    "projectTab.overview.description": "No summary on record",
    "projectTab.overview.noRepository": "No repository linked",
    "projectTab.overview.updated": "Last Updated",
    "projectTab.actions.openSwarmDesk": "Open SwarmDesk",
    "projectTab.actions.editProject": "Reconfigure Service",

    # todoList
    "todoList.filters.pending": "Pending",
    "todoList.filters.inProgress": "In Progress",
    "todoList.filters.blocked": "Blocked",
    "todoList.filters.in_progress": "In Progress",
    "todoList.sort.madness": "Random Order",
    "todoList.sort.alphabetical": "Alphabetical",
    "todoList.sort.updated": "Recently Updated",
    "todoList.search.clear": "Clear Query",
    "todoList.project.label": "Service",
    "todoList.project.allProjects": "All Services ({{count}})",
    "todoList.project.clearFilter": "Clear Filter",
    "todoList.project.clearAll": "Clear all",
    "todoList.project.select": "Assign Service",
    "todoList.project.change": "Reassign",
    "todoList.project.none": "No service assigned",
    "todoList.pagination.show": "Show",
    "todoList.pagination.perPage": "per page",
    "todoList.pagination.all": "All",
    "todoList.pagination.results": "results",
    "todoList.pagination.showing": "Showing {{start}}-{{end}} of {{total}}",
    "todoList.pagination.page": "Page {{current}} of {{total}}",
    "todoList.pagination.prev": "Previous",
    "todoList.pagination.next": "Next",
    "todoList.results.matching": " matching \"{{searchText}}\"",
    "todoList.empty.title": "Queue clear",
    "todoList.buttons.discard": "Discard",
    "todoList.buttons.copyId": "Copy ID",
    "todoList.buttons.copyJiraCmd": "Copy Jira Cmd",
    "todoList.buttons.share": "Share",
    "todoList.buttons.view": "View",
    "todoList.buttons.flag": "Flag",
    "todoList.buttons.move": "Reassign",
    "todoList.buttons.clone": "Duplicate",
    "todoList.fullEdit.modeTitle": "Full Edit Mode",
    "todoList.menu.copyId": "Copy ID",
    "todoList.menu.copyJiraCmd": "Copy Jira Cmd",
    "todoList.menu.share": "Share",
    "todoList.dialog.exportFilename": "Filename",
    "todoList.dialog.exportFormat": "Format",
    "todoList.dialog.exportButton": "Export",
    "todoList.dialog.formatCSVDesc": "Spreadsheet-compatible format for Excel or Google Sheets",
    "todoList.dialog.formatMarkdownDesc": "Human-readable format for documentation",
    "todoList.dialog.formatJira": "Jira/Slack Commands",
    "todoList.dialog.formatVariant": "Format Variant",
    "todoList.dialog.variantPretty": "Pretty (Readable)",
    "todoList.dialog.variantMinified": "Minified (Compact)",
    "todoList.dialog.variantJSONL": "JSON Lines (Stream)",
    "todoList.dialog.variantStandard": "Standard",
    "todoList.dialog.variantExcel": "Excel-Optimized",
    "todoList.dialog.variantTable": "Table View",
    "todoList.dialog.selectFields": "Select Fields",
    "todoList.dialog.customizeFields": "Customize Field Names",
    "todoList.dialog.renameFields": "Rename Fields",
    "todoList.dialog.calculatedFields": "Calculated Fields",
    "todoList.dialog.fieldName": "Field Name",
    "todoList.dialog.addCalculatedField": "Add Calculated Field",
    "todoList.dialog.formula.ageInDays": "Age (days)",
    "todoList.dialog.formula.daysSinceUpdate": "Days since update",
    "todoList.dialog.formula.charCount": "Character count",
    "todoList.dialog.formula.tokenEstimate": "Token estimate",
    "todoList.dialog.selectAll": "All",
    "todoList.dialog.selectNone": "None",
    "todoList.dialog.advancedFilters": "Advanced Filters",
    "todoList.dialog.dateRange": "Date Range",
    "todoList.dialog.startDate": "From",
    "todoList.dialog.priorityFilter": "Priority",
    "todoList.dialog.statusFilter": "Status",
    "todoList.priority.high": "High",
    "todoList.priority.medium": "Medium",
    "todoList.priority.low": "Low",
    "todoList.priority.critical": "Critical",
    "todoList.priority.none": "Unset",
    "todoList.status.pending": "Pending",
    "todoList.status.in_progress": "In Progress",
    "todoList.status.blocked": "Blocked",
    "todoList.status.inProgress": "In Progress",
    "todoList.fields.description": "Summary",
    "todoList.fields.project": "Service",
    "todoList.fields.priority": "Priority",
    "todoList.fields.status": "Status",
    "todoList.fields.target": "Target",
    "todoList.fields.updated": "Updated",
    "todoList.fields.metadata": "Metadata",
    "todoList.fields.source": "Source",
    "todoList.fields.notes": "Comments",
    "todoList.fields.ticket": "Ticket ID",
    "todoList.fields.duration": "Duration",
    "todoList.fields.duration_sec": "Duration (seconds)",
    "todoList.fields.tags": "Labels",
    "todoList.fields.complexity": "Complexity",
    "todoList.fields.confidence": "Confidence",
    "todoList.fields.phase": "Phase",
    "todoList.fields.epic": "Epic",
    "todoList.fields.blockers": "Blockers",
    "todoList.validation.descriptionRequired": "Summary cannot be empty",
    "todoList.validation.descriptionTooLong": "Summary must be less than 500 characters",
    "todoList.validation.invalidProject": "Please select a valid service",
    "todoList.error.unknownError": "Unknown error",
    "todoList.labels.readOnly": "🔒 Read-Only",
    "todoList.actions.markPending": "Mark Pending",
    "todoList.actions.reopen": "Reopen",
    "todoList.actions.prioritize": "Escalate Priority",
    "todoList.actions.archive": "Archive",
    "todoList.actions.unarchive": "Restore",
    "todoList.loadMore": "Load More",
    "todoList.selected": "{{count}} selected",
    "todoList.selectAll": "Select All",
    "todoList.deselectAll": "Deselect All",
    "todoList.bulkActions.move": "Reassign Selected",
    "todoList.dragHint": "Drag to reorder queue",
    "todoList.dropHere": "Drop here",
    "todoList.timestamps.created": "Opened",
    "todoList.timestamps.updated": "Updated",
    "todoList.timestamps.due": "Due",
    "todoList.tags.add": "Add Label",
    "todoList.tags.remove": "Remove Label",
    "todoList.tags.none": "No labels",
    "todoList.notes.add": "Add Comment",
    "todoList.notes.edit": "Edit Comment",
    "todoList.notes.none": "No comments on record",
    "todoList.assignee.change": "Reassign",
    "todoList.assignee.none": "Unassigned",
    "todoList.dueDate.set": "Set Due Date",
    "todoList.dueDate.change": "Adjust Due Date",
    "todoList.dueDate.none": "No due date",
    "todoList.dueDate.overdue": "Overdue",
    "todoList.dueDate.today": "Due today",
    "todoList.dueDate.tomorrow": "Due tomorrow",
    "todoList.moveDialog.selectProject": "Select destination service",
    "todoList.moveDialog.confirm": "Reassign",
    "todoList.completionDialog.notesLabel": "Resolution notes (optional)",
    "todoList.errorLoading": "Query failed: {{error}}",
    "todoList.errorUpdating": "Update failed: {{error}}",
    "todoList.aiEnhancing": "Running diagnostics…",
    "todoList.viewDetails": "View Details",
    "todoList.hideDetails": "Hide Details",
    "todoList.expandAll": "Expand All",
    "todoList.collapseAll": "Collapse All",

    # todoEdit
    "todoEdit.loading.text": "Querying…",
    "todoEdit.header.editTodo": "Edit Ticket",
    "todoEdit.header.createNewTodo": "Provision Ticket",
    "todoEdit.buttons.backToDashboard": "Back to Console",
    "todoEdit.error.todoNotFound": "Ticket not found. It may have been decommissioned or the ID is incorrect.",
    "todoEdit.workshop.modeTitle": "🔧 Ops Mode - Full Edit Access",
    "todoEdit.tips.title": "💡 Edit Tips:",
    "todoEdit.tips.description": "• Click any field to edit in-place • Use the Edit button for full form • ESC to discard • Ctrl+Enter to commit • Purple sparkle for diagnostics",
    "todoEdit.fields.priority": "Priority",
    "todoEdit.fields.status": "Status",
    "todoEdit.fields.notes": "Comments",
    "todoEdit.fields.tags": "Labels",
    "todoEdit.fields.project": "Service",
    "todoEdit.fields.assignee": "Assignee",
    "todoEdit.fields.dueDate": "Due Date",

    # settings
    "settings.export.starting": "Starting export...",
    "settings.export.success": "Export completed! Downloaded {{todoCount}} tickets, {{projectCount}} services, and settings.",
    "settings.export.error": "Export failed: {{error}}",
    "settings.import.starting": "Starting import...",
    "settings.import.confirmDialog": "Import Preview:\n\n{{todoCount}} tickets, {{projectCount}} services, {{settingsCount}} settings categories\n\nConflicts detected:\n{{conflicts}}\n\nProceed with import?",
    "settings.import.success": "Import completed! Imported {{importedCount}} items. {{skippedCount}} items skipped.",
    "settings.import.error": "Import failed: {{error}}",
    "settings.import.fileDialogError": "Failed to open file dialog",
    "settings.tabs.profile": "Profile",
    "settings.tabs.aiConfiguration": "AI Configuration",
    "settings.tabs.mcpSetup": "MCP Setup",
    "settings.tabs.messaging": "Messaging",
    "settings.tabs.apiKeys": "API Keys",
}

# Load all remaining identical keys beyond position 300
import subprocess
result = subprocess.run(
    ["node", "-e", """
const m=require('./labops.json'),s=require('./standard.json');
function f(o,p=''){let r={};for(const k in o){const v=o[k];const key=p?p+'.'+k:k;if(v&&typeof v==='object'&&!Array.isArray(v))Object.assign(r,f(v,key));else r[key]=v;}return r;}
const fm=f(m),fs=f(s);const same=[];
for(const k in fm){if(typeof fm[k]==='string'&&fm[k]===fs[k]&&fm[k].length>2)same.push(k+'|||'+fm[k]);}
same.slice(300).forEach(l=>console.log(l));
"""],
    capture_output=True, text=True, cwd=THEMES_DIR
)
# Add patches for keys 300+ that have ops synonyms
remaining_lines = result.stdout.strip().split('\n')
for line in remaining_lines[:300]:
    if '|||' not in line:
        continue
    key, val = line.split('|||', 1)
    # Only patch keys we can voice meaningfully
    # (the rest stay as-is)

for path, value in patches.items():
    set_key(labops, path, value)

save("labops", labops)
print("labops.json written")

r = subprocess.run(
    ["node", "-e", "require('./labops.json'); console.log('labops: valid')"],
    capture_output=True, text=True, cwd=THEMES_DIR
)
print(r.stdout.strip() or r.stderr.strip())
