#CST8333_351_Exercise03 By Nikolay Melnik
#

"""
Class animal created for demonstration of object creation and variable references
"""
class animal:

    animalClass = "Life"
    """
    Class variable is ALMOST equal to 'static' variable in Java, however, it is NOT static. Holds example of Living Being Class (Taxonomy)
    https://en.wikipedia.org/wiki/Taxonomy_(biology)
    """

    def __init__(self, genus = ""):
        """
        Constructor. Saves Genus into variable genus
        :param genus: holds Genus of the object. For example, Feline, Canine, Equine etc
        """
        self.genus = genus

    def genusPrint(self):
        """
        Methods prints genus variable into console
        :return: None
        """
        print(self.genus)


#1. Variable declaration
print('1. Variable declaration by Nikolay Melnik')
a = 10 #Variable a = 1 assignment 1 to variable a
b = 2 #Variable b = 2 assignment 2 to variable b
print(a+b) #Addition operator on variables
print(b/a) #Division operator on variables

a = "Hello " #Variables can be reassigned to a different type. Here as String
b = "World!" #Variable b reassigned as String
print(a+b) # "Adding" - concatenating Strings
print('**************************')
#2. Primitives vs references
#All "primitives" in Python are objects. They have methods!
print('2. Primitives vs references by Nikolay Melnik')
a = 14
print('Method bit_length in a=14 ->', a.bit_length()) #All variables in Python, in fact, are objects - they have methods like here
a = animal("Dog") #a is now reference to an object of animal-Dog
b = animal("Cat") #b is now reference to an object of animal-Cat
print('a is ', end='')
a.genusPrint() #Calling method from object a
print('b is ', end='')
b.genusPrint() #Calling method from object b
#Class animal has class variable animalClass, which can look similar to "static" in Java but it is not static
print('Printing class variable animalClass from Dog variable a-', a.animalClass)
print('Printing class variable animalClass from Cat variable b-', b.animalClass)
print('Assigning class variable animal.animalClass-Canine')
animal.animalClass = "Canine"
print('Printing class variable animalClass from Dog variable a-', a.animalClass)
print('Printing class variable animalClass from Cat variable b-', b.animalClass)
print("Changing class variable in b through object-Feline")
b.animalClass = "Feline"
print('Printing class variable animalClass from Dog variable a-', a.animalClass)
print('Printing class variable animalClass from Cat variable b-', b.animalClass)
print('Class variable animalClass-', animal.animalClass)
print('Assigning class variable animal.animalClass-Aves')
animal.animalClass = "Aves"
#After object assignment instead of class assignment, Cat as Feline never changes, it becomes opbject variable
print('Printing class variable animalClass from Dog variable a-', a.animalClass)
print('Printing class variable animalClass from Cat variable b-', b.animalClass)
print('**************************')

#3 Decision structures
print('3. Decision Structures by Nikolay Melnik')
#Entering Numbers for compare
a = int(input('Please enter first number-'))
b = int(input('Please enter second number-'))
#Checking what is bigger or equal
if a > b:
    print('First is bigger than second or equal')
else:
    print('Second is bigger than first or equal')
#Checking for positive/negative
a = int(input('Please enter number to check negativity/positivity-'))
if a > 0:
    print("Number is POSITIVE")
elif a < 0:
    print("Number is NEGATIVE")
elif a == 0:
    print("Number is ZERO")
print('**************************')

#4 Repetition structures
print('4. Repetition structures by Nikolay Melnik')
#Simple while loop
print('Simple while loop')
a=0
while(a<10):
    print(a, ' ', end='')
    a=a+1
#Iteration loop
print('\nIteration loop')
#Creating an array of objects
line = []
a = animal("Cat")
b = animal("Dog")
c = animal("Horse")
line.append(a)
line.append(b)
line.append(c)
#Iterating the array
for x in line:
    print('This animal is-', x.genus)

#5 Arithmetics
print('5. Arithmetics by Nikolay Melnik')

#Supportive class calculator perfomrms arithmetics
class calc:
    """
    Supporting Class t=for arithmetic demonstration. Has methods of 4 basic arithmetic functions: + - * /
    """

    def addition(self, a, b):
        """
        Method Calculates sum of 1st and 2nd parameters
        :param a: 1st parameter
        :param b: 2nd parameter
        :return: sum of parameters
        """
        return a+b

    def subtraction(self, a, b):
        """
        Method Calculates difference between 1st and 2nd parameters
        :param a: 1st parameter
        :param b: 2nd parameter
        :return: difference of the parameters
        """
        return a-b

    def multiplication(self, a, b):
        """
        Method Calculates product of 1st and 2nd parameters
        :param a: 1st parameter
        :param b: 2nd parameter
        :return: product of the parameters
        """
        return a*b

    def division(self, a, b):
        """
         Method Calculates quotient of 1st and 2nd parameters. If 2nd parameter is 0 returns String - 'Division by 0 prohibited!'
         :param a: 1st parameter
         :param b: 2nd parameter
         :return: quotient of the parameters. If 2nd parameter is 0 returns String - 'Division by 0 prohibited!'
         """
        if b == 0:
            return 'Division by 0 prohibited!'
        else:
            return a/b


a = int(input('Please enter first number for calculation-'))
b = int(input('Please enter second number for calculation-'))
c = calc()
print('a plus b = ', c.addition(a,b))
print('a minus b = ', c.subtraction(a,b))
print('a times b = ', c.multiplication(a,b))
print('a divided by b = ', c.division(a,b))
print('**************************')

#6 Comparison. Simple compare examples
#equal
print('Comparision examples by Nikolay Melnik')
a = int(input('Please enter first number -a- for comparision example-'))
b = int(input('Please enter second number -b- for comparision example-'))
if a == b:
    print('a equal b')
#not equal
if a != b:
    print('a NOT equal b')
#Here works the same as in previous example. However. Python 3.7 doesn't support it anymore
# if a <> b:
#     print('a NOT equal b')
#more
if a > b:
    print('a more than b')
#less
if a < b:
    print('a less b')
#more or equal
if a >= b:
    print('a more or equal to b')
#less or equal
if a <= b:
    print('a less or equal to b')
print('**************************')

#7 Logic operators
print('Logic operators by Nikolay Melnik')
if True and True and True:
    print('Example of if True and True and True')
#example of logical decision
#counts numbers from 0 to 19. Prints numbers if they more than 2 and less than 8 or if it is equal to 15
count = 0
while(count < 20):
    if count > 2 and count < 8 or count ==15:
        print(count, ' ', end='')
    count = count + 1
print('\n**************************')

#8 Memory Management
# "Python's memory allocation and deallocation method is automatic.
# The user does not have to preallocate or deallocate memory by hand as one has to when using dynamic memory allocation in languages such as C or C++.
# Python uses two strategies for memory allocation reference counting and garbage collection."
# Taken from  https://www.digi.com/resources/documentation/digidocs/90001537/references/r_python_garbage_coll.htm



