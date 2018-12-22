# To the Glory of God!
# CST8333 Exercise05 by Nikolay Melnik
from abc import ABCMeta, abstractmethod

class TunaSkeleton(metaclass=ABCMeta):
    """
    This TunaSkeleton class is purely abstract class designed to demonstrate Inheritance capability of Python.
    Author: Nikolay Melnik
    """

    @abstractmethod
    def setTunaFeatures(self, array=[]):
        """
        Takes an array of parameters - [4] and sets them into created Tuna object
        Author: Nikolay Melnik
        """
        pass

    @abstractmethod
    def getTunaFeatures(self):
        """
        Returns all the fields of Tuna object as a list
        :return: [4] - fields of Tuna object as a list String values
        :rtype: list
        Author: Nikolay Melnik
        """
        pass

class RedRoe:
    """
    This class has only one variable roe = "Red caviar" to show inheritance
    Author: Nikolay Melnik
    """

    roe = "Red caviar"
    """ This variable contains string of roe type - Red caviar"""

class YellowRoe:
    """
    This class has only one variable roe = "Yellow roe" to show inheritance
    Author: Nikolay Melnik
    """

    roe = "Yellow roe"
    """ This variable contains string of roe type - Yellow roe"""

# Class which extends abstract class TunaSkeleton by Nikolay Melnik
class Tuna(TunaSkeleton, YellowRoe):
    """
    Tuna class inherits abstract TunaSkeleton. Modified for the Exercise05
    Author: Nikolay Melnik
    """

    def __init__(self, REF_DATE="", GEO="", DGUID="", FOODCATEGORIES=""):
        """
        Tuna Constructor initializes 4 fields of Tuna object as Strings
        Author: Nikolay Melnik
        """
        self.REF_DATE = REF_DATE
        self.GEO = GEO
        self.DGUID = DGUID
        self.FOODCATEGORIES = FOODCATEGORIES

    def setTunaFeatures(self, array=[]):
        """
        This method sets all the fields from the list array into the Tuna object
        :param: A list of strings [4] holding all fields of the object to be changed
        :type: list[4] of strings
        :return: None
        Author: Nikolay Melnik
        """
        self.REF_DATE = array[0]
        self.GEO = array[1]
        self.DGUID = array[2]
        self.FOODCATEGORIES = array[3]

    def getTunaFeatures(self):
        """
        The method returns all the fields of the Tuna object as an array of strings
        :return: list [4] - fields of the tuna object
        :rtype: list[4] of strings
        Author: Nikolay Melnik
        """
        x = [self.REF_DATE, self.GEO, self.DGUID, self.FOODCATEGORIES]
        return x

class Salmon(TunaSkeleton, RedRoe):
    """
    Salmon class inherits abstract TunaSkeleton. Now we have a Salmon with Tuna skeleton (weird but it's ok :))) )
    Author: Nikolay Melnik
    """

    def __init__(self, dob="", length="", weight="", colour="pink"):
        """
        Salmon Constructor initializes 4 fields of Salmon object as Strings
        Author: Nikolay Melnik
        """
        self.dob = dob
        self.length = length
        self.weight = weight
        self.colour = colour

    def setTunaFeatures(self, array=[]):
        """
        This method sets all the fields from the list array into the Salmon object (It's called setTunaFeatures though)
        :param: A list of strings [4] holding all fields of the object to be changed
        :type: list[4] of strings
        :return: None
        Author: Nikolay Melnik
        """
        self.dob = array[0]
        self.length = array[1]
        self.weight = array[2]
        self.colour = array[3]

    def getTunaFeatures(self):
        """
        The method returns all the fields of the Salmon object as an array of strings (It's called getTunaFeatures though)
        :return: list [4] - fields of the tuna object
        :rtype: list[4] of strings
        Author: Nikolay Melnik
        """
        return [self.dob, self.length, self.weight, self.colour]


def monsanto(x):
    """
    This is a "terrible" method. It takes any fish - Tuna or Salmon and modifies them with a set of features.
    So it is doesn't matter what goes in. It must have method setTunaFeatures()
    :param x: Object for modification
    :type: class extended from TunaSkeleton
    :return:
    """
    # Process splicing
    x.setTunaFeatures(['Feature #1', 'Feature #2', 'Feature #3', 'Feature #4'])


### Major function
def main():
    """
    Main Entry into the program.
    :return: None
    Author: Nikolay Melnik
    """
    tuna = Tuna('1960', 'Canada', '2016A000011124', 'Food available')
    salmon = Salmon('01/01/2018', '100cm', '5kg', 'Red')

    print("Original Tuna -", tuna.getTunaFeatures(), "Roe type-", tuna.roe)
    print("Original salmon -", salmon.getTunaFeatures(), "Roe type-", salmon.roe)
    print("Warning! Here comes GMO stuff :)")
    monsanto(tuna)
    monsanto(salmon)
    print("Genetically modified Tuna -", tuna.getTunaFeatures(), "Roe type-", tuna.roe)
    print("Genetically modified Salmon -", salmon.getTunaFeatures(), "Roe type-", salmon.roe)

# Mandatory stuff
if __name__ == "__main__": main()
