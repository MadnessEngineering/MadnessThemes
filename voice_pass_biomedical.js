#!/usr/bin/env node
/* Biomedical voice pass — tail batch.
 * Applies the biomedical voice card (VOICE_GUIDE.md) to keys still identical to standard.json.
 * Tone = LOW/clinical. validation.* and error bodies stay PLAIN per the rubric (rule 1).
 * Noun-map: Assay=todo · Study=project · Station=panel/instrument · Database/Biorepository=data layer.
 */
const fs = require('fs');
const path = require('path');
const file = path.join(__dirname, 'biomedical.json');
const bio = JSON.parse(fs.readFileSync(file, 'utf8'));
const std = JSON.parse(fs.readFileSync(path.join(__dirname, 'standard.json'), 'utf8'));

// dotted-path -> biomedical value
const MAP = {
  'desktop.viewOnGitHub': 'Open on GitHub',
  'createProject.demoMode.label': 'OBSERVATION MODE',
  'createProject.fields.description.placeholder': 'Describe your research objectives and methodology...',
  // createProject.validation.* — kept plain (rule 1)
  'tabs.swarmdesk': '3D Lab View',
  'tabs.chat': 'Lab Console',
  'tabs.sessions': 'Study Sessions',
  'common.perPage': 'per batch',
  'common.copyId': 'Copy Sample ID',
  'common.copy': 'Replicate',
  'common.back': 'Previous Step',
  'common.next': 'Next Step',
  'common.previous': 'Previous Step',
  'common.sort': 'Sort Results',
  'common.clear': 'Clear Fields',
  'common.apply': 'Apply Protocol',
  'demo.label': 'OBSERVATION - Read Only',
  'menu.documentation': 'Protocols',
  'projectNavigator.enterButton.helpText': 'Enter or #{{number}} to register',
  'projectNavigator.viewInSwarmDesk': 'Open in SwarmDesk',
  'projectTab.projectTypes.web': 'Web Application',
  'projectTab.projectTypes.mobile': 'Mobile App',
  'projectTab.projectTypes.desktop': 'Desktop Application',
  'projectTab.projectTypes.api': 'API/Service',
  'projectTab.buttons.demoMode': 'Observation Mode',
  'projectTab.actions.openSwarmDesk': 'Open SwarmDesk',
  'todoTab.project.default': 'General Lab Work',
  'todoList.filters.pending': 'Pending',
  'todoList.sort.newest': 'Newest',
  'todoList.sort.oldest': 'Oldest',
  'todoList.sort.priority': 'Priority',
  'todoList.sort.madness': 'Randomized',
  'todoList.project.clearAll': 'Clear all',
  'todoList.pagination.perPage': 'per batch',
  'todoList.results.matching': ' matching "{{searchText}}"',
  'todoList.buttons.copyId': 'Copy Sample ID',
  'todoList.buttons.clone': 'Replicate',
  'todoList.menu.copyId': 'Copy Sample ID',
  'todoList.dialog.exportFilename': 'Output Filename',
  'todoList.dialog.exportFilenameHelp': 'Export file name (extension added automatically)',
  'todoList.dialog.exportFormat': 'Output Format',
  'todoList.dialog.formatJSON': 'JSON — Structured Data',
  'todoList.dialog.formatCSV': 'CSV — Spreadsheet',
  'todoList.dialog.formatCSVDesc': 'Spreadsheet format — compatible with Excel and Google Sheets',
  'todoList.dialog.formatMarkdown': 'Markdown — Documentation',
  'todoList.dialog.formatMarkdownDesc': 'Human-readable format for documentation',
  'todoList.dialog.formatHTML': 'HTML — Web Page',
  'todoList.dialog.formatHTMLDesc': 'Styled web page for browser viewing',
  'todoList.dialog.formatJira': 'Jira/Slack Output',
  'todoList.dialog.formatJiraDesc': 'Ready-to-paste Slack commands for Jira tickets',
  'todoList.dialog.selectFields': 'Select Columns',
  'todoList.dialog.customizeFields': 'Customize Column Names',
  'todoList.dialog.fieldName': 'Field',
  'todoList.dialog.advancedFilters': 'Screening Filters',
  'todoList.status.pending': 'Pending',
  'todoList.status.initial': 'Initializing',
  'todoList.fields.source': 'Origin',
  'todoList.fields.notes': 'Annotations',
  'todoList.fields.ticket': 'Ticket ID',
  'todoList.fields.duration_sec': 'Duration (s)',
  // todoList.validation.* — kept plain
  'todoList.error.unknownError': 'Unknown error',
  'todoList.actions.reopen': 'Reactivate',
  'todoList.actions.prioritize': 'Escalate Priority',
  'todoList.actions.unarchive': 'Restore from Archive',
  'todoList.dueDate.none': 'No due date',
  'todoList.dueDate.set': 'Set Due Date',
  'todoList.dueDate.overdue': 'Overdue',
  'todoList.notes.add': 'Add Annotation',
  'todoList.notes.none': 'No annotations on record',
  'todoList.deselectAll': 'Clear Selection',
  'todoList.dropHere': 'Drop to insert',
  'todoList.hideDetails': 'Collapse Details',
  'todoEdit.fields.notes': 'Annotations',
  'settings.tabs.aiConfiguration': 'Analysis Config',
  'settings.tabs.advanced': 'Advanced',
  'settings.tabs.messaging': 'Role Config',
  'settings.tabs.umlData': 'Code Map Archive',
  'settings.tabs.keyboardShortcuts': 'Hotkeys',
  'settings.tabs.notifications': 'Alert Channels',
  'settings.tabs.general': 'General',
  'settings.swarmdesk.movementTitle': 'Camera Movement Parameters',
  'settings.swarmdesk.movementDescription': 'Configure camera traversal rates for Orbital and FPS modes in the SwarmDesk 3D environment.',
  'settings.swarmdesk.resetDefaults': 'Reset to Baseline',
  'settings.swarmdesk.orbitalDescription': 'Camera traversal config for orbital (free-fly) navigation mode.',
  'settings.swarmdesk.orbitalBaseSpeed': 'Base Rate',
  'settings.swarmdesk.fpsDescription': 'Camera traversal config for first-person navigation mode.',
  'settings.swarmdesk.fpsBaseSpeed': 'Walk Rate',
  'settings.swarmdesk.fpsSprintSpeed': 'Sprint Rate (Ctrl held)',
  'settings.messaging.roleIdDisabled': 'Role ID is locked',
  'settings.messaging.npcConfig': 'SwarmDesk NPC Config',
  'settings.messaging.npcEnabled': 'Register as SwarmDesk NPC',
  'settings.messaging.npcCount': 'Instance Count',
  'settings.messaging.npcCountHelper': 'Number of instances of this role to register in SwarmDesk (0-5).',
  'settings.messaging.npcRole': 'NPC Role Label',
  'settings.messaging.npcRoleHelper': 'Shown above the NPC in SwarmDesk. Leave blank to inherit the display label.',
  'settings.messaging.npcPersonalityHelper': 'Sets the default behavior profile and fallback dialogue for this NPC.',
  'settings.ai.failed': 'Endpoint unreachable',
  'settings.ai.connected': 'Endpoint verified',
  'settings.language.description': 'Console interface language',
  'settings.notifications.description': 'Enable alert routing',
  'auth.buttons.googleLogin': 'Authenticate via Google',
  // auth.errors.* — kept plain
  'editableTodoCard.labels.duration': 'Duration (elapsed)',
  'editableTodoCard.status.pending': 'Pending',
  'editableTodoCard.actions.share': 'Share Record',
  'editableTodoCard.actions.clone': 'Replicate',
  'editableTodoCard.fields.notes': 'Annotations',
  'editableTodoCard.viewMode': 'Read Mode',
  'mindMap.controls.fullscreen': 'Fullscreen',
  'mindMap.controls.center': 'Recenter',
  'mindMap.controls.exitFullscreen': 'Exit Fullscreen',
  'mindMap.info.nodeCount': '{{count}} nodes mapped',
  'mindMap.instructions.dragToMove': 'Drag to Reposition',
  'mindMap.instructions.dragging': 'Repositioning…',
  'mindMap.instructions.doubleTapBurst': 'Double-tap to burst',
  'mindMap.instructions.doubleTapPhysics': 'Double-tap for physics',
  'mindMap.filter.clearAll': 'Deselect All',
  'mindMap.tooltips.disableStaticMode': 'Deactivate Static Mode',
  'mindMap.tooltips.enableStaticMode': 'Activate Static Mode',
  'mindMap.sequence.stopAnimation': 'Halt Animation',
  'mindMap.nodeInfo.type': 'Node Type',
  'mindMap.nodeInfo.energy': 'Load',
  'mindMap.layout.radial': 'Radial',
  'mindMap.layout.force': 'Force-Directed',
  'mindMap.layout.grid': 'Grid',
  'mindMap.deleteNode': 'Archive Node',
  // chat errors stay plain in body but voiced labels:
  'chatAssistant.errors.noResponse': 'Query received but no analysis returned. Please retry.',
  'chatAssistant.status.typing': 'Analysis in progress',
  'chatAssistant.notConfigured.title': 'Analysis System Offline',
  'chatAssistant.notConfigured.configureButton': 'Configure Analysis',
  'chatAssistant.title': '🔬 Lab Console',
  'chatAssistant.actions.delete': 'Purge',
  'mobileChatInterface.quickActions.help': 'Query Help',
  'mobileChatInterface.header.statusOnline': 'Nominal',
  'mobileChatInterface.placeholder': 'Query the analysis system…',
  'swarmDesk.ui.navigation.movement': '⌨️ WASD: Traverse | Mouse: Orient',
  'swarmDesk.ui.navigation.interaction': '🖱️ Click: Interact | E: Execute | Space: Quick Action',
  'swarmDesk.panels.shortcuts.categories.actions.title': '⚡ Operations',
  'swarmDesk.panels.mcp.title': '🔗 MCP Integration Hub',
  'swarmDesk.panels.mcp.subtitle': 'Service Integration Layer',
  'swarmDesk.panels.mcp.description': 'The Model Context Protocol (MCP) connects to external tools and services for enhanced automation and lab functionality.',
  'swarmDesk.panels.mcp.gettingStarted': 'Setup instructions:',
  'swarmDesk.panels.mcp.tools.connectedAs': 'Authenticated as: {{username}}',
  'swarmDesk.panels.mcp.debug.authentication': 'Auth: {{status}}',
  'swarmDesk.panels.mqtt.logs.lastMessage': 'Last event: {{time}}',
  'swarmDesk.projectData.projectReadmes.omnispindle.title': '🔗 Omnispindle — Integration Platform',
  'swarmDesk.projectData.projectReadmes.omnispindle.description': 'Communication and coordination platform connecting tools and services for streamlined workflow.',
  'swarmDesk.errors.loadingError': '⚠️ Query Error',
  'swarmDesk.errors.unknownError': '❓ Unknown Error',
  'swarmDesk.actions.connect': '🔗 Register Service',
  'swarmDesk.controls.exitFullscreen': 'Exit Fullscreen',
  'swarmDesk.controls.rotate': 'Orient',
  'swarmDesk.controls.fullscreen': 'Fullscreen',
  'swarmDesk.controls.move': 'Traverse',
  'swarmDesk.tour.navigation': 'WASD to traverse, mouse to orient',
  'swarmDesk.agentPanel.status.active': 'Operational',
  'swarmDesk.agentPanel.empty': 'No agents registered.',
  'swarmDesk.hotkeys.mouse': 'Mouse: Orient',
  'swarmDesk.hotkeys.tab': 'TAB: Switch Station',
  'swarmDesk.hotkeys.wasd': 'WASD: Traverse',
  'swarmDesk.filters.pending': 'Pending',
  'spells.errors.aiError': 'Analysis system error',
  'spells.errors.networkError': 'Network error',
  'spells.history.duration': 'Runtime:',
  'spells.title': '🔬 Analysis Tools',
  'umlData.errors.uploadFailed': 'Failed to upload map file',
  'umlData.instructions.title': 'How to use:',
  'umlData.instructions.step1': 'Install the map generator: npm install -g @madnessengineering/cartogomancy',
  'umlData.instructions.step2': 'Generate map from codebase: cartogomancy /path/to/project -o project-uml.json',
  'umlData.storage.info': '{{count}} visualization(s) on record. Storage limit: {{limit}}',
  'umlData.actions.view': 'Open in SwarmDesk',
  'umlData.empty.title': 'No code maps on record',
  'warRoom.backgroundImage.uploads': 'Your Field Maps',
  'chronomancy.today': 'Today',
  'chronomancy.yesterday': 'Yesterday',
  'chronomancy.daysAgo': '{{days}}d ago',
  'automationRecipes.priority': 'Urgency',
  'lessonsViewer.references.noMatches': 'No matches',
};

function getStd(p) {
  return p.split('.').reduce((o, k) => (o == null ? o : o[k]), std);
}
function setPath(obj, p, val) {
  const ks = p.split('.');
  let o = obj;
  for (let i = 0; i < ks.length - 1; i++) {
    if (o[ks[i]] == null || typeof o[ks[i]] !== 'object') return false;
    o = o[ks[i]];
  }
  o[ks[ks.length - 1]] = val;
  return true;
}
function getPath(obj, p) {
  return p.split('.').reduce((o, k) => (o == null ? o : o[k]), obj);
}

let applied = 0, skippedNotIdentical = 0, missing = 0, noChange = 0;
for (const [p, val] of Object.entries(MAP)) {
  const cur = getPath(bio, p);
  if (cur === undefined) { missing++; console.warn('MISSING key:', p); continue; }
  const sv = getStd(p);
  if (cur !== sv) { skippedNotIdentical++; console.warn('SKIP (already voiced, not == standard):', p, '=>', JSON.stringify(cur)); continue; }
  if (val === sv) { noChange++; continue; } // intentional keep-as-standard (neutral best)
  setPath(bio, p, val);
  applied++;
}

fs.writeFileSync(file, JSON.stringify(bio, null, 2) + '\n');
console.log(`\nApplied: ${applied}  KeptNeutral: ${noChange}  SkippedAlreadyVoiced: ${skippedNotIdentical}  Missing: ${missing}`);
