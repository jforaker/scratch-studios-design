# Small Currents Design

[link](https://jforaker.github.io/small-currents-design/style-guide/)

The design system for Small Currents' four instruments: SC-01 Break, SC-02 Trace, SC-03 Scratch and SC-04 Gauge. Quiet, instrument-like software that looks like a well-made field notebook.

## What's here

| Path                             | What                                                                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `tokens/tokens.json`             | **The source of truth.** Every color (Paper and Night), the type styles, spacing and radius.                                   |
| `docs/design-system.md`          | The rules: color, verdicts, state grounds, type, marks, app icons, layout and voice.                                           |
| `components/`                    | Seven component specs (`README.md`) with HTML previews: Reading, Navigation, Chart, Verdict, Ring button, Pills, Settings row. |
| `exports/react-native/tokens.ts` | Generated for the apps. **Don't edit it by hand.**                                                                             |
| `scripts/generate-tokens.py`     | Regenerates the export from `tokens.json`.                                                                                     |
| `icons/break/`                   | Break's Peel icon: the iOS 1024 icon, Icon Composer layers and Android mipmaps.                                                |
| `icons/trace/`                   | Trace's Signal icon (reference PNG).                                                                                           |
| `icons/scratch/`                 | Scratch's Stroke icon.                                                                                                         |
| `icons/gauge/`                   | Gauge's Ticks icon: SVG and 1024 masters, the macOS iconset, and the menu-bar template glyph.                                  |
| `style-guide/index.html`         | The editorial style guide as one self-contained page; the starting point for the studio homepage.                              |

## Changing a value

1. Edit `tokens/tokens.json`.
2. Run `python3 scripts/generate-tokens.py`.
   This writes both `exports/react-native/tokens.ts` and `exports/swift/ScratchTokens.swift`. Never edit either by hand.
3. Update `docs/design-system.md` if a rule changed.
4. Bump `version` in `package.json`, merge, and tag the release to match (`v1.6.0`).
5. In each app, bump the `small-currents-design` dependency to the new tag. When migrating from `@scratch-studios/design`, also update imports and any native file references into `node_modules`.

## Fonts

The fonts are bundled in each app, not here. All three are under the SIL Open Font License, from the google/fonts repo:

- Barlow (Light, Regular, Medium)
- IBM Plex Mono (Light, Regular, Medium)
- Cutive Mono (Regular; wordmarks only)

## Publishing the style guide

`style-guide/index.html` runs as is on any static host (GitHub Pages, Netlify, Cloudflare Pages). Its fonts and images are embedded in the page.

## Mirrors

The same system lives as two claude.ai artifacts:
**Small Currents Design System** and **Small Currents Style Guide**. When values change, update this repo and the artifact together so they don't drift.

## Swift Package Manager

Add `https://github.com/jforaker/small-currents-design.git` as a versioned Swift package dependency (starting with v1.7.2), then add the `SmallCurrentsDesign` library product to your target. Import `SmallCurrentsDesign` to use the generated `ScratchTokens`, `ScratchType`, and related public types. Commit your app's `Package.resolved` so builds use the same revision. SwiftPM fetches the tokens automatically; no sibling checkout is required. Fonts remain bundled by each app.
