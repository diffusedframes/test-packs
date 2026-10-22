# Run protocol · ltx-i2v-01 / 0.1.0-pilot

**Pilot:** no reference render has been executed. If a control or output differs from this description, report it as a compatibility observation rather than inventing a measurement. No ComfyUI instance, GPU or model is contacted by these documentation files.

## Before measuring

- Record your actual hardware, RAM, OS, driver, ComfyUI backend/frontend, Python, PyTorch/CUDA and attention/offloading configuration. State whether execution is local or cloud and whether other GPU workloads are active.
- Keep model downloads/installations outside the timer. Confirm the exact model files and pinned revision from `manifest.json`; record substitutions explicitly.
- Use the shared input, prompt and preset unchanged. Keep the second/refinement noise seed at 42.
- Record the actual output frame count, dimensions, FPS, codec and container. The upstream duration expression is `duration × FPS + 1`: the preset requests 73 frames at 24 FPS.
- Record peak VRAM only when you have a measurement. State the tool, sampling interval and whether it is dedicated GPU usage or framework allocated/reserved memory; these are different metrics. Never replace “not measured” with zero.

## Timing scope

Use total workflow execution time from the start of executing the queued graph to the output-save node completing. Include model loading when it occurs, conditioning, sampling, latent upscaling/refinement, video/audio decoding and encoding/saving. Record the method (ComfyUI reported duration or stopwatch/log timestamps) and keep it consistent. Exclude time spent waiting in the queue; if that cannot be separated, label queue-inclusive timing and do not compare it as execution-only time.

These are end-to-end workflow measurements, not diffusion-only speed. OS file caches can remain warm; this protocol does not claim cold disk or hardware-cache measurements.

## First run

Only when no existing work would be interrupted, begin with a fresh ComfyUI process with the relevant models unloaded. Set the main seed to **41000**, keep refinement seed **42**, and queue once. Record its status and total seconds. This is the **first-process-run** measurement, including model loading. If you cannot use a fresh process, state that and leave the cold/first-run metric unmeasured.

## Three repeat runs

In the same process, without deliberately unloading models, run sequentially with main seeds **41001**, **41002** and **41003**. Keep all other preset settings identical. Record each run separately and retain each original output. These are three different controlled samples, not three requests for a cached identical graph.

**Verify fresh work:** confirm both sampling stages actually execute for every measured run and a new output is saved. Merely queuing an unchanged workflow can reuse cached work. If sampling is skipped, mark the run cached/invalid and do not count its near-zero time. State any cache settings used. Models may stay loaded; that is intentional for repeat runs. If they offload/reload because of memory pressure, record it.

For a summary, report the median of the three successful repeat durations only when all three are available, with the individual values and measurement scope. With fewer completed runs show the observations without claiming a three-run median. Compare runs with the same model/preset and disclose environment differences.

## Inspect the shots

Watch every measured output at normal speed, then inspect matching early/middle/late frames. Note:

- slow continuous forward/right camera motion;
- straight glass edges and stable mountain geometry;
- reflection coherence and temporal stability;
- unwanted text, logos, people, new objects, flashes or cuts;
- how many of the three repeat shots meet the README acceptance criteria;
- any manual repair or extra generation required, recorded separately from measured workflow time.

Do not add an intro, retime, upscale or colour-grade the evidence clips. If you share a presentation edit, also provide the original measured outputs.

## Failures and submissions

An out-of-memory or compatibility failure is useful. State which step failed, any retry/change and the sanitized error evidence. A failed run has a failure status and optional time-to-failure; it is never a successful zero-second result.

Fill `results.csv` without inserting made-up zeros. Submit it with setup details, all measured outputs and the exact sanitized workflow using the repository result form. Identify any modified preset. Select whether measurements/media may be featured on the website; all GitHub issues are public regardless of that selection.
