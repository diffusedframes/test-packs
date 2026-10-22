# LTX 2.5 I2V · prompting and format review

Checked 22 October 2026. Applies to `ltx-i2v-01 / 0.2.0-pilot` and its pinned two-stage graph. This note adds documentation; it does not change the released ZIP or claim a clean GPU reference run.

## Sources and scope

- [LTX local image-to-video guide](https://docs.ltx.io/open-source-model/usage-guides/image-to-video)
- [LTX prompting guide](https://docs.ltx.io/api-documentation/implementation-guides/prompting-guide/) — its prompt-enhancer section explicitly covers local pipelines/templates; API-specific options are not automatically local features.
- [Comfy template at 447747bf](https://github.com/Comfy-Org/workflow_templates/blob/447747bf37b7e2f6d5fab3f15288e03bf889b82f/templates/video_ltx2_5_i2v.json)
- [Node implementation reviewed at edb3db00](https://github.com/Comfy-Org/ComfyUI/blob/edb3db00fd88f059e748c8a400391b5eab76266b/comfy_extras/nodes_lt.py) — source review, not a claim that every contributor uses this revision.

The beginner guide describes base-stage width/height and doubling them. The pinned template instead exposes nominal final-size controls and halves them through `a/2` before the first latent stage. Its model filenames also differ from the guide's BF16 examples: this pack uses pinned INT8 convrot transformer/text-encoder files. Follow the actual graph and manifest when identifying a measurement condition.

## Prompt review

The local guide recommends motion, camera and audio descriptions for I2V. The general guide favours a flowing present-tense paragraph for a continuous shot, with concrete actions and a focused scene. Four to eight sentences is guidance, not a validator constraint. Prompt enhancement adds a rewrite/inference pass; leaving it off preserves the submitted wording.

Pack v0.2.0 has enhancement off. Its wording asks for a head turn, hand contact with a cup and a push-in during a short shot, while prohibiting cup translation. The hand/prop instruction is a deliberate constraint to evaluate, but “steadies” leaves the manner of contact underspecified. A future control condition can separate a static hand/cup from the head/camera action. That changes the tested action and must receive a new version. Keep failures from the original prompt in that version's observations.

Do not assume the negative-conditioning branch enforces every natural-language exclusion. The pinned distilled graph has fixed dual-CFG settings; record these with the exact negative prompt and distinguish them from a full-model sampling path.

## Exact current input

- `inputs/df-cafe-start.png`, SHA-256 in the released manifest.
- PNG, **1672 × 941**, **8 bits per channel, RGB**, no alpha.
- No embedded ICC, sRGB, gamma/chromaticity or cICP chunk was found in the supplied PNG. It is used as display RGB; a verified colour-managed sRGB conversion is not claimed.
- The image and its checksum are unchanged. The website WebP is a presentation preview and is not the test input.

The graph uses `ResizeImageMaskNode` with longer edge **1536** and **Lanczos** interpolation. `LTXVPreprocess` has `img_compression=18`; in the reviewed implementation it performs a **one-frame H.264 round trip at CRF 18 through yuv420p**, then returns RGB. It is not PNG or JPEG quality 18. The conditioning nodes resize with bilinear interpolation and a centre crop to their latent-derived dimensions, using strengths **0.7** then **1.0**.

Consequently the model receives resized, potentially cropped and compression-processed conditioning, even though the distributed source is a lossless PNG. Source aspect ratio and conditioning aspect ratio differ slightly; that crop belongs in the test's input contract.

## Requested and expected output

| Item | v0.2.0 value |
| --- | --- |
| Requested nominal dimensions | 1280 × 736 |
| First-stage requested dimensions | 640 × 368 |
| First-stage 32-pixel latent alignment | 640 × 352 |
| Expected decoded size after 2× upscale | **1280 × 704** |
| Duration control / FPS | 3 seconds / 24 |
| Frame expression | `duration × FPS + 1` = **73 frames**, satisfying `8n + 1` |
| Exact frame-count duration | **73/24 ≈ 3.041667 seconds** |
| SaveVideo encoding controls | `auto` / `auto`; probe the delivered container/codecs rather than promise them |

The final height follows `2 × 32 × floor((736/2)/32) = 704`. Both final-size controls should be divisible by 64 for this graph to preserve them exactly. That does not apply unchanged to single-stage FLF, IC-LoRA or other pipelines.

**Known issue:** the original v0.2.0 README calls the requested 1280 × 736 value an output size. Treat **1280 × 704 as this graph's expected delivery size**. This correction is a source/format review, not a hidden edit to the archived release. Keep v0.2.0 runs at their original settings and record actual metadata. Any numeric/prompt/input correction belongs to a new pack version.

## Outstanding validation

A clean reference baseline remains pending. A full check must confirm actual graph/software/model versions, input processing, output metadata, visual criteria, audio and measured timing scope. A JSON/hash check or dimensional calculation cannot validate cup control, performance or generation speed. Record startup overrides and concurrent GPU applications for each run; do not infer per-application VRAM use from total GPU memory alone.
