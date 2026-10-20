# Build notes

How Sound School's audio was prepared and how its reference mixes were measured. Use this when adding a song or changing a reference.

## The songs

| ID | Song | Source | Tempo | Excerpt | Start / length |
|---|---|---|---|---|---|
| `wwy` | We Worship You | Studio stems (TWM Multitracks), 94 BPM, A | 94 | Bars 3–34 (verse into chorus) | 7.660 s / 79.149 s |
| `lhc` | Let's Have Church | Live multitrack, 50 mics | 170 | Bars 12–52 | 17.938 s / 56.471 s |
| `isg` | I'm So Glad I Met Jesus | Live multitrack, same band and mic list | 180 | Bars 16–56 | 27.652 s / 53.333 s |
| `gsg` | God So Good | Life.Church live stems (15 stereo stems, raw files in `stems/GodsoGoodLifeChurch/`, not in git) | 77.5 | The whole song (bar 1 = 0:00) | 0 s / 326.3 s |
| `rcc` | RCC Sunday (Feb 15, 2026), **hidden** | RCC's own live multitrack (Google Drive). Not in the song lists or drills (`hidden:true`); it still powers the soundcheck, the Sunday run, the tom gates and "Our mix vs. Bethel" until it's replaced by another service. RCC Song 1 and 2 (`rcc1`, `rcc2`) were removed from the app; their stems are still in `stems/` and Storage. | 136 | Bars 12–170 (song into the MC) | 43:00–48:45 of the service recording |

Bar numbers for the live songs count from the first click (`lhc` first click at 0.997 s, `isg` at 6.319 s). Tempo came from the median spacing of click-track onsets.

**Encoding:** every stem is AAC from Apple's encoder (`-c:a aac_at`, macOS): 96 kbps mono, 128 kbps stereo, 48 kbps for click and cues. ffmpeg's built-in AAC at 48–64 kbps (used at first) cut God So Good's cymbals above 14 kHz and left swishy artifacts; the re-encode kept every music channel within 0.5 dB of its old level, so the reference mixes didn't move. Stereo stems folded to mono use the -3 dB pan law (`pan=mono|c0=0.7071*c0+0.7071*c1`).

**Live songs** were combined into console-style channels with `tools/encode_live_song.sh`:

- Kick = Kick In + Kick Out **with Kick Out's polarity flipped**. Unflipped, the pair cancels: about 4 dB less low end.
- Snare = Snare 1 Top + Snare Top 2 (the bottom mic and triggers are left out of the board).
- Stereo pairs (overheads, guitars, keys, B3, tracks, crowd) are joined into stereo files.
- Left out: ACC 2 and Loops Sub in `lhc` (empty), drum triggers, FOH mics. In `isg` the snare and count tracks are silent in the excerpt, so they're left off that song's board.
- `x_*` files are the separate mics used by the Phase & Polarity drills.

**RCC Sunday (`rcc`)** was pulled from the shared Drive folder with HTTP byte-range requests (only the 43:00–48:45 span of each WAV, not the full 25–30 GB). There are no real kick or snare-top mics on that board, so the drum channels use the KickReplace and SnareReplace tracks; the snare bottom mic is its own channel. The `mc` channel plays the real announcements mic (`stems/voices/mc.m4a`, MC 2 from the same service) from bar 153. Its reference mix is an estimate: no Bethel fit yet.

**God So Good (`gsg`)** stems are printed at the record's balance (bar 1 starts at 0:00; the click lines up with that grid within 0.2 ms). Lead vocal, bass, synth bass and the three electrics are mono at 48 kbps; the rest stereo at 72 kbps (37 MB). The click, cue and count tracks aren't on the board. The cue track was used to find the song's sections (`sections` in `index.html`): cues that say the same word were grouped by comparing their sound, then named by matching against spoken section names and the arrangement. The names are a best guess; the boundaries are exact. The mixer can loop any section.

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

## Our other two songs and their sections

The Feb 15 service has four click-tracked songs: 18:41–25:46, 31:30–39:20, 41:40–47:20 (`rcc`, RCC Sunday) and 1:42:30–1:54:35 after the sermon. The click runs at 136 BPM throughout with no accent, and no cue track was recorded during the songs, so sections were found from the arrangement: where the mix of instruments changes, snapped to the crash or kick hit at the change. Most land on 8- or 16-bar lengths. Sections that sound alike share a letter ("Part D (1)", "Part D (2)"); the names are placeholders until someone who knows the songs renames them. `rcc1` and `rcc2` use RCC Sunday's reference balance (same band, mics and board). Big songs (`rcc`, `rcc1`, `rcc2`, `gsg`) load only when opened.

## Speech

`stems/voices/pastor.m4a` is 50 seconds of our pastor's sermon mic (Lav 1, 1:13:22 into the Feb 15 service), loudness-normalized. It's private like the song stems. `stems/voices/mc.m4a` is 50 seconds of the announcements mic (MC 2, 51:36 into the same service), matched to the pastor clip's loudness (-21.7 LUFS). The synthetic voices were deleted; every speaking drill uses these two real voices. The ringing examples add only the feedback effect to the real voice.

## Hosting and sign-in

- **Live at https://rcc-training.web.app** (Firebase project **RCC Training**, `rcc-training`). Deploy with `firebase deploy --only hosting`.
- **Sign-in:** Google, or an emailed sign-in link for people without Google. `@rochesterchristian.church` accounts get in automatically. Anyone else appears on the leader's **Team progress** page (Settings) and waits for approval.
- **Leaders** are listed in three places that must match: `LEADERS` in `index.html`, `firestore.rules` and `storage.rules`.
- **Data:** `users/{uid}` holds each person's progress (merged with the device on sign-in); `approvals/{uid}` is written only by leaders.
- **Approved list:** leaders can add volunteers by email on the Team page (`invites/{email}`, lowercase). The first time an invited person signs in, the app creates their own `approvals/{uid}` (the rules allow only that). Removing someone also removes their invite.
- **Audio in Storage:** all stems and the pastor's voice are uploaded to `gs://rcc-training.firebasestorage.app` (US-EAST1) with a one-week cache header, and the bucket allows the app's sites (CORS). The storage rules read `approvals/` through the Firestore service-agent role. Re-upload with the scratch `upload.js` approach (it uses the Firebase CLI's login) and bump `AUDIO_VER` in `index.html` whenever stems change, so devices drop their saved copies.
- **Saved on the device:** audio files go into the browser's offline cache and each song's level measurements into local storage, so later visits load in seconds.
- **Budget:** a $5/month budget on the billing account emails at 50%, 90% and 100%.
- **Song stems** are kept out of public hosting (`firebase.json`) and load from Firebase Storage, which `storage.rules` limits to approved people. Storage needs the Blaze plan.
- **Local copies** (localhost or the Wi-Fi test server) skip sign-in and load stems from this folder. Add `?cloud` to the URL to test sign-in locally.

## Hands-on games (Oct 2026)
- **Set the gain** (`gainSetQ`, tool `gainset`): real channels from any loaded song. Easy starts very low or clipping; Hard is a three-channel soundcheck with Listen buttons. Graded on the true peak over the loop (raw peak + gain) against -18 to -6 dBFS.
- **Fit it in the mix** (`fitQ`, tool `volfit`): one channel's fader starts 4–14 dB off. The target fader position is random, so the number gives nothing away. Graded within 3.5 / 2.5 / 2 dB. Each channel's role (`fitRole`) is repeated in the hint and the feedback.
- **Set it in the mix** (`eqmixQ`): the band at its starting points, with one instrument flat. The feedback repeats that instrument's starting-point reasons (`eqWhy`), and so do Fix the EQ and the starting-points quiz.

## Read aloud and character voices (Oct 2026)
Settings → Read aloud. Each character reads lesson pages, questions and feedback, a piece at a time (title, paragraph, question, hint). A piece with a recording plays `tts/<hash>.m4a`, where the hash is `ttsId(who, text)`; `tts/index.json` lists the recorded ones. Anything else, like feedback with numbers worked out on the spot, uses the device's built-in voice (`CAST` in index.html). Reading stops when a clip plays.

The recordings come from **Kokoro** (open source, runs on the Mac, free). The voices the user picked are in `CAST` in `tools/tts/build.py`:
- Sona af_heart, Pip bf_lily (+2.5 semitones), Fenn am_michael, Kit bf_emma, Hugo am_fenrir.
- Bram bm_lewis, Echo am_santa, Verb am_onyx, Penny bf_isabella (−1 semitone).

To update after lesson text changes:
1. Install once: `/opt/homebrew/bin/python3.12 -m venv tools/tts/.venv && tools/tts/.venv/bin/pip install kokoro-onnx soundfile`. Put `kokoro-v1.0.onnx` and `voices-v1.0.bin` (from the kokoro-onnx GitHub release `model-files-v1.0`) in `tools/tts/models/`.
2. Run `python3 tools/tts/save_server.py tools/tts/lines.json`, then paste `tools/tts/crawl.js` into the browser console on the local app.
3. Run `tools/tts/.venv/bin/python tools/tts/build.py`. It only records new lines. Then deploy hosting.

Old files for text that no longer exists are harmless. Delete `tts/` and rebuild to clean up.

## M32 EQ in the games, and Starting points in sections (Oct 2026)
- **Fix the EQ** and **Set it in the mix** use the console's M32 channel EQ (`vM32Eq('_lesson', q.state.ch)`): Low Cut, then LOW shelf, LO MID, HI MID and HIGH shelf, each with Gain, Freq and Q, plus the draggable curve and the EQ on/off and RESET buttons. The lesson channel has the same shape as a console channel (`lessonCh()`). Grading reads any mid band through `midCut`, `midBoost` and `hiCut`. The Sunday Mix mixer uses the same M32 EQ (`eqPanel` → `vM32Eq('_mix:'+k, …)`, `mixEqSet`). Its Low Cut and the channel's HPF menu are the same setting (`m.hpf`), which the filter scoring reads. `eqSetAny` routes knobs and drags to the lesson, the mixer or the console.
- **Starting points** is split into four sections (`EQ_SECTIONS`): Drums, Bass and guitars, Keys/loops/vocals, The whole band. Each has a 4-question quick check, a hidden exercise `sp-<id>`, and needs 3 to pass. Progress saves per section, and the path shows "Starting points n/4". The old 8-question pass (`S.ex.eqstart >= 6`) still counts as done.

## Volunteer-readiness additions (Oct 18, 2026)
- **Ride the mix** (`rideQ`, tool `ride`, exercise `ride`, also in the Mixing unit). The song plays once with scripted events on a channel (`RIDE_KINDS`: solo, keys feature, singer backs off, belted chorus). The event's level change is built into the audio. It's scored on reaching the target in time (early is good), holding it, and returning. "Hear it ridden right" plays the ideal moves.
- **Stage Setup** unit (`stage`, Bram, a side unit after Foundations) with lessons, `STAGE_TEXT`, and the **Set up the stage** game (`stageQ`): mic or DI per source, +48V, and on Hard, patching by an input list.
- **Sunday Routine** unit (`routine`, Kit, a side unit at the end of The basics) with lessons, `ROUTINE_TEXT`, the **Sunday in order** game (`orderQ`), and the **Sunday checklist** screen (`vChecklist`, Practice tab). The checklist resets daily (`S.check`).
- Side units (`side:true`) don't block the path: `unitOpen` looks back to the previous main unit (`prevMain`).
- **Review** (`trackAnswer` → `S.stats[unit:level]`, `reviewPool`, `startReview`): weighted toward recent misses and skills not practiced lately.
- **Sunday-ready check** (hidden exercise `sundayready`, 12 questions, `SR_PASS` = 10) sets `S.sundayReady`.
- **Trainer sign-off**: `signoffs/{uid}` (leader write, self read) from the Team page, shown on Me.

## Your own songs (leaders) (Oct 20, 2026)
Leaders open **Team progress → Songs** (or Settings → Songs) to upload a church's own stems and to hide built-in songs from the team.
- **Add a song** (`vSongAdd`): shows the export rules, then the title, BPM and files. `analyzeStems` decodes the files at 48 kHz, checks length, silence and clipping, and guesses roles from file names (`ROLE_GUESS`, editable, including "Leave it out").
- **Building the song:** `buildSongSpec` produces everything a song needs. Channel keys come from the role (kick, snare, bass, acc, eg, keys, lv1, bgv1…), so colors, high-pass coaching and grouping all work. It also builds groups, missions (with a messy mission-2 start), windows (full band, verse, gap, from per-bar activity) and a starting balance from each stem's active level against the lead vocal (`ROLE_LVL`, capped at +10 dB).
- **Compressing and saving:** `encodeStem` compresses to AAC in an .m4a in the browser (WebCodecs plus mp4-muxer from jsDelivr, loaded only here), falling back to 16-bit WAV. Files go to Storage at `stems/custom/<id>/<k>.m4a` (leader write only, audio, < 80 MB). The song is saved to Firestore at `songs/<id>` as a `spec` JSON string, plus `rev`.
- **Loading:** `loadCustomSongs` runs after sign-in, adds those songs to the front of SONGS and reads `config/songs.hidden`. A leader's trainer-mode "make this the reference mix" on a custom song saves it to Firestore for everyone (rev bump → new calibration key).
- **Testing without signing in:** run locally (not signed in), a song works on this device until reload, using blob URLs.

## Loading (Oct 20, 2026)
- The Firebase compat scripts are `defer`red. `cloudInit` runs on DOMContentLoaded, so the first screen doesn't wait for them (about 0.3 s to the sign-in screen on a normal visit).
- `songFiles(song)` splits each song into **core** channels (loaded and decoded before "ready") and **extras**: traps (click, cues, count, smpte, crowd) and the `x_*` mic pairs. Extras load in the background (`song.extras` / `song.extrasReady`); until then those channels just play silence. The Phase unit waits for `extrasReady`.
- `prefetchFirstSong()` runs when Home renders. It downloads the first song's core files and the voices into the offline cache (no decoding), so "Loading the band…" is mostly decoding. It's skipped when Save-Data is on.
- The voices load in parallel with the first song instead of before it.
- The biggest remaining cost is audio: about 12 MB for the first song on a first visit (cached after that). Lowering the bitrate would cut it, but it would hurt what the app is training people to hear.
