// Lists every line the app can read aloud and posts it to tools/tts/save_server.py (port 8766), which writes tools/tts/lines.json.
// Run in the browser console on the local app (http://127.0.0.1:8765/Sound%20School/index.html) after the page loads.
(async()=>{
window.SS_MAX_SONGS=99;   // keep every song loaded while listing lines
await initAudio(); S.setup=true; const ra=S.readAloud; S.readAloud=false;
for(const s of LISTED().map(x=>x.id)) await withAudio(null,s);
await prepEqGuide(); A.gateOk=await ensureGate(); prepGateFix();
const lines={}, add=(who,text)=>{ if(text) lines[ttsId(who,text)]={who, text:sayable(text)}; };
const con0=S.console;
for(const c of Object.keys(CONSOLES)){ S.console=c; for(const u of UNITS) for(let i=0;i<(u.learn||[]).length;i++){ UI={screen:'learn',unit:u.id,slide:i}; render(); readable().forEach(x=>add(x.who,x.text)); } }
S.console=con0;
const combos=new Map();
for(const u of UNITS) if(GEN[u.id]) for(const l of [1,2,3]) combos.set(u.id+l, [u.id,l,{}]);
for(const x of EXERCISES) for(const pl of (x.plan||[])) combos.set(JSON.stringify(pl), [pl[0],pl[1],pl[2]||{}]);
for(const pl of PLACEMENT) combos.set(JSON.stringify(pl), [pl[0],pl[1],pl[2]||{}]);
const songs=readySongs();
for(const [,[id,l,o]] of combos){ const N=['gate','comp','gain','eqfix'].includes(id)?12:30;
  for(let k=0;k<N;k++){ const song=songs[k%songs.length];
    const q=Object.assign({song:song.id}, GEN[id](l,song,o), {unit:id, level:l});
    UI={screen:'lesson', lesson:{unit:id, level:l, n:8, i:0, qs:[q], picked:null, correct:0, seed:0}}; render(); readable().forEach(x=>add(x.who,x.text));
    if(q.explain){ UI.lesson.picked=q.answer; render(); readable().forEach(x=>add(x.who,x.text)); } } }
for(const m of POSES) ['Nice ears!','You heard it!','That\'s it!','Sharp ears!','Not quite'].forEach(h=>add(m,h));
for(const u of UNITS.filter((u,i,a)=>a.findIndex(x=>x.mascot===u.mascot)===i)) add(u.mascot, `Hi, I'm ${u.who.split(',')[0]}. ${u.id==='found'?'I\'m your guide.':`I teach ${u.title}.`}`);
add('sona','Hi! I\'ll read the lessons to you. Each of us has our own voice.');
S.readAloud=ra; window.SS_MAX_SONGS=0; go({screen:'home'});
await fetch('http://127.0.0.1:8766/save',{method:'POST',body:JSON.stringify(lines)});
console.log('Saved', Object.keys(lines).length, 'lines');
})();
