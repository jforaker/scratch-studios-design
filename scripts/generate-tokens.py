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
  gauge: {{ model: 'SS-04', accent: 'gaugeAccent', selection: 'gaugeSelection', chartFill: 'gaugeChartFill' }},
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
/** Quota-style readings (how much is left, as in Gauge): above 50% good, 20–50% fair, below 20% poor. */
export const quotaThresholds = {{ fair: 50, poor: 20 }} as const;
export function quotaVerdict(percentLeft: number): 'good' | 'fair' | 'poor' {{
  if (percentLeft < quotaThresholds.poor) return 'poor';
  if (percentLeft <= quotaThresholds.fair) return 'fair';
  return 'good';
}}

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

# ---------------------------------------------------------------------------
# Native export: Swift (AppKit + UIKit + SwiftUI) from the same tokens.json.
# ---------------------------------------------------------------------------
def rgba(v):
    v=v.strip()
    if v.startswith('#'):
        return int(v[1:3],16),int(v[3:5],16),int(v[5:7],16),1.0
    m=re.match(r'rgba?\(\s*(\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\s*\)',v)
    return int(m[1]),int(m[2]),int(m[3]),float(m[4] or 1)
def sw(v):
    r,g,b,a=rgba(v); return f"ScratchRGBA({r}, {g}, {b}, {num(a)})"
def pair(x):
    v=x['value']; return (v,v) if isinstance(v,str) else (v['light'],v['dark'])
ccases='\n'.join(f"    /** {x['usage']} */\n    public static let {camel(x['name'])} = ScratchColor({sw(pair(x)[0])}, {sw(pair(x)[1])})" for x in toks)
objc_cases='\n'.join(f"    @objc public static let {camel(x['name'])}: NSColor = ScratchTokens.{camel(x['name'])}.platform" for x in toks)
sw_styles=[]
for g in t['type']['groups']:
    for s in g['styles']:
        fam=s.get('family',g['family']); fs=num(s['fontSize']); w=int(s['fontWeight'])
        lh=s['lineHeight']; lh=round(float(lh)*fs) if not str(lh).endswith('px') else num(lh)
        ls=s.get('letterSpacing'); ls=round(float(ls.replace('em',''))*fs,2) if ls else 0
        sw_styles.append(f"    public static let {camel(s['name'])} = ScratchTextStyle(face: ScratchFonts.{fam}[{w}]!, size: {fs}, lineHeight: {lh}, tracking: {ls})")
fam_sw='\n'.join(f"    public static let {k}: [Int: String] = [" + ', '.join(f"{w}: {q(n)}" for w,n in v.items()) + "]" for k,v in faces.items())
sp_sw='\n'.join(f"    public static let s{x['name'].split('-')[1]}: CGFloat = {num(x['value'])} // {x['usage']}" for x in t['spacing']['tokens'])
rd_sw='\n'.join(f"    public static let {x['name'].split('-')[1]}: CGFloat = {num(x['value'])} // {x['usage']}" for x in t['radius']['tokens'])
swift=f'''// Scratch Studios Design System — tokens for Swift (AppKit, UIKit, SwiftUI).
// Generated from tokens.json (v{t['version']}). Do not edit by hand: change the design system, then regenerate.
//
// Colors are dynamic: they resolve Paper or Night from the effective appearance.
// To force a theme, set NSApp.appearance (macOS) or overrideUserInterfaceStyle (iOS)
// with ScratchTheme; to follow the system, set it to nil.
import SwiftUI
#if canImport(AppKit)
import AppKit
public typealias ScratchPlatformColor = NSColor
public typealias ScratchPlatformFont = NSFont
#elseif canImport(UIKit)
import UIKit
public typealias ScratchPlatformColor = UIColor
public typealias ScratchPlatformFont = UIFont
#endif

public struct ScratchRGBA {{
    public let r: Double, g: Double, b: Double, a: Double
    public init(_ r: Int, _ g: Int, _ b: Int, _ a: Double) {{
        self.r = Double(r) / 255; self.g = Double(g) / 255; self.b = Double(b) / 255; self.a = a
    }}
}}

/// The user's Theme setting: System · Paper · Night.
public enum ScratchTheme: String, CaseIterable {{
    case system, paper, night

#if canImport(AppKit)
    /// Value for NSApp.appearance. nil follows the system.
    public var appearance: NSAppearance? {{
        switch self {{
        case .system: return nil
        case .paper: return NSAppearance(named: .aqua)
        case .night: return NSAppearance(named: .darkAqua)
        }}
    }}
#endif
#if canImport(UIKit)
    public var userInterfaceStyle: UIUserInterfaceStyle {{
        switch self {{
        case .system: return .unspecified
        case .paper: return .light
        case .night: return .dark
        }}
    }}
#endif
}}

/// One token: a Paper value and a Night value, resolved from the appearance at draw time.
public struct ScratchColor {{
    public let paper: ScratchRGBA
    public let night: ScratchRGBA
    public init(_ paper: ScratchRGBA, _ night: ScratchRGBA) {{ self.paper = paper; self.night = night }}

    public var platform: ScratchPlatformColor {{
        let paper = self.paper, night = self.night
        func make(_ c: ScratchRGBA) -> ScratchPlatformColor {{
            ScratchPlatformColor(red: c.r, green: c.g, blue: c.b, alpha: c.a)
        }}
#if canImport(AppKit)
        return NSColor(name: nil) {{ appearance in
            appearance.bestMatch(from: [.aqua, .darkAqua]) == .darkAqua ? make(night) : make(paper)
        }}
#else
        return UIColor {{ traits in traits.userInterfaceStyle == .dark ? make(night) : make(paper) }}
#endif
    }}

    public var color: Color {{
#if canImport(AppKit)
        return Color(nsColor: platform)
#else
        return Color(uiColor: platform)
#endif
    }}
}}

public enum ScratchTokens {{
{ccases}

    /** Scratch (SS-03) instrument: its accent and the two grounds tinted from it. */
    public static let accent = scratchAccent
    public static let selection = scratchSelection
    public static let chartFill = scratchChartFill
}}

#if canImport(AppKit)
/// Objective-C access for AppKit views (`SSTokens.ink`). Colors are dynamic, like the Swift ones.
@objc(SSTokens) public final class ScratchObjCTokens: NSObject {{
{objc_cases}

    /// Apply the Theme setting ("system", "paper" or "night") to the whole app, so every
    /// native view resolves the same Paper or Night values as the React Native side.
    @objc public static func applyTheme(_ name: String) {{
        NSApp?.appearance = (ScratchTheme(rawValue: name) ?? .system).appearance
    }}
}}
#endif

/// PostScript names of the bundled font files, by weight.
public enum ScratchFonts {{
{fam_sw}
}}

public struct ScratchTextStyle {{
    public let face: String
    public let size: CGFloat
    public let lineHeight: CGFloat
    public let tracking: CGFloat
    public var platformFont: ScratchPlatformFont {{
        ScratchPlatformFont(name: face, size: size) ?? ScratchPlatformFont.systemFont(ofSize: size)
    }}
    public var font: Font {{ Font.custom(face, fixedSize: size) }}
}}

public enum ScratchType {{
{chr(10).join(sw_styles)}
}}

public enum ScratchSpace {{
{sp_sw}
}}

public enum ScratchRadius {{
{rd_sw}
}}
'''
os.makedirs(os.path.join(ROOT,'exports','swift'),exist_ok=True)
open(os.path.join(ROOT,'exports','swift','ScratchTokens.swift'),'w').write(swift)
print(len(swift))
