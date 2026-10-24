# Break app icon: Peel (SS-01)

Three swell lines wrapping a point, peeling right into the bay. The kelp dot is the rock at the point and the mark's one accent. Break uses the dark icon in every appearance.

## Files
- `break-icon-1024.png`: the iOS icon. It's 1024 × 1024, square, with no transparency; iOS applies the mask and makes the tinted variant itself.
- `break-icon.svg`: the vector master (viewBox 100).
- `layers/`: background, swell and point as separate SVGs for Icon Composer (iOS 26), plus `glyph-1024.png` on transparent.
- `android/res/`: ready-to-copy mipmaps.
  - An adaptive icon (`mipmap-anydpi-v26`) with foreground, background and monochrome layers.
  - Legacy square and round PNGs, from mdpi to xxxhdpi.
- `android/play-store-512.png`: the Play Store listing icon.
- `android/*.svg`: the adaptive foreground and background as vectors (108-unit canvas).

## Values
- Ground #1C1C1A (graphite), lines #ECEAE4 (chalk), dot #93AE98 (nominal, night)
- Lines 3.4 units wide on a 100-unit canvas, round caps; dot radius 4.4 at (44, 38)
- Registration marks rgba(236,234,228,.22), matching the construction of Trace's icon
