# Desktop characters on Linux

Desktop characters use one transparent Electron window on X11. On a Wayland
desktop, launch Hermes through XWayland to use the preview. The helper sets
only the X11 input region. Transparent space, sprite holes, shadows and passive
effects let mouse input reach the app behind them. Solid sprite pixels and the
open character output panel receive input. If the helper fails, the character
window closes.

## Use XWayland

Quit Desktop, add this flag to the existing `desktop` section of the Hermes
configuration, and launch Desktop again.

```yaml
desktop:
  electron_flags:
    - --ozone-platform=x11
```

For a Linux source build, the helper needs a C compiler and the X11 and Xext
development libraries (`libx11-dev` and `libxext-dev` on Debian and Ubuntu).
The runtime needs XWayland or Xorg, X Shape 1.1, `libX11.so.6` and
`libXext.so.6`. Open **Bots → Monitor → Show bot characters**.

## What works where

| Feature | COSMIC 1.0.0 · XWayland | GNOME 46 · XWayland | Native Wayland |
| --- | --- | --- | --- |
| Transparent backdrop and stacking | Visible in the compositor capture over the focused synthetic backdrop | Visible in the compositor capture over the focused synthetic backdrop at 2× scale | Preview refused before it can widen the overlay |
| Click-through and character actions | Named backdrop received clicks through a gap, a transparent sprite pixel and a vacated position. Solid sprite and panel controls received their clicks | Same checks passed | A stale character snapshot also left the existing mascot window at its small size |
| Drag, gravity and animation | Drag, gravity, walking and frame changes passed | Drag, gravity, walking and frame changes passed | Character preview unavailable |
| More than one display | One connected display in the trial | One connected display in the trial | Character preview unavailable |
| Main window minimized | Five characters kept walking and animating | Five characters kept walking and animating | Character preview unavailable |

COSMIC can place its own dock above XWayland surfaces, and its XWayland
work area did not expose the panel inset in this session. The COSMIC input
fixture uses the part of the bottom strip outside the dock. Both trials used
real compositor sessions, the built Desktop renderer and preload, and the
production IPC and X11 adapter. The fixture's foreground window and five
Lanternling color variants were synthetic. The two-display IPC test checks a
layout with a negative secondary origin, and the renderer test drags across that
seam. Physical multi-display and mixed-scale behavior remain unverified.

COSMIC advertised `zwlr_layer_shell_v1`. Electron's native Wayland windows use
the toplevel role, so a native COSMIC implementation needs a separate layer-shell
surface host. GNOME did not advertise layer shell. Native Wayland toplevels
also lack the placement and stacking operations this overlay uses.
[Electron window limits](https://www.electronjs.org/docs/latest/api/browser-window#platform-notices)
· [Layer-shell protocol](https://github.com/swaywm/wlr-protocols/blob/master/unstable/wlr-layer-shell-unstable-v1.xml)

## Five pets versus a closed overlay

| Session | CPU baseline → five pets | Summed RSS baseline → five pets |
| --- | ---: | ---: |
| COSMIC · 1920 × 1080 at 1× | 0.83% → 11.54% | 518.7 → 764.8 MiB |
| GNOME · 2560 × 1600 at 2× | 4.96% → 15.28% | 581.5 → 902.4 MiB |

CPU is a percentage of one logical core over 12 seconds. RSS is the mean
summed RSS of the Electron fixture process tree over the same interval, so
shared pages can be counted in multiple processes. The baseline has only the
synthetic foreground window. The five-pet sample uses the same foreground and
adds the animated overlay and helper. The fixture uses software rendering.
Use the change within each machine to read the overlay cost.

- [COSMIC compositor capture](images/linux-pets-cosmic.webp)
- [GNOME compositor capture](images/linux-pets-gnome.webp)
- [Compositor and performance receipts](../verification/linux-desktop-pets-results.json)

## Reproduce

Apply the [stable-full kit](stable-full-kit.md) to its pinned upstream commit
and build `apps/desktop` with `npm run build`. Set `SOURCE` to that checkout,
`FIXTURE` to a new directory, and `ELECTRON` to the matching Electron binary.
Run from an active graphical session with its display and session bus exported.

```sh
python3 scripts/test_linux_desktop_pets.py prepare "$SOURCE" "$FIXTURE"
python3 scripts/test_linux_desktop_pets.py run "$FIXTURE" "$ELECTRON" "$RESULT"
```

Use a fresh `RESULT` directory for each run. The script starts an isolated
temporary home, closes its test windows, and writes `run.jsonl`, `stderr.log`
and a bottom-strip renderer capture. Run with `--backend wayland` for the
native guard. Use `--no-sandbox` for the local unpacked test binary if required
by the host's Electron sandbox setup.

On COSMIC, run with `--input uinput` when the current account can open
`/dev/uinput`. For a compositor capture, prepare with `--cosmic-capture`
(requires Wayland development headers and protocols), then run with
`--capture-command "$FIXTURE/cosmic-capture.sh"`. On GNOME, use
`--capture-command "$FIXTURE/gnome-capture.py"` with the session's Mutter
ScreenCast service, GStreamer PipeWire source, Python GI and ImageMagick.
Open only the synthetic backdrop in the capture area. Both helpers write
the bottom strip directly.
