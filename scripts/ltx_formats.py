"""Source-derived geometry checks for the pinned two-stage LTX graph. No ML imports."""

def two_stage_size(width, height):
    """Exposed full-size controls -> half-size integer/32 latent grid -> 2x output."""
    for value in (width, height):
        if type(value) is not int or value < 64 or value % 2:
            raise ValueError('This graph review expects even integer dimensions of at least 64.')
    return tuple(2 * 32 * ((value // 2) // 32) for value in (width, height))


def frame_duration(frames, fps):
    if type(frames) is not int or frames < 1 or (frames - 1) % 8:
        raise ValueError('LTX frame count must be 8n + 1.')
    if not isinstance(fps, (int, float)) or isinstance(fps, bool) or fps <= 0:
        raise ValueError('FPS must be positive.')
    return frames / fps
