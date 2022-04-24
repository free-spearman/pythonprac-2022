import unittest
import prog

class TestSolveSquare(unittest.TestCase):
    def test_lower_zero(self):
        self.assertEqual(prog.solveSquare(10, 1, 1), None)

    def test_equal_zero(self):
        self.assertEqual(prog.solveSquare(2, 4, 2), (-1, -1))

    def test_greater_zero(self):
        self.assertEqual(prog.solveSquare(1, -11, 10), (1, 10))

if __name__ == '__main__':
    unittest.main()