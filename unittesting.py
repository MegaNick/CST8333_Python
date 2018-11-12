# To the Glory of God!
# CST8333 Project by Nikolay Melnik
# Combination of unittest test methods
""" CST8333_Final_Project by Nikolay Melnik
    unittest module program as a partial fulfillment of the CST8333 course.
    Works with major module - MAJOR.py by Nikolay Melnik
    Ottawa, ON Canada. September-December 2018
"""
import tkinter

"""
CST8333 18F (350, 351) Dataset Attribution
Attribution and License
The dataset for use in CST8333 18F Section 350, 351 comes from the Open Government of Canada, published by Statistics Canada.

You can obtain the dataset here:
Statistics Canada. (May 30, 2018). Food available in Canada [webpage] Retrieved on August 29, 2018 from https://open.canada.ca/data/en/dataset/a683c640-b5fd-48f8-a0f1-d619b8f7e04c

You need to review the Open Government License which is found here: http://open.canada.ca/en/open-government-licence-canada
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
        """
        Preparation method in testing. Counts tests
        :return: None

        Overridden method: setUp
        Author: Nikolay Melnik
        Date created: 10/14/2018
        Date last modified: 10/20/2018
        Python Version: 3.7
        """
        print('Starting test #', TestTuna.counter)
        TestTuna.counter = TestTuna.counter + 1

        # self.pump_events()

    def tearDown(self):
        """
        Finishing method. Does nothing except printing my name
        :return: None

        Overridden method: tearDown
        Author: Nikolay Melnik
        Date created: 10/14/2018
        Date last modified: 10/20/2018
        Python Version: 3.7
        """
        print('Finished. Tests prepared by Nikolay Melnik')

    def test_classes(self):
        """
        Test methods checks two classes FirstScreen and SecondScreen for integrity. Creates them and checks for null
        :return: None

        Test Method: test_classes
        Author: Nikolay Melnik
        Date created: 10/26/2018
        Date last modified: 10/26/2018
        Python Version: 3.7
        """
        self.root = tkinter.Tk()
        x = FirstScreen(self.root)
        self.assertIsNotNone(x)
        if self.root:
            self.root.destroy()
        x = None
        self.root = tkinter.Tk()
        y = SecondScreen(self.root)
        self.assertIsNotNone(y)
        if self.root:
            self.root.destroy()
        y = None

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
        array = ['REF_DATE', 'GEO', 'DGUID', 'FOODCATEGORIES', 'COMMODITY', 'UOM', 'UOM_ID',
                        'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'VALUE', 'STATUS', 'SYMBOL', 'TERMINATED',
                        'DECIMALS']
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
        self.assertEqual(Data.tunas_saver(path),0)

        #Checking loading
        Data.tunasHeader = Tuna()
        Data.tunas = []
        self.assertEqual(Data.tunas_loader(path),0)
        x = Data.tunas[0]
        z = x.getTunaFeatures
        #Check 2 arrays at once https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
        for x, y in zip (z, array2):
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
            port=Data.db_info[1],
            user=Data.db_info[2],
            passwd=Data.db_info[3],
            database=Data.db_info[4]
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
        #Creating tuna
        tuna = Tuna('1960', 'Canada', '2016A000011124', 'Food available', 'aaa', 'Litres per person, per year',
                    'zzz', 'Units', 'xxx', 'ccc', 'vvv', '10', '', '', '', '2')
        # inserting into Data.tunas
        Data.tunas = [tuna]
        # Creating table
        Data.db_create_table(self)
        Data.save_tunas_in_db(self)
        Data.read_tunas_from_db(self)
        x = tuna.getTunaFeatures
        y = Data.tunas[0].getTunaFeatures
        for z in range(0,16):
            self.assertEqual(x[z], y[z])


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
        # Data.tunas = [tuna, tuna1, tuna2, tuna3, tuna4, tuna5]
        Data.tunas = [tuna5, tuna4, tuna3, tuna2, tuna1, tuna]
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


    def populate_gui(self):
        """
        Support method creates GUI and populates it with predefined data
        :return: Tuple of (Tkinter root, Second screen class)
        :rtype: tuple

        Method: populate_gui
        Author: Nikolay Melnik
        Date created: 10/26/2018
        Date last modified: 10/26/2018
        Python Version: 3.7
        """

        Data.tunas = []
        #Creating an instance of second screen but NO CALL to maninloop
        self.root = tkinter.Tk()
        s = SecondScreen(self.root)
        # Populating user entry boxes with mock data
        s.en_refDate.set(1960)
        s.food_avail.current(0)
        s.en_commodity.set('test')
        s.uom_sel.current(0)
        s.en_uomid.set('aaa')
        s.scal_sel.current(0)
        s.en_scalarid.set('bbb')
        s.en_vector.set('ccc')
        s.en_coordinate.set('ddd')
        s.en_value.set('eee')
        s.en_status.set('fff')
        s.en_symbol.set('ggg')
        s.en_terminated.set('hhh')
        s.en_decimals.set('iii')
        # The same thing in array
        array = ['1960', 'Canada', '2016A000011124', 'Food available', 'test', 'Litres per person, per year', 'aaa',
                 'Units', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii']
        #Returns Tuple of (Tkinter root, Second screen class, array of model)
        return (self.root, s, array)

    # Testing create button
    def test_create_button(self):
        """
        Testing Method Checks "Create Button" functionality by creating mock entry and comparing it after processing
        Using Tkinter instance without root.mainloop()
        :return: None

        Test Method: test_create_button
        Author: Nikolay Melnik
        Date created: 10/26/2018
        Date last modified: 10/26/2018
        Python Version: 3.7
        """
        self.root, s, array = self.populate_gui()
        # Mocking "Create button" click. Idea - http://code.activestate.com/recipes/578978-using-tkinters-invoke-method-for-testing/
        s.frame_bottom5.children['but_create'].invoke()
        # Mocked data as an array

        # Compare fresh Tuna with mocked data
        z = Data.tunas[0].getTunaFeatures
        for x, y in zip (z, array):
            # Must be equal. If not - error
            self.assertEqual(x, y)
        if self.root:
            self.root.destroy()

   # Testing delete button
    def test_delete_button(self):
        """
        Testing Method "presses" Create button with populated data, then focus on the first line in the treeview
        and then "presses" delete button
        Using Tkinter instance without root.mainloop()
        :return: None

        Test Method: test_delete_button
        Author: Nikolay Melnik
        Date created: 10/26/2018
        Date last modified: 10/26/2018
        Python Version: 3.7
        """
        self.root, s, array = self.populate_gui()
        # Mocking "Create button" click. Idea - http://code.activestate.com/recipes/578978-using-tkinters-invoke-method-for-testing/
        s.frame_bottom5.children['but_create'].invoke()
        # Mocked data as an array

        # Compare fresh Tuna with mocked data
        z = Data.tunas[0].getTunaFeatures
        for x, y in zip (z, array):
            # Must be equal. If not - error
            self.assertEqual(x, y)
         # Setting focus
        s.tree.focus(0)
        # "Press" Delete entry button
        s.frame_bottom5.children['but_delete'].invoke()
        # After deletion, tunas length should be 0
        self.assertEqual(len(Data.tunas), 0)
        if self.root:
            self.root.destroy()

   # Testing update button by Nikolay Melnik
    def test_update_button(self):
        """
        Testing Method "presses" Create button with populated data, then focus on the first line in the treeview
        and then "presses" update button with modified entry. Checks for integrity
        Using Tkinter instance without root.mainloop()
        :return: None

        Test Method: test_update_button
        Author: Nikolay Melnik
        Date created: 10/26/2018
        Date last modified: 10/26/2018
        Python Version: 3.7
        """
        self.root, s, array = self.populate_gui()
        # Mocking "Create button" click. Idea - http://code.activestate.com/recipes/578978-using-tkinters-invoke-method-for-testing/
        s.frame_bottom5.children['but_create'].invoke()
        # Mocked data as an array

        # Compare fresh Tuna with mocked data
        z = Data.tunas[0].getTunaFeatures
        for x, y in zip (z, array):
            # Must be equal. If not - error
            self.assertEqual(x, y)
        # Setting focus
        s.tree.focus(0)
        # Mocking new data
        s.en_refDate.set(1961)
        s.food_avail.current(0)
        s.en_commodity.set('aaa')
        s.uom_sel.current(0)
        s.en_uomid.set('bbb')
        s.scal_sel.current(0)
        s.en_scalarid.set('ccc')
        s.en_vector.set('ddd')
        s.en_coordinate.set('eee')
        s.en_value.set('fff')
        s.en_status.set('ggg')
        s.en_symbol.set('hhh')
        s.en_terminated.set('iii')
        s.en_decimals.set('jjj')
        # The same thing in array
        array = ['1961', 'Canada', '2016A000011124', 'Food available', 'aaa', 'Litres per person, per year', 'bbb',
                 'Units', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj']
        # "Press" Update entry button
        s.frame_bottom5.children['but_update'].invoke()
        z = Data.tunas[0].getTunaFeatures
        # Compare after update
        for x, y in zip (z, array):
            # Must be equal. If not - error
            self.assertEqual(x, y)
        if self.root:
            self.root.destroy()

if __name__ == '__main__':
    unittest.main()