"""Unit tests for canSum, howSum, and bestSum."""

import unittest

from best_sum import best_sum_memo, best_sum_tab
from can_sum import can_sum_memo, can_sum_tab
from how_sum import how_sum_memo, how_sum_tab


class TestCanSum(unittest.TestCase):
    def test_memo_examples(self):
        self.assertTrue(can_sum_memo(7, [2, 3]))
        self.assertTrue(can_sum_memo(7, [5, 3, 4, 7]))
        self.assertFalse(can_sum_memo(7, [2, 4]))
        self.assertTrue(can_sum_memo(8, [2, 3, 5]))
        self.assertFalse(can_sum_memo(300, [7, 14]))

    def test_tab_examples(self):
        self.assertTrue(can_sum_tab(7, [2, 3]))
        self.assertTrue(can_sum_tab(7, [5, 3, 4, 7]))
        self.assertFalse(can_sum_tab(7, [2, 4]))
        self.assertTrue(can_sum_tab(8, [2, 3, 5]))
        self.assertFalse(can_sum_tab(300, [7, 14]))

    def test_zero_target(self):
        self.assertTrue(can_sum_memo(0, [1, 2, 3]))
        self.assertTrue(can_sum_tab(0, [1, 2, 3]))


class TestHowSum(unittest.TestCase):
    def _assert_valid(self, combo, target, numbers):
        self.assertIsNotNone(combo)
        self.assertEqual(sum(combo), target)
        for n in combo:
            self.assertIn(n, numbers)

    def test_memo_examples(self):
        self._assert_valid(how_sum_memo(7, [2, 3]), 7, [2, 3])
        self._assert_valid(how_sum_memo(7, [5, 3, 4, 7]), 7, [5, 3, 4, 7])
        self.assertIsNone(how_sum_memo(7, [2, 4]))
        self._assert_valid(how_sum_memo(8, [2, 3, 5]), 8, [2, 3, 5])
        self.assertIsNone(how_sum_memo(300, [7, 14]))

    def test_tab_examples(self):
        self._assert_valid(how_sum_tab(7, [2, 3]), 7, [2, 3])
        self._assert_valid(how_sum_tab(7, [5, 3, 4, 7]), 7, [5, 3, 4, 7])
        self.assertIsNone(how_sum_tab(7, [2, 4]))
        self._assert_valid(how_sum_tab(8, [2, 3, 5]), 8, [2, 3, 5])
        self.assertIsNone(how_sum_tab(300, [7, 14]))

    def test_zero_target(self):
        self.assertEqual(how_sum_memo(0, [1, 2, 3]), [])
        self.assertEqual(how_sum_tab(0, [1, 2, 3]), [])


class TestBestSum(unittest.TestCase):
    def _assert_shortest(self, combo, target, numbers, expected_len):
        self.assertIsNotNone(combo)
        self.assertEqual(sum(combo), target)
        self.assertEqual(len(combo), expected_len)
        for n in combo:
            self.assertIn(n, numbers)

    def test_memo_examples(self):
        self._assert_shortest(best_sum_memo(7, [5, 3, 4, 7]), 7, [5, 3, 4, 7], 1)
        self._assert_shortest(best_sum_memo(8, [2, 3, 5]), 8, [2, 3, 5], 2)
        self._assert_shortest(best_sum_memo(8, [1, 4, 5]), 8, [1, 4, 5], 2)
        self._assert_shortest(best_sum_memo(100, [1, 2, 5, 25]), 100, [1, 2, 5, 25], 4)
        self.assertIsNone(best_sum_memo(7, [2, 4]))

    def test_tab_examples(self):
        self._assert_shortest(best_sum_tab(7, [5, 3, 4, 7]), 7, [5, 3, 4, 7], 1)
        self._assert_shortest(best_sum_tab(8, [2, 3, 5]), 8, [2, 3, 5], 2)
        self._assert_shortest(best_sum_tab(8, [1, 4, 5]), 8, [1, 4, 5], 2)
        self._assert_shortest(best_sum_tab(100, [1, 2, 5, 25]), 100, [1, 2, 5, 25], 4)
        self.assertIsNone(best_sum_tab(7, [2, 4]))

    def test_zero_target(self):
        self.assertEqual(best_sum_memo(0, [1, 2, 3]), [])
        self.assertEqual(best_sum_tab(0, [1, 2, 3]), [])


if __name__ == "__main__":
    unittest.main()
