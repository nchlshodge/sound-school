# Sound School character bible

Nine animal teachers, one shared style. Use this guide whenever you make new art (new poses, moods, icons, scenes) so every image looks like it came from the same set.

The source of truth is the art in `img/`: `m-<id>-<mood>.webp`. When an image tool accepts a reference picture, **always attach that character's `m-<id>-happy.webp`**. A reference picture keeps a character on-model far better than any description.

---

## 1. The shared style (every character)

- **Look:** a soft, rounded 3D-style children's cartoon, like a modern animated film character rendered as a sticker. The shading is smooth and gentle, with a light fur or feather texture. There are no hard black outlines.
- **Proportions:** chibi. The head is very large, about 45% of total height. The bodies are small and rounded, with short limbs.
- **Eyes:** big, glossy, dark brown to black, each with two white highlights (a large one upper-left and a small one lower-right). There are friendly eyebrows just above.
- **Face:** a soft pink blush on both cheeks. The mouth is open and smiling in most moods, with a pink tongue and a few small teeth.
- **Hands and feet:** small paws, wings or feet in a darker tone than the body.
- **Framing:** the whole body is in view, centered, facing the viewer or at a slight three-quarter angle, on a **transparent background** with no ground shadow.
- **Mood:** warm, encouraging, never scary or sarcastic. These are friendly teachers for nervous beginners.

**Style line to paste into any prompt:**
> Cute 3D-style children's cartoon character, soft rounded shapes, chibi proportions with a very large head, big glossy dark eyes with two white highlights, rosy pink blush cheeks, friendly open smile, smooth soft shading with subtle fur texture, no outlines, full body, centered, isolated on a transparent background, no shadow, no text.

**Never:** an owl (too close to Duolingo), realistic animals, sharp teeth or angry faces, text or logos on the character, extra characters in a single-character image, or changes to a character's colors, accessories or species.

---

## 2. Technical specs for app art

| | |
|---|---|
| Size | 256 × 256 px in the app (`.webp` with transparency). Keep a 1024 × 1024 PNG master if you can. |
| Placement | The character fills about 90% of the square, centered, with a little room at the edges. |
| File names | `img/m-<id>-<mood>.webp`, with `<id>` from the table below |
| Moods the app uses | `happy`, `celebrating`, `thinking`, `encouraging`, `surprised`, `sleeping` |

The moods appear in these moments:
- **happy:** introductions and the default.
- **celebrating:** a right answer or a finished level. Arms up, eyes squeezed shut with joy, confetti optional.
- **thinking:** an open question. A paw or wing to the chin, looking up and to the side, mouth closed or small.
- **encouraging:** a wrong answer. A gentle smile, thumbs up or one paw raised, kind eyes.
- **surprised:** a mistake or a clipping warning. Wide eyes, small "o" mouth, paws raised.
- **sleeping:** idle or a break. Eyes closed, small smile, a "z" is fine in this mood only.

---

## 3. The cast

| id | Name | Teaches | Voice (Read aloud, Kokoro) |
|---|---|---|---|
| sona | Sona the bat | Foundations, Mixing (the guide) | af_heart |
| pip | Pip the mouse | Gain Staging, Volume | bf_lily, +2.5 semitones |
| fenn | Fenn the fennec fox | EQ | am_michael |
| kit | Kit the meerkat | Gates | bf_emma |
| hugo | Hugo the koala | Compression | am_fenrir |
| bram | Bram the beaver | Limiters | bm_lewis |
| echo | Echo the parrot | Delay | am_santa |
| verb | Verb the whale | Reverb | am_onyx |
| penny | Penny the pigeon | Livestream | bf_isabella, −1 semitone |

Each character below has: the signature features that must never change, the palette (sampled from the app art), personality, and two ready-made prompts. One prompt is for use **with** the reference image and one is for when you can only use text.

To make a new mood, replace `[MOOD]` in a prompt with a line from section 2. For example: "celebrating: both arms raised, eyes squeezed shut with joy."

---

### Sona the bat (`sona`), the guide

- **Signature features:** charcoal plum-gray fur. Two very large, pointed ears with **pink** inner ears. Wide **pink, membrane wings** with darker plum finger-bones, usually spread open like arms. A cream fluffy chest patch. A tiny dark button nose and two small fangs in an open smile. Short legs with dark feet.
- **Palette:** fur #563844 / #391A22, wing and ear pink #EE9393 / #C66E79, wing bones #8C505E, chest #F4D2C6.
- **Personality:** warm, calm and welcoming. The teacher who makes you feel you can do this. Bats navigate by ear, which is the whole point of Sound School.
- **Props (optional):** studio headphones (dark gray with a purple accent, the app color #3F3399).
- **With reference:** "Using the attached image of Sona the bat as the exact character reference, keep Sona's face, colors, pink ears and pink wings, proportions and style identical. Show Sona [MOOD]. Full body, centered, transparent background, no shadow, no text."
- **Text only:** "Sona, a cute charcoal plum-gray cartoon bat with very large pointed ears with pink insides, wide pink membrane wings with darker plum wing bones spread open, a cream fluffy chest, big glossy dark brown eyes, rosy cheeks, two tiny fangs in a happy open smile, [MOOD]. " + style line.

### Pip the mouse (`pip`)

- **Signature features:** light warm-gray fur. **Huge round ears** with pink insides. A pink triangular nose and pink paws and feet. A long, thin **pink tail** curling to one side. A cream belly. Small and quick, the smallest of the cast.
- **Palette:** fur #C7AEA8 / #B28D89, pink #F68E89 / #F5ACA3, belly #F9E8DE.
- **Personality:** careful, bright and detail-minded. Pip is all about small moves making a big difference (1 dB, a touch of gain).
- **Props (optional):** a tiny VU meter or a small gain knob.
- **With reference:** "Using the attached image of Pip the mouse as the exact character reference, keep Pip's face, huge round pink-lined ears, pink tail, colors and proportions identical. Show Pip [MOOD]. Full body, centered, transparent background, no shadow, no text."
- **Text only:** "Pip, a small cute light warm-gray cartoon mouse with huge round ears with pink insides, a pink nose, pink paws and feet, a long thin pink tail, a cream belly, big glossy dark eyes, rosy cheeks, a happy open smile, [MOOD]. " + style line.

### Fenn the fennec fox (`fenn`)

- **Signature features:** bright orange fur. **Very tall, pointed ears** with cream insides and dark brown tips. A **green scarf** knotted at the neck (the signature accessory, always there). A cream muzzle and chest. A big fluffy orange tail with a **white tip**. Dark brown paws and feet. A confident fist-pump pose.
- **Palette:** orange #F57419 / #F8A451, dark brown #752A09, cream #F9D5B4 / #FBEDD6, scarf green about #4CAF50.
- **Personality:** curious, sharp-eared and a little proud of those ears. Fenn hears every frequency and loves explaining why an EQ move helps the mix.
- **Props (optional):** an EQ curve or a frequency slider.
- **With reference:** "Using the attached image of Fenn the fennec fox as the exact character reference, keep Fenn's face, tall ears, green scarf, white-tipped tail, colors and proportions identical. Show Fenn [MOOD]. Full body, centered, transparent background, no shadow, no text."
- **Text only:** "Fenn, a cute bright orange cartoon fennec fox with very tall pointed ears with cream insides and dark tips, a green scarf knotted at the neck, a cream muzzle and chest, a fluffy orange tail with a white tip, dark brown paws, big glossy dark eyes, rosy cheeks, a happy open smile, [MOOD]. " + style line.

### Kit the meerkat (`kit`)

- **Signature features:** golden-orange fur with a pale cream belly. **Dark brown eye patches** around big eyes. A small brown **tuft of hair** on top of the head. Small round ears, dark brown hands and feet. A thin tail with a dark tip. Stands upright and alert, often with both arms waving.
- **Palette:** orange #E6792B / #FAA448, dark brown #56220E, mid brown #A75323, belly #FBEFD4.
- **Personality:** watchful and quick, the lookout. Kit stands guard and only lets the good sound through (gates).
- **Props (optional):** a small gate or a "lookout" stance with a paw shading the eyes.
- **With reference:** "Using the attached image of Kit the meerkat as the exact character reference, keep Kit's face, dark eye patches, head tuft, colors and proportions identical. Show Kit [MOOD]. Full body, centered, transparent background, no shadow, no text."
- **Text only:** "Kit, a cute golden-orange cartoon meerkat standing upright, with dark brown patches around big glossy eyes, a small brown tuft of hair on top of the head, small round ears, a pale cream belly, dark brown hands and feet, a thin tail with a dark tip, rosy cheeks, a happy open smile, [MOOD]. " + style line.

### Hugo the koala (`hugo`)

- **Signature features:** soft lavender-gray fur. **Big fluffy round ears** with white fluff and pink insides. A **large dark oval nose**. A white chest and tummy, and round dark-brown paw pads on hands and feet. A chunky, soft, round body, usually **sitting** with arms open.
- **Palette:** gray #B199A3 / #D9C5CA, paw pads #70464E, ear pink #DEABB2, white #FBF0EC.
- **Personality:** laid-back, even-keeled and steady. Nothing rattles Hugo, which is what a compressor does: smooths out the ups and downs.
- **Props (optional):** a eucalyptus branch, or a gain-reduction meter.
- **With reference:** "Using the attached image of Hugo the koala as the exact character reference, keep Hugo's face, big fluffy ears, large dark nose, colors and sitting proportions identical. Show Hugo [MOOD]. Full body, centered, transparent background, no shadow, no text."
- **Text only:** "Hugo, a cute chunky lavender-gray cartoon koala, with big fluffy round ears with white fluff and pink insides, a large dark oval nose, a white chest and tummy, round dark brown paw pads, big glossy dark eyes, rosy cheeks, a happy open smile, sitting, [MOOD]. " + style line.

### Bram the beaver (`bram`)

- **Signature features:** warm chestnut-brown fur with a lighter tan muzzle and belly. **Two big white front teeth**. Small round ears and a dark nose. A **flat dark-brown paddle tail**. Arms often **crossed** confidently. A sturdy stance.
- **Palette:** brown #A36039 / #B66B40, dark #512C1C, tail #814121, muzzle #E2AA7E.
- **Personality:** dependable, practical, protective. Bram builds the dam so nothing floods the speakers (limiters).
- **Props (optional):** a small log or a tiny dam, or a hard hat for "builder" moments.
- **With reference:** "Using the attached image of Bram the beaver as the exact character reference, keep Bram's face, big front teeth, flat dark tail, colors and proportions identical. Show Bram [MOOD]. Full body, centered, transparent background, no shadow, no text."
- **Text only:** "Bram, a cute sturdy chestnut-brown cartoon beaver with a tan muzzle and belly, two big white front teeth, small round ears, a dark nose, a flat dark-brown paddle tail, big glossy dark eyes, rosy cheeks, a confident happy smile, [MOOD]. " + style line.

### Echo the parrot (`echo`)

- **Signature features:** a **blue-and-gold macaw**: bright blue head crest, back, wings and tail, with a golden-yellow chest and belly. A **large curved dark-gray beak**. A white face patch around the eye. Gray feet, usually **perched on a small wooden T-perch**.
- **Palette:** blue #357AD5 / #194FAC, gold #EFBC3F / #F7DB84, beak #5A3930, perch #825A45.
- **Personality:** chatty, playful, fun. Echo repeats what it hears ("I repeat what I hear. I repeat what I hear."), which is exactly what a delay does.
- **Props (optional):** the wooden perch (default), or sound-wave rings that get smaller to show repeats.
- **With reference:** "Using the attached image of Echo the parrot as the exact character reference, keep Echo's face, blue and gold feathers, curved dark beak, colors and proportions identical. Show Echo [MOOD]. Full body, centered, transparent background, no shadow, no text."
- **Text only:** "Echo, a cute cartoon blue-and-gold macaw parrot with a bright blue head crest, wings and tail, a golden-yellow chest, a large curved dark-gray beak, a white face patch, big glossy dark eyes, rosy cheeks, a happy open beak smile, perched on a small wooden T-perch, [MOOD]. " + style line.

### Verb the whale (`verb`)

- **Signature features:** a round, plump **periwinkle-blue whale** with a lighter lavender-white belly. A small **water spout** of two or three blue droplets on top. A tail fluke raised behind. A small side fin. Big gentle eyes with a soft smile. It floats with no legs, and the body is wider than it is tall.
- **Palette:** blue #5464E4 / #4C54CD, deep #3341B2, belly #DDD5EA, spout #5076E9.
- **Personality:** gentle, spacious, unhurried. Verb fills a room the way whale song fills the ocean (reverb). Speaks slowly and warmly.
- **Props (optional):** soft ripple rings or bubbles around the body.
- **Note:** the current app art is cropped on the right edge. A new master should show the whole whale inside the frame.
- **With reference:** "Using the attached image of Verb the whale as the exact character reference, keep Verb's face, round blue body, light belly, water spout, colors and proportions identical, and show the whole whale fully inside the frame. Show Verb [MOOD]. Centered, transparent background, no shadow, no text."
- **Text only:** "Verb, a cute round plump periwinkle-blue cartoon whale with a light lavender-white belly, a small water spout of blue droplets on top, a raised tail fluke, a small side fin, big gentle glossy eyes, rosy cheeks, a soft happy smile, floating, whole body fully inside the frame, [MOOD]. " + style line.

### Penny the pigeon (`penny`)

- **Signature features:** soft gray feathers with darker gray wing bars. An **iridescent teal-green neck band**. A gray head with a short dark beak. Coral-pink feet. A **yellow messenger bag** worn across the body with a white **play-button triangle** on the flap (the livestream).
- **Palette:** gray #ABA5A9 / #6B7A87, dark #594244, neck #659E9C, bag #E8A93C, feet coral.
- **Personality:** friendly, reliable, always on time. Penny carries your mix to everyone watching from home (the livestream).
- **Props (optional):** the messenger bag (always), a phone, a little "LIVE" dot. Keep it as a red dot only, with no text.
- **With reference:** "Using the attached image of Penny the pigeon as the exact character reference, keep Penny's face, gray and teal feathers, yellow messenger bag with the play triangle, colors and proportions identical. Show Penny [MOOD]. Full body, centered, transparent background, no shadow, no text."
- **Text only:** "Penny, a cute cartoon pigeon with soft gray feathers, darker gray wing bars, an iridescent teal-green neck band, a short dark beak, coral-pink feet, wearing a yellow messenger bag across the body with a white play-button triangle on the flap, big glossy dark eyes, rosy cheeks, a happy smile, [MOOD]. " + style line.

---

## 4. Group shots (the team picture)

Group images drift the most. Keep them consistent this way:
- Attach `img/team.webp` (the current team picture) plus the happy pose of each character you want to fix.
- Name every character with its key features in one sentence each, left to right. Image models lose track of pronouns.
- Say what stays the same: "keep every character's face, colors and accessories identical to the references".

**Prompt:** "A friendly group picture of nine cute 3D-style cartoon animal teachers standing together in a row, the same style as the attached references: from left to right, Pip the light-gray mouse with huge pink-lined ears; Kit the golden-orange meerkat with dark eye patches; Fenn the orange fennec fox with a green scarf; Sona the charcoal bat with pink ears and wings spread, in the center; Hugo the lavender-gray koala, sitting; Bram the chestnut beaver with big front teeth; Echo the blue-and-gold macaw on a wooden perch; Penny the gray pigeon with a teal neck and a yellow messenger bag; and Verb the round periwinkle-blue whale with a water spout. Everyone smiling at the viewer, soft even lighting, transparent background, no text."

---

## 5. Workflow tips

1. **Reference first.** Attach the character's happy pose and describe only what changes (the mood or a prop). Say what stays the same.
2. **One change at a time.** Change the pose first, then add a prop in a second edit.
3. **Check against this page.** Compare the result with the signature features list. A missing scarf, the wrong tail color or a changed eye style means regenerate.
4. **Finish for the app.** Remove the background so it's transparent, center the character with a little room at the edges, then export 256 × 256 `.webp` into `img/` with the right name.
