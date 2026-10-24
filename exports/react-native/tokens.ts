/**
 * Scratch Studios Design System — tokens for React Native.
 * Generated from tokens.json (v3). Do not edit by hand: change the design system, then regenerate.
 *
 * Type: Barlow (grotesk), IBM Plex Mono (labels, Trace numerals), Cutive Mono (wordmarks only).
 * Paper is the light theme, Night the dark theme. Every color has a value for each.
 * Rules that ride along with these values live in the design system README:
 *  - An accent is only ever text, a 1px line or a dot. Never a fill.
 *  - Selected rows shift to the instrument's selection ground. No edge bars.
 *  - Destructive actions are clay text. There is no red ground.
 */
import { useColorScheme } from 'react-native';

export type ThemeName = 'paper' | 'night';

export const colors = {
  paper: {
    /** Page ground. Paper by day, Night by night. */
    ground: "#F6F5F1",
    /** Raised layer: Card on paper, Graphite on night (sidebars). Separated from ground by a ground shift and a hairline, never a shadow. */
    raised: "#FCFBF8",
    /** Recessed track behind a segmented control or stepper. The selected segment sits on raised. */
    track: "#EDEAE3",
    /** Primary text, headings and numerals. 16.6:1 on paper, 15.7:1 on night. */
    ink: "#161616",
    /** Secondary text: descriptions, units beside a numeral, inactive segments. 8.4:1 on paper, 8.9:1 on night. */
    inkSoft: "#4A4843",
    /** Mono labels and metadata (Stone on paper, Ash on night). 4.5:1 and 5.5:1: small caps labels only, never body text. */
    label: "#73706A",
    /** 1px hairlines between rows, blocks and panels. Full rules divide; partial edges never highlight. */
    rule: "rgba(22, 22, 22, 0.12)",
    /** 1px outline of a control: pills, secondary buttons, steppers, the edges of a window. */
    ruleStrong: "rgba(22, 22, 22, 0.20)",
    /** Idle marks: empty rating dots, unfilled progress ticks. */
    sand: "#D8D3C9",
    /** Kelp. Break's instrument accent: chart line, live dot, the status dot on the mark, and 'good' on Break's verdicts. Text, 1px lines and dots only. 5.5:1 on paper, 7.9:1 on night. */
    nominal: "#4C6A55",
    /** Selected row or cell ground in Break. Never an edge highlight. */
    nominalSelection: "#E8EAE5",
    /** Peak of the chart fade under a nominal line. Fades to nothing at the baseline. */
    nominalChartFill: "#D4D9D2",
    /** Olive phosphor, after a P1 scope trace. Trace's instrument accent: chart line, sparklines, live dot, progress ticks, and 'good' on Trace's verdicts. 5.4:1 on paper, 9.7:1 on night. */
    phosphor: "#5C6B24",
    /** Selected row or nav item ground in Trace. Never an edge highlight. */
    phosphorSelection: "#EAEAE1",
    /** Peak of the chart fade under a phosphor line. */
    phosphorChartFill: "#D7D9C8",
    /** Cyanotype. Scratch's accent: links, cursor, current state. 7.0:1 on paper, 8.1:1 on night. */
    scratchAccent: "#2F5872",
    /** Selected note or row ground in Scratch. Never an edge highlight. */
    scratchSelection: "#E6E8E7",
    /** Peak of the chart fade under a cyanotype line. */
    scratchChartFill: "#CED6D8",
    /** Ground of a marked span: Break's best window, Trace's test interval, a found match in Scratch. Always bounded by a rule-strong hairline at each edge; labels sit outside it. */
    window: "#E7E4DD",
    /** Verdict 'fair' in every instrument. 5.6:1 on paper, 6.5:1 on night. */
    ochre: "#7C5D29",
    /** Verdict 'poor', the Stop ring, and the only signal for a destructive action (clay text, never a red panel). 4.9:1 on paper, 6.4:1 on night. */
    clay: "#A0583F",
    /** Studio accent. Studio surfaces only (site, guide), never inside an app. 7.6:1 on paper, 8.8:1 on night. */
    survey: "#334A94",
    /** Text selection on studio surfaces only. */
    surveyWash: "#DBDDE4",
  },
  night: {
    /** Page ground. Paper by day, Night by night. */
    ground: "#111110",
    /** Raised layer: Card on paper, Graphite on night (sidebars). Separated from ground by a ground shift and a hairline, never a shadow. */
    raised: "#1C1C1A",
    /** Recessed track behind a segmented control or stepper. The selected segment sits on raised. */
    track: "#1C1C1A",
    /** Primary text, headings and numerals. 16.6:1 on paper, 15.7:1 on night. */
    ink: "#ECEAE4",
    /** Secondary text: descriptions, units beside a numeral, inactive segments. 8.4:1 on paper, 8.9:1 on night. */
    inkSoft: "#B5B2AA",
    /** Mono labels and metadata (Stone on paper, Ash on night). 4.5:1 and 5.5:1: small caps labels only, never body text. */
    label: "#8C8A84",
    /** 1px hairlines between rows, blocks and panels. Full rules divide; partial edges never highlight. */
    rule: "rgba(255, 255, 255, 0.10)",
    /** 1px outline of a control: pills, secondary buttons, steppers, the edges of a window. */
    ruleStrong: "rgba(255, 255, 255, 0.20)",
    /** Idle marks: empty rating dots, unfilled progress ticks. */
    sand: "#3A3935",
    /** Kelp. Break's instrument accent: chart line, live dot, the status dot on the mark, and 'good' on Break's verdicts. Text, 1px lines and dots only. 5.5:1 on paper, 7.9:1 on night. */
    nominal: "#93AE98",
    /** Selected row or cell ground in Break. Never an edge highlight. */
    nominalSelection: "#212420",
    /** Peak of the chart fade under a nominal line. Fades to nothing at the baseline. */
    nominalChartFill: "#2B302B",
    /** Olive phosphor, after a P1 scope trace. Trace's instrument accent: chart line, sparklines, live dot, progress ticks, and 'good' on Trace's verdicts. 5.4:1 on paper, 9.7:1 on night. */
    phosphor: "#B3C07A",
    /** Selected row or nav item ground in Trace. Never an edge highlight. */
    phosphorSelection: "#24261D",
    /** Peak of the chart fade under a phosphor line. */
    phosphorChartFill: "#313425",
    /** Cyanotype. Scratch's accent: links, cursor, current state. 7.0:1 on paper, 8.1:1 on night. */
    scratchAccent: "#8EAEC4",
    /** Selected note or row ground in Scratch. Never an edge highlight. */
    scratchSelection: "#202426",
    /** Peak of the chart fade under a cyanotype line. */
    scratchChartFill: "#2A3034",
    /** Ground of a marked span: Break's best window, Trace's test interval, a found match in Scratch. Always bounded by a rule-strong hairline at each edge; labels sit outside it. */
    window: "#24221E",
    /** Verdict 'fair' in every instrument. 5.6:1 on paper, 6.5:1 on night. */
    ochre: "#B29362",
    /** Verdict 'poor', the Stop ring, and the only signal for a destructive action (clay text, never a red panel). 4.9:1 on paper, 6.4:1 on night. */
    clay: "#C5876F",
    /** Studio accent. Studio surfaces only (site, guide), never inside an app. 7.6:1 on paper, 8.8:1 on night. */
    survey: "#A0B1DB",
    /** Text selection on studio surfaces only. */
    surveyWash: "#2A3042",
  },
} as const;

export type ColorToken = keyof typeof colors.paper;
export type ThemeColors = { [K in ColorToken]: string };

/** Each instrument owns one accent and the two grounds tinted from it. */
export const instruments = {
  break: { model: 'SS-01', accent: 'nominal', selection: 'nominalSelection', chartFill: 'nominalChartFill' },
  trace: { model: 'SS-02', accent: 'phosphor', selection: 'phosphorSelection', chartFill: 'phosphorChartFill' },
  scratch: { model: 'SS-03', accent: 'scratchAccent', selection: 'scratchSelection', chartFill: 'scratchChartFill' },
} as const satisfies Record<string, { model: string; accent: ColorToken; selection: ColorToken; chartFill: ColorToken }>;

export type Instrument = keyof typeof instruments;

/**
 * PostScript names of the bundled font files, by weight.
 * Check these against the .ttf/.otf files the app actually ships and adjust here only.
 */
export const fontFaces = {
  grotesk: { 300: "Barlow-Light", 400: "Barlow-Regular", 500: "Barlow-Medium" },
  mark: { 400: "CutiveMono-Regular" },
  mono: { 300: "IBMPlexMono-Light", 400: "IBMPlexMono-Regular", 500: "IBMPlexMono-Medium" },
  personal: { 400: "CourierPrime-Regular" },
} as const;

export const type = {
    /** Numerals · Break's hero reading. Barlow Light. */
    numeralXl: { fontFamily: fontFaces.grotesk[300], fontSize: 112, lineHeight: 112, letterSpacing: -3.36 },
    /** Numerals · Secondary reading; unit beside it at 16px in ink-soft. */
    numeralL: { fontFamily: fontFaces.grotesk[300], fontSize: 60, lineHeight: 60, letterSpacing: 0 },
    /** Mono numerals · Trace's readings. Plex Mono 300, never Courier. */
    numeralMono: { fontFamily: fontFaces.mono[300], fontSize: 56, lineHeight: 56, letterSpacing: -1.12 },
    /** Grotesk · Screen titles. */
    title: { fontFamily: fontFaces.grotesk[400], fontSize: 36, lineHeight: 41, letterSpacing: 0 },
    /** Grotesk · Wordmarks only: Break, Trace, Scratch, Scratch Studios. Cutive Mono caps, tracked. Never in UI chrome. */
    mark: { fontFamily: fontFaces.mark[400], fontSize: 24, lineHeight: 24, letterSpacing: 10.08 },
    /** Grotesk · Place names and pills: Barlow Medium caps. */
    place: { fontFamily: fontFaces.grotesk[500], fontSize: 18, lineHeight: 22, letterSpacing: 2.52 },
    /** Grotesk */
    heading: { fontFamily: fontFaces.grotesk[400], fontSize: 22, lineHeight: 29, letterSpacing: 0 },
    /** Grotesk */
    body: { fontFamily: fontFaces.grotesk[400], fontSize: 15, lineHeight: 23, letterSpacing: 0 },
    /** Grotesk */
    small: { fontFamily: fontFaces.grotesk[400], fontSize: 13, lineHeight: 20, letterSpacing: 0 },
    /** Label mono · Always caps, always tracked. */
    label: { fontFamily: fontFaces.mono[400], fontSize: 11, lineHeight: 15, letterSpacing: 1.76 },
} as const;

export const space = {
  1: 4, // Base unit. Gap between a numeral and its unit.
  2: 8, // Label to value.
  3: 12, // Row padding, tight.
  4: 16, // Row padding, default; mobile side gutter.
  6: 24, // Between blocks.
  8: 32, // Between blocks, roomy.
  12: 48, // Between sections.
  16: 64, // Between sections, roomy.
} as const;

export const radius = {
  none: 0, // Panels, rows, cells, charts.
  sm: 2, // Small controls.
  md: 7, // Desktop controls: segmented controls, steppers, secondary buttons.
  round: 999, // Pills, dots and ring buttons.
} as const;

/** Motion stays short and settling. Numbers count; only a live dot loops. */
export const motion = { maxDuration: 160, easing: 'ease-out' } as const;

/** Verdict levels, shared by every instrument. Good uses the instrument's own accent. */
export function verdictColor(level: 'good' | 'fair' | 'poor', instrument: Instrument, c: ThemeColors): string {
  if (level === 'good') return c[instruments[instrument].accent];
  return level === 'fair' ? c.ochre : c.clay;
}

/** Resolve a theme for one instrument: all tokens plus accent, selection and chartFill. */
export function tokensFor(instrument: Instrument, themeName: ThemeName) {
  const c: ThemeColors = colors[themeName];
  const i = instruments[instrument];
  return {
    ...c,
    accent: c[i.accent],
    selection: c[i.selection],
    chartFill: c[i.chartFill],
    model: i.model,
    themeName,
  };
}

/** Follows the system appearance unless the user picked Paper or Night in settings. */
export function useTokens(instrument: Instrument, override?: ThemeName) {
  const scheme = useColorScheme();
  return tokensFor(instrument, override ?? (scheme === 'dark' ? 'night' : 'paper'));
}
