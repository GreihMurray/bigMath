import unittest
import bigMath

class TestMath(unittest.TestCase):
    def test_convertToDecimal(self):
        self.assertAlmostEqual(bigMath.convertToDecimal(str(2.345), str(5)), [2, 3, 4, 5, 0, 0])
        self.assertAlmostEqual(bigMath.convertToDecimal(str(9.5874), str(6)), [9, 5, 8, 7, 4, 0, 0])
        self.assertAlmostEqual(bigMath.convertToDecimal(str(1.25), str(3)), [1, 2, 5, 0])
        self.assertAlmostEqual(bigMath.convertToDecimal(str(3.254), str(5)), [3, 2, 5, 4, 0, 0])
        self.assertAlmostEqual(bigMath.convertToDecimal(str(5.6987), str(12)), [5, 6, 9, 8, 7, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_reverseList(self):
        self.assertAlmostEqual(bigMath.reverseList([2, 5, 4, 3, 6]), [6, 3, 4, 5, 2])
        self.assertAlmostEqual(bigMath.reverseList([7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7])
        self.assertAlmostEqual(bigMath.reverseList([9, 5, 1, 3, 7]), [7, 3, 1, 5, 9])
        self.assertAlmostEqual(bigMath.reverseList([9, 3, 1, 7]), [7, 1, 3, 9])
        self.assertAlmostEqual(bigMath.reverseList([3, 6, 9, 8, 7, 4, 1, 2, 5]), [5, 2, 1, 4, 7, 8, 9, 6, 3])

    def test_convertToScientificNotation(self):
        self.assertAlmostEqual(bigMath.convertToScientifcNotation([2, 9, 8, 6, 0, 0, 0]), ("2.986", 6))
        self.assertAlmostEqual(bigMath.convertToScientifcNotation([4, 3, 6, 0, 2, 0, 0]), ("4.3602", 6))
        self.assertAlmostEqual(bigMath.convertToScientifcNotation([5, 0, 2, 3, 0, 0]), ("5.023", 5))
        self.assertAlmostEqual(bigMath.convertToScientifcNotation([9, 4, 0, 2]), ("9.402", 3))
        self.assertAlmostEqual(bigMath.convertToScientifcNotation([8, 9, 4, 3, 5, 2, 5, 0, 0, 2, 0]), ("8.943525002", 10))