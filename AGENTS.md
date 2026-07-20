# Repository Guidelines

A multi-platform theme collection porting the Tokyonight + GitHub palette family across three editor surfaces:

1. **Obsidian** — `Telcat` theme (CSS + Style Settings).
2. **VSCode (Markdown Preview Enhanced)** — `Tokyonight Storm` port (LESS).
3. **Cherry Studio** — `Tokyonight` port with dark/light auto-switch (CSS).

Three platforms share one design language (heading decorations, hr ✦-star, KaTeX hover lift, list drawer, link brackets) but each has its own file layout, host quirks, and constraints. There is **no JS/TS runtime, no test framework, no linter, no CI** — pure static assets driven by one Python build script.

---

## Architecture & Data Flow

```
obsidian/theme-origin.css  ─┐
                            │   python build_theme.py
                            │   (no I/O deps, stdlib only)
obsidian/build_theme.py  ───┤
                            ▼
              obsidian/theme.css   (Obsidian ships this)

VSCode/Tokyonight_storm/style.less   (manual; VSCode/Less compiles)
VSCode/Tokyonight_storm/config.js    (MPE katex/mathjax/mermaid config)
VSCode/Tokyonight_storm/parser.js    (MPE onWillParse/onDidParse hooks)
VSCode/Tokyonight_storm/head.html    (injected into preview <head>)

cherry_studio/Tokyonight.css         (manual; only editable Cherry Studio file)
cherry_studio/Claude.css             ┐
cherry_studio/Miku-more.css          │
cherry_studio/Modern_Workspace.css   ├─ read-only references (do NOT modify)
cherry_studio/(others).css           ┘
```

- `theme-origin.css` is the **single source of truth** for the Obsidian palette. The build script normalizes all four schemes to identical 37-key shape via `UNIFIED_KEYS` and re-emits them with consistent ordering.
- The VSCode and Cherry Studio files are **manual siblings** — they mirror the Obsidian source visually but have no automatic generation.
- All three platforms consume the same conceptual CSS variable set (`--bg-color`, `--text-color`, `--primary-color`, `--secondary-color`, `--accent-color`, `--glow-color`, `--link-color`, `--link-hover-color`, `--code-block-bg`, …).

---

## Key Directories

| Path | Purpose |
|---|---|
| `obsidian/` | Telcat Obsidian theme. **The authoritative source.** |
| `obsidian/theme-origin.css` | Source CSS with `@settings` YAML block + 4 scheme blocks. |
| `obsidian/theme.css` | Generated output. Byte-identical successor of `theme-origin.css` after `build_theme.py` runs. |
| `obsidian/build_theme.py` | Pure-stdlib Python builder. Defines `UNIFIED_KEYS` (37) and `SCHEMES` (4). |
| `obsidian/manifest.json` | Obsidian theme metadata (`name`, `version`, `minAppVersion`, `author`). |
| `obsidian/README.md` | User-facing readme (Chinese display text + emoji-friendly). |
| `VSCode/Tokyonight_storm/` | VSCode MPE port. `.less` not `.css`. |
| `VSCode/Tokyonight_storm/style.less` | Main file. Root selector `.markdown-preview.markdown-preview`. |
| `VSCode/Tokyonight_storm/config.js` | KaTeX/MathJax/Mermaid config passed to MPE. |
| `VSCode/Tokyonight_storm/parser.js` | MPE `onWillParseMarkdown` / `onDidParseMarkdown` no-op hooks. |
| `VSCode/Tokyonight_storm/head.html` | `<head>` injection (currently a DOMContentLoaded stub). |
| `cherry_studio/Tokyonight.css` | **The only editable Cherry Studio file.** `.markdown` / `.tiptap` selectors + `@media (prefers-color-scheme)`. |
| `cherry_studio/Claude.css`, `Miku-more.css`, `Modern_Workspace.css`, `universe.css`, `vscode.css`, `奶油国风Mac代码块.css`, `粉紫色.css`, `赛博飞升·霓虹毛玻璃满配版.css` | READ-ONLY references for cherry-picked patterns. **Do not edit.** |
| `markdown元素对照/MD元素设置对照.md` | Element-by-element behavior reference (callouts, lists, code, tables, math). |
| `markdown元素对照/test1.md`, `test2.md` | Visual fixtures (code blocks, tables) for inspecting the rendered output. |
| `AGENTS.md` (project root) | This file — agent guidance. |

---

## Development Commands

```bash
# Regenerate obsidian/theme.css from obsidian/theme-origin.css
python obsidian/build_theme.py

# Verify idempotency (output should be byte-identical to source after build)
diff -q obsidian/theme.css obsidian/theme-origin.css
```

No package install steps. No `npm`/`pnpm`/`pip install`. No Makefile, no shell scripts.

VSCode and Cherry Studio styles are edited by hand. There is no compile step for `style.less` outside of MPE itself, and no compile step for `Tokyonight.css` outside of Cherry Studio reloading it.

---

## Code Conventions & Common Patterns

### CSS variables — kebab-case, semantic

```
--bg-color            --text-color             --primary-color
--secondary-color     --accent-color           --glow-color
--link-color          --link-hover-color       --code-block-bg
--text-color-secondary   --border-color
```

All three themes share this conceptual set; Obsidian additionally carries `--h2-bg-gradient`, `--h2-shadow-*`, `--text-bold`, `--code-block-header-bg`, etc. (see `obsidian/build_theme.py` `UNIFIED_KEYS` for the full 37-key list).

### Scheme identifiers

| Light | Dark |
|---|---|
| `theme-light-tokyonight` | `theme-dark-tokyonight` |
| `theme-light-github` | `theme-dark-github` |

These class names are applied to the root and selected by the Style Settings `class-select` (see `obsidian/theme-origin.css` `@settings` block).

### Specificity & `!important`

- Doubled selectors (`.markdown-preview.markdown-preview`) are used to win against MPE's internal selectors.
- `!important` is used deliberately to defend against host-injected dynamic variables (Obsidian Live Preview / CodeMirror overrides `--font-monospace`, etc.), and to guarantee hover color behavior on H1–H6.
- **Forbidden pattern:** do NOT set `position: relative;` on `.markdown-preview.markdown-preview` — it breaks MPE's scroll-sync alignment.

### Obsidian font cascade — must target `-*-theme`, not the bare `--font-*`

Obsidian's built-in `app.css` declares a three-tier cascade on `body`:

```
--font-interface / --font-text / --font-monospace
  = var(--<name>-override), var(--<name>-theme), var(--<name>-default)
```

`--<name>-override` is written by Settings → Appearance when the user picks a font; `--<name>-theme` is the slot themes are expected to fill; `--<name>-default` is the system stack. Do NOT set the bare `--font-text` / `--font-interface` / `--font-monospace` on `:root` or `body` and expect it to win — `app.css` re-declares those names on `body` at equal specificity and overrides the theme value. The global-font block at the tail of `obsidian/theme-origin.css` (the `/* Font Setup */` section) therefore:

1. Sets `--font-text-theme` / `--font-interface-theme` / `--font-monospace-theme` (the slots Obsidian actually consumes).
2. Also pins `--<name>-override` so Settings → Appearance cannot silently revert the theme font.
3. Adds an element-selector `!important` layer on `body`, `.markdown-preview-view`, `.markdown-source-view.mod-cm6 .cm-scroller`, `.workspace-leaf-content`, and the app-chrome containers as belt-and-suspenders against plugin CSS that re-declares the cascade.
4. Code surfaces (`code, kbd, pre, .cm-inline-code, .HyperMD-codeblock, …`) keep the monospace stack and are forced via element selector `!important` — this is why code fonts worked even when the global font did not.

Cross-platform slices: this cascade is Obsidian-specific. `VSCode/Tokyonight_storm/style.less` and `cherry_studio/Tokyonight.css` set `font-family` directly on their host containers because neither host has the same three-tier variable cascade. When porting font changes, do not blindly copy the Obsidian `-*-theme` pattern into the other two files.

### `color-mix` handling

- Obsidian uses native CSS `color-mix(in srgb, …)`.
- VSCode MPE (.less) cannot rely on it, so all `color-mix()` calls have been pre-computed into `rgba()` values and hard-coded in `style.less`.
- Cherry Studio: handle per-target — when porting snippets from the reference files, prefer `rgba()` to avoid surprises.

### Comment language

- **English only** in all CSS/LESS/Python code comments. No emoji, no chatty tone.
- `@settings … .zh` and `description.zh` YAML fields are user-facing Chinese display text for the Style Settings plugin — **not** code comments. These are intentionally bilingual.
- Cherry Studio reference files (`Claude.css`, etc.) are allowed to have their own comment conventions; do not rewrite them.

### Shared design patterns (must stay consistent across all three platforms)

- H1–H6 hover: color shift to primary + `transform: translateX(4px)`.
- Heading decoration icons: dot-matrix SVG (`--h3-icon-shape`, …) — see `VSCode/Tokyonight_storm/style.less` for the data-URI pattern.
- Horizontal rule (`:root` and host `<hr>`): star-dashed style with center `✦` glyph (from `cherry_studio/Claude.css`), hover rotates 180° + 1.3× scale.
- KaTeX math hover lift (`:root` host): `display: block !important; position: relative !important; translateY(-4px) scale(1.02)`. Inline uses `scale(1.05)` + glow. Forced display/position fixes the inline-vs-block layout drift.
- List drawer: `translateX(6px)` on item hover, plus `:has(> li:hover) > li:not(:hover)` to dim siblings to `opacity: 0.6`. Reading-mode-only; suppress in Live Preview.
- Editor/Live Preview reaction: drop physical transforms (no `translateX`/`scale`), keep only color shifts for H1–H6 and links. Code inline gets a `* { color: #fff }` override to defeat CodeMirror span partitioning.

### Naming — do not create a second convention

- File names: lowercase with hyphens (`theme-origin.css`) or underscores for VSCode subfolder (`Tokyonight_storm`). Don't introduce camelCase or spaces.
- CSS classes derived from Style Settings: `theme-light-*`, `theme-dark-*`, `layout-*` (e.g. `layout-default`, `layout-cards`).
- Folder for VSCode MPE ports: capital-T `Tokyonight_storm/` (matches the manifest label).

### Forbidden patterns (cherry_studio/)

- `Cherry.css`, `Claude.css`, `Miku-more.css`, `Modern_Workspace.css`, `universe.css`, `vscode.css`, `奶油国风Mac代码块.css`, `粉紫色.css`, `赛博飞升·霓虹毛玻璃满配版.css` are **READ-ONLY.** Reference them for inspiration only.

---

## Important Files

- `obsidian/build_theme.py` — single source of build automation. Modifying the `UNIFIED_KEYS` list reshapes the output schema; modifying `SCHEMES` retunes one of the four palettes.
- `obsidian/theme-origin.css` — the canonical CSS. First ~120 lines are the `@settings` YAML (do not break YAML syntax — Style Settings reads this directly).
- `obsidian/manifest.json` — must keep fields: `name`, `version`, `minAppVersion`, `author`. Do not add `authorUrl` / `fundingUrl` unless explicitly requested.
- `obsidian/README.md` — user-facing. One line per feature. No verbose descriptions. No bold-wrapped link text (e.g. links should be `[Link](url)` not `[**Link**](url)`).
- `cherry_studio/Tokyonight.css` — the only Cherry Studio file you may edit. Top of the file holds `--dark-*` and `--light-*` variables underneath `@media (prefers-color-scheme: dark)` / `:not(...)`. Editing this requires understanding how the file switches palettes automatically.
- `markdown元素对照/MD元素设置对照.md` — declarative reference for which elements get which treatments. Cross-check before adding new effects.

---

## Runtime / Tooling Preferences

- **Language:** Python 3.x stdlib only. No third-party deps.
- **No package manager.** No `package.json`, no `requirements.txt`, no `pyproject.toml`, no `bun.lockb`.
- **Build command:** `python obsidian/build_theme.py`.
- **Editor formatting:** preserve source ordering — do NOT run `prettier` / `csscomb` on `theme-origin.css`; the build script intentionally emits variables in `UNIFIED_KEYS` order regardless of dict insertion order.
- **VSCode MPE root container:** `.markdown-preview.markdown-preview` — never add `position: relative;` here (MPE scroll-sync bug).
- **Obsidian Live Preview:** the trailing "编辑模式 (Live Preview)" block in `theme-origin.css` deliberately strips physical transforms for editor fluidity — preserve it when touching the file.
- **Cherry Studio reference files:** read-only. Cherry-pick patterns, do not import wholesale.

---

## Testing & QA

**There is no automated test framework.** Verification is manual + visual + idempotency:

1. **Build idempotency** — after `python obsidian/build_theme.py`, compare:
   ```bash
   diff -q obsidian/theme.css obsidian/theme-origin.css
   ```
   The build is expected to regenerate `theme.css` byte-identical to the source (the source already emits the normalized form; `theme.css` is the canonical published artifact).

2. **Visual fixtures** — open `markdown元素对照/test1.md` (code blocks) and `markdown元素对照/test2.md` (tables) in:
   - Obsidian (with Style Settings installed)
   - VSCode with Markdown Preview Enhanced (open preview side-by-side with editor)
   - Cherry Studio (with the theme applied)

   Check heading hover, list drawer, hr star, code-block red/yellow/green dots, KaTeX lift, table cell hover — all three platforms should look identical.

3. **Element behavior reference** — `markdown元素对照/MD元素设置对照.md` enumerates which elements should look like what. Confirm new changes against it before considering work done.

4. **No unit tests / no lint / no coverage.** Keep changes locally verifiable and re-runnable through the two scripts above.

---

## Workflow Notes for AI Assistants

- Edits to CSS/LESS/Python: English comments only, professional tone, no in-character language.
- Cross-platform changes: if you change a design rule in one theme, mirror it in the other two (the user expects all three platforms to remain visually consistent — `translateX(4px)`, `✦` hr, KaTeX lift, etc.).
- If you touch `theme-origin.css`, run `python obsidian/build_theme.py` afterwards and verify `theme.css` still matches. Never hand-edit `theme.css` directly.
- If you think the user wants to break a convention (e.g. add `authorUrl`, edit a read-only reference file, change `UNIFIED_KEYS` ordering), push back with the rule name from this file and confirm before acting.
- Workspace is on Windows (`win32`); use forward slashes in paths when calling tools.
