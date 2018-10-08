# To the Glory of God!
# CST8333 Project by Nikolay Melnik

from abc import ABCMeta, abstractmethod
from tkinter import *
from tkinter import ttk, filedialog
from tkinter import messagebox

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class TunaSkeleton(metaclass=ABCMeta):
    """
    This class is purely abstract class designed to demonstrate Inheritance capability of Python
    """

    @abstractmethod
    def setTunaFeatures(self, array):
        """
        Takes an array of parameters - [16] and sets them into created Tuna object
        :param array: Array of data for Tuna object. places 0 and 12 must be ints, the rest - Strings
        :return: null
        """
        pass

    @abstractmethod
    def getTunaFeatures(self):
        """
        Returns all the fields of Tuna object as an array
        :return: [16] - fields of Tuna object
        """
        pass


class Tuna(TunaSkeleton):
    def __init__(self, REF_DATE=0, GEO="", DGUID="", FOODCATEGORIES="", COMMODITY="", UOM="", UOM_ID="",
                 SCALAR_FACTOR="", SCALAR_ID="", VECTOR="", COORDINATE="", VALUE=0, STATUS="", SYMBOL="", TERMINATED="",
                 DECIMALS=""):
        """
        Tuna Constructor
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

    def setTunaFeatures(self, array):
        """
        This method sets all the fields from the array into Tuna object
        :param array: array [17] holds all fields of the object
        :return:
        """
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

    def getTunaFeatures(self):
        """
        The method returns all the fields of the Tuna object as an array of strings
        :return: array [17] - fields
        """
        x = [self.REF_DATE, self.GEO, self.DGUID, self.FOODCATEGORIES, self.COMMODITY, self.UOM, self.UOM_ID,
             self.SCALAR_FACTOR, self.SCALAR_ID, self.VECTOR,
             self.COORDINATE, self.VALUE, self.STATUS, self.SYMBOL, self.TERMINATED, self.DECIMALS]
        return x


class Data:
    tunas = []
    tunasHeader = Tuna()
    analyzedTunasLitres = {}
    analyzedTunasKilos = {}


# Second GUI Starter
class SecondScreen:

    # CSV array analyzer
    def analyzeTuna(self):
        for x in Data.tunas:
            # Skip adjusted for losses food. Shouldn't be too complicated
            # Another thing is eliminating repetition
            if x.FOODCATEGORIES == 'Food available adjusted for losses':
                continue
            if x.UOM == '"Litres per person, per year"':
                key = x.COMMODITY
                temp = Data.analyzedTunasLitres.get(key)
                if temp is None:
                    Data.analyzedTunasLitres.update({key: {int(x.REF_DATE): float(x.VALUE)}})
                else:
                    temp.update({int(x.REF_DATE): float(x.VALUE)})
                    Data.analyzedTunasLitres.update({key: temp})
            elif x.UOM == '"Kilograms per person, per year"':
                key = x.COMMODITY
                temp = Data.analyzedTunasKilos.get(key)
                if temp is None:
                    Data.analyzedTunasKilos.update({key: {int(x.REF_DATE): float(x.VALUE)}})
                else:
                    temp.update({int(x.REF_DATE): float(x.VALUE)})
                    Data.analyzedTunasKilos.update({key: temp})

    def __init__(self):
        root = Tk()
        # self.master = master

        # Second screen styling
        self.analyzeTuna()
        root.resizable(False, False)  # Not resizable screen
        root.geometry('1500x828+50+50')
        root.title('CST8333_FinalProject by Nikolay Melnik')
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))

        # Forming Top Frame
        self.frame_top = ttk.Frame(root)
        self.frame_top.pack()
        ttk.Label(self.frame_top, text='Time line graphical representation').grid(row=0, column=0)

        # Data for plotting
        # Taken from https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py
        z = Data.analyzedTunasLitres.get('Apple juice')
        x = []
        #Years to observe
        for y in range(1960, 2017):
            x.append(z.get(y))
                    #
                    # t = np.arange(1960, 2017, 1)
                    # f = Figure(figsize=(50, 5), dpi=50)
                    # a = f.add_subplot(111)
                    # a.plot(t, x)

        t = np.arange(1960, 2017, 1)
        s = 1 + np.sin(2 * np.pi * t)

        # fig = Figure(figsize=(5, 5), dpi=50)
        fig, ax = plt.subplots()
        fig.set_dpi(80)
        fig.set_figwidth(13)

        ax.plot(t, x)

        ax.set(xlabel='YEAR', ylabel='Liters per person per year',
               title='Price variation 1960-2017')
        ax.grid()

        canvas = FigureCanvasTkAgg(fig, self.frame_top)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)
        ttk.Label(self.frame_top, text='Choose food for the graph: ').grid(row=2, column=0, sticky="w")

    # https://www.programcreek.com/python/example/104110/tkinter.ttk.Combobox
        # https://stackoverflow.com/questions/6876518/set-a-default-value-for-a-ttk-combobox
        keysList = list(Data.analyzedTunasLitres.keys())
        self.countryvar = StringVar()
        keepvalue = self.countryvar.get()
        self.country = ttk.Combobox(self.frame_top, textvariable=keepvalue, width=60, values=keysList)
        self.country.state(['readonly'])
        self.country.current(0)
        self.country.grid(row=2, column=1, sticky="w")
        x= list(Data.analyzedTunasLitres.keys())
        a=x

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

        try:
            with open(filename.name) as f:
                count = 0
                for line in f:

                    # Here Lines have bad zeros - 0x00 or bad characters above 0x80. We need to get rid of them as well as from \n
                    a = ""
                    for x in line:
                        if x < ' ':
                            if x != '\t':
                                continue
                        elif x >= '\x80':
                            continue
                        a = a + x

                    # a is clean, do split
                    b = a.split('\t')

                    # if a contains 16 elements, we are good, if not, do next
                    if len(b) != 16:
                        continue

                    # Are we processing correct file?
                    if count == 0:
                        if (b[1] != 'GEO') or (b[2] != 'DGUID'):
                            raise IOError("Data set is corrupted or not specified")
                    count = count + 1

                    # Create Tuna object
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
        Data.tunas = sorted(Data.tunas, key=lambda tuna: (tuna.REF_DATE, tuna.COMMODITY))

        # Destroying window
        self.master.destroy()

        SecondScreen()

    def secondButton(self):
        print('Button 2 pressed')

    def thirdButton(self):
        self.master.destroy()
        print('Button 3 pressed')


### Major function
def main():
    root = Tk()
    # root.geometry('440x120+20+20')
    FirstScreen(root)

    root.mainloop()


if __name__ == "__main__": main()
