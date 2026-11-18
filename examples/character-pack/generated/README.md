# Generated desktop character packs

The native atlases supply nine rows of art for each character. Open a PNG
contact sheet to review all rows at the Mac gateway's **96 × 104 px** cell size.
The line in each cell marks the ground anchor.

| Pack | Motion weight | Contact sheet |
| --- | --- | --- |
| [Copper Wren](copper-reed/manifest.json) | Light | [PNG](copper-reed/contact-sheet.png) |
| [Moon Jelly](jellune/manifest.json) | Light | [PNG](jellune/contact-sheet.png) |
| [Moth Scout](mothsmith/manifest.json) | Standard | [PNG](mothsmith/contact-sheet.png) |
| [Mint Parcel](parcel-bug/manifest.json) | Heavy | [PNG](parcel-bug/contact-sheet.png) |
| [Puddle Frog](puddlecap/manifest.json) | Heavy | [PNG](puddlecap/contact-sheet.png) |
| [Fernpot](terracotta-fern/manifest.json) | Heavy | [PNG](terracotta-fern/contact-sheet.png) |

From the repository root, point a patched Hermes CLI at a pack directory.

```sh
hermes pets validate ./examples/character-pack/generated/jellune
hermes pets show --pack ./examples/character-pack/generated/jellune --cycle --once
```

The folder's `manifest.json` and `spritesheet.webp` form the schema 1 native
pack. The terminal activity cycle plays idle, wave, work, jump, fail, waiting
and review. Inspect the eight-frame directional walks in the contact sheet.
The [pack guide](../../../docs/character-pack.md) covers import and assignment.

## Source actions

`actions.webp` is a separate lossless RGBA sheet. The accompanying
`actions.json` records the cell dimensions, number of columns, and ground
anchor `[48, 93]` in pixels from the top-left corner of a cell. For each action
it gives a zero-based row, number of frames and one suggested duration in
milliseconds per frame. Read from the left of the row and ignore the transparent
trailing cells. The suggested durations are for authoring and review.

The source sheet includes parcel throw, parcel catch, angry stomp, sleep and
yawn, and landing. Puddle Frog has an extra waiting sequence with a question
mark. Hermes imports the native atlas. The source sheet stays in this folder
for future event wiring. The contact sheet shows both files in frame order.

## Art provenance and prompts

The original designs are shown in the
[creator reference](../../../docs/images/character-creator.webp). Codex's
built-in image generation used a crop of the matching character and two
transparent pose sheets per pack. Both prompts requested a four-column,
six-row grid, a three-quarter right-facing character, the original palette
and proportions, quiet backgrounds with genuine alpha, isolated poses and
clear gutters. No lettering was requested except for the waiting pictogram.

- The native-pose prompt asked for idle breathing and blink, weighted walk or
  roll, work at the original small device, waiting with a question mark, a
  five-stage celebration planned from four drawn poses, and stumble with a
  dust puff. Moon Jelly instead used those last two source rows for idle and
  thinking studies.
- The second prompt asked for a held, wound-up, released and departing parcel,
  an incoming, contacted, compressed and secured parcel, an angry wind-up and
  steam stomp, a nap and open-mouth yawn, a descending, squashed, rebounding
  and settled landing, and a friendly wave. It specified the character's own
  way of moving, including the truck's suspension and the fern's fronds.

The generated poses were cropped and aligned locally to a native foot or
wheel line at y=186. Some key poses use small scale and position changes for
intermediate frames. The left walk mirrors the right walk. Newly drawn native
poses were rasterized at 96 × 104 px and stored at twice that resolution to
fit the native atlas geometry. Moon Jelly's
[celebration](../../../docs/images/moon-jelly-celebration-frames.webp) and
[failure](../../../docs/images/moon-jelly-failure-frames.webp) rows and
Puddle Frog's [waiting](../../../docs/images/puddle-frog-waiting-frames.webp)
row preserve the decoded reference pixels.

The pack manifests use the repository's [MIT licence](../../../LICENSE).
