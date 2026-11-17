# Make a native-atlas character pack

The current development kit can **lint a local folder** before installation.
It checks creator metadata and the same atlas geometry/pixels used by generated
Hermes pets. A passing result does not install the pack or make its metadata
active in Desktop. This is the draft native-atlas subset of the characters
feature; pack import, bot assignment and extended interactions are still open.

## Start with the original example

Use a Hermes Python environment with Pillow and this source patch applied:

```sh
python examples/character-pack/make_example.py ./lanternling
hermes pets validate ./lanternling
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
  "spritesheet": "spritesheet.png"
}
```

Exactly these six fields are supported. Name, author and licence must each be
1–160 printable characters with nonblank content; Unicode names are supported.
The licence text records your statement; lint cannot prove ownership or legal
permission. Use original art or art you have permission to adapt/distribute.
Duplicate keys, other schema versions and unknown fields fail validation.

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
   Animated GIF/APNG/WebP, Lottie and legacy eight-row sheets are outside this
   folder contract. Renaming another format to `.png` does not enable it.
4. Fill the manifest with your name and actual permission/licence statement.
5. Run `hermes pets validate ./my-character`. Fix errors before sharing it.
   To check an image alone, use `hermes pets validate ./my-character/spritesheet.png`.
6. Inspect the exported sheet in your image editor. Pack-based animation preview
   and installation are not wired yet. Existing **installed** pets can still be
   previewed with `hermes pets show <slug> --cycle --once`.

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

## Read the result

Success prints the pack name, author, licence, dimensions and populated rows.
Warnings alone return exit **0**; errors return **1**, including unreadable files
or metadata. Validation does not install a pet, select a profile, change settings,
start a model or fetch an asset.

FPS, anchor/footprint, custom per-event mappings, sounds, ZIP import, GIF/APNG/
Lottie decoding, install/uninstall/assign and a pack creation skill are future
parts of the full format. They are rejected or absent here rather than silently
advertised as working options. Existing native geometry and animation scheduling
remain in control. Lint is not proof of the five-character CPU/RAM budget or
of enter/exit, handoff, retry, review or group-celebration behavior.
