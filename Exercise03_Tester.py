#CST8333_351_Exercise03_Tester By Nikolay Melnik
#Needs Exercise03.py by Nikolay Melnik to work properly
#
import unittest
from Exercise03 import calc


class TestExercise03CalcClass(unittest.TestCase):
    """
    Testing integrity of Exercise03 Calculator class
    Ideas are taken from here https://docs.python.org/3/library/unittest.html
    """

    def setUp(self):
        """
        Overridden Method sets up testing environment. At this case - instantiates calc class
        :return: None
        """
        self.x = calc()  # Instance of calculator from Exercise03

    def test_calc(self):
        print("unittest module by Nikolay Melnik")

        # TESTING ZONE
        self.assertIsNotNone(self.x)
        """
        Testing: has an instance of calc been created?
        """

        self.assertEqual(self.x.addition(2, 2), 4, "Checking Addition")
        """
        Testing if result of 2+2 is equal to 4
        """

        self.assertNotEqual(self.x.addition(2, 2), 5)
        """
        Testing if result of 2+2 is NOT equal to 5
        """

        self.assertEqual(self.x.multiplication(2, 2), 4)
        """
        Testing if result of 2x2 is equal to 4
        """

        self.assertNotEqual(self.x.multiplication(2, 2), 5)
        """
        Testing if result of 2x2 is NOT equal to 5
        """

        self.assertEqual(self.x.subtraction(5, 2), 3)
        """
        Testing if result of 5-2 is equal to 3
        """

        self.assertNotEqual(self.x.subtraction(5, 2), 5)
        """
        Testing if result of 5-2 is NOT equal to 5
        """

        self.assertAlmostEqual(self.x.division(10, 3), 3.33, 2)
        """
        Testing if result of 10/3 is ALMOST equal to 3.3333 with precision of 2 decimal places
        """

        self.assertNotAlmostEqual(self.x.division(10, 3), 3.55, 2)
        """
         Testing if result of 10/3 is ALMOST NOT equal to 3.55 with precision of 2 decimal places
        """

        self.assertEqual(self.x.division(10, 0), "Division by 0 prohibited!")
        """
        Testing division on 0. Must return String 'Division by 0 prohibited!' 
        """


if __name__ == '__main__':
    unittest.main()