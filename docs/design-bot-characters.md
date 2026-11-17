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
