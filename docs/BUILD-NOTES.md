# Build notes

How Sound School's audio was prepared and how its reference mixes were measured. Use this when adding a song or changing a reference.

## The songs

| ID | Song | Source | Tempo | Excerpt | Start / length |
|---|---|---|---|---|---|
| `wwy` | We Worship You | Studio stems (TWM Multitracks), 94 BPM, A | 94 | Bars 3–34 (verse into chorus) | 7.660 s / 79.149 s |
| `lhc` | Let's Have Church | Live multitrack, 50 mics | 170 | Bars 12–52 | 17.938 s / 56.471 s |
| `isg` | I'm So Glad I Met Jesus | Live multitrack, same band and mic list | 180 | Bars 16–56 | 27.652 s / 53.333 s |
| `rcc` | RCC Sunday (Feb 15, 2026) | RCC's own live multitrack (Google Drive) | 136 | Bars 12–170 (song into the MC) | 43:00–48:45 of the service recording |

Bar numbers for the live songs count from the first click (`lhc` first click at 0.997 s, `isg` at 6.319 s). Tempo came from the median spacing of click-track onsets.

**Studio stems** were cut with ffmpeg and encoded to AAC at 96 kbps stereo; click and cues at 48 kbps mono.

**Live songs** were combined into console-style channels with `tools/encode_live_song.sh`:

- Kick = Kick In + Kick Out **with Kick Out's polarity flipped**. Unflipped, the pair cancels: about 4 dB less low end.
- Snare = Snare 1 Top + Snare Top 2 (the bottom mic and triggers are left out of the board).
- Stereo pairs (overheads, guitars, keys, B3, tracks, crowd) are joined into stereo files.
- Left out: ACC 2 and Loops Sub in `lhc` (empty), drum triggers, FOH mics. In `isg` the snare and count tracks are silent in the excerpt, so they're left off that song's board.
- `x_*` files are the separate mics used by the Phase & Polarity drills.

**RCC Sunday (`rcc`)** was pulled from the shared Drive folder with HTTP byte-range requests (only the 43:00–48:45 span of each WAV, not the full 25–30 GB). There are no real kick or snare-top mics on that board, so the drum channels use the KickReplace and SnareReplace tracks; the snare bottom mic is its own channel. The `mc` channel plays the TTS stand-in (`stems/speech/male.m4a`) from bar 153 until the MC and lav speakers OK using their real recordings. Its reference mix is an estimate: no Bethel fit yet.

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

## Service Run and Soundcheck

- **Soundcheck:** the chorus (bars 60–68) loops, and each channel's ideal gain puts the loudest peak in that loop at −11 dBFS. The meters hold the loudest peak over a full loop. Shorter holds missed snare transients and read 4–6 dB low.
- **Into speaking:** scored 35% balance, 25% MC mic timing, 15% pad held, 15% pad tucked, 10% MC level, minus 25 per leak (click or crowd in the house).
- **Quick mix / mixer EQ:** each channel has a 3-band EQ (low shelf 120 Hz, sweepable mid, high shelf 8 kHz). Quick mix plants one or two tone problems (mud, boxy, honk, harsh, boom, dull). A problem counts as fixed when the remaining error is within 3 dB at every frequency.

## Our Mix vs. Bethel

`stems/rcc/mb1–3.m4a` are 20 s of the board's stereo mix (Master Burn, Feb 15) from three worship songs: about 23:00, 37:00 and 44:00 into the service. Measured over 2.5 minutes of each song, against the Bethel averages above:

- Loudness: −12.6 to −13.3 LUFS, peaks −0.3 dBFS, 2.1–2.5 dB short-term range (about the same as Bethel).
- Tone: +1 to +3 dB at 125 Hz, −2 to −5 dB from 500 Hz to 2 kHz, +1 to +2 dB at 4 kHz.
- Width: side minus mid 3–7 dB below Bethel from 250 Hz to 2 kHz.

`OURS_TONE` (low shelf 150 Hz −3.2, peak 640 Hz +2.5 Q 0.5, high shelf 4 kHz −2.1) and `OURS_WIDE` (side-only peak 1370 Hz +8.5 Q 0.4) were fitted so the three clips land within about 2 dB of Bethel in each octave band. Every variant is level-matched at load.

## Speech

`stems/speech/male.m4a` and `female.m4a` are an original sermon passage read by macOS voices (Reed and Samantha) with `say`, loudness-normalized. They're stand-ins until a real recording of a pastor (with their permission) replaces them.

## Hosting and sign-in

- **Live at https://rcc-training.web.app** (Firebase project **RCC Training**, `rcc-training`). Deploy with `firebase deploy --only hosting`.
- **Sign-in:** Google, or an emailed sign-in link for people without Google. `@rochesterchristian.church` accounts get in automatically. Anyone else appears on the leader's **Team progress** page (Settings) and waits for approval.
- **Leaders** are listed in three places that must match: `LEADERS` in `index.html`, `firestore.rules` and `storage.rules`.
- **Data:** `users/{uid}` holds each person's progress (merged with the device on sign-in); `approvals/{uid}` is written only by leaders.
- **Song stems** are kept out of public hosting (`firebase.json`) and load from Firebase Storage, which `storage.rules` limits to approved people. Storage needs the Blaze plan.
- **Local copies** (localhost or the Wi-Fi test server) skip sign-in and load stems from this folder. Add `?cloud` to the URL to test sign-in locally.
