import unittest
import bigMath

class TestMath(unittest.TestCase):
    def test_convertToDecimal(self):
        self.assertAlmostEqual(bigMath.convertToDecimal(str(2.345), str(5)), [2, 3, 4, 5, 0, 0])
        self.assertAlmostEqual(bigMath.convertToDecimal(str(9.5874), str(6)), [9, 5, 8, 7, 4, 0, 0])
        self.assertAlmostEqual(bigMath.convertToDecimal(str(1.25), str(3)), [1, 2, 5, 0])
        self.assertAlmostEqual(bigMath.convertToDecimal(str(3.254), str(5)), [3, 2, 5, 4, 0, 0])
        self.assertAlmostEqual(bigMath.convertToDecimal(str(5.6987), str(12)), [5, 6, 9, 8, 7, 0, 0, 0, 0, 0, 0, 0, 0])