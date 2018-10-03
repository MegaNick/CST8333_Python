import unittest
import MAJOR

# class TestCalc(unittest.TestCase):
#
#     def test_add(self):
#         result = calc.add(10,2)
#         self.assertEqual(result, 15)

class TestTuna(unittest.TestCase):
    """
    Testing integrity of Tuna Object
    """

    def testTuna(self):
        x = MAJOR.Tuna()
        x.setTunaFeatures([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        y = x.getTunaFeatures()
        count = 1
        for z in y:
            self.assertEqual(count, z)
            count = count + 1

if __name__ == '__main__':
    unittest.main()