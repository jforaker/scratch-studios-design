import json,re
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
t=json.load(open(os.path.join(ROOT,'tokens','tokens.json')))
camel=lambda s: re.sub(r'-([a-z0-9])',lambda m:m.group(1).upper(),s)
def q(s): return json.dumps(s)
def num(v):
    v=float(str(v).replace('px','')); return int(v) if v==int(v) else round(v,2)
toks=t['color']['tokens']
def theme(th):
    lines=[]
    for x in toks:
        v=x['value']; v=v if isinstance(v,str) else v[th]
        lines.append(f"    /** {x['usage']} */\n    {camel(x['name'])}: {q(v)},")
    return '\n'.join(lines)
faces={'grotesk':{300:'Barlow-Light',400:'Barlow-Regular',500:'Barlow-Medium'},
       'mark':{400:'CutiveMono-Regular'},
       'mono':{300:'IBMPlexMono-Light',400:'IBMPlexMono-Regular',500:'IBMPlexMono-Medium'},
       'personal':{400:'CourierPrime-Regular'}}
styles=[]
for g in t['type']['groups']:
    for s in g['styles']:
        fam=s.get('family',g['family']); fs=num(s['fontSize']); w=int(s['fontWeight'])
        lh=s['lineHeight']; lh=round(float(lh)*fs) if not str(lh).endswith('px') else num(lh)
        ls=s.get('letterSpacing'); ls=round(float(ls.replace('em',''))*fs,2) if ls else 0
        face=faces[fam][w]
        doc=f"    /** {g['name']}{' · '+s['usage'] if s.get('usage') else ''} */\n" 
        styles.append(doc+f"    {camel(s['name'])}: {{ fontFamily: fontFaces.{fam}[{w}], fontSize: {fs}, lineHeight: {lh}, letterSpacing: {ls} }},")
space='\n'.join(f"  {x['name'].split('-')[1]}: {num(x['value'])}, // {x['usage']}" for x in t['spacing']['tokens'])
radius='\n'.join(f"  {x['name'].split('-')[1]}: {num(x['value'])}, // {x['usage']}" for x in t['radius']['tokens'])
facelines='\n'.join(f"  {k}: {{ "+', '.join(f"{w}: {q(n)}" for w,n in v.items())+" },"  for k,v in faces.items())
out=f'''/**
 * Scratch Studios Design System — tokens for React Native.
 * Generated from tokens.json (v{t['version']}). Do not edit by hand: change the design system, then regenerate.
 *
 * Type: Barlow (grotesk), IBM Plex Mono (labels, Trace numerals), Cutive Mono (wordmarks only).\n * Paper is the light theme, Night the dark theme. Every color has a value for each.
 * Rules that ride along with these values live in the design system README:
 *  - An accent is only ever text, a 1px line or a dot. Never a fill.
 *  - Selected rows shift to the instrument's selection ground. No edge bars.
 *  - Destructive actions are clay text. There is no red ground.
 */
import {{ useColorScheme }} from 'react-native';

export type ThemeName = 'paper' | 'night';

export const colors = {{
  paper: {{
{theme('light')}
  }},
  night: {{
{theme('dark')}
  }},
}} as const;

export type ColorToken = keyof typeof colors.paper;
export type ThemeColors = {{ [K in ColorToken]: string }};

/** Each instrument owns one accent and the two grounds tinted from it. */
export const instruments = {{
  break: {{ model: 'SS-01', accent: 'nominal', selection: 'nominalSelection', chartFill: 'nominalChartFill' }},
  trace: {{ model: 'SS-02', accent: 'phosphor', selection: 'phosphorSelection', chartFill: 'phosphorChartFill' }},
  scratch: {{ model: 'SS-03', accent: 'scratchAccent', selection: 'scratchSelection', chartFill: 'scratchChartFill' }},
}} as const satisfies Record<string, {{ model: string; accent: ColorToken; selection: ColorToken; chartFill: ColorToken }}>;

export type Instrument = keyof typeof instruments;

/**
 * PostScript names of the bundled font files, by weight.
 * Check these against the .ttf/.otf files the app actually ships and adjust here only.
 */
export const fontFaces = {{
{facelines}
}} as const;

export const type = {{
{chr(10).join(styles)}
}} as const;

export const space = {{
{space}
}} as const;

export const radius = {{
{radius}
}} as const;

/** Motion stays short and settling. Numbers count; only a live dot loops. */
export const motion = {{ maxDuration: 160, easing: 'ease-out' }} as const;

/** Verdict levels, shared by every instrument. Good uses the instrument's own accent. */
export function verdictColor(level: 'good' | 'fair' | 'poor', instrument: Instrument, c: ThemeColors): string {{
  if (level === 'good') return c[instruments[instrument].accent];
  return level === 'fair' ? c.ochre : c.clay;
}}

/** Resolve a theme for one instrument: all tokens plus accent, selection and chartFill. */
export function tokensFor(instrument: Instrument, themeName: ThemeName) {{
  const c: ThemeColors = colors[themeName];
  const i = instruments[instrument];
  return {{
    ...c,
    accent: c[i.accent],
    selection: c[i.selection],
    chartFill: c[i.chartFill],
    model: i.model,
    themeName,
  }};
}}

/** Follows the system appearance unless the user picked Paper or Night in settings. */
export function useTokens(instrument: Instrument, override?: ThemeName) {{
  const scheme = useColorScheme();
  return tokensFor(instrument, override ?? (scheme === 'dark' ? 'night' : 'paper'));
}}
'''
open(os.path.join(ROOT,'exports','react-native','tokens.ts'),'w').write(out)
print(len(out))
