# To the Glory of God!
# CST8333 Project by Nikolay Melnik
""" CST8333_Final_Project by Nikolay Melnik
    as a partial fulfillment of the CST8333 course.
    Ottawa, ON Canada. September-December 2018
"""
__version__ = "1.0"
__author__ = "Nikolay Melnik (id-040874855)"


from abc import ABCMeta, abstractmethod
from tkinter import *
from tkinter import ttk, filedialog
from tkinter import messagebox
from tkinter.font import Font
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import operator
import mysql.connector
from mysql.connector import errorcode

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
        #Assigning one variable's value to another by Nikolay Melnik
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

    db_info = ['localhost', 'pytester', 'password', 'py_final_project']
    """
    MySQL credentials: ('host', 'user', 'passwd', 'db')
    """




    #Loading CSV file by Nikolay Melnik. TESTED
    @staticmethod
    def tunas_loader(x=""):
        """
        This class method is taking a full file path and loading a CSV File, check it's integrity and then
        transfers it into list (array) of Tunas
        :param: String having a full filepath to CSV file
        :type: str
        :return: None. The array is put into class variable Data.tunas[]

        Method: tunas_loader
        Author: Nikolay Melnik
        Date created: 10/9/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        try:
            with open(x) as f:
                #Primitive int assignment by Nikolay Melnik
                count = 0
                for line in f:

                    # If file has bad zeros - 0x00 or bad characters above 0x80. We need to get rid of them as well as from \n and "
                    a = ""
                    #Decision structures by Nikolay Melnik
                    for x in line:
                        if x < ' ':
                            if x != '\t':
                                continue
                        elif x >= '\x80':
                            continue
                        elif x == '"':
                            continue
                        a = a + x

                    # a is clean, do split
                    b = a.split(',')

                    #If it is the first line combine together columns 5 and 6
                    if count > 0:
                        b[5] = b[5] + ',' + b[6]
                        b.pop(6)

                    # if a contains 16 elements, we are good, if not, do next
                    if len(b) != 16:
                        continue

                    # Are we processing correct file?
                    if count == 0:
                        if (b[1] != 'GEO') or (b[2] != 'DGUID'):
                            raise IOError("Data set is corrupted or not specified")
                    #Math by Nikolay Melnik
                    count = count + 1

                    # Create Tuna object by Nikolay Melnik
                    tuna = Tuna()
                    tuna.setTunaFeatures(b)
                    Data.tunas.append(tuna)

        except IOError as error:
            messagebox.showerror("FILE READING ERROR",
                                 "There was an ERROR during loading\nPlease press OK and repeat loading")
            return
        messagebox.showinfo("LOAD SUCCESS", "Your File was successfully loaded\nPlease press OK to continue")
        Data.tunasHeader = Data.tunas[0]
        Data.tunas.pop(0)
        # Sorting Tunas. Idea is taken from https://andrefsp.wordpress.com/2012/02/27/sorting-object-lists-in-python/
        # and https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
        Data.tunas.sort(key=lambda tuna: (tuna.REF_DATE, tuna.COMMODITY))

    #Saving tunas to CSV by Nikolay Melnik. TESTED
    @staticmethod
    def tunas_saver(name=""):
        """
        Saving Tunas into a CSV file according to the given path
        :param: String having a full filepath to CSV file
        :type: str
        :return: None

        Method: tunas_saver
        Author: Nikolay Melnik
        Date created: 10/9/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """

        def compactor(y=Tuna):
            """
            Nested method takes Tuna and returns a String of CSV coded Tuna
            :param y: Tuna object to be compacted into CSV style
            :return: String of CSV Tuna
            """
            line = ""
            t = y.getTunaFeatures
            count = 0
            for z in t:
                line = line + z
                if count < 15:
                    line = line + ','
                count = count + 1
            line = line + '\n'
            return line

        #Open file for processing. Some ideas are form here https://www.w3schools.com/python/python_file_write.asp
        try:
            f = open(name, "w")
            f.write(compactor(Data.tunasHeader))
            for tuna in Data.tunas:
                f.write(compactor(tuna))
            f.close()
        except IOError:
            messagebox.showerror("FILE SAVING ERROR",
                                 "There was an ERROR during saving\nPlease press OK and repeat saving")
            return
        messagebox.showinfo("SAVING SUCCESS", "Your File was successfully saved\nPlease press OK to continue")

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
    # ideas from here
    def db_create_table(self):
        """
        Method creates table 'records' in database from Data.db_info (by default - py_final_project)
        May show GUI error in case of error
        :return: None. Table created in DB

        Method: db_create_table
        Author: Nikolay Melnik
        Date created: 10/14/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        try:
            mydb = mysql.connector.connect(
                host=Data.db_info[0],
                user=Data.db_info[1],
                passwd=Data.db_info[2],
                database=Data.db_info[3]
            )
            mycursor = mydb.cursor()

            sql = "DROP TABLE IF EXISTS records"
            mycursor.execute(sql)

            sql = 'CREATE TABLE records ('
            #Getting list of header info
            x = Data.tunasHeader.getTunaFeatures
            count = 0
            for y in x:
                sql = sql+'`'+y+'`'+' VARCHAR(50)'
                # add comma if not the last block
                if count <15:
                    sql = sql + ','
                count = count + 1
            sql = sql + ')'
            mycursor.execute(sql)
            mycursor.close()
            mydb.close()
        except (Exception) as error:
            messagebox.showerror("MySQL SAVING ERROR",
                                 "There was an ERROR during saving into DB\nPlease press OK and repeat saving")
            mycursor.close()
            mydb.close()

    #Save tunas in DB. TESTED
    # ideas from here https://www.w3schools.com/python/python_mysql_insert.asp
    def save_tunas_in_db(self):
        """
        Method saves current tunas into MySQL 'records' DB.
        May show GUI error in case of error
        :return: None

        Method: save_tunas_in_db
        Author: Nikolay Melnik
        Date created: 10/14/2018
        Date last modified: 10/14/2018
        Python Version: 3.7
        """
        # Open DB
        try:
            mydb = mysql.connector.connect(
                host=Data.db_info[0],
                user=Data.db_info[1],
                passwd=Data.db_info[2],
                database=Data.db_info[3]
            )
            mycursor = mydb.cursor()
            #Preparing transaction
            sql = "INSERT INTO records VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            for x in Data.tunas:
                val = x.getTunaTuple()
                mycursor.execute(sql, val)
            # Commit transaction
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            mycursor.close()
            mydb.close()
        except Exception as error:
            messagebox.showerror("MySQL SAVING ERROR",
                                 "There was an ERROR during saving into DB\nPlease press OK and repeat saving")
            mycursor.close()
            mydb.close()

    # Tunas loader from DB. TESTED
    def read_tunas_from_db(self):
        try:
            mydb = mysql.connector.connect(
                host=Data.db_info[0],
                user=Data.db_info[1],
                passwd=Data.db_info[2],
                database=Data.db_info[3]
            )
            Data.tunas = []
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
                Data.tunas.append(tuna)

        except Exception as error:
            messagebox.showerror("MySQL SAVING ERROR",
                                 "There was an ERROR during saving into DB\nPlease press OK and repeat saving")
            mycursor.close()
            mydb.close()

        mycursor.close()
        mydb.close()


# Second GUI Starter
class SecondScreen:
    # Variable for sorting
    # class variable to track direction of column
    # header sort
    SortDir = True  # descending

     #printing graph data
    def printGraph(self, master):

        # Grid Graphic forgetter
        # Taken from here https://stackoverflow.com/questions/23189610/remove-widgets-from-grid-in-tkinter
        for label in self.frame_top.grid_slaves():
            if int(label.grid_info()["row"]) == 1:
                label.grid_forget()

        # Data for plotting
        # Taken from https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py
        # Re-declare type by Nikolay Melnik
        z = 1000 # Here z is int
        z = Data.currentData.get(Data.currentKey) # Here z is dictionary
        # Declare variable x as array by Nikolay Melnik
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
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, pady=10)



    ### This Block is taken from https://pyinmyeye.blogspot.com/2012/07/tkinter-multi-column-list-demo.html
    ### Adjusted fot This final project
    def list_panel(self, mf):

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
        This
        :param parent:
        :return:
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

        self.tree.bind("<ButtonRelease-1>", self.OnDoubleClick)

    def OnDoubleClick(self, event):
        curItem = self.tree.focus()
        # print(self.tree.item(curItem))
        # print("iid x-", curItem)
        #Transfer commodities
        x = self.tree.item(curItem).get('values')
        #print(x)
        #Avoid wrong x type
        if type(x) is not list:
            return
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

        self.data = []
        for x in Data.tunas:
            self.data.append(x.getTunaTuple())

        # configure column headings
        for c in self.dataCols:
            self.tree.heading(c, text=c.title(), command=lambda c=c: self._column_sort(c, SecondScreen.SortDir))
            self.tree.column(c, width=Font().measure(c.title()))

        # Add counter
        count = 0
        # add data to the tree
        for item in self.data:
            self.tree.insert('', 'end', iid=count, values=item)
            count = count + 1

    def _column_sort(self, col, descending=False):

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


    def save_file_button(self):
        # Call filechooser
        filename = filedialog.asksaveasfilename(filetypes=(("Comma-separated files", "*.csv"), ("All files", "*.*")))
        if filename is None: return  # Return if Cancel is pressed
        # filename = filename +'.csv'
        Data.tunas_saver(filename)

    def boxes_clear(self):
        """
        Cleans all entry boxes
        :return: None
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



    ### Buttons callbacks

    #Create button pressed
    def create_button(self):
        print('Create button')
        #Create an array and fill it with data from the screen
        tu = []
        tu.append(self.en_refDate.get())
        try:
            x = int(tu[0])
            if x < 1960 or x > 2017:
                raise ValueError
        except ValueError as error:
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
        Data.tunas.append(tuna)
        self.boxes_clear()

        #Default values for boxes
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



    #Update Button pressed
    def update_button(self):
        # If no focus - return
        x = self.tree.focus()
        if x== '':
            return
        x = int(x)
        #Create an array and fill it with data from the screen
        tu = []
        tu.append(self.en_refDate.get())
        try:
            y = int(tu[0])
            if y < 1960 or y > 2017:
                raise ValueError
        except ValueError as error:
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

    #Delete button
    def button_delete(self):
        print('Delete button')
        #If no focus - return
        x = self.tree.focus()
        if x=='':
            return
        x = int(x)
        print(int(x))
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
    def __init__(self):
        self.root = Tk()

        #Adding file menu. Taken from https://www.lynda.com/MyPlaylist/Watch/15528494/184095?autoplay=true
        self.root.option_add('*tearOff', False)
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        file = Menu(menubar)
        menubar.add_cascade(menu=file, label='File')
        file.add_command(label='New File', command=self.new_file)
        file.add_command(label='Save File', command=self.save_file_button)
        file.add_separator()
        file.add_command(label='Exit', command=lambda: self.root.destroy())

        # Second screen styling
        self.root.resizable(False, False)  # Not resizable screen
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
        self.keysList = list(Data.currentData.keys())
        Data.currentKey = self.keysList[0]

        #Printing Graph
        self.printGraph(self.frame_top)

        ttk.Label(self.frame_top, text='Time line graphical representation').grid(row=0, column=0, columnspan=4, pady=5)
        ttk.Label(self.frame_top, text='Shows available food, NOT ajusted for losses').grid(row=2, column=0, columnspan=4, pady=10)
        ttk.Label(self.frame_top, text='Choose food for the graph: ').grid(row=3, column=2, sticky="w",pady=10)
        ttk.Label(self.frame_top, text='Choose UOM: ').grid(row=3, column=0, sticky="w", pady=10)


        #Callback method for UOM box
        def changeUOM(event):

            Data.currentUOM = self.choice.get()
            if self.choice.get() == 'Litres per person, per year':
                Data.currentData = Data.analyzedTunasLitres
                self.keysList = list(Data.currentData.keys())
                self.comm['values'] = self.keysList
                if len(self.keysList) < 1:
                    self.comm.set('')
                else:
                    self.comm.current(0)

                #Refresh Graph
                Data.currentKey = self.comm.get()
                self.printGraph(self.frame_top)

            elif self.choice.get() == 'Kilograms per person, per year':
                Data.currentData = Data.analyzedTunasKilos
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
        self.choice.grid(row=3, column=1, sticky="w", pady=10)

        # self.analyzeTuna()
        # Data.currentKey = self.keysList[0]
        # self.printGraph(self.frame_top)

        #Callback method for Commodity box
        def changeComm(event):
            Data.currentKey = self.comm.get()
            print(self.comm.get())
            self.printGraph(self.frame_top)

        commvar = StringVar()
        keepvalue2 = commvar.get()
        self.comm = ttk.Combobox(self.frame_top, textvariable=keepvalue2, width=60, values=self.keysList)
        self.comm.state(['readonly'])
        self.comm.bind('<<ComboboxSelected>>', changeComm)
        self.comm.current(0)
        self.comm.grid(row=3, column=3, sticky="w")
        # x= list(Data.analyzedTunasLitres.keys())

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
        ttk.Button(self.frame_bottom5, text="Create New Entry", command=self.create_button).pack(side=LEFT, pady=5, padx=10)
        ttk.Button(self.frame_bottom5, text="Update Entry", command=self.update_button).pack(side=LEFT, pady=5, padx=10)
        ttk.Button(self.frame_bottom5, text="Delete Entry", command=self.button_delete).pack(side=LEFT, pady=5, padx=10)

        #Show treevie on screen
        self.list_panel(self.frame_bottom1)

# First GUI Starter
class FirstScreen:

    def __init__(self, master):
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
        ttk.Button(master, text=' Load data from MySql database (if exists) ', command=self.secondButton).grid(row=4,
                                                                                                               column=0,
                                                                                                               pady=5)
        ttk.Button(master, text=' Exit ', command=self.thirdButton).grid(row=5, column=0, pady=5)

    def firstButton(self):

        # Call filechooser
        filename = filedialog.askopenfile(filetypes=(("Comma-separated files", "*.csv"), ("All files", "*.*")))
        if filename is None: return  # Return if Cancel is pressed
        print(filename.name)

        #Load file and process Tunas
        Data.tunas_loader(filename.name)

        # Destroying window
        self.master.destroy()
        #Call for second screen
        SecondScreen()

    def secondButton(self):
        print('Button 2 pressed')

    def thirdButton(self):
        self.master.destroy()
        print('Button 3 pressed')


### Major function
def main():
    root = Tk()
    plt.rcParams.update({'figure.max_open_warning': 0}) #Blocking Matplotlib Warnings as per https://github.com/clawpack/visclaw/issues/75
    FirstScreen(root)

    root.mainloop()


if __name__ == "__main__": main()
