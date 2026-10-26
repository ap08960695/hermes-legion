# Quiet automatic Slack status notices

To suppress automatic paused-work notices for a Slack bot, edit that bot's private native profile configuration. Merge these keys into the existing mapping; retain all credentials and other settings outside this repository.

```yaml
platforms:
  slack:
    gateway_restart_notification: false
    extra:
      system_status_notifications: false
```

`gateway_restart_notification` is the existing native switch for startup/restart/shutdown notices. The Legion `system_status_notifications` opt-out suppresses the automatic paused refusal on the actual answering Slack adapter. Omitted or true keeps the prior notice behavior. Use a YAML boolean, not the string `"false"`.

A silent paused turn returns the native empty-response block. It never passes the gate as an allowed new agent turn. Recognized control commands, approval replies and steering for existing running work retain their native policy; ordinary task results are unchanged. Other messaging platforms keep their current behavior. This preference does not change a quota, provider, paid fallback or global pause state.

After installing the reviewed source, reload the serving Gateway through the normal graceful lifecycle when no work is active. Do not force-stop workers or resume a paused fleet just to test a notification preference. Offline adapter tests cover both the silent and default notice paths, the still-engaged pause and the control-command bypass. Fresh process/source/config evidence is separate from a real Slack message test; no live test message or model request is needed.

## Existing posts

Changing the preference does not remove earlier Slack posts. Deletion is a separate, explicit owner action using the original bot identity. Select only confirmed system boilerplate, re-read each exact message before deletion, preserve thread replies and normal task results, and verify that the selected post is absent afterward. Never bulk-delete a channel based on a text fragment. This companion does not ship a credential-bearing cleanup script or any workspace/channel/message IDs.
