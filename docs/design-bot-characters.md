# Bot characters on screen

## Outcome and existing parts

Show active bots as original or user-owned characters, with short event-driven
status and interactions, latest-output preview and canonical chat/report opening.
Idle characters hide or sleep; animation never implies a task started or passed.
Reuse Bot Monitor/delegation state, native pet storage/atlas decoding, PetSprite,
PetBubble and the existing gateway-less overlay IPC/window. One shared renderer,
not one process/window per bot. Keep account/profile/session ownership and Stop
authority; no model calls for animation or invented progress.

## Approaches

Extend the current pet/overlay path: chosen maintainer approach, least duplicate
state/rendering. Independent windows per bot multiply baseline memory and violate
the one-renderer goal. A separate animation application duplicates lifecycle and
chat-opening authority. Keep the existing petdex/legacy renderer fallbacks.

## First completed slice: creator state preview

Existing `hermes pets show --cycle --once` omits run/wave/jump because the atlas
row names differ from canonical activity names. It also repeats a full sequence
as many times as there are states. The working patch cycles all seven canonical
PetState values and stops after one completed sequence; explicit-state precedence,
renderer alias/legacy fallback and cursor restoration are preserved. This fixes
existing author tooling without another command, dependency, process or setting.
Eight focused source tests and the real source CLI through an isolated native
PTY pass with a synthetic atlas. This is terminal preview, not the new desktop
overlay. [Evidence and limits](verification.md#pet-creator-preview--native-terminal-acceptance-unreleased).

## Active-character overlay preview: offline source step

The working source adds **Show bot characters** in Monitor. A loaded, enabled
pet is required. It previews at most five current source-qualified bot/worker
observations in the existing transparent overlay, using that pet's sheet and
PetSprite. Bounded name/source/latest signal and reported step remain plain
text. Current work uses the run pose; reported bot attention uses failed.
It does not infer reasoning, human waiting, completion or progress percentages.

The existing plugin pet door now exposes a scoped replaceable display publisher.
One preview owns the shared overlay; a superseded/disposed publisher cannot
revive or clear the newer snapshot. Identities include plugin, source and stable
bot/worker identity; no worker array-index fallback. Empty replacements cross
IPC. Monitor error/stale/retained/unqualified observations are excluded. The
15-second lease is anchored to the source snapshot time, with independent
receiver expiry. Unmount/unload clears the publisher; stopping restores the
previous mascot mode. No extra polling, model, gateway or per-actor OS window.

The read-only actor stage replaces the global mascot composer while previewing.
It uses short enter/exit transitions and a 15 fps sprite ceiling; reduced motion
uses static poses which still reflect semantic state changes. Native IPC gates
the stage on main-window hide/minimize and lock/suspend, preserves a known lock
through resume, and retires retained state/listeners when the overlay closes.
Normal mascot behavior has regression coverage. All nine Monitor locales have
the new control and its installed-pet/read-only scope hint.

Offline tests/types/lint and renderer/changed-IPC builds pass. Two earlier native
control renderers failed sandbox initialization before overlay loading. A fresh
fixture using the established Chromium sandbox and guarded native launch path
loaded the control renderer, then reached production overlay loading. Its
network guard refused a Google theme-font stylesheet before connection; the
trial closed and remains failed. This does not establish the cause of the two
earlier failures.

The shared theme painter now skips its font-link injection only for exact
`win=overlay`, covering cold boot and later theme paints. Palette, typography
and local font stacks remain; normal main/HUD/secondary windows still load and
deduplicate theme fonts. Suppressed fonts do not poison that cache. Four new
regression cases and 23 neighboring theme cases pass, as do scoped lint,
renderer types and the fixed renderer build. This guards the theme-font branch,
not every custom CSS or asset URL. A fresh contained native fixture subsequently
reached Local60 with the fixed production artifact, zero Desktop SSH and no
font/network refusal. CUA paired screenshots show only its control window's
normal-to-actors button transition. Overlay receiver telemetry stayed null;
actors, motion and mascot restoration are unproved. Observation admission
refused insufficient remaining reserve before the next action and closed the
trial permanently. Raw phase measurements cannot establish character CPU/RAM.
The fixture also lost console error text by using an obsolete callback shape;
a prepared offline repair preserves full event details but has not been run
natively in that round. A later diagnostic captured the missing fixture method
`onPreviewFileChanged`: production preload provides the passive event listener,
while the isolated host omitted it. Reusing that real subscription fixes the
fixture's bootstrap: a distinct host receives a run-bound overlay ACK and
reaches Local60 with unchanged renderer/native IPC artifacts. This identifies a
fixture defect; no product-source fix is inferred. Its app-filtered window
inventory lists control only, so overlay images, five actors, motion and resource
acceptance remain open. The later expanded visual attempt also ended at its
deadline. No completed character acceptance is claimed. [Evidence and limits](verification.md#bot-character-overlay-preview--offline-source-step-unreleased).

Persistent all-bot tracking, character interactions/open controls, per-bot packs,
display-only sleep handling and actual visibility/reduced-motion/resource
acceptance remain open. No version or release for this development step, and
no claim that the five-character CPU/RAM target is met.

## Remaining capability work

The first overlay slice must map actual active bots/workers to bounded actors in
one window, with task/status and enter/exit/work/think/wait/error/done animation.
Add short, skippable handoff/result/review/retry/collaboration/escalation/group-done
interactions only from real events. Reuse canonical open/Stop/Pause, latest-output
preview and safe artifact/viewer/platform-open APIs; never execute artifacts.

Add on/off, edge/corner/multi-monitor placement, maximum actors, reduced motion,
DND and sounds off by default. Movement/idle loops remain active while visible;
static poses in reduced motion. Cap animation15–24fps, lower idle rate, pause fully
when screen locked/off or Hermes hidden/minimized. Measure before/after with five
actors on this Mac: target <=1–2% average CPU and <=60–80MB extra RSS. Report an
actual budget miss and trade-off before release; no budget claim from unit tests.

Character packs still need a documented manifest/animation/fallback/size/frame/
license contract, complete original example, blank template, non-programmer
creation guide, validator/preview/install/assign tooling and creator skill. Reuse
current stores/renderer rather than silently introducing another atlas taxonomy.
Only original/owned art; no borrowed character designs or copied reference art.

Keep these items explicitly unimplemented until their source and native evidence
exist. Full capability release requires screenshots/short recording, real-event
acceptance and measured CPU/RAM. No source/runtime adoption into the owner app,
ai/otherhost access or permission changes; first adoption remains lead/owner-only.
