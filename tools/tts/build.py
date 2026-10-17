# Record every line the app reads aloud in each character's Kokoro voice.
#   1. In the app (local server), run the crawl that writes tools/tts/lines.json (see docs/BUILD-NOTES.md).
#   2. tools/tts/.venv/bin/python tools/tts/build.py      (only records lines that don't have a file yet)
#   3. firebase deploy --only hosting
import json, os, re, subprocess, sys, tempfile, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(D)); OUT = os.path.join(ROOT, 'tts')
# The voices the user picked (Oct 17, 2026): voice, speed, pitch shift in semitones.
CAST = {
  'sona':  ('af_heart',    1.0,   0),
  'pip':   ('bf_lily',     1.06,  2.5),
  'fenn':  ('am_michael',  1.0,   0),
  'kit':   ('bf_emma',     1.0,   0),
  'hugo':  ('am_fenrir',   0.95,  0),
  'bram':  ('bm_lewis',    1.0,   0),
  'echo':  ('am_santa',    1.08,  0),
  'verb':  ('am_onyx',     0.92,  0),
  'penny': ('bf_isabella', 1.0,  -1),
}
SKIP = re.compile(r'ringing near \d')   # random frequencies: never the same twice
lines = json.load(open(os.path.join(D, 'lines.json')))
os.makedirs(OUT, exist_ok=True)
todo = [(k, v) for k, v in lines.items() if not SKIP.search(v['text']) and not os.path.exists(os.path.join(OUT, k + '.m4a'))]
limit = int(sys.argv[1]) if len(sys.argv) > 1 else len(todo)
K = Kokoro(os.path.join(D, 'models/kokoro-v1.0.onnx'), os.path.join(D, 'models/voices-v1.0.bin'))
print(f'{len(todo)} to record', flush=True)
for n, (k, v) in enumerate(todo[:limit]):
    voice, speed, st = CAST[v['who']]
    a, sr = K.create(v['text'], voice=voice, speed=speed, lang='en-us' if voice[0] == 'a' else 'en-gb')
    a = np.asarray(a, dtype=np.float32)
    # Level: speaking parts at -20 dBFS RMS, peaks no higher than -1 dBFS.
    blk = int(0.05 * sr); e = np.array([np.mean(a[i:i+blk]**2) for i in range(0, max(1, len(a)-blk), blk)]) if len(a) > blk else np.array([np.mean(a**2)])
    loud = np.sort(e)[int(len(e) * 0.3):]; rms = np.sqrt(np.mean(loud) + 1e-12)
    g = min(10 ** (-20 / 20) / rms, 10 ** (-1 / 20) / (np.max(np.abs(a)) + 1e-9)); a = a * g
    with tempfile.TemporaryDirectory() as td:
        w = os.path.join(td, 'a.wav'); sf.write(w, a, sr)
        af = 'afade=t=in:d=0.01'
        if st: r = 2 ** (st / 12); af = f'asetrate={sr}*{r:.5f},aresample={sr},atempo={1/r:.5f},' + af
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', w, '-af', af, '-ac', '1', '-c:a', 'aac_at', '-b:a', '48k', os.path.join(OUT, k + '.m4a')], check=True)
    if n % 25 == 0: print(f'{n+1}/{len(todo)}', flush=True)
have = sorted(f[:-4] for f in os.listdir(OUT) if f.endswith('.m4a'))
json.dump(have, open(os.path.join(OUT, 'index.json'), 'w'))
print('done,', len(have), 'recorded lines', flush=True)
