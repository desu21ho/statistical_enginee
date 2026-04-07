# tests/test_stat_engine.py

import unittest
from src.stat_engine import StatEngine
import math


class TestStatEngine(unittest.TestCase):

    def test_mean(self):
        data = [1, 2, 3, 4, 5]
        engine = StatEngine(data)
        self.assertEqual(engine.get_mean(), 3)

    def test_median_odd(self):
        data = [1, 3, 5]
        engine = StatEngine(data)
        self.assertEqual(engine.get_median(), 3)

    def test_median_even(self):
        data = [1, 2, 3, 4]
        engine = StatEngine(data)
        self.assertEqual(engine.get_median(), 2.5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_standard_deviation(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        engine = StatEngine(data)

        # Known population std = 2
        self.assertAlmostEqual(engine.get_standard_deviation(False), 2)

    def test_mode_multimodal(self):
        data = [1, 1, 2, 2, 3]
        engine = StatEngine(data)
        self.assertCountEqual(engine.get_mode(), [1, 2])

    def test_no_mode(self):
        data = [1, 2, 3, 4]
        engine = StatEngine(data)
        self.assertEqual(engine.get_mode(), "No mode (all values are unique)")


if __name__ == '__main__':
    unittest.main()
