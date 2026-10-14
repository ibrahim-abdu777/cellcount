import unittest
from src.cellcount import count_rows


class TestRows(unittest.TestCase):
    def test_counts(self):
        self.assertEqual(count_rows(["a|b", "c", "d|e|f"]), 2)


if __name__ == "__main__":
    unittest.main()
