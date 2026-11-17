"""Create the original CC0 Lanternling native-atlas example in a new folder."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw

from agent.pet.generate.atlas import CELL_HEIGHT, CELL_WIDTH, ROW_SPECS, compose_atlas
from agent.pet.pack import validate_pack


def frame(state: str, index: int):
    image = Image.new("RGBA", (CELL_WIDTH, CELL_HEIGHT))
    draw = ImageDraw.Draw(image)
    y = 48 + (0, 2, 4, 2)[index % 4]
    draw.line((96, y - 20, 96, y), fill="#355c45", width=5)
    draw.ellipse((87, y - 29, 105, y - 11), fill="#e8ca66")
    draw.rounded_rectangle((43, y, 149, y + 120), radius=24, fill="#58866a", outline="#294d3b", width=4)
    draw.rounded_rectangle((54, y + 14, 138, y + 70), radius=16, fill="#f1d78a")
    for x in (74, 113):
        if index % 6 == 4:
            draw.line((x - 4, y + 38, x + 4, y + 38), fill="#294d3b", width=3)
        else:
            draw.ellipse((x - 4, y + 31, x + 4, y + 41), fill="#294d3b")
    draw.line((88, y + 52, 103, y + 52), fill="#294d3b", width=3)
    foot = 3 if index % 2 else 0
    draw.rounded_rectangle((57, y + 116, 83, y + 134 + foot), radius=6, fill="#294d3b")
    draw.rounded_rectangle((108, y + 116, 134, y + 137 - foot), radius=6, fill="#294d3b")
    if state == "running":
        draw.rectangle((51, y + 83, 141, y + 120), fill="#c4dacb", outline="#294d3b", width=3)
        draw.line((47, y + 123, 145, y + 123), fill="#294d3b", width=5)
    elif state == "waving":
        draw.line((147, y + 84, 164, y + 50 - index % 2 * 10), fill="#294d3b", width=10)
    elif state == "failed":
        draw.arc((80, y + 49, 112, y + 66), 190, 350, fill="#294d3b", width=3)
    elif state == "waiting":
        draw.ellipse((155, y + 3, 172, y + 20), fill="#e8ca66")
    return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT) if state == "running-left" else image


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="New output folder (must not exist)")
    args = parser.parse_args()
    sheet = compose_atlas({state: [frame(state, i) for i in range(count)] for state, _, count in ROW_SPECS})
    args.output.mkdir(parents=True, exist_ok=False)
    meta = json.loads(Path(__file__).with_name("manifest.json").read_text())
    (args.output / "manifest.json").write_text(json.dumps(meta, indent=2) + "\n")
    sheet.save(args.output / "spritesheet.png")
    result = validate_pack(args.output)
    assert result["ok"] and not result["warnings"], result
    print(f"Created {args.output}: original CC0 atlas, all native rows populated")


if __name__ == "__main__":
    main()
