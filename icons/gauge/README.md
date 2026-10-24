# SS-04 Gauge · Ticks

Gauge's own reading made into the mark: twelve ticks between two hairline rules, the spent ones dimmed, and a dot over the leading tick.

All values come from the design system (Night):

| Part | Token | Value |
|---|---|---|
| Ground | `ground` | #111110 |
| Remaining ticks | `ink` | #ECEAE4 |
| Leading tick and dot | `gauge-accent` | #9AAFC6 |
| Spent ticks | `sand` | #3A3935 |
| Rules | `rule-strong`, flattened on ground | #4A4A47 |

## Files

- `gauge-ticks-night.svg`: the vector master (100 × 100, full bleed).
- `gauge-ticks-1024.png`: the 1024 master. Opaque and full bleed: macOS applies its own mask, so never use a pre-rounded PNG as the AppIcon source.
- `gauge.iconset/`: every size for an Xcode asset catalog. Rebuild the `.icns` on a Mac with `iconutil -c icns gauge.iconset`.
- `gauge.icns`: a convenience build. It lacks the 16 and 32 @1x entries, so prefer the `iconutil` build.
- `gauge-ticks-paper.svg`, `gauge-ticks-paper-1024.png`: a Paper preview, for docs only. The app icon is Night in every appearance.
- `menubar/`: the menu-bar template glyph (pure black, `isTemplate = true`, never tinted). The live dot beside it is drawn in code, in the verdict color of the lowest reading.
