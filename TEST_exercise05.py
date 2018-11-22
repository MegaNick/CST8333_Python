import unittest
from Exercise05 import *

class TestExercise05(unittest.TestCase):
    """ Testing Tuna from Exercise05
        by Nikolay Melnik
    """

    def setUp(self):
        """Test prefix. Printed every test"""
        print("New test by Nikolay Melnik")

    def test_Tuna(self):
        """Testing Tuna is not null"""
        tuna = Tuna("1", "2", "3", "4")
        self.assertIsNotNone(tuna)

    def test_setTunaFeatures(self):
        """Testing Tuna's setTunasFeatures method works"""
        tuna = Tuna()
        array = ["1", "2", "3", "4"]
        tuna.setTunaFeatures(array)
        self.assertEqual(tuna.getTunaFeatures(), array)

    def test_getTunaFeatures(self):
        """Testing Tuna's getTunasFeatures method works"""
        tuna = Tuna("1", "2", "3", "4")
        array = ["1", "2", "3", "4"]
        self.assertEqual(tuna.getTunaFeatures(), array)


