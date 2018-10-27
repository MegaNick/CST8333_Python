# To the Glory of God!
# Exercise 04 program by Nikolay Melnik
# CST8333_351 Algonquin College. October 2018
import datetime
from tkinter import ttk, Tk, StringVar

class Exercise04(object):
    """
    Class as a part of Exercise 04. This class is responsible for GUI. Shows the screen

    Class: Exercise04
    Extends: object
    Author: Nikolay Melnik
    Date created: 10/26/2018
    Date last modified: 10/26/2018
    Python Version: 3.7
    """

    def run_clocks(self):
        """

        Method shows elapsed program time in seconds. Run as Tkinter thread.
        Restarts itself every second, synchronizes itself with system clock
        :return: None

        Method: run_clocks
        Author: Nikolay Melnik
        Date created: 10/26/2018
        Date last modified: 10/26/2018
        Python Version: 3.7
        """
        # calculate difference from start until now and print it in the Label
        x = str(int((datetime.datetime.now() - self.clock).total_seconds()))
        self.timeLabel.set('Program run time in seconds:' + x)
        self.master.after(1, self.run_clocks)

    def __init__(self, master):
        """
        Constructor of the class and GUI screen
        :param master: Tkinter object of the window
        :param: Tk

        Method: __init__ (Constructor)
        Author: Nikolay Melnik
        Date created: 10/26/2018
        Date last modified: 10/26/2018
        Python Version: 3.7
        """

        self.master = master
        # First screen styling
        self.master.resizable(False, False)  # Not resizable screen
        self.master.geometry('450x368+735+356')
        self.master.title('CST8333_Exercise04 by Nikolay Melnik')
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 12))

        # Labels placement
        self.master.columnconfigure(0, weight=1)
        ttk.Label(self.master, text='\n\n\nCST8333_351 Exercise04. Threads in Tkinter').grid(row=0, column=0)
        ttk.Label(self.master, text='by Nikolay Melnik, student ID-040874855').grid(row=1, column=0)
        ttk.Label(self.master, text='Algonquin College. Ottawa, ON. October 2018\n\n\n\n').grid(row=2, column=0)

        #Testing field
        self.timeLabel = StringVar()
        self.timeLabel.set('Program run time in seconds:0')
        ttk.Label(self.master, textvariable=self.timeLabel).grid(row=3, column=0, pady=5)

        #Initializing timer
        #Taking current system time
        self.clock = datetime.datetime.now()
        self.run_clocks()

### Major function
def main():
    """
    Main Entry into the program. Starts the GUI
    :return: None

    Method: main
    Author: Nikolay Melnik
    Date created: 10/26/2018
    Date last modified: 10/26/2018
    Python Version: 3.7
    """
    root = Tk()
    x = Exercise04(root)
    root.mainloop()

# Mandatory stuff
if __name__ == "__main__": main()
