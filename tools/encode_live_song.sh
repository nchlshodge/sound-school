#!/usr/bin/env bash
# Cut and encode a live multitrack (one WAV per mic) into Sound School's console channels.
#
# Usage: tools/encode_live_song.sh <song-id> <source-folder> <start-seconds> <duration-seconds>
#   start = time of the song's first click + (first bar × seconds per bar)
#   e.g.  tools/encode_live_song.sh lhc "$HOME/Downloads/Let's Have Church" 17.938 56.471
#
# Track names below match the "Let's Have Church" / "I'm So Glad I Met Jesus" sessions.
# Edit them to match a new session. Needs ffmpeg.
set -euo pipefail
ID=$1; SRC=$2; START=$3; DUR=$4
OUT="$(dirname "$0")/../stems/$ID"; mkdir -p "$OUT"

mono(){ # out, bitrate, files... (summed)
  local out=$1 br=$2; shift 2; local args=() n=0
  for f in "$@"; do args+=(-ss "$START" -t "$DUR" -i "$SRC/$f.wav"); n=$((n+1)); done
  if [ $n -eq 1 ]; then ffmpeg -v error -y "${args[@]}" -ar 48000 -ac 1 -c:a aac -b:a "$br" "$OUT/$out.m4a"
  else ffmpeg -v error -y "${args[@]}" -filter_complex "amix=inputs=$n:normalize=0" -ar 48000 -ac 1 -c:a aac -b:a "$br" "$OUT/$out.m4a"; fi
}
stereo(){ # out, left file, right file
  ffmpeg -v error -y -ss "$START" -t "$DUR" -i "$SRC/$2.wav" -ss "$START" -t "$DUR" -i "$SRC/$3.wav" \
    -filter_complex "join=inputs=2:channel_layout=stereo" -c:a aac -b:a 96k "$OUT/$1.m4a"
}

# Kick: Kick In + Kick Out with Kick Out's polarity flipped (they cancel otherwise; measured +2.7 dB).
ffmpeg -v error -y -ss "$START" -t "$DUR" -i "$SRC/Kick In.wav" -ss "$START" -t "$DUR" -i "$SRC/Kick Out.wav" \
  -filter_complex "[1]volume=-1[o];[0][o]amix=inputs=2:normalize=0" -ar 48000 -ac 1 -c:a aac -b:a 56k "$OUT/kick.m4a"
mono snare 56k "Snare 1 Top" "Snare Top 2"; mono toms 56k "Tom 1" "Tom 2"; mono hat 56k "Hat"
stereo oh "OH L" "OH R"; mono bass 56k "Bass" "Bass Dirty"; mono acc 56k "ACC 1"
stereo gtr1 "GTR 1 L" "GTR 1 R"; stereo gtr2 "GTR 2 L" "GTR 2 R"; stereo keys "Keys 1 L" "Keys 1 R"
for v in "Melinda Watts:melinda" "Corbin Phillips:corbin" "Taylor Gall:taylor"; do mono "${v##*:}" 64k "${v%%:*}"; done
# Chloe's file name differs between sessions ("Chloe Gall" / "CHLOE GALL").
if [ -f "$SRC/Chloe Gall.wav" ]; then mono chloe 64k "Chloe Gall"; else mono chloe 64k "CHLOE GALL"; fi
mono click 32k "Click"; mono count 32k "Count"; mono smpte 32k "SMPTE"

# B3: low rotor into both sides.
ffmpeg -v error -y -ss "$START" -t "$DUR" -i "$SRC/B3 Top L.wav" -ss "$START" -t "$DUR" -i "$SRC/B3 Top R.wav" -ss "$START" -t "$DUR" -i "$SRC/B3 Low.wav" \
  -filter_complex "[2]asplit[l2][r2];[0][l2]amix=inputs=2:normalize=0[L];[1][r2]amix=inputs=2:normalize=0[R];[L][R]join=inputs=2:channel_layout=stereo" -c:a aac -b:a 96k "$OUT/b3.m4a"
# Tracks: synth, gang and percussion loops (add "Loops Sub" if it has content in the section).
ARGS=(); for f in "Loops Synths L" "Loops Gang L" "Loops Perc L" "Loops Synth R" "Loops Gang R" "Loops Perc R"; do ARGS+=(-ss "$START" -t "$DUR" -i "$SRC/$f.wav"); done
ffmpeg -v error -y "${ARGS[@]}" -filter_complex "[0][1][2]amix=inputs=3:normalize=0[L];[3][4][5]amix=inputs=3:normalize=0[R];[L][R]join=inputs=2:channel_layout=stereo" -c:a aac -b:a 96k "$OUT/tracks.m4a"
# Crowd mics: four pairs.
ARGS=(); for s in L R; do for i in 1 2 3 4; do ARGS+=(-ss "$START" -t "$DUR" -i "$SRC/Crowds $i $s.wav"); done; done
ffmpeg -v error -y "${ARGS[@]}" -filter_complex "[0][1][2][3]amix=inputs=4:normalize=0[L];[4][5][6][7]amix=inputs=4:normalize=0[R];[L][R]join=inputs=2:channel_layout=stereo" -c:a aac -b:a 64k "$OUT/crowd.m4a"

# Separate mics for the Phase & Polarity drills.
for pair in "Kick In:x_kick_in" "Kick Out:x_kick_out" "Snare 1 Top:x_sn_top" "Snare 1 Bott:x_sn_bot" "Bass:x_bass_di" "Bass Dirty:x_bass_amp"; do
  ffmpeg -v error -y -ss "$START" -t "$DUR" -i "$SRC/${pair%%:*}.wav" -ar 48000 -ac 1 -c:a aac -b:a 56k "$OUT/${pair##*:}.m4a"
done
echo "Encoded $(ls "$OUT" | wc -l | tr -d ' ') files into $OUT"
