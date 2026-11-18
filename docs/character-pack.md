# Make a native-atlas character pack

The current development kit can **lint, preview and import a local native-atlas
folder**. Validation/preview leave installed entries alone. Explicit import adds
a new entry to the current profile; selecting it remains a separate action.
This is the draft native-atlas subset. The unreleased Desktop preview can use an
[installed pack for one bot](#assign-an-installed-pack-to-a-bot) on compatible
gateways. Extended interaction events remain open.

## Start with the original example

Use a Hermes Python environment with Pillow and this source patch applied:

```sh
python examples/character-pack/make_example.py ./lanternling
hermes pets validate ./lanternling
hermes pets show --pack ./lanternling --cycle --once
```

The output folder must be new. The generator creates the complete original
**Lanternling** demonstration atlas and manifest, with every native row filled.
Its geometric art and manifest are offered under CC0-1.0; no external character
art or model call is used. The example is generated from the shipped Python
recipe rather than distributing a binary image in the source kit.

For your own art, copy
[blank-manifest.json](../examples/character-pack/blank-manifest.json) as
`manifest.json`, fill the three empty text fields and add your atlas. The blank
template intentionally fails validation until you supply those fields and art.

## Create with a Hermes agent

The [character-pack-creator skill](../skills/character-pack-creator/SKILL.md)
guides a description or permitted reference image through state planning,
original/owned frames, exact local atlas assembly, lint and terminal preview.
It uses the existing composer and pets commands; it adds no image provider,
dependency or runtime setting. It can be copied alone into the intended
profile's native skills directory (for example, its
`skills/creative/character-pack-creator/SKILL.md`). Preserve any existing copy;
installing a skill is separate from importing or selecting a character.

Once available to that profile, ask the agent: "Use character-pack-creator to
make an original lantern gardener in a new folder; preview it, without importing
or selecting it." Supply the author and actual permission/licence terms for
your art. The skill records provenance in `creator-notes.md`; lint cannot prove
that statement. An authorized image tool is optional; original programmatic art
or your own frames also work. It preserves existing import authorization without
treating a creation-only request as permission to install or change selection.

The one-file copy includes the supported geometry/manifest and native composer
recipe. Its installed native discovery/read, embedded recipe and isolated CLI
workflow are checked. This is deterministic tooling evidence, not proof that an
artist agent or image model will produce good art or obey every instruction.
Extended formats and events remain future work.

## Folder contract, schema 1

```text
my-character/
  manifest.json
  spritesheet.png       # or spritesheet.webp
```

```json
{
  "schema_version": 1,
  "format": "hermes-native-atlas",
  "name": "My character",
  "author": "Your name",
  "licence": "Your art's licence or permission terms",
  "spritesheet": "spritesheet.png",
  "motion_weight": "standard"
}
```

`motion_weight` is optional. The other six fields are required.
Name, author and licence must each be
1–160 printable characters with nonblank content; Unicode names are supported.
The licence text records your statement; lint cannot prove ownership or legal
permission. Use original art or art you have permission to adapt/distribute.
Duplicate keys, other schema versions and unknown fields fail validation.

For an assigned Mac desktop character, set `motion_weight` to `light`,
`standard` or `heavy`. Light pets walk faster and take a longer, higher
bounce. Heavy pets walk slower, squash harder on impact and rebound less.
Omit the field for standard movement or compatibility with older pack installers.

On the Mac desktop, a newly completed worker can play this pack's jumping
row once after landing, then return to waving. Fill the jumping row to
give the finished worker a custom celebration. Missing jumping frames
keep the wave, and Reduce Motion keeps the resting pose. The completed
pet still opens its saved report.

The manifest is UTF-8 (an optional BOM is accepted), at most 64 KiB. The asset
must have the exact filename `spritesheet.png` or `spritesheet.webp` beside it,
be a regular static PNG/WebP and at most 16 MiB. URLs, nested asset paths,
traversal, symlinks in directory/file paths and special files are refused.
Pack reads use bounded file snapshots and check opened file identity. Other
folder contents are not inspected or executed; this is not an archive scanner
or a safe installer for hostile concurrent directory changes.

## Draw and export the sheet

1. Draw your own character on transparent **192 × 208 px** cells. Keep it large
   enough to read, with a consistent baseline and scale across poses.
2. Draw a short sequence for each row below. Put frames left to right without
   gaps; leave unused cells fully transparent. Do not hide another pose inside
   one cell.
3. Export the entire **1536 × 1872 px** sheet as static PNG or lossless WebP.
   For a bot character on Desktop, keep the sheet at or below **4 MiB**.
   Animated GIF/APNG/WebP, Lottie and legacy eight-row sheets are outside this
   folder contract. Renaming another format to `.png` does not enable it.
4. Fill the manifest with your name and actual permission/licence statement.
5. Run `hermes pets validate ./my-character`. Fix errors before sharing it.
   To check an image alone, use `hermes pets validate ./my-character/spritesheet.png`.
6. In a terminal, run `hermes pets show --pack ./my-character --cycle --once`
   to preview all seven current activity states. Use `--state run --once` for
   one state; explicit `--state` takes priority over `--cycle`. Without either,
   preview uses idle; omit `--once` to loop until Ctrl+C. Use `--mode unicode`
   if needed. Inspect both directional walk rows separately in the source
   frames or the atlas.
7. When ready, import under a new slug as described below. Existing **installed**
   pets keep `hermes pets show <slug> --cycle --once`; do not combine a slug with
   `--pack`.

| Row, from top | Native atlas name | Generator cells | Existing activity alias |
|---|---|---:|---|
| 0 | idle | 6 | idle |
| 1 | running-right | 8 | walk right |
| 2 | running-left | 8 | walk left |
| 3 | waving | 4 | wave |
| 4 | jumping | 5 | jump |
| 5 | failed | 8 | failed |
| 6 | waiting | 6 | waiting |
| 7 | running | 6 | run/work |
| 8 | review | 6 | review |

These are the existing generator rows, not new event mappings. Some renderers
limit how many physical columns they use. Missing rows produce warnings; packs
must contain a populated idle row. A warning does not establish that a missing
activity will look correct: fill the native rows before seeking visual acceptance.
The shared validator also reports empty atlases, undersized/collapsed poses,
multi-pose outliers and invisible pixels retaining RGB colour.

### Using generated art

1. Ask an authorized image tool for one original character in several poses on
   a transparent background. Keep the same colors, scale and distinguishing
   features across poses. Ask for generous empty space between them.
2. Open the source over a colored backdrop to check its alpha. Crop one pose
   at a time so nearby poses and marks stay out of the cell. Size the poses
   together and align their feet, wheels or base to the same baseline.
3. Export **192 × 208 px** RGBA frames and assemble them with the
   [creator skill's recipe](../skills/character-pack-creator/SKILL.md#assemble-and-describe-the-folder).
   Check the first and last frames of each loop together. Use a new pack
   folder and keep the generated source, prompt and permission terms with it.
4. Check the finished sheet against the **4 MiB** Desktop limit, run lint
   and terminal preview, then import into the intended bot profile. Check
   the result in Monitor at the size people will see on the desktop.

For a celebration, give the five jumping cells distinct poses. Start with a
crouch, stretch into takeoff, tuck at the peak, extend on descent and settle
back to the original baseline. Use one art scale across the set so movement
comes from the drawings and their vertical offsets. When revising an existing
pack, compare the decoded pixels in every untouched cell, including the unused
cells, and import the revision under a new slug.

![Moon Jelly crouching, taking off, cheering in the air, descending and settling in five transparent sprite cells](images/moon-jelly-celebration-frames.webp)

For a failed worker, use the eight cells in the failed row. Give the last
cell a clear resting pose for reduced motion and saved reports. A fresh
failure plays the row once when the character lands. The final pose still
opens the saved report.

![Eight Moon Jelly poses showing a dropped parcel, a soft stumble and a quiet recovery](images/moon-jelly-failure-frames.webp)

For a bot waiting for an answer, use six cells that loop smoothly. Keep the
supporting foot in the same place while the other foot lifts and taps. Play
two loops at desktop size to check the seam. Hermes supplies the
“Needs your answer” label live.

![Six Puddle Frog waiting poses with a planted foot, a foot tap and a blink](images/puddle-frog-waiting-frames.webp)

## Preview without adopting the pack

`show --pack` uses the exact bytes that passed validation, copied into a private
bounded temporary snapshot. It uses the supplied pack directly and leaves pet
settings unchanged. The temporary snapshot lasts through rendering and is removed on
normal exit, Ctrl+C or a handled error. Pack/source bytes stay unchanged.
The existing terminal graphics detection and default scale apply; `--scale`
can override the preview size. No TTY means a clear refusal with exit 1.

Lint permits missing rows with warnings. Preview reports an error before drawing
if a requested state has no frames: fill that row or request a populated state.
Previewing the native atlas does not implement the future interaction events,
select a bot character or prove its Desktop appearance/CPU/RAM budget.

## Import into the current profile

Choose an unused slug with 1–64 lowercase ASCII letters, digits and single
hyphens, such as `my-character`:

```sh
hermes pets import ./my-character my-character
hermes pets list --installed
hermes pets show my-character --cycle --once
```

Import copies the exact validated image and keeps creator name/author/licence
in `manifest.json` beside normal `pet.json` metadata. Extra source files and
scripts are not copied or executed. The original folder stays unchanged.
Current selection and settings stay unchanged; make it active only when you
choose, with `hermes pets select my-character`. This sets the global pet.
To remove the imported copy,
select another pet or turn display off first, then use
`hermes pets remove my-character`; the original creator folder remains.

A file, directory (including an empty one) or symlink at the chosen slug makes
import fail. There is no force/overwrite option. Complete files are staged in a
private container and published together using a native no-replace operation;
existing readers do not expose the unfinished payload. Unsupported atomic
operations fail instead of using an overwriting fallback. The imported directory
is private to its owner on the tested Mac path.

Write/publication failures discard only the task's staging container. If staging
cleanup itself fails, a warning identifies it; a completed import stays successful
and an earlier failure is preserved. An abrupt process/power loss may leave an
unfinished private staging directory: atomic visibility is not a crash-durability
or recovery guarantee. Do not treat unknown staging folders as safe to delete.
Store parent paths must remain trusted/stable during import.

The native acceptance here is macOS. Linux/Windows implementations use their
native no-replace contracts but have not been run in this Mac-only round.
This does not install a new Hermes.app build or prove the character overlay.

## Assign an installed pack to a bot

Import into the bot's own Hermes profile. Each profile's picker lists packs
installed there. Replace `BOT` with that profile's name.

```sh
hermes --profile BOT pets import ./my-character my-character
hermes --profile BOT pets list --installed
```

In the Desktop Bots workspace, open the bot's **Edit profile → Character** section,
choose the installed pack, and save. **Use default** clears the assignment.
Open **Monitor → Show bot characters** to see the selected sprite on the bot
and its workers when activity is present. Monitor shows five characters by
default. Choose **Include a sixth character** when you want to see six.
Active bots take the available slots before individual workers.
An assigned pack must be a readable static native PNG/WebP atlas at most 4 MiB
and 3 million pixels to appear in the preview. If the pack is unavailable,
choose another installed pack or clear the assignment.

The installed-only list makes no Petdex request. The Local Desktop dispatch
test covers own-profile and shared-host reads, assignment, clearing, and stale
saves.

## Read the result

Success prints the pack name, author, licence, dimensions and populated rows.
Warnings alone return exit **0**; errors return **1**, including unreadable files
or metadata. Validation does not install a pet, select a profile, change settings,
start a model or fetch an asset.

FPS, anchor/footprint, custom per-event mappings, sounds, ZIP import, and
GIF/APNG/Lottie decoding are future parts of the full format. Existing native
geometry and animation scheduling remain in control. Visual behavior and the
five-character CPU/RAM budget need separate acceptance.
