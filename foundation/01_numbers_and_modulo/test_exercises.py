import sys
import unittest
from pathlib import Path

LESSON_DIRECTORY = Path(__file__).resolve().parent
if str(LESSON_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(LESSON_DIRECTORY))

from exercises import (  # noqa: E402
    circular_index,
    count_complete_groups,
    is_even,
    remaining_items,
)


class TestNumbersAndModulo(unittest.TestCase):
    def test_is_even(self) -> None:
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(7))

    def test_circular_index(self) -> None:
        self.assertEqual(circular_index(8, 5), 3)
        self.assertEqual(circular_index(5, 5), 0)
        self.assertEqual(circular_index(-1, 5), 4)

    def test_complete_groups(self) -> None:
        self.assertEqual(count_complete_groups(17, 5), 3)
        self.assertEqual(count_complete_groups(4, 5), 0)

    def test_remaining_items(self) -> None:
        self.assertEqual(remaining_items(17, 5), 2)
        self.assertEqual(remaining_items(20, 5), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
