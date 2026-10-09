# Sound School

An ear-training and mixing course for church sound teams, built for Rochester Christian Church. Short lessons and listening drills, in the style of a language-learning app, guided by Sona the bat and a team of animal mascots.

Everything runs in the browser with the Web Audio API: the drills apply EQ, compression, gates, delay, reverb, feedback and mic simulations live to real multitrack recordings.

## What's inside

- **The path:** Foundations, Gain Staging, Volume, Loudness & Your Ears, EQ (music and the spoken word, mic problems, ringing out feedback), Phase & Polarity, Gates, Compression, Limiters, Delay, Reverb (including plate vs. hall), More Effects, Livestream, Mixing, Keys & Auto-Tune (Nashville Number System), and Modern Worship.
- **Mixing units:** The Sunday Mix (house) and The Livestream Mix (broadcast), on a real fader board with high-pass filters and vocal effects returns. Mixes are scored against reference mixes. The Modern Worship references were fitted to measurements of Bethel Church's livestream.
- **Our Mix vs. Bethel:** our Feb 15 board mix next to the same clips with Bethel's measured tone and width, with drills and what to change at the board.
- **Sunday Service Run:** our own band (RCC, Feb 15, 2026). Soundcheck the inputs on a looping chorus, mix the whole song, then hand off to the MC as they walk up. Every channel on the board has a 3-band EQ, and Quick mix plants tone problems to find and fix.
- **Exercises:** short workouts anyone can do anytime, each with a shareable link (`?ex=<id>`).
- **Placement check:** finds what a new volunteer already knows, so they can skip ahead.
- **Console notes:** lessons are universal, with optional notes for the Midas M32 / Behringer X32 (Settings → Your console).

## Running it

The app is a single `index.html`. It loads audio files, so it needs to be served over http (opening the file directly won't work):

```bash
cd "Sound School"
python3 -m http.server 8765
```

Then open http://localhost:8765/.

## Audio files

```
stems/
  speech/   two computer-voice sermon readings
  wwy/      "We Worship You" studio stems
  lhc/      "Let's Have Church" live multitrack
  isg/      "I'm So Glad I Met Jesus" live multitrack
  rcc/      RCC Sunday, our band's live multitrack (song into the MC)
```

The song multitracks are licensed for our church's own use. **Keep this repository private**, and don't publish the stems anywhere public. Each song is defined in the `SONGS` array in `index.html`, which lists the channel files it expects (for example `stems/lhc/kick.m4a`). Stems are short excerpts encoded as AAC (`.m4a`).

To add a song: encode its stems into `stems/<id>/`, then add an entry to `SONGS` with its tempo, channels, reference mix and the bars to use.

## Progress

Progress, XP and streaks are saved in the browser on each device (localStorage).
