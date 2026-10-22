# Diffused Frames · Community Tests

Repeatable tests for AI video, VFX and filmmaking. Download the same inputs and workflow, run them on your setup, and share the output and the time it took.

[Website](https://www.diffusedframes.com/tests/) · [Contribute a result](https://github.com/diffusedframes/test-packs/issues/new?template=test-result.yml) · [Report a pack problem](https://github.com/diffusedframes/test-packs/issues/new?template=pack-problem.yml)

## First pack

| Pack | Version | State |
| --- | --- | --- |
| [LTX 2.5 image-to-video: glass portals](packs/ltx-i2v-01/README.md) | 0.1.1-pilot | Pilot · baseline render pending |

The first pack contains an adapted ComfyUI workflow, a shared first frame, an exact prompt, model references, settings, a timing protocol and a blank results sheet. **No GPU workflow has been run or performance result claimed for this pack.** Pilot contributions can help identify compatibility problems; they are not a verified benchmark or a GPU ranking.

## Take part

1. Download a tagged pack from [Releases](https://github.com/diffusedframes/test-packs/releases). Keep its version with your results.
2. Read its README and model requirements. Models are downloaded separately from their publishers; they are not included here.
3. Run the protocol when your machine is available. Record first-run time separately from repeat runs, and keep every measured output.
4. Use the **Contribute a result** form. It asks for the pack version, hardware, software, settings, timings and output evidence. Failed and out-of-memory runs are useful too.

A GitHub account is required to submit. Issues and attachments are public immediately. Diffused Frames reviews submissions before selecting any for its website; a submission is not automatically a verified result. Do not include private paths, account details, access keys or client material.

## Compare like with like

- Keep the supplied prompt, inputs, settings and model revisions for an unchanged-preset result.
- Report any change, including quantization, attention backend, offloading, tiling or a different resolution. Modified runs are shown separately.
- A seed controls the starting randomness; it does not guarantee identical pixels across GPUs or software versions.
- Report units and measurement methods. Unmeasured values stay blank or “not measured”; they are never zero.
- Record queue, model-loading and total workflow time separately where available. Check that each timed run generated a new output rather than returning cached results.
- Include failures, retries and manual changes. Publish every measured attempt, not only the best take.

## Add a pack

Start with [the pack template](templates/pack-template.md) and follow [CONTRIBUTING.md](CONTRIBUTING.md). Give every pack a stable ID and version. A published version is a snapshot: changing its workflow, prompt, input or timing protocol requires a new version. Keep old releases available so submitted results remain interpretable.

## Files and permissions

The adapted ComfyUI workflow retains the upstream MIT notice in `licenses/Comfy-workflow-templates-MIT.txt`. The Diffused Frames first frame is AI-generated, not a capture of a real location; Diffused Frames permits its use, redistribution and adaptation for running, demonstrating and sharing these tests, with attribution to Diffused Frames. This permission does not cover third-party model weights, logos, or unrelated materials. Model publishers' own licenses and access requirements apply.

Contributors keep ownership of their outputs. The result form lets them choose whether Diffused Frames may feature their measurements and/or submitted media, with their GitHub username as credit. Public issue availability alone is not permission for unrestricted media reuse.

Questions or removal requests: [hello@diffusedframes.com](mailto:hello@diffusedframes.com).
