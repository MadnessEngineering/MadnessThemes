# VOICE_GUIDE.md — Theme Copy Authoring Rubric

This is "the helps": the theme-agnostic guide for writing personality translation files
(`src/locales/themes/*.json`). Every theme shares the same ~1918 keys (`debug.json` is the master
checklist — each value there equals its own dotted key path). What differs between themes is
**voice**, and without a rubric every pass drifts. This document fixes that.

Two parts:
- **Part A — Global principles.** Apply to every theme, every string.
- **Part B — Voice cards.** Per-theme persona + lexicon. mad-wizard is fully written as the
  gold-standard exemplar; the other 11 are one-line stubs to fill in their own sessions.

---

## Part A — Global humane-copy principles

Apply these to every theme. They are about *quality and consistency*, not a specific voice.

1. **Clarity-vs-flavor tiers.** Flavor belongs on labels, buttons, titles, empty states, and
   welcome/onboarding copy. Keep it **off** validation messages, error bodies, and
   destructive-action confirmations — those stay plain and unambiguous. A user about to delete
   data, or staring at a failed save, must not have to decode lore. (So mad-wizard's `validation.*`
   staying neutral is *correct*, not lazy.)

2. **Preserve interpolation placeholders exactly.** Both styles exist in these files:
   double-brace `{{name}}`, `{{count}}` and single-brace `{min}`, `{max}`. Never rename, translate,
   pluralize, or reorder them such that the host sentence breaks. The flavor goes *around* the
   placeholder, never *inside* it.

3. **Buttons stay scannable.** Action-verb first, **≤3 words**. "Channel Changes" ✅. A flavor
   sentence on a button ❌. If a button needs a clause to make sense, the flavor is too heavy.

4. **One concept = one entry in the lexicon.** Build a small in-voice verb/noun map per theme
   (save / cancel / delete / loading / create / search / refresh / export → fixed terms) and reuse
   it everywhere. Don't let "save" drift between inscribe / archive / store across the file. See the
   note on **noun-maps** below — the subtle drift is usually the object noun, not the verb.

5. **Meaning first.** A newcomer must be able to guess what a control does *without* knowing the
   theme's lore. If they can't, dial the flavor back. Flavor is seasoning, not a puzzle.

6. **Match the medium.** Titles can be playful; tooltips explain plainly; status text is
   glanceable; long descriptions may breathe but must stay useful. The same concept earns different
   flavor budgets in different slots.

7. **Emoji discipline.** One consistent icon per category within a theme — don't swap the todo icon
   between 📝 / 📋 / 🔬. Match the theme's top-level `icon` metadata family. When in doubt, fewer.

8. **Case consistency.** Title Case for buttons and labels, sentence case for body copy. Pick the
   convention per theme and hold it across the whole file.

9. **Identical-to-`standard.json` = unfinished worklist**, *not* "neutral by choice" — unless the
   neutral word genuinely is best (e.g. "Email", "OK", "URL"). Treat every match against
   `standard.json` as a string still owed a voice pass. Regenerate the worklist:

   ```bash
   cd src/locales/themes && node -e "const m=require('./THEME.json'),s=require('./standard.json');function f(o,p=''){let r={};for(const k in o){const v=o[k];const key=p?p+'.'+k:k;if(v&&typeof v==='object'&&!Array.isArray(v))Object.assign(r,f(v,key));else r[key]=v;}return r;}const fm=f(m),fs=f(s);for(const k in fm){if(typeof fm[k]==='string'&&fm[k]===fs[k]&&fm[k].length>2)console.log(k+' = '+JSON.stringify(fm[k]));}"
   ```

10. **Read-aloud test.** Read the string out loud. Does it sound like a person *in this world* wrote
    it, or like a model filling a slot? If the latter, rewrite it.

### On lexicons: pin the noun-map, not just the verb

When a theme already has flavor, the drift is usually subtle: the **verb** is consistent but the
**object noun** wanders. mad-wizard, for example, is consistent on *Abandon / Modify / Refresh /
Seal* — but the object swings between **Apparatus**, **Experiment**, **Timeline**, and **Portal**.
That's the harder, more valuable thing to fix. Decide, per theme:

- Which noun names a **tool / form / panel** (the machinery you operate)?
- Which noun names a **work item** (the thing being tracked — a todo)?
- Which noun names a **sequence / queue** (ordered work)?
- Which noun names a **navigation / connection** (moving between views)?

Then map every action onto the right noun. A lexicon that pins both halves — verb *and* object —
is what keeps a 1918-key file from reading like four different authors.

---

## Part B — Per-theme voice cards

### Card template

Copy this block to start a new theme card:

```
### <theme-name>  <icon>

- **Persona** — one line: who is speaking.
- **Setting** — the world they speak from.
- **Lexicon** — fixed in-voice terms:
  - save / cancel / delete / loading / create / search / refresh / export → …
  - noun-map: tool=… · work-item=… · sequence=… · navigation=…
- **Tone dial** — how heavy is the flavor, and where to restrain it.
- **Do / Don't** — two or three of each.
- **Sample transforms** — 3–5 lines, standard → theme.
```

---

### mad-wizard  🧙‍♂️  *(gold-standard exemplar — fully written)*

- **Persona** — a slightly unhinged arcane researcher running experiments in a void-powered
  laboratory. Speaks with the confidence of someone who has definitely caused at least one
  containment breach and considers it a learning opportunity.
- **Setting** — an alchemical lab where todos are *experiments*, the apparatus is the UI, and the
  void is the data layer that swallows and returns things.

- **Lexicon** — pinned canonical terms. Where the file currently drifts, the **Keep** column wins;
  the **Drop** column lists the variants to retire in the rewrite phases.

  | Concept | Keep (canonical) | Drop / retire | Notes |
  |---|---|---|---|
  | save | **Archive Findings** | — | results are *findings* |
  | save (in-progress) | **Channel Changes** | — | active mid-edit save |
  | cancel / discard | **Abandon Experiment** | "Abandon Timeline" | one verb, one object |
  | delete | **Banish to Void** | — | the void is the disposal layer |
  | loading | **Void Tunneling…** | — | reuse verbatim everywhere |
  | edit | **Modify Apparatus** (tools/forms) · **Modify Experiment** (a todo) | — | split by object, see noun-map |
  | refresh | **Refresh Apparatus** | "Refresh Portal" | portals are for navigation, not reload |
  | export | **Extract Research Data** | bare "Export" | |
  | complete (a todo) | **Seal Experiment** | "" (was empty) | Seal = secure/finalize, see note |
  | close (a panel) | **Seal Apparatus** | — | Seal = secure/put away, see note |
  | review | **Peer Review** | — | |
  | AI insights | **Divination** | — | reserve "divination" for AI/prediction only |
  | open externally | **Summon Warp Portal** | — | portals = navigation/connection |

  **Noun-map (the important part):**
  - **Apparatus** = a tool, form, panel, or piece of UI machinery you operate.
  - **Experiment** = a work item (a todo) — the thing being tracked and completed.
  - **Timeline / Findings** = research output and history; *findings* are saved results,
    *timeline* is sequence/history. Do **not** use "timeline" as a generic cancel object.
  - **Void** = the data/storage layer — things are banished to it (delete) and tunnel through it
    (loading).
  - **Portal / Warp** = navigation and external connections only — never "reload."
  - **Divination / Alchemy** = AI and prediction features only — don't let alchemy leak onto plain
    save/create actions.

- **Tone dial** — heavy on titles, buttons, empty states, and onboarding; medium on tooltips
  (flavor + a plain clause); **off** on `validation.*`, error bodies, and destructive confirms.
  The wizard is theatrical, never obstructive.

- **Do / Don't**
  - **Do** keep one verb per concept and split only by object noun (Modify Apparatus vs Modify
    Experiment).
  - **Do** reuse "Void Tunneling…" for every loading state — repetition reads as a consistent world.
  - **Don't** mix the four metaphor families on one action (apparatus / void / alchemy / divination
    each own their domain).
  - **Don't** put lore on a validation message — "Email is required" stays "Email is required."

- **Sample transforms** (standard → mad-wizard)
  - `Save` → **Archive Findings**
  - `Cancel` → **Abandon Experiment**
  - `Delete` → **Banish to Void**
  - `Loading…` → **Void Tunneling…**
  - `No todos yet` → *something like* **The apparatus sits idle — no experiments logged.**

- **Seal collision — resolved (Phase 2):** `common.close = "Seal Apparatus"` and
  `todoList.buttons.complete = "Seal Experiment"` both use **Seal**. Rather than split the verb, we
  embraced it: **Seal = "secure and put away"** consistently — you seal a finished experiment
  (complete) the same way you seal the apparatus (close a panel). The distinct object nouns keep
  them unambiguous. The completed *status* is likewise **"Sealed"**, reinforcing the metaphor.

---

### labops  🔬  *(written)*

- **Persona** — an on-call SRE running the lab like a production system. Calm, procedural,
  instrumentation-minded. Talks in runbooks, telemetry, and tickets; treats every action as an
  operation against live infrastructure. Never panics — escalates.
- **Setting** — an ops control room wired into the lab. Todos are *tickets* on the board, the UI is
  the *console*, work flows through a *queue*, and the data layer is the *datastore / telemetry
  pipeline*.

- **Lexicon** — pinned canonical terms. **Keep** wins where the file drifts.

  | Concept | Keep (canonical) | Notes |
  |---|---|---|
  | save | **Commit** | commit the change to the record |
  | save (in-progress) | **Applying…** | active mid-edit write |
  | cancel / discard | **Discard** · **Roll Back** (revert) | Discard for unsaved, Roll Back to revert applied state |
  | delete | **Decommission** | retire a resource for good |
  | loading | **Querying…** | reuse verbatim for every fetch/loading state |
  | create | **Provision** | stand up a new ticket/resource |
  | edit | **Reconfigure Console** (tools/panels) · **Edit Ticket** (a todo) | split by object |
  | refresh | **Resync** | re-pull current state |
  | search | **Query** | query the system; avoid jargon "grep" on scannable buttons |
  | export | **Export Snapshot** | point-in-time dump |
  | complete (a todo) | **Resolve** | resolve the ticket; completed status = **Resolved** |
  | close (a panel) | **Dismiss** | clear the console view |
  | review | **Triage** | the review queue is the triage queue |
  | AI insights | **Run Diagnostics** | analysis/prediction only |
  | open externally | **Open Console** | jump to an external endpoint |

  **Noun-map:**
  - **Console** = a tool, panel, or form you operate.
  - **Ticket** = a work item (a todo) — opened, triaged, resolved.
  - **Queue** = ordered/pending work (the run queue, the board).
  - **Route** = navigation between views; **Endpoint** = an external connection.
  - **Datastore / Telemetry** = the data + metrics layer — query it, sync from it.

- **Tone dial** — *low-medium.* Ops voice is understated by nature: precise, not theatrical. Flavor
  on labels, empty states, onboarding; plain on `validation.*`, error bodies, destructive confirms
  (ops culture already prizes blunt errors — lean into that). Sentence case for body, Title Case for
  buttons.

- **Do / Don't**
  - **Do** keep "Querying…" as the single loading term everywhere.
  - **Do** treat a todo as a **ticket** consistently — open / triage / resolve.
  - **Don't** over-jargon scannable controls ("Grep", "SIGKILL" on a delete button) — meaning first.
  - **Don't** flavor a validation message — "Email is required" stays as-is.

- **Sample transforms** (standard → labops)
  - `Save` → **Commit**
  - `Cancel` → **Discard**
  - `Delete` → **Decommission**
  - `Loading…` → **Querying…**
  - `No todos yet` → **Board is clear — no open tickets.**

---

### templar-light  ⚔️  *(written)*

- **Persona** — a scribe-knight of a sacred order, keeper of the archive. Formal, reverent,
  ceremonious — but never obscure. Speaks of duty, oaths, and the record. Dignified, not stiff.
- **Setting** — a sunlit chapter house and sacred archive. Todos are *charges* (sworn duties), the
  UI panels are *chambers*, a form is a *record*, work is mustered on a *roster*, and the data layer
  is *the Archive / the Vault*.

- **Lexicon** — pinned canonical terms. **Keep** wins where the file drifts.

  | Concept | Keep (canonical) | Notes |
  |---|---|---|
  | save | **Inscribe** | inscribe into the record |
  | save (in-progress) | **Inscribing…** | active mid-edit write |
  | cancel / discard | **Withdraw** · **Recant** (undo applied) | Withdraw the unsaved, Recant a vow already made |
  | delete | **Expunge** | strike from the Archive |
  | loading | **Consulting the Archive…** | reuse verbatim for every loading state |
  | create | **Pledge** | pledge a new charge |
  | edit | **Amend Record** (tools/forms) · **Amend Charge** (a todo) | split by object |
  | refresh | **Renew** | renew from the Archive |
  | search | **Seek** | seek the records |
  | export | **Transcribe Records** | scribe a copy to carry out |
  | complete (a todo) | **Fulfill** | fulfill the charge; completed status = **Fulfilled** |
  | close (a panel) | **Seal** | seal the chamber |
  | review | **Examine** | the review queue is examination |
  | AI insights | **Seek Counsel** | augury/divination only |
  | open externally | **Open Passage** | a passage to another hall |

  **Noun-map:**
  - **Chamber** = a panel or view you enter; **Record** = a form/document you amend.
  - **Charge** = a work item (a todo) — pledged, examined, fulfilled.
  - **Roster** = ordered/pending work (the muster of charges).
  - **Passage / Hall** = navigation and external connections.
  - **Archive / Vault** = the data layer — inscribed to, expunged from, consulted.

- **Tone dial** — *medium-high* on titles, empty states, onboarding; *medium* on tooltips (reverent
  phrasing + a plain clause); **off** on `validation.*`, error bodies, destructive confirms — a
  failed save or a delete warning stays plain and clear. Title Case for buttons/labels, sentence case
  for body. Reverent, never riddling.

- **Do / Don't**
  - **Do** hold one verb per concept, split only by object (Amend Record vs Amend Charge).
  - **Do** reuse "Consulting the Archive…" for every loading state.
  - **Don't** let ceremony obscure meaning — a newcomer must still guess the control.
  - **Don't** put liturgy on a validation message or a destructive confirm.

- **Sample transforms** (standard → templar-light)
  - `Save` → **Inscribe**
  - `Cancel` → **Withdraw**
  - `Delete` → **Expunge**
  - `Loading…` → **Consulting the Archive…**
  - `No todos yet` → **The roster stands empty — no charges pledged.**

---

### Stubs — fill in their own sessions

Do **not** fabricate voices not yet designed. One line each; promote to a full card when that
theme's rewrite phase runs.

- **banana** 🍌 — playful fruit/snack voice; cheerful, light.
- **biomedical** 🧬 — clinical lab / medical-research register; precise, sterile.
- **corporate-clean** 🏢 — minimal, neutral-professional; flavor near zero by design.
- **corporate-drone** 📊 — satirical corporate jargon; synergy/leverage/circle-back.
- **cyan-lab** 🧪 — bright neon lab tech; energetic, modern.
- **debug** 🐞 — *not a voice*: every value is its own dotted key path (master key checklist). Leave as-is.
- **dwarf** ⛏️ — Dwarf-Fortress-flavored mining/crafting; gruff, sturdy.
- **gunmetal** 🔩 — terse industrial/military; clipped, functional.
- **standard** — the neutral baseline. By definition no flavor; the worklist source for every other theme.

*(labops 🔬 and templar-light ⚔️ are now full cards above.)*

---

## Workflow reminders

- Themes live in a **git submodule** (`src/locales/themes/`, branch `dev`). Commit **inside** the
  submodule first, push, then `git add --force src/locales/themes` in the parent repo — the parent
  hides pointer drift via `ignore=all`.
- Verify parity with `node scripts/check-themes.js` (run from repo root) before and after a pass.
- Use the **theme-keeper agent** for bulk propagation across many theme files; author editorial
  voice work (like this guide and the mad-wizard pilot) by hand.
