# Recover from settings write failures

Version v0.8.13 gives Desktop and dashboard users a next step when saving settings
fails because the destination is not writable or has exhausted disk space/quota.
Permission and read-only filesystem errors advise checking write access on the
destination device. Storage errors advise freeing space or increasing the quota.
Responses contain fixed guidance, never filesystem paths or exception text.
Unknown faults retain the existing generic error and HTTP status behavior.

A failure can happen after replacement, during cleanup or metadata restoration.
The message therefore says the save could not finish; it does not promise that
the old file is unchanged. Existing ordered autosave retention and retry behavior
remain as described in [settings autosave](settings-autosave.md).

## Verification

The six-file native Python selection passes 226 tests. New API cases exercise
permission, read-only storage, full storage, quota, unknown I/O and post-replacement
failures. They verify private-detail suppression, pre-write byte preservation,
unrelated-field preservation and successful retry. Scoped lint, source health and
an independent review pass.

Installed Linux Electron, controlled through existing Playwright in an isolated
home, reproduced the old generic error by removing write permission from that
home. With the fix installed, the same fault displays actionable guidance and
keeps the edited value and window available. Restoring write access and closing
again saves the retained edit; a cold reopen reads that value back. The final
message and recovered value were visually checked at 1280 pixels. Recovery before
the message-only patch also passed at 640 pixels. No GPU device, worker or model request was used.

The backend and regression test were installed on Linux and ARM64 Mac before
publication. The native Mac backend also passes an actual folder-permission
failure, old-file preservation and successful retry under network/GPU restrictions.
Desktop compiled assets are unchanged. Existing production Gateway
processes and protected settings/credential files were preserved. This does not
establish native disk-full injection, network failure recovery, crash durability,
interactive Mac acceptance or production workload savings.
