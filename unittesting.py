# To the Glory of God!
# CST8333 Project by Nikolay Melnik
""" CST8333_Final_Project by Nikolay Melnik
    unittest module program as a partial fulfillment of the CST8333 course.
    Works with major module by Nikolay Melnik
    Ottawa, ON Canada. September-December 2018
"""
import unittest.mock
from MAJOR import *
import os


class TestTuna(unittest.TestCase):
    """
    Testing integrity of Tuna Object
    """

    counter = 1
    """ Class variable which counts start of a new test"""

    def setUp(self):
        print('Starting test #', TestTuna.counter)
        TestTuna.counter = TestTuna.counter + 1

    def test_Tuna(self):
        """
        Testing integrity of Tuna Class constructor
        :return: None

        Test Method: test_Tuna
        Author: Nikolay Melnik
        Date created: 10/12/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        x = Tuna(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
        #Check received list
        y = x.getTunaFeatures
        count = 1
        for z in y:
            self.assertEqual(count, z)
            count = count + 1

    def test_Tuna_fields_setter_getters(self):
         """
         Testing integrity of Tuna fields inserters and receivers
         :return: None

         Test Method: test_Tuna_fields_setter
         Author: Nikolay Melnik
         Date created: 10/12/2018
         Date last modified: 10/14/2018
         Python Version: 3.7
         """
         x = Tuna()
         x.setTunaFeatures([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
         # Check received list
         y = x.getTunaFeatures
         count = 1
         for z in y:
             self.assertEqual(count, z)
             count = count + 1

    def test_Tuna_fields_tuples(self):
        """
        Testing integrity of Tuna fields receiver as tuple
        :return: None

        Test Method: test_Tuna_fields_tuples
        Author: Nikolay Melnik
        Date created: 10/12/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        x = Tuna()
        x.setTunaFeatures([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        #Check tuple
        y = x.getTunaTuple()
        count = 1
        for z in y:
           self.assertEqual(count, z)
           count = count + 1

    def test_save_load(self):
        """
        Testing creation of CSV files, their integrity and loading
        :return: None

        Test Method: test_save_load
        Author: Nikolay Melnik
        Date created: 10/13/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        # Path for file
        path = 'c:/temp/test.csv'
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

    # Testing analyzeTuna
    def test_analyzeTuna(self):
        """
        Testing test_analyzeTuna method functionality with a list populated with marked Tunas
        :return: None

        Test Method: test_analyzeTuna
        Author: Nikolay Melnik
        Date created: 10/14/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        # Creating Tunas
        tuna = Tuna('1960', 'Canada', '2016A000011124', 'Food available', 'aaa', 'Litres per person, per year',
                    'zzz', 'Units', 'xxx', 'ccc', 'vvv', '10', '', '', '', '2')
        tuna1 = Tuna('1960', 'Canada', '2016A000011124', 'Food available', 'bbb', 'Kilograms per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '300', '', '', '', '2')
        tuna2 = Tuna('1965', 'Canada', '2016A000011124', 'Food available', 'aaa', 'Litres per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '20', '', '', '', '2')
        tuna3 = Tuna('1965', 'Canada', '2016A000011124', 'Food available', 'bbb', 'Kilograms per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '200', '', '', '', '2')
        tuna4 = Tuna('1970', 'Canada', '2016A000011124', 'Food available', 'aaa', 'Litres per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '30', '', '', '', '2')
        tuna5 = Tuna('1970', 'Canada', '2016A000011124', 'Food available', 'bbb', 'Kilograms per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '100', '', '', '', '2')
        # Populating
        Data.tunas = [tuna, tuna1, tuna2, tuna3, tuna4, tuna5]
        Data.analyzeTuna()
        # Extracting
        litres = Data.analyzedTunasLitres.get('aaa')
        kilos = Data.analyzedTunasKilos.get('bbb')
        # Testing
        self.assertEqual(litres.get(1960), 10)
        self.assertEqual(litres.get(1965), 20)
        self.assertEqual(litres.get(1970), 30)
        self.assertEqual(kilos.get(1960), 300)
        self.assertEqual(kilos.get(1965), 200)
        self.assertEqual(kilos.get(1970), 100)

    #Db Table Creator
    def test_db_table_creator(self):
        """
        Testing Table creation in MySQL and checking fields names
        :return: None

        Test Method: test_db_table_creator
        Author: Nikolay Melnik
        Date created: 10/14/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """

        tuna = Tuna('REF_DATE', 'GEO', 'DGUID', 'FOODCATEGORIES', 'COMMODITY', 'UOM', 'UOM_ID',
             'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'VALUE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS')
        tunah = tuna.getTunaFeatures
        Data.tunasHeader = tuna
        Data.db_create_table(self)

        # Checking the result of Table headers

        mydb = mysql.connector.connect(
            host=Data.db_info[0],
            user=Data.db_info[1],
            passwd=Data.db_info[2],
            database=Data.db_info[3]
        )
        mycursor = mydb.cursor()
        mycursor.execute("show columns from py_final_project.records")
        myresult = mycursor.fetchall()

        for x, y in zip(myresult,tunah):
            self.assertEqual(x[0],y)
        mycursor.close()
        mydb.close()

    #Saving Tunas in DB
    def test_save_tunas_in_db(self):
        """
        Testing saving tunas into DB, checking all the names
        :return: None

        Test Method: test_save_tunas_in_db
        Author: Nikolay Melnik
        Date created: 10/14/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        #Creating tunas
        #header
        tuna = Tuna('REF_DATE', 'GEO', 'DGUID', 'FOODCATEGORIES', 'COMMODITY', 'UOM', 'UOM_ID',
             'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'VALUE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS')
        Data.tunasHeader = tuna
        #Other tunas
        tuna = Tuna('1960', 'Canada', '2016A000011124', 'Food available', 'aaa', 'Litres per person, per year',
                    'zzz', 'Units', 'xxx', 'ccc', 'vvv', '10', '', '', '', '2')
        tuna1 = Tuna('1960', 'Canada', '2016A000011124', 'Food available', 'bbb', 'Kilograms per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '300', '', '', '', '2')
        tuna2 = Tuna('1965', 'Canada', '2016A000011124', 'Food available', 'aaa', 'Litres per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '20', '', '', '', '2')
        tuna3 = Tuna('1965', 'Canada', '2016A000011124', 'Food available', 'bbb', 'Kilograms per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '200', '', '', '', '2')
        tuna4 = Tuna('1970', 'Canada', '2016A000011124', 'Food available', 'aaa', 'Litres per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '30', '', '', '', '2')
        tuna5 = Tuna('1970', 'Canada', '2016A000011124', 'Food available', 'bbb', 'Kilograms per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '100', '', '', '', '2')
        # Populating
        Data.tunas = [tuna, tuna1, tuna2, tuna3, tuna4, tuna5]
        # Creating table
        Data.db_create_table(self)
        Data.save_tunas_in_db(self)

    #Testing reading Tunas from DB
    def test_read_tunas_from_db(self):
        """
        Testing reading tunas from DB, checking the names
        :return: None

        Test Method: test_read_tunas_from_db
        Author: Nikolay Melnik
        Date created: 10/14/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        #Creating tunas
        #header
        tuna = Tuna('REF_DATE', 'GEO', 'DGUID', 'FOODCATEGORIES', 'COMMODITY', 'UOM', 'UOM_ID',
             'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'VALUE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS')
        Data.tunasHeader = tuna
        #Other tunas
        tuna = Tuna('1960', 'Canada', '2016A000011124', 'Food available', 'aaa', 'Litres per person, per year',
                    'zzz', 'Units', 'xxx', 'ccc', 'vvv', '10', '', '', '', '2')
        tuna1 = Tuna('1960', 'Canada', '2016A000011124', 'Food available', 'bbb', 'Kilograms per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '300', '', '', '', '2')
        tuna2 = Tuna('1965', 'Canada', '2016A000011124', 'Food available', 'aaa', 'Litres per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '20', '', '', '', '2')
        tuna3 = Tuna('1965', 'Canada', '2016A000011124', 'Food available', 'bbb', 'Kilograms per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '200', '', '', '', '2')
        tuna4 = Tuna('1970', 'Canada', '2016A000011124', 'Food available', 'aaa', 'Litres per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '30', '', '', '', '2')
        tuna5 = Tuna('1970', 'Canada', '2016A000011124', 'Food available', 'bbb', 'Kilograms per person, per year',
                     'zzz', 'Thousands', 'xxx', 'ccc', 'vvv', '100', '', '', '', '2')
        # Populating
        Data.tunas = [tuna, tuna1, tuna2, tuna3, tuna4, tuna5]
        # Creating table
        Data.db_create_table(self)
        Data.save_tunas_in_db(self)
        Data.read_tunas_from_db(self)
        Data.tunas.sort(key=lambda tuna: (tuna.REF_DATE, tuna.COMMODITY))
        self.assertEqual(Data.tunas[0].VALUE, '10')
        self.assertEqual(Data.tunas[1].VALUE, '300')
        self.assertEqual(Data.tunas[2].VALUE, '20')
        self.assertEqual(Data.tunas[3].VALUE, '200')
        self.assertEqual(Data.tunas[4].VALUE, '30')
        self.assertEqual(Data.tunas[5].VALUE, '100')

if __name__ == '__main__':
    unittest.main()