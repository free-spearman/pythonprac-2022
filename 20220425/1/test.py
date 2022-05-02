import unittest
from solve_line import solve

class TestSqEq(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(0, 10), None)

    def test_2(self):
        self.assertEqual(solve(0, 0), None)
        
    def test_3(self):
        self.assertEqual(solve(2, 0), 0)
        
    def test_4(self):
        self.assertEqual(solve(5, 10), -2)
