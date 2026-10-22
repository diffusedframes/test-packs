# Pack authoring and release checks

Every pack needs a documented prompting/input/output review before a public pilot download. A structural file check is one part of that review. A clean reference render and visual inspection are separate steps, performed only when the operator authorizes execution.

## 1. Identify the actual model and workflow

- Record the exact model family, version, full/distilled variant, precision/quantization and immutable file revisions.
- Pin the source workflow commit, backend/custom-node revisions and the workflow JSON checksum. Record frontend requirements separately.
- Read the model publisher's current prompting guide, capability guide and workflow documentation. Include source links, date checked and relevant requirements in a model-specific review note.
- Separate local open-weight workflows from hosted APIs. Do not assume they expose the same duration, prompt enhancement, negative-conditioning or output options.
- Trace the actual graph when documentation and template labels disagree. Document the discrepancy. A general divisibility rule may apply to a base stage rather than the exposed final-size field.

## 2. Review the prompt and visual test

- Define what the test is measuring before writing the prompt: one clear production question, concrete action, camera behaviour and acceptance criteria.
- Follow the specific model's prompting conventions. For I2V, use the source image as the appearance reference and describe the intended motion, performance and sound.
- Check the number of actions against the clip duration. Identify what stays fixed and what moves. Avoid contradictory hand/prop instructions and ambiguous verbs.
- Record prompt enhancement on/off, the exact submitted prompt, any rewritten prompt actually used, and separate negative-conditioning text. Record fixed CFG/distilled schedules rather than assuming exclusions will be enforced.
- Verify that the initial image supports the action: framing, visible hands, prop access, eyeline and room for motion.
- Set shot-level pass/fail observations in advance. Failure to follow a constraint remains a test observation; do not discard it or silently rewrite the prompt until a successful take appears.
- A change to prompt, input, action or criteria after execution creates a new pack version or a separately labelled condition.

## 3. Specify the input pixels

- Supply one exact shared input and its SHA-256. Do not substitute the website preview, a screenshot, or a recompressed download.
- Record container/codec, pixel dimensions, aspect ratio, bit depth, channels, alpha, orientation and colour/profile metadata. For ordinary SDR I2V, the default authoring choice is a lossless RGB PNG exported through a known sRGB pipeline. Document when that is an assumption instead of a verified transform/profile.
- Record every graph operation before conditioning: resize size/filter, centre crop or padding, channel conversion, compression and conditioning strength. A lossless source does not imply a lossless preprocessing path.
- Match the intended conditioning aspect ratio where practical. If using a different ratio deliberately, show and document the resulting crop before release.
- Define separate handling for HDR/EXR, masks and alpha workflows. Do not apply the SDR PNG convention to those tests without checking their requirements.
- Report input decode/preprocess time separately where measured. Smaller compressed files do not automatically imply faster or lower-VRAM sampling; generation dimensions, frames and execution settings must also be recorded.

## 4. Separate requested, derived and measured output

Record each of these explicitly:

| Layer | Required information |
| --- | --- |
| Exposed controls | Width, height, duration/frames, FPS and their units |
| Internal stages | Scale factors, latent alignment, integer rounding, conditioning resize/crop and intermediate frame counts |
| Derived output | Expected final dimensions, frame count and duration calculated from that specific graph |
| Delivery encoding | Requested container, video/audio codecs, pixel format/bit depth, colour tags and audio rate/channels where controlled; identify automatic choices |
| Measured file | Probed dimensions, frames, FPS, duration, codec/container, colour/bit-depth tags and audio properties from a real saved output |

Treat a dimensional or frame-count mismatch as a pack/configuration issue to investigate. Preserve the original file and settings. Never label a UI target as a measured delivery size, and never call an upscaled export native output.

For the pinned LTX two-stage graph, read [the LTX review](docs/ltx-2.5-i2v.md). Its final-size controls are halved before a 32-pixel latent grid, so matching the requested final size requires 64-pixel alignment in each dimension. This is a graph-specific rule, not a universal LTX rule.

## 5. Review measurement conditions

- Record GPU/VRAM, CPU/RAM, driver, OS, actual software versions, attention backend, launch flags, memory reservation/offload settings, and local/cloud execution.
- Record other GPU applications and concurrent workloads. Do not attribute a slowdown to one application without evidence. Mark confounded runs as exploratory while retaining their quality observations.
- Define first-process versus repeat-run timing, cache handling, queue inclusion, model loading, decode and save/encode scope. Verify actual sampling runs instead of timing cached outputs.
- Keep individual seeds, attempts, failures and output evidence. Leave missing values unmeasured. Do not merge incompatible precisions, resolutions, conditions or pack versions into one speed ranking.

## 6. Release gates

1. **Documentation and source review:** current official sources, exact input/output contract, prompt review and known discrepancies are recorded.
2. **File preflight:** graph references, input metadata, prompt/control consistency, hashes and release ZIP bytes are checked. These checks must not contact ComfyUI or initialize a model/GPU.
3. **Public pilot:** any unexecuted or incompletely validated pack is clearly labelled, with outstanding questions and no claimed reference performance. A public pilot must still state its source-derived expected format correctly.
4. **Reference run:** only when authorized, run the exact pack in a documented environment, probe its output and review motion, image quality and audio. Record reproducible evidence before describing the pack as validated.
5. **Versioned publication:** tag immutable files, verify the downloaded ZIP against its manifest, and ensure the website's version, input preview, expected output and submission link agree.

Correctable review notes can describe an issue with an old release. They do not silently change its workflow, prompt, input or archived ZIP. Publish changed assets as a new version. Keep benchmark observations and permission to feature contributor media separate from a pack's source review.
