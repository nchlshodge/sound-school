# Build notes

How Sound School's audio was prepared and how its reference mixes were measured. Use this when adding a song or changing a reference.

## The songs

| ID | Song | Source | Tempo | Excerpt | Start / length |
|---|---|---|---|---|---|
| `wwy` | We Worship You | Studio stems (TWM Multitracks), 94 BPM, A | 94 | Bars 3–34 (verse into chorus) | 7.660 s / 79.149 s |
| `lhc` | Let's Have Church | Live multitrack, 50 mics | 170 | Bars 12–52 | 17.938 s / 56.471 s |
| `isg` | I'm So Glad I Met Jesus | Live multitrack, same band and mic list | 180 | Bars 16–56 | 27.652 s / 53.333 s |

Bar numbers for the live songs count from the first click (`lhc` first click at 0.997 s, `isg` at 6.319 s). Tempo came from the median spacing of click-track onsets.

**Studio stems** were cut with ffmpeg and encoded to AAC at 96 kbps stereo; click and cues at 48 kbps mono.

**Live songs** were combined into console-style channels with `tools/encode_live_song.sh`:

- Kick = Kick In + Kick Out **with Kick Out's polarity flipped**. Unflipped, the pair cancels: about 4 dB less low end.
- Snare = Snare 1 Top + Snare Top 2 (the bottom mic and triggers are left out of the board).
- Stereo pairs (overheads, guitars, keys, B3, tracks, crowd) are joined into stereo files.
- Left out: ACC 2 and Loops Sub in `lhc` (empty), drum triggers, FOH mics. In `isg` the snare and count tracks are silent in the excerpt, so they're left off that song's board.
- `x_*` files are the separate mics used by the Phase & Polarity drills.

## Measured facts the drills rely on

- **Kick In / Kick Out:** flipping Kick Out adds 1.6–3.5 dB below 150 Hz in every window; the mics are about 1.8 ms apart.
- **Snare top / bottom:** flipping the bottom adds about 4 dB of body (150–500 Hz), but **only where the snare is played** (`lhc` bars 44–46). Elsewhere the result is meaningless, so the snare drill is limited to those bars.
- **Bass DI / amp:** already in polarity and time-aligned; flipping one loses 16–22 dB of low end.

## Reference mixes

- **Gospel style:** `wwy` uses the stems' own balance (the lead vocal up 1.5 dB). For the live songs, each channel was set to a target level relative to the lead singer, measured over a full-band section. These are estimates.
- **Modern worship and broadcast styles** (`MODERN`, `BCAST` and `FX_REF` in `index.html`): fitted to Bethel Church's livestream of the Oct 4, 2026 evening service (youtu.be/ttH1_ghGtRY). Six songs from the worship set (13:22, 19:30, 34:50, 48:30, 1:00:20, 1:09:00) were measured in octave bands for tonal balance and mid/side stereo width. Bethel's balance varied only 1–2 dB from song to song. The fit adjusts faders (±6 dB on the band, −1 to +2 on vocals) while keeping the vocals' share of the 1–4 kHz range.
- **Trainers can override any reference** in the app (Trainer mode → "make this the reference mix"), which copies the levels to paste back into `index.html`.

Average Bethel target (octave bands 63 Hz–8 kHz, dB relative to the total):
`tonal: -5.1, -8.0, -8.6, -8.1, -9.2, -13.6, -18.5, -20.2`
`width (side minus mid): -19.7, -9.7, -2.8, -2.7, -0.7, -1.5, -2.7, -5.9`

## Speech

`stems/speech/male.m4a` and `female.m4a` are an original sermon passage read by macOS voices (Reed and Samantha) with `say`, loudness-normalized. They're stand-ins until a real recording of a pastor (with their permission) replaces them.

## Hosting (not live yet)

The Firebase project **RCC Training** (`rcc-training`) is set up with a web app named Sound School. `firebase.json` keeps the song stems out of public hosting. The plan is to put the stems in Firebase Storage behind sign-in, which needs the Blaze plan.
