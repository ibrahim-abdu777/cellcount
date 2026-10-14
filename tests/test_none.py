import unittest
from src.cellcount import count_rows


class TestNone(unittest.TestCase):
    def test_none(self):
        self.assertEqual(count_rows(["x", "y"]), 0)


if __name__ == "__main__":
    unittest.main()
