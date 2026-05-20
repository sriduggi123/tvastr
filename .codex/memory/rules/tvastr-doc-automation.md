---
description: "Repository-specific documentation automation expectations for Tvastr."
---
Do not assume code edits automatically update Tvastr product documentation. The current hook behavior is Codex memory/context capture into `.codex/memory/context.md` and `.codex/memory/rules/...`, not mutation of docs such as `Documentation/OffLineEditing/FeatureSet.md`. When a code or prototype change affects documented product behavior, explicitly update the relevant documentation file in the same task unless the user asks not to.
