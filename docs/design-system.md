# Scratch Studios

Quiet, instrument-like software that looks like a well-made field notebook. Calm, precise, analog, never flashy.

One shared language for four instruments: **Break** (surf conditions), **Trace** (network analyzer), **Scratch** (fast notes) and **Gauge** (AI usage). The anatomy stays the same across all of them; only the accent changes.

If it could belong in a well-kept field station, a darkroom, a lab notebook, or a 1980s precision instrument redesigned by a modern Apple team, it is on target. Benchmarks: Braun, Tektronix and HP bench instruments, NASA mission control, Apple Hardware Test, field notebooks.

This system holds the values and rules that code reads. The *Scratch Studios Style Guide* is the editorial companion; when a value changes, it changes here first.

## Principles

- **Calm.** Nothing moves, glows or asks for attention unless it means something. Color is held back for state.
- **Precise.** The reading is the hero. Numerals run big and light; labels whisper beside them in small, spaced mono.
- **Analog.** Paper, ink and hairlines. No glass, no shadows, no gradients except a chart's fading fill.

## Color

Every app runs on **Paper** (light) and **Night** (dark), and every color has a separate value for each. Never use one hex on both grounds.

Accents are pigments, not screens: kelp, olive phosphor, cyanotype, slate, ochre, clay. Low chroma, darkened for paper, lifted and greyed for night.

### Instrument accents

Each instrument owns one accent. It says *which instrument this is*: the chart line, sparklines, live dot, progress ticks and the status dot on the mark.

| Instrument | Accent | Paper | Night | Selection | Chart fill |
|---|---|---|---|---|---|
| Break | `nominal` (kelp) | #4C6A55 | #93AE98 | `nominal-selection` | `nominal-chart-fill` |
| Trace | `phosphor` (olive) | #5C6B24 | #B3C07A | `phosphor-selection` | `phosphor-chart-fill` |
| Scratch | `scratch-accent` (cyanotype) | #2F5872 | #8EAEC4 | `scratch-selection` | `scratch-chart-fill` |
| Gauge | `gauge-accent` (slate) | #4A5866 | #9AAFC6 | `gauge-selection` | `gauge-chart-fill` |
| Studio | `survey` | #334A94 | #A0B1DB | — | — |

`survey` lives on studio surfaces (site, guide), never inside an app.

### Verdicts

One scale for every instrument:

- **Good**: the instrument's own accent. Never a second green beside the chart.
- **Fair**: `ochre`.
- **Poor**: `clay`.
- **Idle dots and ticks**: `sand`.

Quota readings (how much is left, as in Gauge) use fixed cutoffs: above 50% left is good, 20–50% is fair, below 20% is poor. Filled ticks take the verdict color; the numeral stays in ink. The export carries these as `quotaThresholds` and `quotaVerdict()`.

A verdict is a word in label mono plus five dots. The dots carry the count, so meaning never rests on hue alone.

### State grounds

- **Selection** says where you are: selected rows, nav items and cells shift to the instrument's `*-selection` ground. No edge bars, left borders or tinted rounded rows.
- **Window** says when it matters: a marked span (Break's best window, Trace's test interval, a Scratch search match) sits on `window`, with a `rule-strong` hairline at each edge. Labels go outside it.
- **Chart fill** says how much: the area under a line fades from `*-chart-fill` to nothing.
- **Destructive** has no ground. `clay` is always Stop, and a destructive action is clay text on the normal ground.

### The one rule

An accent appears only as text, a 1px line or a dot. Never as a button fill, card tint or background.

## Type

Three voices and a mark:
1. **Grotesk** speaks: Barlow for headings, body and place names. It was drawn from California road signs and license plates: slightly narrow, softly finished, built to be read at a glance.
2. **Label mono** labels: IBM Plex Mono for labels, units, metadata and tab bars. Always caps, always tracked +0.16 em.
3. **Numerals** measure: light, never bold. Break reads in Barlow Light 300 (`numeral-xl`); Trace measures in Plex Mono 300 (`numeral-mono`).
4. **Mark**: Cutive Mono, a typewriter face, sets the wordmarks (BREAK, TRACE, SCRATCH, GAUGE, SCRATCH STUDIOS) and nothing else. Caps, tracked +0.42 em, one weight. Never in tab bars, labels, headers or body.

Courier Prime (`personal`) is only an optional editor font in Scratch's settings. Never in marks, labels, numerals or marketing.

Wordmarks are typed, not drawn: Cutive Mono caps with a Plex Mono descriptor at about 2/5 size (SURF CONDITIONS, NETWORK ANALYZER, FAST NOTES, AI USAGE) and "by Scratch Studios". The only accent on a mark is its status dot.

Each instrument carries a model number, set in label mono beside the mark and on the About screen: **SS-01** Break, **SS-02** Trace, **SS-03** Scratch, **SS-04** Gauge. New instruments take the next number; numbers are never reused.

## App icons

Each instrument's icon rereads one familiar shape, built the same way:
- A square, full-bleed canvas.
- Registration ticks at the edges.
- Three lines.
- One dot in the instrument's accent.

- **SS-01 Break: Peel.** Swell lines wrapping a point, peeling right. Graphite ground, chalk lines, `nominal` dot. Break uses this one icon in every appearance.
- **SS-02 Trace: Signal.** Wifi arcs cut like a section drawing. Paper ground, graphite arcs. The dot should be `phosphor`.
- **SS-03 Scratch: Stroke.** One quick stroke of ink on paper. It has no dot: the stroke is the mark.
- **SS-04 Gauge: Ticks.** Gauge's own reading turned into the mark: twelve ticks between two hairline rules, the spent ones in `sand`, the leading tick and a dot above it in `gauge-accent`. Night ground.

### Menu-bar items

A menu-bar instrument (Gauge) uses a monochrome template glyph, never tinted, so macOS can invert it. Beside it sits one small dot that is live: it takes the verdict color of the lowest reading (accent, `ochre` or `clay`). It is the only icon in the family whose color changes with state.

The files are in the App icons asset group.

## Components

Each card shows the component in the instrument and ground it comes from. Swap the accent; keep the anatomy.

- **Reading**: label, big light numeral, unit; a sparkline and its peak to the right, divided by a full hairline.
- **Navigation**: mono labels with ⌘ shortcuts; the active item is a selection ground, nothing else.
- **Chart**: 1px accent line over a dot grid, fill fading to nothing, optional window band, labels outside the plot.
- **Verdict**: dots plus word; live dot; progress ticks.
- **Ring button**: the reading's start and stop. A 1px ring with a centre dot, never a filled disc.
- **Pills**: place pickers in one scrolling row. The selected pill sits on the selection ground; the rest are outlined in `rule-strong`.
- **Settings row**: label and description left, control right; segmented controls sit in a track.

## Layout

- **Hairlines, not boxes.** 1px `rule` only.
- **Spacing.** 4-pt base. Rows 12–16, blocks 24–32, sections 48–64.
- **Radius.** 0 for panels, rows and charts; 2 and 7 for small and desktop controls; pills, dots and ring buttons fully round.
- **Elevation.** None. Layers separate by a ground shift and a hairline.
- **Motion.** 0–160 ms, ease-out. Numbers count, they don't bounce. Only a live dot loops.

## Voice

Say what the instrument sees. Numbers before adjectives. Sentence case, full stops. No exclamation marks, no emoji, no cheerleading.

- Write: "Download is 21% lower than your reference." / "Calm wind throughout the window. Expect 2–3 ft surf." / "Changes apply immediately. There is no Save button."
- Not: "Uh oh! Your internet seems kind of slow today." / "Don't worry — we'll auto-save everything for you!"

## Exports

`tokens.json` is the source of truth. `exports/react-native/tokens.ts` and `exports/swift/ScratchTokens.swift` are generated from it for the apps. The React Native export has: Paper and Night color sets, the instrument map (accent, selection, chart fill, model number), type styles in points, spacing, radius, and a `useTokens(instrument, override?)` hook. Change a value here first, then regenerate the export; never edit the export by hand. The font names in `fontFaces` must match the font files each app bundles.

## Open items

- Gauge still reads a local token file; switch it to the Swift export in `@scratch-studios/design` v1.6.0.

- Studio mark: square-with-slash glyph versus type-only wordmark is unconfirmed.
- `survey-wash` on night is proposed and unused so far.
