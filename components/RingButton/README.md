# RingButton

The instrument's one big action: a 44px ring with a dot at its centre, and a mono label beside it.

- Start: a 1px `ink` ring, 7px accent dot. Stop: a 1px `clay` ring, 7px `ink` dot. Stop is always clay.
- Never a filled disc. The accent is only ever the dot.
- Secondary actions are outlined buttons: 1px `rule-strong`, `radius-md`, 13px grotesk 500. Links are ink with a `rule-strong` underline.
- A destructive action is `clay` text, sentence case, on the normal ground. No red panel, no confirm ground.

The consumer provides the label and whether the instrument is running.
