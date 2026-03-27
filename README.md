# MadnessThemes

Theme and color palette collection for [Inventorium](https://github.com/MadnessEngineering) — the dashboard, todo system, and 3D workspace by Madness Interactive.

## What's In Here

Each theme has up to two files:

- **`<theme>-colors.json`** — Full color palette: backgrounds, text, borders, status badges, dashboard stats, tags, effects, shadows, overlays, and Three.js material settings.
- **`<theme>.json`** — Translation/personality strings: UI labels, button text, messages, all written in the theme's voice.

### Current Themes

| Theme | Icon | Style | Type |
|-------|------|-------|------|
| **Standard** | 📝 | Cyan & orange, dark background | Dark |
| **Mad Laboratory** | 🧪 | Purple & toxic green, mad scientist | Dark |
| **Corporate Clean** | 💼 | Professional blue & gray | Dark |
| **Corporate Drone** | 💼 | Business jargon personality | Strings only |
| **Gunmetal Arsenal** | 🔫 | Industrial steel & polished metal | Dark |
| **Debug Mode** | 🐛 | Hot pink & lime, high contrast | Dark |
| **Cyan Laboratory** | 🧪 | Soft cyan accents, muted surfaces | Light |
| **LabOps** | 🔬 | Teal-blue, scientific precision | Light |
| **Templar Light** | ⚔️ | Gold & red, knights templar | Light |
| **Banana** | 🍌 | Banana themed | Strings only |
| **Biomedical** | 🧬 | Biomedical research themed | Strings only |
| **Dwarf** | ⛏️ | Mining, lava, and magma | Strings only |
| **Mad Wizard** | 🧙‍♂️ | Mystical laboratory terminology | Strings only |

## Preview

Open **`palette-preview.html`** in your browser to see all themes side-by-side with:

- **Gallery** — Every theme at a glance with palette strips and status badges
- **Swatches** — Full color path comparison between any two themes
- **UI Preview** — Mock dashboard rendered in each theme's colors
- **Diff** — Before/after grid highlighting every changed color value

## Contributing

We'd love contributions! Whether it's a whole new theme, a color tweak, or a fun personality translation — all are welcome.

### Adding a New Color Theme

1. Copy an existing `*-colors.json` as your starting point (pick one close to your vision — light or dark)
2. Update the metadata at the top:
   ```json
   {
     "themeName": "your-theme-name",
     "displayName": "Your Theme Name",
     "description": "Short description of the vibe",
     "icon": "🎨",
     "version": "1.0.0",
     "colors": { ... }
   }
   ```
3. Fill in all color sections — the structure must match exactly so the app can consume it:
   - `primary`, `secondary`, `success`, `warning`, `error`
   - `background` (main, card, header, paper, topBar)
   - `text` (primary, secondary, tertiary, muted, status colors)
   - `border`, `dashboard`, `accent`, `state`, `effects`, `tags`, `shadows`, `overlays`, `status`
   - `threeJS` (colors, materials, lighting — for the 3D workspace)
4. Open `palette-preview.html` to visually verify your theme looks right

### Adding a Personality Translation

1. Copy `standard.json` as your base
2. Rewrite every string in your theme's voice/personality
3. Keep all the same keys — just change the values

### Guidelines

- Keep the JSON structure identical across all color themes — missing keys will cause fallback to standard
- For dark themes: ensure text has enough contrast against dark backgrounds
- For light themes: watch out for washed-out status badges and tags
- Have fun with personality translations — the weirder the better
- Test with `palette-preview.html` before submitting

### Submitting

1. Fork this repo
2. Create a branch (`git checkout -b my-awesome-theme`)
3. Add your theme file(s)
4. Open a Pull Request with a screenshot or description of your theme

---

Built with varying degrees of madness by [Madness Interactive](https://madnessinteractive.cc)
