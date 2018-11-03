# To the Glory of God!
# CST8333 Project by Nikolay Melnik
# The author used www.lynda.com cycle of lectures about Tkinter - https://www.lynda.com/MyPlaylist/Watch/15528494/184085?autoplay=true
# as an inspiration and major source of ideas for this particular project.
""" CST8333_Final_Project by Nikolay Melnik
    Major module program as a partial fulfillment of the CST8333 course.
    Ottawa, ON Canada. September-December 2018
"""
import threading
import datetime
import time

__version__ = "1.0"
__author__ = "Nikolay Melnik (id-040874855)"

"""
CST8333 18F (350, 351) Dataset Attribution
Attribution and License
The dataset for use in CST8333 18F Section 350, 351 comes from the Open Government of Canada, published by Statistics Canada.

You can obtain the dataset here:
Statistics Canada. (May 30, 2018). Food available in Canada [webpage] Retrieved on August 29, 2018 from https://open.canada.ca/data/en/dataset/a683c640-b5fd-48f8-a0f1-d619b8f7e04c

You need to review the Open Government License which is found here: http://open.canada.ca/en/open-government-licence-canada
"""



# Module imports by Nikolay Melnik
from abc import ABCMeta, abstractmethod
from tkinter import *
# Selective import by Nikolay Melnik
from tkinter import ttk, filedialog
from tkinter import messagebox
from tkinter.font import Font
# Example of import aliasing by Nikolay Melnik
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Simple import by Nikolay Melnik
import csv
import mysql.connector

class TunaSkeleton(metaclass=ABCMeta):
    """
    This TunaSkeleton class is purely abstract class designed to demonstrate Inheritance capability of Python.

    Class: TunaSkeleton
    Extends: object
    Author: Nikolay Melnik
    Date created: 10/1/2018
    Date last modified: 10/14/2018
    Python Version: 3.7
    """

    @abstractmethod
    def setTunaFeatures(self, array=[]):
        """
        Takes an array of parameters - [16] and sets them into created Tuna object
        :param: List of data for Tuna object. places 0 and 12 must be ints, the rest - Strings
        :type: list
        :return: None

        Method: setTunaFeatures
        Author: Nikolay Melnik
        Date created: 10/1/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        pass

    @abstractmethod
    def getTunaFeatures(self):
        """
        Returns all the fields of Tuna object as a list
        :return: [16] - fields of Tuna object as a list String values
        :rtype: list

        Method: getTunaFeatures
        Author: Nikolay Melnik
        Date created: 10/1/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        pass

    @abstractmethod
    def getTunaTuple(self):
        """
        Returns all the fields of Tuna object as a tuple
        :return: (16) - fields of Tuna object in a tuple of Strings
        :rtype: tuple

        Method: getTunaTuple
        Author: Nikolay Melnik
        Date created: 10/1/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        pass

# Class wich extends abstract class TunaSceleton by Nikolay Melnik
class Tuna(TunaSkeleton):
    """
    Tuna class inherits abstract TunaSkeleton. Is the foundation of saving objects in the Assignment.
    Keeps all 16 fields derived from CSV file in individual objects. Classic Tuna Architecture :)

    Class: Tuna
    Extends: TunaSkeleton
    Author: Nikolay Melnik
    Date created: 10/1/2018
    Date last modified: 10/14/2018
    Python Version: 3.7
    """

    # Constructor. TESTED
    def __init__(self, REF_DATE=0, GEO="", DGUID="", FOODCATEGORIES="", COMMODITY="", UOM="", UOM_ID="",
                 SCALAR_FACTOR="", SCALAR_ID="", VECTOR="", COORDINATE="", VALUE="", STATUS="", SYMBOL="", TERMINATED="",
                 DECIMALS=""):
        """
        Tuna Constructor initializes 16 fields of Tuna object as Strings

        :param REF_DATE:
        :param GEO:
        :param DGUID:
        :param FOODCATEGORIES:
        :param COMMODITY:
        :param UOM:
        :param UOM_ID:
        :param SCALAR_FACTOR:
        :param SCALAR_ID:
        :param VECTOR:
        :param COORDINATE:
        :param VALUE:
        :param STATUS:
        :param SYMBOL:
        :param TERMINATED:
        :param DECIMALS:
        :type REF_DATE: str
        :type GEO: str
        :type DGUID: str
        :type FOODCATEGORIES: str
        :type COMMODITY: str
        :type UOM: str
        :type UOM_ID: str
        :type SCALAR_FACTOR: str
        :type SCALAR_ID: str
        :type VECTOR: str
        :type COORDINATE: str
        :type VALUE: str
        :type STATUS: str
        :type SYMBOL: str
        :type TERMINATED: str

        Tuna Constructor
        Author: Nikolay Melnik
        Date created: 10/1/2018
        Date last modified: 10/8/2018
        Python Version: 3.7
        """
        self.REF_DATE = REF_DATE
        self.GEO = GEO
        self.DGUID = DGUID
        self.FOODCATEGORIES = FOODCATEGORIES
        self.COMMODITY = COMMODITY
        self.UOM = UOM
        self.UOM_ID = UOM_ID
        self.SCALAR_FACTOR = SCALAR_FACTOR
        self.SCALAR_ID = SCALAR_ID
        self.VECTOR = VECTOR
        self.COORDINATE = COORDINATE
        self.VALUE = VALUE
        self.STATUS = STATUS
        self.SYMBOL = SYMBOL
        self.TERMINATED = TERMINATED
        self.DECIMALS = DECIMALS

    # Tuna features setter/inserter. TESTED
    def setTunaFeatures(self, array):
        """
        This method sets all the fields from the list array into the Tuna object
        :param: A list of strings [16] holding all fields of the object to be changed
        :type: list[16] of strings
        :return: None

        Method: setTunaFeatures
        Author: Nikolay Melnik
        Date created: 10/1/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        # Assigning one variable's value to another by Nikolay Melnik
        # Also assigning instance variables
        self.REF_DATE = array[0]
        self.GEO = array[1]
        self.DGUID = array[2]
        self.FOODCATEGORIES = array[3]
        self.COMMODITY = array[4]
        self.UOM = array[5]
        self.UOM_ID = array[6]
        self.SCALAR_FACTOR = array[7]
        self.SCALAR_ID = array[8]
        self.VECTOR = array[9]
        self.COORDINATE = array[10]
        self.VALUE = array[11]
        self.STATUS = array[12]
        self.SYMBOL = array[13]
        self.TERMINATED = array[14]
        self.DECIMALS = array[15]

    #Method to get all the fields. TESTED
    @property
    def getTunaFeatures(self):
        """
        The method returns all the fields of the Tuna object as an array of strings
        :return: list [16] - fields of the tuna object
        :rtype: list[16] of strings

        Method: getTunaFeatures
        Author: Nikolay Melnik
        Date created: 10/1/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        x = [self.REF_DATE, self.GEO, self.DGUID, self.FOODCATEGORIES, self.COMMODITY, self.UOM, self.UOM_ID,
             self.SCALAR_FACTOR, self.SCALAR_ID, self.VECTOR,
             self.COORDINATE, self.VALUE, self.STATUS, self.SYMBOL, self.TERMINATED, self.DECIMALS]
        return x

    # Tuna features receiver as a tuple. TESTED
    def getTunaTuple(self):
        """
        The method returns all the fields of the Tuna object as a tuple of Strings
        :return: Tuple (16) - fields of the Tuna object
        :rtype: tuple(16) of strings

        Method: getTunaTuple
        Author: Nikolay Melnik
        Date created: 10/1/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        x = tuple((self.REF_DATE, self.GEO, self.DGUID, self.FOODCATEGORIES, self.COMMODITY, self.UOM, self.UOM_ID,
             self.SCALAR_FACTOR, self.SCALAR_ID, self.VECTOR,
             self.COORDINATE, self.VALUE, self.STATUS, self.SYMBOL, self.TERMINATED, self.DECIMALS))
        return x

# Custom Exception about bad loading by Nikolay Melnik
class LoadError(Exception):
    """
    This class is a template for a custom exception
    Original is taken from here https://docs.python.org/2/tutorial/errors.html

    Class: LoadError
    Extends: Exception
    Author: Nikolay Melnik
    Date created: 10/17/2018
    Date last modified: 10/17/2018
    Python Version: 3.7
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


# Class declaration by Nikolay Melnik
class Data(object):
    """
    This class is holding important data for use through the program. Also holds several methods to work with the data.

    Class: Data
    Extends: object
    Author: Nikolay Melnik
    Date created: 10/1/2018
    Date last modified: 10/14/2018
    Python Version: 3.7
    """

    # Class variable declaration by Nikolay Melnik
    tunas = []
    """List (array) of Tuna objects representing CSV file"""

    tunasHeader = Tuna()
    """A Tuna object with information from the first line of CSV"""

    analyzedTunasLitres = {}
    """Analyzed dictionary of Tunas separated according to litter volume. Keys - years from 1960-2017"""

    analyzedTunasKilos = {}
    """Analyzed dictionary of Tunas separated according to kilogrammes. Keys - years from 1960-2017"""

    currentUOM = ""
    """
    Current UOM in the graph as a string: 'Litres per person, per year' or 'Kilograms per person, per year'
    """

    currentData = {}
    """
    Current data for the graph as dictionary. A copy from analyzedTunasLitres or from analyzedTunasKilos 
    according to user's choice.
    """

    currentKey = ""
    """
    Keys extracted from dictionary to be presented as a choice in GUI
    """

    db_info = ['localhost', '3306','pytester', 'password', 'py_final_project']
    """
    MySQL credentials: ('host', 'port', 'user', 'passwd', 'db')
    """

    #Loading CSV file by Nikolay Melnik. TESTED
    def tunas_loader(x=''):
        """
        This class method is taking a full file path and loading a CSV File, check it's integrity and then
        transfers it into list (array) of Tunas
        :param: String having a full filepath to CSV file
        :type: str
        :return: int of error or succes: 0 - ok, 1- IOError, 2 - error - data corrupted. The array is put into class variable Data.tunas[]
        :rtype: int

        Method: tunas_loader
        Author: Nikolay Melnik
        Date created: 10/9/2018
        Date last modified: 10/25/2018
        Python Version: 3.7
        """
        # Loading file with WITH statement by Nikolay Melnik (abridged!)
        tunas = []
        try:
            with open(x, 'r') as f:

                dialect = csv.Sniffer().sniff(f.read(1024))
                f.seek(0)
                reader = csv.reader(f, dialect)
                count = 0
                for x in reader:
                    temp = []
                    for z in x:
                        # ASCII filter from https://stackoverflow.com/questions/40872126/python-replace-non-ascii-character-in-string/40872225
                        z = re.sub(r'[^\x20-\x7f]',r'', z)
                        z = z.replace('"','')
                        temp.append(z)

                    # Are we processing correct file?
                    if count == 0:
                        if (temp[1] != 'GEO') or (temp[2] != 'DGUID'):
                            raise LoadError("Data set is corrupted or not specified")

                    # if a contains 16 elements, we are good, if not, rise exception
                    if len(temp) != 16:
                        raise LoadError("Data set is corrupted or not specified")

                    #Math by Nikolay Melnik
                    count = count + 1

                    # Create Tuna object by Nikolay Melnik
                    tuna = Tuna()
                    # Using object's methods by Nikolay Melnik
                    tuna.setTunaFeatures(temp)
                    tunas.append(tuna)

        except IOError:
            # If loading failed
            return 1
        except LoadError:
            # If data corrupted
            return 2
        # If all ok - continue
        Data.tunas = tunas
        Data.tunasHeader = tunas[0]
        Data.tunas.pop(0)
        # Sorting Tunas. Idea is taken from https://andrefsp.wordpress.com/2012/02/27/sorting-object-lists-in-python/
        # and https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
        Data.tunas.sort(key=lambda tuna: (tuna.REF_DATE, tuna.COMMODITY))
        # If all ok
        return 0


    #Saving tunas to CSV by Nikolay Melnik. TESTED
    @staticmethod
    def tunas_saver(name=""):
        """
        Saving Tunas into a CSV file according to the given path
        :param: String having a full filepath to CSV file
        :type: str
        :return: Int value of error or success: 0 - all ok, 1 - error during saving
        :rtype: int

        Method: tunas_saver
        Author: Nikolay Melnik
        Date created: 10/9/2018
        Date last modified: 10/25/2018
        Python Version: 3.7
        """
        #Open file for processing. Some ideas are form here https://www.pythonforbeginners.com/csv/using-the-csv-module-in-python
        # Simple file writing and exception handling by Nikolay Melnik
        try:
            f = open(name, "w", newline='')
            writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerow(['REF_DATE', 'GEO', 'DGUID', 'FOODCATEGORIES', 'COMMODITY', 'UOM', 'UOM_ID',
                        'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'VALUE', 'STATUS', 'SYMBOL', 'TERMINATED',
                        'DECIMALS'])
            for tuna in Data.tunas:
                writer.writerow(tuna.getTunaFeatures)
        except IOError as error:
            return 1
        finally:
            # If variable 'f' - file exists, close it
            if 'f' in locals():
                f.close()
        return 0

    # CSV array analyzer by Nikolay Melnik. TESTED
    @staticmethod
    def analyzeTuna():
        """
        Static method analyzes Data.tunas list. Skips all the 'Food available adjusted for losses' positions.
        Creates two dictionaries: Data.analyzedTunasLitres and Data.analyzedTunasKilos separated according to FOODCATEGORIES:
        'Litres per person, per year' and 'Kilograms per person, per year'. Every dictionary has a key: a int number in between 1960 and 2017
        and a float of VALUE. This dictionaries will be used in graph representation
        :return: None. Changes made in Data.analyzedTunasKilos and Data.analyzedTunasLitres

        Method: analyzeTuna
        Author: Nikolay Melnik
        Date created: 10/3/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        #Erasing data
        Data.analyzedTunasKilos = {}
        Data.analyzedTunasLitres = {}
        for x in Data.tunas:
            # Skip adjusted for losses food. Graph shouldn't be too complicated
            # Another thing is eliminating repetition
            try:
                #Skipping adjusted for losses food
                if x.FOODCATEGORIES == 'Food available adjusted for losses':
                    continue
                if x.UOM == 'Litres per person, per year':
                    key = x.COMMODITY
                    temp = Data.analyzedTunasLitres.get(key)
                    if temp is None:
                        Data.analyzedTunasLitres.update({key: {int(x.REF_DATE): float(x.VALUE)}})
                    else:
                        temp.update({int(x.REF_DATE): float(x.VALUE)})
                        Data.analyzedTunasLitres.update({key: temp})
                elif x.UOM == 'Kilograms per person, per year':
                    key = x.COMMODITY
                    temp = Data.analyzedTunasKilos.get(key)
                    if temp is None:
                        Data.analyzedTunasKilos.update({key: {int(x.REF_DATE): float(x.VALUE)}})
                    else:
                        temp.update({int(x.REF_DATE): float(x.VALUE)})
                        Data.analyzedTunasKilos.update({key: temp})
            except ValueError as error:
                # This is done if there is garbage in columns
                continue

    # DB Mysql creating table. TESTED
    # ideas from here https://www.w3schools.com/python/python_mysql_select.asp
    def db_create_table(self):
        """
        Method creates table 'records' in database from Data.db_info (by default - py_final_project)
        May show GUI error in case of error
        :return: int 0 - all ok, 1 -error. Table created in DB
        :rtype: int

        Method: db_create_table
        Author: Nikolay Melnik
        Date created: 10/14/2018
        Date last modified: 10/25/2018
        Python Version: 3.7
        """
        try:
            mydb = mysql.connector.connect(
                host=Data.db_info[0],
                port=Data.db_info[1],
                user=Data.db_info[2],
                passwd=Data.db_info[3],
                database=Data.db_info[4]
            )
            mycursor = mydb.cursor()
            # Dropping table
            sql = "DROP TABLE IF EXISTS records"
            mycursor.execute(sql)
            # Creating new table
            sql = 'CREATE TABLE records ('
            #header info
            x = ['REF_DATE', 'GEO', 'DGUID', 'FOODCATEGORIES', 'COMMODITY', 'UOM', 'UOM_ID',
                        'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'VALUE', 'STATUS', 'SYMBOL', 'TERMINATED',
                        'DECIMALS']
            count = 0
            for y in x:
                sql = sql+'`'+y+'`'+' VARCHAR(100)'
                # add comma if not the last block
                if count <15:
                    sql = sql + ','
                count = count + 1
            sql = sql + ')'
            mycursor.execute(sql)
            mydb.commit()
            return 0
        except (Exception) as error:
            return 1
        finally:
            # Checking variable for existance https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists
            if 'mycursor' in locals():
                mycursor.close()
            if 'mydb' in locals():
                mydb.close()

    #Save tunas in DB. TESTED
    # ideas from here https://www.w3schools.com/python/python_mysql_insert.asp
    def save_tunas_in_db(self):
        """
        Method saves current tunas into MySQL 'records' DB.
        May show GUI error in case of error
        :return: int 0 - all ok, 1 - error
        :rtype: int

        Method: save_tunas_in_db
        Author: Nikolay Melnik
        Date created: 10/14/2018
        Date last modified: 10/25/2018
        Python Version: 3.7
        """
        # Open DB
        try:
            mydb = mysql.connector.connect(
                host=Data.db_info[0],
                port=Data.db_info[1],
                user=Data.db_info[2],
                passwd=Data.db_info[3],
                database=Data.db_info[4]
            )
            mycursor = mydb.cursor()
            #Preparing transaction
            sql = "INSERT INTO records VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            for x in Data.tunas:
                val = x.getTunaTuple()
                mycursor.execute(sql, val)
            # Commit transaction
            mydb.commit()
            return 0
        except Exception as error:
            return 1
        finally:
            # Checking variable for existance https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists
            if 'mycursor' in locals():
                mycursor.close()
            if 'mydb' in locals():
                mydb.close()

    # Tunas loader from DB. TESTED
    def read_tunas_from_db(self):
        """
        Method reads Tunas from DB. Reads Header into Data.tunasHeader and data into Data.tunas
        :return: None

        Method: read_tunas_from_db
        Author: Nikolay Melnik
        Date created: 10/14/2018
        Date last modified: 10/25/2018
        Python Version: 3.7
        """
        tunas = []
        try:
            mydb = mysql.connector.connect(
                host=Data.db_info[0],
                port=Data.db_info[1],
                user=Data.db_info[2],
                passwd=Data.db_info[3],
                database=Data.db_info[4]
            )
            mycursor = mydb.cursor()
            #Receive Header names
            tuna = Tuna()
            mycursor.execute("show columns from py_final_project.records")
            myresult = mycursor.fetchall()
            y = []
            for x in myresult:
                y.append(x[0])
            tuna.setTunaFeatures(y)
            Data.tunasHeader = tuna
            # Receive all rows
            mycursor.execute("SELECT * FROM records")

            myresult = mycursor.fetchall()

            for x in myresult:
                tuna = Tuna()
                tuna.setTunaFeatures(list(x))
                tunas.append(tuna)
        except Exception:
            messagebox.showerror("MySQL READING ERROR",
                                 "There was an ERROR during loading from DB\nPlease press OK and repeat loading")
            return 1
        finally:
            # Checking variable for existance https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists
            if 'mycursor' in locals():
                mycursor.close()
            if 'mydb' in locals():
                mydb.close()
        # If all ok - continue
        Data.tunas = tunas
        # Sorting Tunas. Idea is taken from https://andrefsp.wordpress.com/2012/02/27/sorting-object-lists-in-python/
        # and https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
        Data.tunas.sort(key=lambda tuna: (tuna.REF_DATE, tuna.COMMODITY))
        return 0

# Second GUI Starter
class SecondScreen(object):
    """
    Class responsible for GUI and call backs of the Second window

    Class: SecondScreen
    Extends: object
    Author: Nikolay Melnik
    Date created: 10/7/2018
    Date last modified: 10/14/2018
    Python Version: 3.7
    """

    # Class Variable for sorting
    # class variable to track direction of column
    # header sort
    SortDir = True
    """Class variable responsible for ascending/descending style of treeview
        true - ascending, false - descending        
    """

    def run_clocks(self):
        """
        Method shows elapsed program time in seconds. Run as Tkinter thread.
        Restarts itself every second, synchronize itself with system clock
        :return: None

        Method: run_clocks
        Author: Nikolay Melnik
        Date created: 10/26/2018
        Date last modified: 10/26/2018
        Python Version: 3.7
        """
        # calculate difference from start until now and print it in the Label
        x = str(int((datetime.datetime.now() - self.clock).total_seconds()))
        self.timeLabel.set('Program run time:'+x)
        self.root.after(1, self.run_clocks)

    # printing graph data
    def printGraph(self, master):
        """
        Method prints graph in the second window according to supplied data. All the ideas are taken from the developer's
        website - https://matplotlib.org/
        :param: master: Tkinter object of the parent widget
        :type Tkinter object
        :return: None

        Method: printGraph
        Author: Nikolay Melnik
        Date created: 10/8/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """

        # Grid Graphic forgetter. Made to forget all the widgets in row 1
        # Taken from here https://stackoverflow.com/questions/23189610/remove-widgets-from-grid-in-tkinter
        for label in self.frame_top.grid_slaves():
            if int(label.grid_info()["row"]) == 1:
                label.grid_forget()

        # Data for plotting
        # Taken from https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py
        # Re-declare type by Nikolay Melnik
        z = 1000 # Here z is int
        z = Data.currentData.get(Data.currentKey) # Here z is dictionary
        # Declare variable x as list by Nikolay Melnik
        x = []
        #Years to observe
        # Decision structures by Nikolay Melnik
        for y in range(1960, 2017):
            if z is None:
                x.append(0)
            else:
                k = z.get(y)
                if k is None:
                    x.append(0)
                else:
                    x.append(k)

        t = np.arange(1960, 2017, 1)
        fig, ax = plt.subplots()
        fig.set_dpi(80)
        fig.set_figwidth(13)
        ax.plot(t, x)
        ax.set(xlabel='YEAR', ylabel=Data.currentUOM,
               title='Availability variation 1960-2017')
        ax.grid()
        canvas = FigureCanvasTkAgg(fig, master)
        canvas.draw()
        canvas.get_tk_widget().grid(row=3, column=0, columnspan=4, pady=10)

    ### This Block is taken from https://pyinmyeye.blogspot.com/2012/07/tkinter-multi-column-list-demo.html
    ### Adjusted fot This final project
    def list_panel(self, mf):
        """
        This method creates treeview (Listview) of the tunas list derivied from CSV data class.
        Also it is capable to create user's data and supplies information for other GUI modules
        The code and ideas were taken from https://pyinmyeye.blogspot.com/2012/07/tkinter-multi-column-list-demo.html
        Design and implementation were changed according to Project requirements.
        :param mf: Parent widget (window) where will be put this treeview
        :type: Tkinter module (frame)
        :return: None

        Method: list_panel
        Author: Nikolay Melnik
        Date created: 10/8/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """

        # Remove all slaves. Taken from here https://stackoverflow.com/questions/12364981/how-to-delete-tkinter-widgets-from-a-window
        list = mf.pack_slaves()
        for l in list:
            l.destroy()

        demoPanel = Frame(mf)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
        self._create_treeview(demoPanel)
        self._load_data()

    def _create_treeview(self, parent):
        """
        This method is a part of list_panel method. Creates GUI sceleton for future processing
        The code and ideas were taken from https://pyinmyeye.blogspot.com/2012/07/tkinter-multi-column-list-demo.html
        Design and implementation were changed according to Project requirements.
        :param parent: Parent frame
        :type: Tkinter frame object
        :return: None

        Method: _create_treeview
        Author: Nikolay Melnik
        Date created: 10/8/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        f = ttk.Frame(parent)
        f.pack(side=TOP, fill=BOTH, expand=Y)

        # create the tree and scrollbars
        self.dataCols = ('REF_DATE', 'GEO       ', 'DGUID               ', 'FOODCATEGORIES                    ',
                         'COMMODITY                               ',
                         'UOM                                    ', 'UOM_ID', 'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR      ',
                         'COORDINATE', 'VALUE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS')
        self.tree = ttk.Treeview(columns=self.dataCols, show='headings')

        ysb = ttk.Scrollbar(orient=VERTICAL, command=self.tree.yview)
        xsb = ttk.Scrollbar(orient=HORIZONTAL, command=self.tree.xview)
        self.tree['yscroll'] = ysb.set
        self.tree['xscroll'] = xsb.set

        # add tree and scrollbars to frame
        self.tree.grid(in_=f, row=0, column=0, sticky=NSEW, padx=5)
        ysb.grid(in_=f, row=0, column=1, sticky=NS)
        xsb.grid(in_=f, row=1, column=0, sticky=EW)

        # set frame resize priorities
        f.rowconfigure(0, weight=1)
        f.columnconfigure(0, weight=1)

        # Setting call back function for treeview
        self.tree.bind("<ButtonRelease-1>", self.treeViewClick)

    def treeViewClick(self, event):
        """
        Call back method assigned by treeview. Called when user clicks mouse o treeview objects
        :param event: Ignored
        :type: Virtual event method
        :return: None but copies data from selected row (tuna) to the GUI

        Method: treeViewClick
        Author: Nikolay Melnik
        Date created: 10/8/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        # Getting focus from treeview as an objects ID number
        curItem = self.tree.focus()
        #Transfer commodities
        x = self.tree.item(curItem).get('values')
        #Avoid wrong x type
        if type(x) is not list:
            return
        # Copying values to GUI
        self.en_refDate.set(x[0])
        if x[3] == 'Food available':
            self.food_avail.current(0)
        else:
            self.food_avail.current(1)
        self.en_commodity.set(x[4])
        if x[5] == 'Litres per person, per year':
            self.uom_sel.current(0)
        else:
            self.uom_sel.current(1)
        self.en_uomid.set(x[6])
        if x[7] == 'units ':
            self.scal_sel.current(0)
        else:
            self.scal_sel.current(1)
        self.en_scalarid.set(x[8])
        self.en_vector.set(x[9])
        self.en_coordinate.set(x[10])
        self.en_value.set(x[11])
        self.en_status.set(x[12])
        self.en_symbol.set(x[13])
        self.en_terminated.set(x[14])
        self.en_decimals.set(x[15])

    def _load_data(self):
        """
        Method takes data from Data.tunas list and unpack it into treeview.
        Gives to every row object an ID for future processing starting from 0
        The code and ideas were taken from https://pyinmyeye.blogspot.com/2012/07/tkinter-multi-column-list-demo.html
        Design and implementation were changed according to Project requirements.
        :return: None

        Method: _load_data
        Author: Nikolay Melnik
        Date created: 10/8/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        # Unpacking tuna into list of tuples
        # looping structures - for loop by Nikolay Melnik
        self.data = []
        for x in Data.tunas:
            self.data.append(x.getTunaTuple())

        # configure column headings
        for c in self.dataCols:
            self.tree.heading(c, text=c.title(), command=lambda c=c: self._column_sort(c, SecondScreen.SortDir))
            self.tree.column(c, width=Font().measure(c.title()))

        # Add counter for ID
        count = 0
        # add data to the tree
        for item in self.data:
            self.tree.insert('', 'end', iid=count, values=item)
            count = count + 1

    def _column_sort(self, col, descending=False):
        """
        Call back method for sorting columns. Part of treeview, designed for lambda function
        The code and ideas were taken from https://pyinmyeye.blogspot.com/2012/07/tkinter-multi-column-list-demo.html
        Design and implementation were changed according to Project requirements.
        :param col: Column to be sorted
        :param descending: Ascending or descending sorting. True for descending, False for ascending
        :type col: string
        :type descending:
        :return: None. Sorted column

        Method: _column_sort
        Author: Nikolay Melnik
        Date created: 10/8/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """

        # grab values to sort as a list of tuples (column value, column id)
        # e.g. [('Apple juice', 'I001'), ('Apple pie filling', 'I002'), ('Apple sauce', 'I003')]
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]

        # reorder data
        # tkinter looks after moving other items in
        # the same row
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            self.tree.move(item[1], '', indx)  # item[1] = item Identifier

        # reverse sort direction for next sort operation
        SecondScreen.SortDir = not descending

    ####### End of Tree view


    # Passing self is the pathing an instance to the method
    # By Nikolay Melnik
    def save_file_button(self):
        """
        Call back method to be called when user chooses "Save file" on the menu
        Calls FileChooser to get file path and submits it to Data.tunas_saver
        :return: None

        Method: save_file_button
        Author: Nikolay Melnik
        Date created: 10/8/2018
        Date last modified: 10/17/2018
        Python Version: 3.7
        """
        # Call filechooser
        filename = filedialog.asksaveasfilename(filetypes=(("Comma-separated files", "*.csv"), ("All files", "*.*")))
        if filename is None or filename == '':
            # Return if Cancel is pressed
            return
        x = Data.tunas_saver(filename)
        #Printing return messageboxes: 0 - ok, 1 - error
        if x == 0:
            messagebox.showinfo("SAVING SUCCESS", "Your File was successfully saved\nPlease press OK to continue")
        elif x == 1:
            messagebox.showerror("FILE SAVING ERROR",
                             "There was an ERROR during saving\nPlease press OK and repeat saving")
            return

        # Useless loop for looping demo by Nikolay Melnik
        c = 0
        while c < 5:
            c = c + 1

    def boxes_clear(self):
        """
        Cleans all entry boxes in the Second window GUI
        :return: None

        Method: boxes_clear
        Author: Nikolay Melnik
        Date created: 10/10/2018
        Date last modified: 10/17/2018
        Python Version: 3.7
        """
        #Clearing boxes
        self.en_refDate.set('')
        self.food_avail.current(0)
        self.en_commodity.set('')
        self.uom_sel.current(0)
        self.en_uomid.set('')
        self.scal_sel.current(0)
        self.en_scalarid.set('')
        self.en_vector.set('')
        self.en_coordinate.set('')
        self.en_value.set('')
        self.en_status.set('')
        self.en_symbol.set('')
        self.en_terminated.set('')
        self.en_decimals.set('')

    def new_file(self):
        """
        Call back method is run when user chooses New File in File menu
        Does not take any parameters. Does not return any. Cleans all variables, kills all tunas and cleans GUI screens
        :return:None

        Method: new_file
        Author: Nikolay Melnik
        Date created: 10/10/2018
        Date last modified: 10/17/2018
        Python Version: 3.7
        """
        #Delete all Tunas
        Data.tunas = []
        Data.currentData = {}
        Data.currentUOM = 'Litres per person, per year'
        self.keysList = []
        Data.currentKey = ""
        self.comm['values'] = self.keysList
        self.comm.set('')

        #Making Graph again
        #Refresh graph
        self.printGraph(self.frame_top)
        #Refresh List
        self.list_panel(self.frame_bottom1)
        self.boxes_clear()

    def save_to_db(self):
        """
        Call back method is run when user chooses 'Save to Database' in File menu
        Does not take any parameters. Does not return any. Saves data into DB and prompts success or failure
        :return: None

        Method: save_to_db
        Author: Nikolay Melnik
        Date created: 10/25/2018
        Date last modified: 10/25/2018
        Python Version: 3.7
        """
        # Creating table
        x = Data.db_create_table(self)
        # Saving to db
        y = Data.save_tunas_in_db(self)
        # Check for errors
        if x == 0 and y == 0:
            messagebox.showinfo("SAVING SUCCESS", "Your File was successfully saved to Database\nPlease press OK to continue")
        else:
            messagebox.showerror("MySQL SAVING ERROR",
                                 "There was an ERROR during saving to Database\nPlease press OK and repeat saving")

    def load_from_db(self):
        """
        Call back method is run when user chooses 'Load from Database' in File menu
        Does not take any parameters. Does not return any. Loads data from DB as a new data set
        :return: None

        Method: load_from_db
        Author: Nikolay Melnik
        Date created: 10/25/2018
        Date last modified: 10/25/2018
        Python Version: 3.7
        """
        # Loading data from the Database
        x = Data.read_tunas_from_db(self)
        if x == 0:
            messagebox.showinfo("LOAD SUCCESS", "Your File was successfully loaded\nPlease press OK to continue")
        elif x == 1:
            messagebox.showerror("MySQL READING ERROR",
                                 "There was an ERROR during loading from DB\nPlease press OK and repeat loading")
        # If no tunas loaded - exit
        # if len(Data.tunas) < 1:
        #     return
        # Cleaning GUI boxes
        self.boxes_clear()
        #Delete all Tunas
        # Data.tunas = []
        Data.currentData = {}
        Data.currentUOM = 'Litres per person, per year'
        self.keysList = []
        Data.currentKey = ""
        self.comm['values'] = self.keysList
        self.comm.set('')

        #Default values for boxes just to make sure that there is no repetition
        Data.analyzeTuna()
        Data.currentUOM = 'Litres per person, per year'
        Data.currentData = Data.analyzedTunasLitres
        self.keysList = list(Data.currentData.keys())
        self.comm['values'] = self.keysList
        self.comm.set('')
        #Printing Graph
        self.printGraph(self.frame_top)
        #Refresh List
        self.list_panel(self.frame_bottom1)

    def open_file(self):
        """
        Call back method is run when user chooses 'Open File' in File menu
        Does not take any parameters. Does not return any. Loads data from file as a new data set
        :return: None

        Method: open_file
        Author: Nikolay Melnik
        Date created: 10/25/2018
        Date last modified: 10/25/2018
        Python Version: 3.7
        """
        # Call filechooser
        filename = filedialog.askopenfile(filetypes=(("Comma-separated files", "*.csv"), ("All files", "*.*")))
        if filename is None: return  # Return if Cancel is pressed

        #Load file and process Tunas
        x = Data.tunas_loader(filename.name)
        if x == 0:
            messagebox.showinfo("LOAD SUCCESS", "Your File was successfully loaded\nPlease press OK to continue")
        elif x == 1:
            messagebox.showerror("FILE READING ERROR",
                                 "There was an ERROR during loading\nPlease press OK and repeat loading")
            return
        elif x == 2:
            messagebox.showerror("FILE READING ERROR",
                                 "Data set is corrupted or not specified\nPlease press OK and repeat loading")
            return

        # # Return if no Tunas loaded
        # if len(Data.tunas) == 0:
        #     return
        # Cleaning GUI boxes
        self.boxes_clear()

        #Delete all Tunas
        # Data.tunas = []
        Data.currentData = {}
        Data.currentUOM = 'Litres per person, per year'
        self.keysList = []
        Data.currentKey = ""
        self.comm['values'] = self.keysList
        self.comm.set('')

        #Default values for boxes just to make sure that there is no repetition
        Data.analyzeTuna()
        Data.currentUOM = 'Litres per person, per year'
        Data.currentData = Data.analyzedTunasLitres
        self.keysList = list(Data.currentData.keys())
        self.comm['values'] = self.keysList
        #Printing Graph
        self.printGraph(self.frame_top)
        #Refresh List
        self.list_panel(self.frame_bottom1)


    # ********* GUI Buttons callbacks *********
    #Create button pressed. TESTED
    def create_button(self):
        """
        Call back method when user clicks 'Create new entry' button
        Does not take any parameters. Does not return any. It takes all entered information from GUI screen,
        checks refDate box value for validity (should be between 1960 - 2017). If it's not - throws error box.
        Then creates a tuna with given data  and INSERTs it into array of tunas. Also does sorting.
        :return: None

        Method: create_button
        Author: Nikolay Melnik
        Date created: 10/10/2018
        Date last modified: 10/17/2018
        Python Version: 3.7
        """
        #Create an array and fill it with data from the screen
        tu = []
        # Checking refDate for validity, should be 1960-2017
        tu.append(self.en_refDate.get())
        try:
            x = int(tu[0])
            if x < 1960 or x > 2017:
                raise ValueError
        except ValueError:
            # Entry is wrong, showing error box and exits
            messagebox.showerror("ENTRY ERROR",
                                 "REF_DATE must be between 1960 and 2017")
            return
        tu.append('Canada')
        tu.append('2016A000011124')
        tu.append(self.food_avail.get())
        tu.append(self.en_commodity.get())
        tu.append(self.uom_sel.get())
        tu.append(self.en_uomid.get())
        tu.append(self.scal_sel.get())
        tu.append(self.en_scalarid.get())
        tu.append(self.en_vector.get())
        tu.append(self.en_coordinate.get())
        tu.append(self.en_value.get())
        tu.append(self.en_status.get())
        tu.append(self.en_symbol.get())
        tu.append(self.en_terminated.get())
        tu.append(self.en_decimals.get())
        # Creating Tuna and populating it with data
        tuna = Tuna()
        tuna.setTunaFeatures(tu)
        # INSERTs Tuna into tunas list by Nikolay Melnik
        Data.tunas.append(tuna)
        # Cleaning GUI boxes
        self.boxes_clear()

        #Default values for boxes just to make sure that there is no repetition
        Data.analyzeTuna()
        Data.currentUOM = 'Litres per person, per year'
        Data.currentData = Data.analyzedTunasLitres
        self.keysList = list(Data.currentData.keys())
        self.comm['values'] = self.keysList

        # Sorting Tunas. Idea is taken from https://andrefsp.wordpress.com/2012/02/27/sorting-object-lists-in-python/
        # and https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
        Data.tunas.sort(key=lambda tuna: (tuna.REF_DATE, tuna.COMMODITY))

        #Printing Graph
        self.printGraph(self.frame_top)
        #Refresh List
        self.list_panel(self.frame_bottom1)

    #Update Button pressed. TESTED
    def update_button(self):
        """
        Call back method when user clicks 'Update entry' button
        Does not take any parameters. Does not return any. It takes all entered information from GUI screen,
        checks refDate box value for validity (should be between 1960 - 2017). If it's not - throws error box.
        Then it finds correct tuna in the list and updates it with a new tuna. Also does sorting.
        :return: None

        Method: update_button
        Author: Nikolay Melnik
        Date created: 10/11/2018
        Date last modified: 10/17/2018
        Python Version: 3.7
        """
        # If no focus - return
        x = self.tree.focus()
        if x == '':
            return
        x = int(x)
        #Create an array and fill it with data from the screen
        tu = []
        # Checking refDate for validity, should be 1960-2017
        tu.append(self.en_refDate.get())
        try:
            y = int(tu[0])
            if y < 1960 or y > 2017:
                raise ValueError
        except ValueError:
            # Entry is wrong, showing error box and exits
            messagebox.showerror("ENTRY ERROR",
                                 "REF_DATE must be between 1960 and 2017")
            return
        tu.append('Canada')
        tu.append('2016A000011124')
        tu.append(self.food_avail.get())
        tu.append(self.en_commodity.get())
        tu.append(self.uom_sel.get())
        tu.append(self.en_uomid.get())
        tu.append(self.scal_sel.get())
        tu.append(self.en_scalarid.get())
        tu.append(self.en_vector.get())
        tu.append(self.en_coordinate.get())
        tu.append(self.en_value.get())
        tu.append(self.en_status.get())
        tu.append(self.en_symbol.get())
        tu.append(self.en_terminated.get())
        tu.append(self.en_decimals.get())
        tuna = Tuna()
        tuna.setTunaFeatures(tu)
        self.boxes_clear()

        #replacing old Tuna
        Data.tunas[x] = tuna

        # Sorting Tunas. Idea is taken from https://andrefsp.wordpress.com/2012/02/27/sorting-object-lists-in-python/
        # and https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
        Data.tunas.sort(key=lambda tuna: (tuna.REF_DATE, tuna.COMMODITY))

        #Default values for boxes to avoid repetition
        Data.analyzeTuna()
        if Data.currentUOM == 'Litres per person, per year':
            Data.currentData = Data.analyzedTunasLitres
        else:
            Data.currentData = Data.analyzedTunasKilos
        self.keysList = list(Data.currentData.keys())
        self.comm['values'] = self.keysList

        #Printing Graph
        self.printGraph(self.frame_top)
        #Refresh List
        self.list_panel(self.frame_bottom1)

    #Delete button. TESTED
    def button_delete(self):
        """
        Call back method when user clicks 'Delete entry' button
        Does not take any parameters. Does not return any. It takes focus information from GUI treeview screen,
        references focus to the position in tunas list and DELETEs that tuna.
        :return: None

        Method: button_delete
        Author: Nikolay Melnik
        Date created: 10/11/2018
        Date last modified: 10/17/2018
        Python Version: 3.7
        """
        # print('Delete button')
        #If no focus - return
        x = self.tree.focus()
        if x=='':
            return
        x = int(x)
        # print(int(x))
        Data.tunas.pop(x)
        if len(Data.tunas) == 0:
            #If Tunas length == 0, do like New file
            self.new_file()
            return
        #If Tunas have something, then do as in update
        self.boxes_clear()
        #Default values for boxes
        Data.analyzeTuna()
        if Data.currentUOM == 'Litres per person, per year':
            Data.currentData = Data.analyzedTunasLitres
        else:
            Data.currentData = Data.analyzedTunasKilos
        self.keysList = list(Data.currentData.keys())
        self.comm['values'] = self.keysList

        #Printing Graph
        self.printGraph(self.frame_top)
        #Refresh List
        self.list_panel(self.frame_bottom1)

    #Second screen Constructor
    def __init__(self, master):
        """
        This constructor is responsible for creation of the second window GUI. It creates windows,
        pack them with widgets and assigns call back functions

        Method: __init__ (Constructor)
        Author: Nikolay Melnik
        Date created: 10/5/2018
        Date last modified: 10/18/2018
        Python Version: 3.7
        """
        self.root = master
        #Adding file menu. Taken from https://www.lynda.com/MyPlaylist/Watch/15528494/184095?autoplay=true
        self.root.option_add('*tearOff', False)
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        file = Menu(menubar)
        menubar.add_cascade(menu=file, label='File')
        file.add_command(label='New File', command=self.new_file)
        file.add_separator()
        file.add_command(label='Open File', command=self.open_file)
        file.add_command(label='Save File', command=self.save_file_button)
        file.add_separator()
        file.add_command(label='Load from Database', command=self.load_from_db)
        file.add_command(label='Save to Database', command=self.save_to_db)
        file.add_separator()
        file.add_command(label='Exit', command=lambda: self.root.destroy())

        # Second screen styling
        # Not resizable screen - resizeable only horizontally
        self.root.resizable(True, False)
        self.root.geometry('1500x1000+150+0')
        self.root.title('CST8333_FinalProject by Nikolay Melnik')
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 10))

        # Forming Top Frame
        self.frame_top = ttk.Frame(self.root)
        self.frame_top.pack()

        #Default values for boxes
        Data.analyzeTuna()
        Data.currentUOM = 'Litres per person, per year'
        Data.currentData = Data.analyzedTunasLitres
        # Set data for graphs and comboboxes
        self.keysList = list(Data.currentData.keys())

        self.timeLabel = StringVar()
        self.timeLabel.set('Program run time:0000')
        ttk.Label(self.frame_top, textvariable=self.timeLabel).grid(row=0, column=0, columnspan=4, pady=5)
        ttk.Label(self.frame_top, text='Time line graphical representation').grid(row=2, column=0, columnspan=4, pady=5)
        ttk.Label(self.frame_top, text='Shows available food, NOT ajusted for losses').grid(row=4, column=0, columnspan=4, pady=10)
        ttk.Label(self.frame_top, text='Choose food for the graph: ').grid(row=5, column=2, sticky="w",pady=10)
        ttk.Label(self.frame_top, text='Choose UOM: ').grid(row=5, column=0, sticky="w", pady=10)


        #Callback method for UOM box
        def changeUOM(event):
            """
            Nested supply method. Called when user changes UOM combobox. Changes data sets: according to litters or kilos
            for graphical representation. Refreshes graph.
            :param event: Virtual event from UOM combobox
            :type: event
            :return: None

            Nested Method: changeUOM
            Author: Nikolay Melnik
            Date created: 10/11/2018
            Date last modified: 10/17/2018
            Python Version: 3.7
            """

            # Check what was selected
            Data.currentUOM = self.choice.get()
            if self.choice.get() == 'Litres per person, per year':
                Data.currentData = Data.analyzedTunasLitres
            elif self.choice.get() == 'Kilograms per person, per year':
                Data.currentData = Data.analyzedTunasKilos
            # Set data for graphs and comboboxes
            self.keysList = list(Data.currentData.keys())
            self.comm['values'] = self.keysList
            if len(self.keysList) < 1:
                self.comm.set('')
            else:
                self.comm.current(0)
            #Refresh Graph
            Data.currentKey = self.comm.get()
            self.printGraph(self.frame_top)

        #combo box change UOM
        # https://www.programcreek.com/python/example/104110/tkinter.ttk.Combobox
        # https://stackoverflow.com/questions/6876518/set-a-default-value-for-a-ttk-combobox
        choice_box = StringVar()
        keepvalue2 = choice_box.get()
        self.choice = ttk.Combobox(self.frame_top, textvariable=keepvalue2, width=30,
                                   values=['Litres per person, per year', 'Kilograms per person, per year'])
        self.choice.state(['readonly'])
        self.choice.bind('<<ComboboxSelected>>', changeUOM)
        self.choice.current(0)
        self.choice.grid(row=5, column=1, sticky="w", pady=10)

        #Callback method for Commodity box
        def changeComm(event):
            """
            Nested supply method. Called when user changes Commodity combobox. Takes commodity name as a key
            for graphical representation. Refreshes graph.
            :param event: Virtual event from commodity combobox
            :type: event
            :return: None

            Nested Method: changeComm
            Author: Nikolay Melnik
            Date created: 10/11/2018
            Date last modified: 10/17/2018
            Python Version: 3.7
            """
            Data.currentKey = self.comm.get()
            self.printGraph(self.frame_top)

        commvar = StringVar()
        keepvalue2 = commvar.get()
        self.comm = ttk.Combobox(self.frame_top, textvariable=keepvalue2, width=60, values=self.keysList)
        self.comm.state(['readonly'])
        self.comm.bind('<<ComboboxSelected>>', changeComm)

        self.comm['values'] = self.keysList
        if len(self.keysList) < 1:
            self.comm.set('')
        else:
            self.comm.current(0)

        #self.comm.current(0)
        self.comm.grid(row=5, column=3, sticky="w")
        # x= list(Data.analyzedTunasLitres.keys())
        #Printing Graph
        Data.currentKey = self.comm.get()
        self.printGraph(self.frame_top)

        #Second Part of the screen, 2nd frame Constructing
        # Forming Top Frame
        self.frame_bottom1 = ttk.Frame(self.root)
        self.frame_bottom1.pack()
        self.frame_bottom2 = ttk.Frame(self.root)
        self.frame_bottom2.pack(anchor=W)
        self.frame_bottom3 = ttk.Frame(self.root)
        self.frame_bottom3.pack(anchor=W)
        self.frame_bottom4 = ttk.Frame(self.root)
        self.frame_bottom4.pack(anchor=W)
        self.frame_bottom5 = ttk.Frame(self.root)
        self.frame_bottom5.pack(anchor=W)

        # #Packing stuff
        #Packing stuff
        ######## Here is 1st line
        ttk.Label(self.frame_bottom1, text='Table View').pack()
        ttk.Label(self.frame_bottom2, text='                    REF_DATE(1960-2017):').pack(side=LEFT, pady=5)

        self.en_refDate = StringVar()
        ttk.Entry(self.frame_bottom2, textvariable=self.en_refDate, width=5).pack(side=LEFT, pady=5)

        ttk.Label(self.frame_bottom2, text='   GEO: Canada').pack(side=LEFT, pady=5)
        ttk.Label(self.frame_bottom2, text='   DGUID: 2016A000011124').pack(side=LEFT, pady=5)
        ttk.Label(self.frame_bottom2, text='    Food Categories: ').pack(side=LEFT, pady=5)
        #Food Categories Combo box
        fcat = StringVar()
        foodcat = fcat.get()
        self.food_avail = ttk.Combobox(self.frame_bottom2, textvariable=foodcat, width=35, values=['Food available', 'Food available adjusted for losses'])
        self.food_avail.state(['readonly'])
        #### self.comm.bind('<<ComboboxSelected>>', changeComm)
        self.food_avail.current(0)
        self.food_avail.pack(side=LEFT, pady=5)

        ttk.Label(self.frame_bottom2, text='    Commodity: ').pack(side=LEFT, pady=5)
        self.en_commodity = StringVar()
        ttk.Entry(self.frame_bottom2, textvariable=self.en_commodity, width=60).pack(side=LEFT, pady=5)

        ######## Here is 2nd line
        ttk.Label(self.frame_bottom3, text='                    UOM: ').pack(side=LEFT, pady=5)
        #UOM Categories Combo box
        fuom = StringVar()
        uomlist = fuom.get()
        self.uom_sel = ttk.Combobox(self.frame_bottom3, textvariable=uomlist, width=35, values=['Litres per person, per year', 'Kilograms per person, per year'])
        self.uom_sel.state(['readonly'])
        #### self.comm.bind('<<ComboboxSelected>>', changeComm)
        self.uom_sel.current(0)
        self.uom_sel.pack(side=LEFT, pady=5)

        ttk.Label(self.frame_bottom3, text='   UOM_ID: ').pack(side=LEFT, pady=5)
        self.en_uomid = StringVar()
        ttk.Entry(self.frame_bottom3, textvariable=self.en_uomid, width=5).pack(side=LEFT, pady=5)

        ttk.Label(self.frame_bottom3, text='   SCALAR_FACTOR: ').pack(side=LEFT, pady=5)
        #Scalar Factor Combo box
        fscal = StringVar()
        scallist = fscal.get()
        self.scal_sel = ttk.Combobox(self.frame_bottom3, textvariable=scallist, width=10, values=['Units', 'Thousands'])
        self.scal_sel.state(['readonly'])
        #### self.comm.bind('<<ComboboxSelected>>', changeComm)
        self.scal_sel.current(0)
        self.scal_sel.pack(side=LEFT, pady=5)

        ttk.Label(self.frame_bottom3, text='   SCALAR_ID: ').pack(side=LEFT, pady=5)
        self.en_scalarid = StringVar()
        ttk.Entry(self.frame_bottom3, textvariable=self.en_scalarid, width=5).pack(side=LEFT, pady=5)

        ttk.Label(self.frame_bottom3, text='   VECTOR: ').pack(side=LEFT, pady=5)
        self.en_vector = StringVar()
        ttk.Entry(self.frame_bottom3, textvariable=self.en_vector, width=10).pack(side=LEFT, pady=5)

        ttk.Label(self.frame_bottom3, text='   COORDINATE: ').pack(side=LEFT, pady=5)
        self.en_coordinate = StringVar()
        ttk.Entry(self.frame_bottom3, textvariable=self.en_coordinate, width=10).pack(side=LEFT, pady=5)

        ######## Here is 3rd line
        ttk.Label(self.frame_bottom4, text='                    VALUE: ').pack(side=LEFT, pady=5)
        self.en_value = StringVar()
        ttk.Entry(self.frame_bottom4,  textvariable= self.en_value, width=5).pack(side=LEFT, pady=5)

        ttk.Label(self.frame_bottom4, text='   STATUS: ').pack(side=LEFT, pady=5)
        self.en_status = StringVar()
        ttk.Entry(self.frame_bottom4, textvariable=self.en_status, width=5).pack(side=LEFT, pady=5)

        ttk.Label(self.frame_bottom4, text='   SYMBOL: ').pack(side=LEFT, pady=5)
        self.en_symbol = StringVar()
        ttk.Entry(self.frame_bottom4, textvariable=self.en_symbol, width=5).pack(side=LEFT, pady=5)

        ttk.Label(self.frame_bottom4, text='   TERMINATED: ').pack(side=LEFT, pady=5)
        self.en_terminated = StringVar()
        ttk.Entry(self.frame_bottom4, textvariable=self.en_terminated, width=5).pack(side=LEFT, pady=5)

        ttk.Label(self.frame_bottom4, text='   DECIMALS: ').pack(side=LEFT, pady=5)
        self.en_decimals = StringVar()
        ttk.Entry(self.frame_bottom4, textvariable=self.en_decimals, width=5).pack(side=LEFT, pady=5)

        ### Buttons
        ttk.Label(self.frame_bottom5, text='           ').pack(side=LEFT, pady=10)
        ttk.Button(self.frame_bottom5, name='but_create', text="Create New Entry", command=self.create_button).pack(side=LEFT, pady=5, padx=10)
        ttk.Button(self.frame_bottom5, name='but_update', text="Update Entry", command=self.update_button).pack(side=LEFT, pady=5, padx=10)
        ttk.Button(self.frame_bottom5, name='but_delete', text="Delete Entry", command=self.button_delete).pack(side=LEFT, pady=5, padx=10)

        #Show treeview on screen
        self.list_panel(self.frame_bottom1)

        #Initializing timer
        #Taking current system time
        self.clock = datetime.datetime.now()
        self.run_clocks()



# First GUI Starter
class FirstScreen(object):
    """
    Class responsible for GUI and call backs of the First window

    Class: FirstScreen
    Extends: object
    Author: Nikolay Melnik
    Date created: 10/1/2018
    Date last modified: 10/14/2018
    Python Version: 3.7
    """

    def __init__(self, master):
        """
        Constructor of the class and First GUI screen
        :param master: Tkinter object of the first window
        :param: Tk

        Method: __init__ (Constructor)
        Author: Nikolay Melnik
        Date created: 10/3/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """

        self.master = master
        # First screen styling
        master.resizable(False, False)  # Not resizable screen
        master.geometry('450x368+735+356')
        master.title('CST8333_FinalProject by Nikolay Melnik')
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))

        # Labels placement
        master.columnconfigure(0, weight=1)
        ttk.Label(master, text='\n\n\nCST8333_351 Final Project').grid(row=0, column=0)
        ttk.Label(master, text='by Nikolay Melnik, student ID-040874855').grid(row=1, column=0)
        ttk.Label(master, text='Algonquin College. Ottawa, ON. December 2018\n\n\n\n').grid(row=2, column=0)

        # Buttons placement
        ttk.Button(master, text=' Open and load .CSV file ', command=self.firstButton).grid(row=3, column=0, pady=5)
        ttk.Button(master, text=' Load data from MySql database (if exists) ', command=self.secondButton).grid(row=4, column=0, pady=5)
        ttk.Button(master, text=' Exit ', command=self.thirdButton).grid(row=5, column=0, pady=5)


    def firstButton(self):
        """
        Call back method from taking the first choice in the first screen:
        Button: ' Open and load .CSV file '. Loads file, destroys first screen and goes to the second
        :return: None.

        Method: secondButton
        Author: Nikolay Melnik
        Date created: 10/3/2018
        Date last modified: 10/14/2018
        Python Version: 3.7

        :return:
        """

        # Call filechooser
        filename = filedialog.askopenfile(filetypes=(("Comma-separated files", "*.csv"), ("All files", "*.*")))
        if filename is None: return  # Return if Cancel is pressed

        #Load file and process Tunas
        x = Data.tunas_loader(filename.name)
        #Throwing messages according to returned results: 0 -ok, 1 - load error, 2 - corrupted file
        if x == 0:
            messagebox.showinfo("LOAD SUCCESS", "Your File was successfully loaded\nPlease press OK to continue")
        elif x ==1:
            messagebox.showerror("FILE READING ERROR",
                                 "There was an ERROR during loading\nPlease press OK and repeat loading")
            return
        elif x ==2:
            messagebox.showerror("FILE READING ERROR",
                                 "Data set is corrupted or not specified\nPlease press OK and repeat loading")
            return

# Return if no Tunas loaded
        if len(Data.tunas) == 0:
            return

        # Destroying window
        self.master.destroy()
        #Call for second screen
        root = Tk()
        SecondScreen(root)

    def secondButton(self):
        """
        Call back method from taking the second choice in the first screen:
        Button: ' Load data from MySql database (if exists) '. Load data from DB, destroys first screen and goes to the second
        :return: None.

        Method: secondButton
        Author: Nikolay Melnik
        Date created: 10/3/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        # print('Button 2 pressed')
        # Loading data from the Database
        x = Data.read_tunas_from_db(self)
        if x == 0:
            messagebox.showinfo("LOAD SUCCESS", "Your File was successfully loaded\nPlease press OK to continue")
        elif x == 1:
            messagebox.showerror("MySQL READING ERROR",
                                 "There was an ERROR during loading from DB\nPlease press OK and repeat loading")
        # If no tunas loaded - exit
        if len(Data.tunas) < 1:
            return
        # Destroying window
        self.master.destroy()
        #Call for second screen
        root = Tk()
        SecondScreen(root)

    def thirdButton(self):
        """
        Call back method from taking the third choice in the first screen:
        Button: ' Exit '. Destroys the window and exits
        :return: None.

        Method: thirdButton
        Author: Nikolay Melnik
        Date created: 10/3/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """

        self.master.destroy()
        # print('Button 3 pressed')



### Major function
def main():
    """
    Main Entry into the program. Starts the first screen
    :return: None

    Method: main
    Author: Nikolay Melnik
    Date created: 10/1/2018
    Date last modified: 10/1/2018
    Python Version: 3.7
    """
    root = Tk()
    plt.rcParams.update({'figure.max_open_warning': 0}) #Blocking Matplotlib Warnings as per https://github.com/clawpack/visclaw/issues/75
    FirstScreen(root)

    root.mainloop()

# Mandatory stuff
if __name__ == "__main__": main()
