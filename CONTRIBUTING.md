# Contributing test results

Use the result form for measurements and the pack-problem form for missing nodes, broken inputs or documentation problems. No generation runs are triggered by submitting a form or opening a pull request.

## Result checklist

- Supply the exact pack ID and version, run date and local/cloud execution location.
- Record GPU model and dedicated VRAM, CPU, system RAM, OS, driver, ComfyUI version, Python, PyTorch/CUDA and relevant custom-node revisions.
- State the model files/revisions and any deviation from the supplied preset. Do not upload model weights or credentials.
- Record each measured run in seconds, its seed, status and output link. Leave unavailable measurements blank and explain the method used for VRAM measurements.
- Upload the original workflow used, a sanitized log and outputs, or provide public links. Include all measured outputs. Remove local usernames, paths and tokens from logs and workflow metadata.
- Distinguish a completed run from a usable shot. A failed run or out-of-memory error is a valid observation, not a zero-second generation.

## Review process

New result issues receive `community-result` and `needs-review`. A maintainer checks the pack version, settings, timing scope, evidence and publication choice. Questions stay in the issue. Reviewed observations may receive `reviewed`; this means the submission was checked, not independently reproduced. Independent reproduction must be stated separately.

The website is curated manually. It does not execute uploaded workflows, ingest issue text automatically or publish arbitrary attachments. A website entry should link to the source issue, identify contributor-reported measurements, list changes and respect the contributor's publication choice. Do not grant `reviewed` based only on a successful workflow validation or a plausible time.

## New or revised packs

Use `templates/pack-template.md`. Include workflow JSON, input assets, prompt, manifest, model references with immutable revisions where available, source/license notices, and a measurement protocol. Keep large checkpoints out of Git. Keep outputs in release assets or external links when appropriate.

State validation honestly: `pilot-baseline-pending` until a reference GPU run, actual environment and unedited output are recorded. Record the reference setup separately from an upstream workflow's declared node version. A structural JSON check is not a generation test. Promote a pilot only after compatibility and the measurement method have been checked on a real run.

Changes to a released pack's prompt, inputs, graph, model revision, preset or protocol require a new version and refreshed checksums. Never replace a release asset with a different file under the same name/version.
