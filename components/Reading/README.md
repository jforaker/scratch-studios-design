# Reading

The hero of every instrument: a label, a big light numeral and its unit, with a sparkline and peak to the right.

- Label in label mono (`label`), numeral in the instrument's numeral voice (`numeral-mono` for Trace, `numeral-xl` or `numeral-l` for Break), unit beside it in `ink-soft`.
- The sparkline is a 1px line in the instrument accent. No fill on sparklines.
- Secondary readings sit in a row below, divided by full `rule` hairlines.
- Numbers count on change (≤160 ms); they never bounce.

The consumer provides the label, value, unit, peak and series.
