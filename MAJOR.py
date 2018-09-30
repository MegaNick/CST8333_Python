# To the Glory of God!
# CST8333 Project by Nikolay Melnik

from abc import ABCMeta, abstractmethod
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

Tunas = {}

class TunaSkeleton(metaclass=ABCMeta):
    """
    This class is purely abstract class designed to demonstrate Inheritance capability of Python
    """

    @abstractmethod
    def setTunaFeatures(self, array):
        """
        Takes an array of parameters - [17] and sets them into created Tuna object
        :param array: Array of data for Tuna object. places 0 and 12 must be ints, the rest - Strings
        :return: null
        """
        pass

    @abstractmethod
    def getTunaFeatures(self):
        """
        Returns all the fields of Tuna object as an array
        :return: [17] - fields of Tuna object
        """
        pass


class Tuna(TunaSkeleton):
    def __init__(self, REF_DATE=0, GEO="", DGUID="", Food="", categories="", Commodity="", UOM="", UOM_ID="",
                 SCALAR_FACTOR="", SCALAR_ID="", VECTOR="", COORDINATE="", VALUE=0, STATUS="", SYMBOL="", TERMINATED="",
                 DECIMALS=""):
        """
        Tuna Constructor
        :param REF_DATE:
        :param GEO:
        :param DGUID:
        :param Food:
        :param categories:
        :param Commodity:
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
        self.Food = Food
        self.categories = categories
        self.Commodity = Commodity
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
        self.Food = array[3]
        self.categories = array[4]
        self.Commodity = array[5]
        self.UOM = array[6]
        self.UOM_ID = array[7]
        self.SCALAR_FACTOR = array[8]
        self.SCALAR_ID = array[9]
        self.VECTOR = array[10]
        self.COORDINATE = array[11]
        self.VALUE = array[12]
        self.STATUS = array[13]
        self.SYMBOL = array[14]
        self.TERMINATED = array[15]
        self.DECIMALS = array[16]

    def getTunaFeatures(self):
        """
        The method returns all the fields of the Tuna object as an array of strings
        :return: array [17] - fields
        """
        x = [self.REF_DATE, self.GEO, self.DGUID, self.Food, self.categories, self.Commodity, self.UOM, self.UOM_ID, self.SCALAR_FACTOR, self.SCALAR_ID,  self.VECTOR,
             self.COORDINATE, self.VALUE, self.STATUS, self.SYMBOL, self.TERMINATED, self.DECIMALS]
        return x

#First GUI Starter
class FirstScreen:
    def __init__(self, master):

        master.resizable(False, False) # Not resizable screen
        master.geometry('450x368+735+356')
        master.title('CST8333_FinalProject by Nikolay Melnik')
        self.style = ttk.Style()
        self.style.configure('TLabel', font = ('Arial', 10))
#        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
        ttk.Label(master, text='CST8333_351 Final Project').place(x=130, y=63, width=170, height=31)
        ttk.Label(master, text='By Nikolay Melnik, student ID-040874855').place(x=91, y=84, width=250, height=31)





  #      master.columnconfigure(0, weight=1)
# ttk.Label(master,           text='\nCST8333_351 Final Project\nBy Nikolay Melnik, student ID-040874855\nAlgonquin College. Ottawa, ON. December 2018') \
#     .place(x=580, y=183, width=170, height=21)


### Major function
def main():
    root = Tk()
    # root.geometry('440x120+20+20')
    gui = FirstScreen(root)
    root.mainloop()

if __name__ == "__main__": main()
