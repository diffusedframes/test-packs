# LTX 2.5 image-to-video: a cafe moment

**Pack:** `ltx-i2v-01` · **Version:** `0.2.0-pilot` · **State:** pilot, baseline render pending.

This is an experimental first pack. Its JSON, assets and references have been checked structurally, but **no GPU render has been run for this pack**. Compatibility, resource requirements, the output and the timing procedure still need confirmation on a real run. There are no claimed reference timings or minimum-VRAM promises.

## What this tests

Animate the same cinematic cafe first frame: a woman beside a rainy window turns slightly towards the camera and gently steadies a red cup as the camera slowly pushes in. Observe facial identity, hand anatomy, cup and handle continuity, natural performance, lighting and reflections. Compare full workflow time and memory observations across documented setups. This is one narrative shot, not a general ranking of model quality or GPUs.

![Shared first frame](inputs/df-cafe-start.png)

## Included

- `workflow.json`: adapted from Comfy Org's LTX 2.5 I2V template; upstream commit and license are recorded in `manifest.json` and `licenses/`.
- `inputs/df-cafe-start.png`: the exact AI-generated fictional cafe first frame, 1672 × 941 pixels, with no branding. People and the location are fictional.
- `prompt.txt`: the exact prompt, also stored in the workflow.
- `PROTOCOL.md`: run order, timing scope, cache checks and acceptance criteria.
- `manifest.json`: preset, pinned model references, validation state and file hashes.
- `results.csv`: empty measurement fields for a first run and three repeat runs. Blank values are not zero.

## Prepare when your machine is available

1. Unzip the pack into its own folder. Read the protocol before running it.
2. Use a separate ComfyUI installation or a suitable existing environment with subgraph support. **Do not update or restart a running render to install this pack.** Upstream nodes declare `comfy-core 0.30.0`; this is the upstream declaration, not an environment tested by Diffused Frames. Record your actual backend/frontend versions.
3. Download the five model files linked in `manifest.json` into their listed folders. Their URLs pin Lightricks revision `49b093a39c19169a8a81721dcc541e07e945232f`. Review and accept the [publisher's model terms/access requirements](https://huggingface.co/Lightricks/LTX-2.5) yourself. No model weights are bundled. The workflow retains an optional prompt-enhancer branch, but enhancement is off; that optional model is not part of the required preset.
4. Copy `inputs/df-cafe-start.png` into your ComfyUI input folder, then import `workflow.json` using ComfyUI's Open command. The first-frame loader must show that exact file. Importing a workflow does not mean you have to queue it.
5. Check the exposed settings against the table below. If the UI reports missing models/nodes, stop and use [the pack-problem form](https://github.com/diffusedframes/test-packs/issues/new?template=pack-problem.yml). Do not silently substitute another model or preset.
6. When ready, follow `PROTOCOL.md` and record every attempt. The pack contains no automatic runner, installer or upload script.

## Preset

| Setting | Value |
| --- | --- |
| Model | LTX 2.5 22B distilled, Comfy INT8 convrot |
| Output width × height | 1280 × 736; keep these exact dimensions |
| Duration setting / FPS | 3 seconds / 24 FPS, yielding 73 frames (about 3.04 seconds) |
| Prompt enhancement | Off |
| Sampling | Euler ancestral, upstream 8-step first stage and 3-step refinement |
| First-run main seed | 41000 |
| Repeat-run main seeds | 41001, 41002, 41003 |
| Refinement noise seed | 42, fixed for every run |
| Decode | Upstream tiled video decode; audio generation and decode retained |
| Encoding | Upstream auto container/codec; report the actual output format |

The resolution selector has been removed so it cannot override the fixed dimensions. The prompt, first-frame path, duration and main seeds were changed for this pack; cached upstream API metadata was removed. No changes were made to the upstream sampling/decoding graph apart from fixed control values and disabling prompt enhancement.

Changing quantization, attention, offloading, tiling, dimensions, prompt or input makes a **modified-preset** result. It is still useful if every change is documented. Identical seeds do not promise pixel-identical outputs across hardware or software.

## Acceptance criteria

Judge the result at normal speed and inspect representative frames. The woman should turn slightly towards the camera with a restrained expression and steady the cup while it stays on the table. Her identity, hair and clothes should remain consistent; fingers and the cup handle should retain plausible anatomy and geometry; the push-in should be smooth; lighting, reflections and background depth should stay coherent. Record missed actions, hand/cup defects, identity drift, temporal tears, cuts and new objects. A completed workflow can still produce an unusable shot.

## Share a result

Use [Contribute a test result](https://github.com/diffusedframes/test-packs/issues/new?template=test-result.yml). Attach the CSV, original measured outputs and sanitized workflow/log evidence, or provide public links. Submit failures too. GitHub submissions and attachments are public immediately; website features are reviewed separately and follow your publication choice.

## Attribution and permissions

Workflow source: [Comfy Org LTX 2.5 I2V template at commit 447747bf](https://github.com/Comfy-Org/workflow_templates/blob/447747bf37b7e2f6d5fab3f15288e03bf889b82f/templates/video_ltx2_5_i2v.json), MIT; notice retained in `licenses/Comfy-workflow-templates-MIT.txt`. Diffused Frames' graph modifications are provided under those same MIT terms. Model weights have separate publisher terms and are not redistributed.

The supplied first frame was created for Diffused Frames using AI image generation. The people and cafe are fictional; the image is not camera-captured footage. Diffused Frames permits its use, redistribution and adaptation for running, demonstrating and sharing these tests, with attribution to Diffused Frames. See the repository README for contributor output permissions.

Version 0.2.0 replaces the earlier branded portal scene with a narrative cafe shot, updates the prompt and visual criteria, and retains the same numerical preset and timing protocol. Results from different pack versions must remain separate.
