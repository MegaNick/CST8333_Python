# To the Glory of God!
# CST8333 Project by Nikolay Melnik

from abc import ABCMeta, abstractmethod
from tkinter import *
from tkinter import ttk, filedialog
from tkinter import messagebox
from tkinter.font import Font


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

    @abstractmethod
    def getTunaTuple(self):
        """
         Returns all the fields of Tuna object as Tuple
         :return: (16) - fields of Tuna object
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
        :return: array [16] - fields
        """
        x = [self.REF_DATE, self.GEO, self.DGUID, self.FOODCATEGORIES, self.COMMODITY, self.UOM, self.UOM_ID,
             self.SCALAR_FACTOR, self.SCALAR_ID, self.VECTOR,
             self.COORDINATE, self.VALUE, self.STATUS, self.SYMBOL, self.TERMINATED, self.DECIMALS]
        return x

    def getTunaTuple(self):
        """
        The method returns all the fields of the Tuna object as a Tuple of Strings
        :return: Tuple [16] - fields
        """
        x = tuple((self.REF_DATE, self.GEO, self.DGUID, self.FOODCATEGORIES, self.COMMODITY, self.UOM, self.UOM_ID,
             self.SCALAR_FACTOR, self.SCALAR_ID, self.VECTOR,
             self.COORDINATE, self.VALUE, self.STATUS, self.SYMBOL, self.TERMINATED, self.DECIMALS))
        return x


class Data:
    tunas = []
    tunasHeader = Tuna()
    analyzedTunasLitres = {}
    analyzedTunasKilos = {}
    currentUOM = ""
    currentData = {}
    currentKey = ""


# Second GUI Starter
class SecondScreen:

    # CSV array analyzer
    def analyzeTuna(self):
        for x in Data.tunas:
            # Skip adjusted for losses food. Shouldn't be too complicated
            # Another thing is eliminating repetition
            try:

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
                continue
    #printing graph data
    def printGraph(self, master):

        # Grid Graphic forgetter
        # Taken from here https://stackoverflow.com/questions/23189610/remove-widgets-from-grid-in-tkinter
        for label in self.frame_top.grid_slaves():
            if int(label.grid_info()["row"]) == 1:
                label.grid_forget()

        # Data for plotting
        # Taken from https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py
        z = Data.currentData.get(Data.currentKey)
        x = []
        #Years to observe
        for y in range(1960, 2017):
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

    def list_panel(self, mf):

        demoPanel = Frame(mf)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)

        self._create_treeview(demoPanel)
        self._load_data()

    ### This Block is taken from https://pyinmyeye.blogspot.com/2012/07/tkinter-multi-column-list-demo.html
    def _create_treeview(self, parent):
        """
        This
        :param parent:
        :return:
        """
        f = ttk.Frame(parent)
        f.pack(side=TOP, fill=BOTH, expand=Y)

        # create the tree and scrollbars
        self.dataCols = ('REF_DATE', 'GEO', 'DGUID', 'FOODCATEGORIES', 'COMMODITY', 'UOM',
                         'UOM_ID', 'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'VALUE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS')
        self.tree = ttk.Treeview(columns=self.dataCols,
                                 show='headings')

        ysb = ttk.Scrollbar(orient=VERTICAL, command=self.tree.yview)
        xsb = ttk.Scrollbar(orient=HORIZONTAL, command=self.tree.xview)
        self.tree['yscroll'] = ysb.set
        self.tree['xscroll'] = xsb.set

        # add tree and scrollbars to frame
        self.tree.grid(in_=f, row=0, column=0, sticky=NSEW)
        ysb.grid(in_=f, row=0, column=1, sticky=NS)
        xsb.grid(in_=f, row=1, column=0, sticky=EW)

        # set frame resize priorities
        f.rowconfigure(0, weight=1)
        f.columnconfigure(0, weight=1)

        self.tree.bind("<ButtonRelease-1>", self.OnDoubleClick)

    def OnDoubleClick(self, event):
        curItem = self.tree.focus()
        print(self.tree.item(curItem))
        print("iid x-", self.tree.focus())

    def _load_data(self):

        self.data = []
        for x in Data.tunas:
            y = x.getTunaTuple()
            self.data.append(x.getTunaTuple())

        # configure column headings
        for c in self.dataCols:
            self.tree.heading(c, text=c.title()) #, command=lambda c=c: self._column_sort(c, MCListDemo.SortDir)
            self.tree.column(c, width=Font().measure(c.title()))

        # Add counter
        count = 0
        # add data to the tree
        for item in self.data:
            self.tree.insert('', 'end', iid=count, values=item)
            count = count + 1

            # and adjust column widths if necessary
            for idx, val in enumerate(item):
                iwidth = Font().measure(val)
                if self.tree.column(self.dataCols[idx], 'width') < iwidth:
                    self.tree.column(self.dataCols[idx], width=iwidth)
    ####### End of Tree view



















    def __init__(self):
        root = Tk()
        # self.master = master

        # Second screen styling
        self.analyzeTuna()
        root.resizable(False, False)  # Not resizable screen
        root.geometry('1500x1000+150+0')
        root.title('CST8333_FinalProject by Nikolay Melnik')
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 10))

        # Forming Top Frame
        self.frame_top = ttk.Frame(root)
        self.frame_top.pack()

        ttk.Label(self.frame_top, text='Time line graphical representation').grid(row=0, column=0, columnspan=4, pady=5)
        ttk.Label(self.frame_top, text='Shows available food, NOT ajusted for losses').grid(row=2, column=0, columnspan=4, pady=10)
        ttk.Label(self.frame_top, text='Choose food for the graph: ').grid(row=3, column=2, sticky="w",pady=10)
        ttk.Label(self.frame_top, text='Choose UOM: ').grid(row=3, column=0, sticky="w", pady=10)

        #Default values for boxes
        Data.currentUOM = 'Litres per person, per year'
        Data.currentData = Data.analyzedTunasLitres
        self.keysList = list(Data.currentData.keys())

        #Callback method for UOM box
        def changeUOM(event):

            Data.currentUOM = self.choice.get()
            if self.choice.get() == 'Litres per person, per year':
                Data.currentData = Data.analyzedTunasLitres
                self.keysList = list(Data.currentData.keys())
                self.comm['values'] = self.keysList
                self.comm.current(0)
                #Refresh Graph
                Data.currentKey = self.comm.get()
                self.printGraph(self.frame_top)

            elif self.choice.get() == 'Kilograms per person, per year':
                Data.currentData = Data.analyzedTunasKilos
                self.keysList = list(Data.currentData.keys())
                self.comm['values'] = self.keysList
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

        Data.currentKey = self.keysList[0]
        self.printGraph(self.frame_top)


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
        self.frame_bottom1 = ttk.Frame(root)
        self.frame_bottom1.pack()
        self.frame_bottom2 = ttk.Frame(root)
        self.frame_bottom2.pack(anchor=W)
        self.frame_bottom3 = ttk.Frame(root)
        self.frame_bottom3.pack(anchor=W)
        self.frame_bottom4 = ttk.Frame(root)
        self.frame_bottom4.pack(anchor=W)
        self.frame_bottom5 = ttk.Frame(root)
        self.frame_bottom5.pack(anchor=W)

        # #Packing stuff
        #Packing stuff
        ######## Here is 1st line
        ttk.Label(self.frame_bottom1, text='Table View').pack()
        ttk.Label(self.frame_bottom2, text='                    REF_DATE(1960-2017):').pack(side=LEFT, pady=5)
        self.en_refDate = ttk.Entry(self.frame_bottom2, width=5).pack(side=LEFT, pady=5)
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
        self.en_commodity = ttk.Entry(self.frame_bottom2, width=60).pack(side=LEFT, pady=5)

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
        self.en_uomid = ttk.Entry(self.frame_bottom3, width=5).pack(side=LEFT, pady=5)
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
        self.en_scalarid = ttk.Entry(self.frame_bottom3, width=5).pack(side=LEFT, pady=5)
        ttk.Label(self.frame_bottom3, text='   VECTOR: ').pack(side=LEFT, pady=5)
        self.en_vector = ttk.Entry(self.frame_bottom3, width=10).pack(side=LEFT, pady=5)
        ttk.Label(self.frame_bottom3, text='   COORDINATE: ').pack(side=LEFT, pady=5)
        self.en_coordinate = ttk.Entry(self.frame_bottom3, width=10).pack(side=LEFT, pady=5)

        ######## Here is 3rd line
        ttk.Label(self.frame_bottom4, text='                    VALUE: ').pack(side=LEFT, pady=5)
        self.en_value = ttk.Entry(self.frame_bottom4, width=5).pack(side=LEFT, pady=5)
        ttk.Label(self.frame_bottom4, text='   STATUS: ').pack(side=LEFT, pady=5)
        self.en_status = ttk.Entry(self.frame_bottom4, width=5).pack(side=LEFT, pady=5)
        ttk.Label(self.frame_bottom4, text='   SYMBOL: ').pack(side=LEFT, pady=5)
        self.en_symbol = ttk.Entry(self.frame_bottom4, width=5).pack(side=LEFT, pady=5)
        ttk.Label(self.frame_bottom4, text='   TERMINATED: ').pack(side=LEFT, pady=5)
        self.terminated = ttk.Entry(self.frame_bottom4, width=5).pack(side=LEFT, pady=5)
        ttk.Label(self.frame_bottom4, text='   DECIMALS: ').pack(side=LEFT, pady=5)
        self.decimals = ttk.Entry(self.frame_bottom4, width=5).pack(side=LEFT, pady=5)

        ### Buttons
        ttk.Label(self.frame_bottom5, text='           ').pack(side=LEFT, pady=10)
        buttonCreate = ttk.Button(self.frame_bottom5, text="Create New Entry").pack(side=LEFT, pady=5, padx=10)
        buttonUpdate = ttk.Button(self.frame_bottom5, text="Update Entry").pack(side=LEFT, pady=5, padx=10)
        buttonDelete = ttk.Button(self.frame_bottom5, text="Update Entry").pack(side=LEFT, pady=5, padx=10)

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
                        elif x == '"':
                            continue
                        a = a + x

                    # a is clean, do split
                    b = a.split(',')

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
    plt.rcParams.update({'figure.max_open_warning': 0}) #Blocking Matplotlib Warnings as per https://github.com/clawpack/visclaw/issues/75
    FirstScreen(root)

    root.mainloop()


if __name__ == "__main__": main()
