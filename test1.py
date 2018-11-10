import datetime
import threading
import time


class Stopwatch(threading.Thread):
    """
    Multithreading class. Counts time and changing GUI according to System time.

    Class: Stopwatch
    Extends: threading.Thread
    Author: Nikolay Melnik
    Date created: 10/22/2018
    Date last modified: 10/26/2018
    Python Version: 3.7
    """

    def __init__(self):
        """
        This constructor prepares a thread for time calculation during GUI work
        :param: master: Reference to StringVar object representing Label in GUI to be displayed
        :return: None
        :type: StringVar:

        Method: __init__ (Constructor)
        Author: Nikolay Melnik
        Date created: 10/22/2018
        Date last modified: 10/26/2018
        Python Version: 3.7
        """
        threading.Thread.__init__(self)
        self.clock = datetime.datetime.now()

    def run(self):
        """
        Overridden methods which continuously perform time calculation since program started and updates GUI
        :return: None

        Method: run
        Author: Nikolay Melnik
        Date created: 10/22/2018
        Date last modified: 10/26/2018
        Python Version: 3.7
        """
        while (True):
            # calculate difference from start until now and print it in the Label
            x = int((datetime.datetime.now() - self.clock).total_seconds())
            print('Program run time:',x)
            time.sleep(0.1)




thread = Stopwatch()
thread.start()
