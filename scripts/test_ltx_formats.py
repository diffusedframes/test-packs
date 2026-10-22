import unittest
from ltx_formats import frame_duration, two_stage_size


class LtxFormatTests(unittest.TestCase):
    def test_half_stage_alignment_catches_the_pilot_height_mismatch(self):
        self.assertEqual(two_stage_size(1280, 736), (1280, 704))
        self.assertEqual(two_stage_size(1280, 704), (1280, 704))
        self.assertEqual(two_stage_size(1280, 768), (1280, 768))

    def test_requested_seconds_and_frame_count_duration_are_distinct(self):
        self.assertAlmostEqual(frame_duration(73, 24), 3.0416666666666665)
        with self.assertRaises(ValueError):
            frame_duration(72, 24)
        with self.assertRaises(ValueError):
            frame_duration(73, 0)

    def test_unsupported_geometry_does_not_get_a_false_exact_size(self):
        for pair in [(1280, 735), (32, 704), (True, 704), (1280, 736.0)]:
            with self.assertRaises(ValueError):
                two_stage_size(*pair)


if __name__ == '__main__':
    unittest.main()
