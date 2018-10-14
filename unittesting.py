import unittest
import unittest.mock
from MAJOR import *
import os

# class TestCalc(unittest.TestCase):
#
#     def test_add(self):
#         result = calc.add(10,2)
#         self.assertEqual(result, 15)

class TestTuna(unittest.TestCase):
    """
    Testing integrity of Tuna Object
    """

    def setUp(self):
        print('Starting test')

    def test_Tuna(self):
        """
        Testing integrity of Tuna Class
        :return: None
        """
        x = Tuna()
        x.setTunaFeatures([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        #Check array
        y = x.getTunaFeatures
        count = 1
        for z in y:
            self.assertEqual(count, z)
            count = count + 1
        #Check tuple
        y = x.getTunaTuple()
        count = 1
        for z in y:
            self.assertEqual(count, z)
            count = count + 1


    # @unittest.mock.patch('messagebox.showinfo', autospec=True)
    def test_save_load(self):
        path = 'c:/temp/test.csv' #Path for file
        #Create Header
        #Data must be in special format
        array = ['a','GEO','DGUID','d','e','f','aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'aaa', 'bbb', 'ccc', 'ddd']
        array2 = ['0','1','2','3','4',"5,5",'6','7','8','9','a','b','c','d','e','f']

        tuna = Tuna()
        tuna.setTunaFeatures(array)
        Data.tunasHeader = tuna
        #Create Data Tuna
        x = Tuna()
        x.setTunaFeatures(array2)
        #Form new array
        Data.tunas = []
        Data.tunas.append(x)
        #Saving file
        Data.tunas_saver(path)

        #Checking loading
        Data.tunasHeader = Tuna()
        Data.tunas = []
        Data.tunas_loader(path)
        x=Data.tunasHeader
        z = x.getTunaFeatures
        #Check 2 arrays at once https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
        for x, y in zip (z, array):
             self.assertEqual(x, y)
        os.remove(path)



if __name__ == '__main__':
    unittest.main()