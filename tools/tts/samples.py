# Make a voice-audition page: each character introduces themselves in two candidate Kokoro voices.
#   tools/tts/.venv/bin/python tools/tts/samples.py
import os, soundfile as sf
from kokoro_onnx import Kokoro
D = os.path.dirname(os.path.abspath(__file__))
K = Kokoro(os.path.join(D, 'models/kokoro-v1.0.onnx'), os.path.join(D, 'models/voices-v1.0.bin'))
# character: (name, role line, [(voice, speed), ...])
# character: (name, role line, [(voice, speed, semitones), ...])  semitones shifts the pitch after Kokoro (keeps the timing)
CAST = {
  'sona':  ('Sona the bat',     "I'm your guide. Bats find their way with their ears, and that's what you'll learn here.", [('af_heart',1.0,0), ('bf_alice',0.98,0), ('af_river',0.97,0)]),
  'pip':   ('Pip the mouse',    "I teach gain and volume. Small moves make a big difference.",                            [('af_sky',1.08,3), ('bf_lily',1.06,2.5), ('am_puck',1.08,4)]),
  'echo':  ('Echo the parrot',  "I teach delay. I repeat what I hear. I repeat what I hear.",                              [('am_santa',1.08,0), ('am_adam',1.06,0), ('bm_daniel',1.08,0)]),
  'penny': ('Penny the pigeon', "I teach the livestream. I carry your mix to everyone watching from home.",               [('af_jessica',1.0,0), ('af_nova',1.0,0), ('bf_isabella',1.0,-1)]),
}
out = os.path.join(D, 'samples', 'round2'); os.makedirs(out, exist_ok=True)
import subprocess
rows = []
for cid, (name, line, opts) in CAST.items():
    text = f"Hi, I'm {name}. {line} Aim for peaks around minus eighteen to minus six D B F S, and high-pass the vocal around two hundred hertz."
    cells = []
    for i, (v, sp, st) in enumerate(opts):
        a, sr = K.create(text, voice=v, speed=sp, lang='en-us' if v[0]=='a' else 'en-gb')
        f = f'{cid}-{v}{"-up"+str(st) if st else ""}.wav'; path=os.path.join(out, f); sf.write(path, a, sr)
        if st:   # pitch shift: play faster (higher), then stretch back to the same length
            r=2**(st/12); tmp=path+'.tmp.wav'
            subprocess.run(['ffmpeg','-v','error','-y','-i',path,'-af',f'asetrate={sr}*{r:.5f},aresample={sr},atempo={1/r:.5f}',tmp],check=True); os.replace(tmp,path)
        cells.append(f'<div><b>Option {"ABC"[i]}</b> <small>{v}{f" (pitch +{st})" if st>0 else f" (pitch {st})" if st else ""}</small><audio controls preload="none" src="{f}"></audio></div>')
    rows.append(f'<section><h2>{name}</h2><div class="opts">{"".join(cells)}</div></section>')
    print(name, 'done', flush=True)
open(os.path.join(out, 'index.html'), 'w').write('''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Character voices</title><style>body{font:16px system-ui;max-width:720px;margin:24px auto;padding:0 16px;background:#fafaf7;color:#1e2235}
h1{font-size:24px}h2{font-size:18px;margin:22px 0 8px}.opts{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.opts div{background:#fff;border:1px solid #ddd;border-radius:12px;padding:10px}small{color:#777}audio{width:100%;margin-top:6px}
@media(max-width:560px){.opts{grid-template-columns:1fr}}</style>
<h1>Character voices, round 2</h1><p>Already chosen: Fenn am_michael, Hugo am_fenrir, Bram bm_lewis, Kit bf_emma, Verb am_onyx. Pick A, B or C for each of these.</p>''' + ''.join(rows))
