import unittest
from unittest.mock import MagicMock, patch
from prog import solveSquareSquareSquare, SquareIO

class TestSqEq(unittest.TestCase):

    def test_positive_d(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [1, -11, 10])
        SquareIO.printResult = MagicMock()
        solveSquareSquare()
        result = SquareIO.printResult.call_args.args[0]
        assert result == (1.0, 10.0)

    def test_negative_d(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [1, 1, 1000])
        SquareIO.printResult = MagicMock()
        solveSquareSquare()
        result = SquareIO.printResult.call_args.args[0]
        assert result == 'no solution'
        
    def test_zero_d(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [10, -20, 10])
        SquareIO.printResult = MagicMock()
        solveSquareSquare()
        result = SquareIO.printResult.call_args.args[0]
        assert result == (1, 1)
        
    def test_zero_abc(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [0, 0, 0])
        SquareIO.printResult = MagicMock()
        solveSquareSquare()
        result = SquareIO.printResult.call_args.args[0]
        assert result == 'R'
        
    def test_zero_ab(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [0, 0, 7])
        SquareIO.printResult = MagicMock()
        solveSquareSquare()
        result = SquareIO.printResult.call_args.args[0]
        assert result == 'no solution'
        
    def test_zero_a(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [0, 5, 10])
        SquareIO.printResult = MagicMock()
        solveSquareSquare()
        result = SquareIO.printResult.call_args.args[0]
        assert result == (-2.0,)
        
    def test_incorrect_input(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [0, -2, 'hehe'])
        SquareIO.printResult = MagicMock()
        result = SquareIO.printResult.call_args.args[0]
        assert result == 'bad... wrong number entered'
