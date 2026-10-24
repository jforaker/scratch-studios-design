# Chart

A 1px line in the instrument accent over a dot grid, with the area beneath fading from `*-chart-fill` to nothing.

- The dot grid uses `rule-strong` at one spacing step. No solid gridlines.
- A marked span sits on `window` with a `rule-strong` hairline at each edge, behind the fill and line. Name it in a label above the plot, in the accent ("BEST 6P–11P").
- Axis labels and units sit outside the plot in `label`. Nothing is written inside the plot.
- Radius 0. No shadows, no glow on the line, no second color.

The consumer provides the series, the window range (optional) and the axis labels.
