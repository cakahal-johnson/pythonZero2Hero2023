"""
A Lambda function is a small anonymous function which can take any number of arguments, but can only have one expression
SYNTAX:
lambda arguments : expression

where the expression is executed and the result is returned...
"""
#
# x = lambda a: a + 10
# print(x(5))  # 15
#
# # Multiply argument b with argument c and return the result
# e = lambda b, c : b * c
# print(e(5, 6))  # 30
#
#
# # Summarize argument
# f = lambda g, h, j : g + h + j
# print(f(5, 6, 2))

"""
WHY USING LAMBDA FUNCTIONS
The power of lambda is better show when you use them as an anonymous function inside another function

where we have a function definition that takes one arguments, and that arguments will be multiplied with an unknown number
"""

# def myFunc(n):
#     return lambda k : k * n
#
# myVar = myFunc(2)
# myVar1 = myFunc(3)
#
# print(myVar(11))  # 22
# print(myVar1(11)) # 33

# we use lambda function when an anonymous function is required for a short period of time...

"""
PYTHON CLASSES/OBJECTS (OOP)
Python is an object oriented programming language
where A class is like an object constructor, or a "blueprint" for creating objects

Almost everything python is an object, with its properties and methods

"""

# Creating a Class: we use the keyword class
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

# __init__() Function
"""
with the above classes and objects in their simplest form, and are not really useful in real life applications

To understand the meaning classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated

we use the __init__() function to assign values to object properties, or other operations that are necessary to do when 
the object is created

"""

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# player1 = Person("Johnson", 70)
#
# print(player1.name)
# print(player1.age)


"""
Objects can also contain methods in objects are functions that belong to the object
lets insert a function that prints a greeting, and execute it on the player1

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(("Hello is nice to meet you! " + self.name))

player1 = Person("Johnson", 70)

player1.myfunc()

"""
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs class.

it does not have to be named self, you can call it whatever you like, but is has to be the first parameter of any
function in the class

"""

class Person1:
    def __init__(myOBJ, Name, Age):
        myOBJ.Name = Name
        myOBJ.Age = Age

    def myFunc(abc):
        print("Hello welcome to your dashboard " + abc.Name)


player2 = Person1("John", 45)
# we can modify properties on objects
player2.Age = 40

player2.myFunc()
print(player2.Age)


# Delete Object Properties: with the keyword del

class Person2:
    def __init__(myOBJ, NAME, AGE):
        myOBJ.NAME = NAME
        myOBJ.AGE = AGE

    def myFunc(abcd):
        print("Hello welcome to your dashboard " + abcd.NAME)


player3 = Person2("Cakahal", 45)
# we can delete properties on objects
del player3.AGE  # Person2 object has no attribute 'age'

player3.myFunc()
# print(player3.AGE)

"""
The PASS Statement
since class can't be empty we use pass

"""


class Person4:
    pass


"""
PYTHON INHERITANCE
    these allows us to define a class that inherits all the methods and properties from another class
    Parent Class: is the class being inherited from, also called the base class
    Child Class: is the class the inherits from another class, also called derived class

"""


# class PERSON:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def myFullname(self):
#         print(self.firstname, self.lastname)
#
# # we use python class to create an object, and the execute the myFullname method:
# a = PERSON("Cakahal", "Johnson")
# a.myFullname()


"""
To create a child class the inherits the functionality from another class, send the parent class as a parameter
 when creating the child class
"""

# class PERSON:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def myFullname(self):
#         print(self.firstname, self.lastname)
#
#     # here we add the child class
# class Student(PERSON):
#     pass
#
# # we use python class to create an object, and the execute the myFullname method:
# a = PERSON("Cakahal", "Johnson")
# a.myFullname()
#
# b = Student("UBA", "OBI")
# b.myFullname()


"""
Adding the __init__() function in the child is used instead of the pass keyword it overrides the inheritance of the 
parent's
"""
#
# class PERSON:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def myFullname(self):
#         print(self.firstname, self.lastname)
#
#     # here we add the child class
# class Student(PERSON):
#     # pass
#     # here use init function in child class
#     def __init__(self, fname, lname):
#         PERSON.__init__(self, fname, lname)
#
# # we use python class to create an object, and the execute the myFullname method:
# a = PERSON("Cakahal", "Johnson")
# a.myFullname()
#
# b = Student("UBA", "OBI")
# b.myFullname()

# when you add the __init__() function, the child class will no longer inherit the parent's __init__() function
# To Keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

"""
Using the super() Function
python also has a super() function that will make the child class inherit all the methods and properties from it's parent
"""

#
# class PERSON:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def myFullname(self):
#         print(self.firstname, self.lastname)
#
#     # here we add the child class
# class Student(PERSON):
#     # pass
#     # here use init function in child class
#     def __init__(self, fname, lname):
#         # HERE we use super() function
#         super().__init__(fname, lname)
#         self.graduationYear = 2023 # hardcoding the year
#
# # we use python class to create an object, and the execute the myFullname method:
# a = PERSON("Cakahal", "Johnson")
# a.myFullname()
#
# b = Student("UBA", "OBI")
# b.myFullname()
# print(b.graduationYear)

# MAKING THE YEAR DYNAMIC


# class PERSON:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def myFullname(self):
#         print(self.firstname, self.lastname)
#
#     # here we add the child class
# class Student(PERSON):
#     # pass
#     # here use init function in child class
#     def __init__(self, fname, lname, year):
#         # HERE we use super() function
#         super().__init__(fname, lname)
#         self.graduationYear = year  # making the year dynamic
#
# # we use python class to create an object, and the execute the myFullname method:
# a = PERSON("Cakahal", "Johnson")
# a.myFullname()
#
# b = Student("UBA", "OBI", 2023)
# b.myFullname()
# print(b.graduationYear)

# Adding more property method
class PERSON:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def myFullname(self):
        print(self.firstname, self.lastname)

    # here we add the child class
class Student(PERSON):
    # pass
    # here use init function in child class
    def __init__(self, fname, lname, year):
        # HERE we use super() function
        super().__init__(fname, lname)
        self.graduationYear = year  # making the year dynamic

        # adding more property method
        def welcome(self):
            print("Welcome", self.firstname, self.lastname, "to the class of ", self.graduationYear)

# we use python class to create an object, and the execute the myFullname method:
a = PERSON("Cakahal", "Johnson")
a.myFullname()

b = Student("UBA", "OBI", 2023)
b.myFullname()
print(b.graduationYear)
b.welcome()

c = Student("Cakahal", "Johnson", 2022)
c.myFullname()
print(c.graduationYear)
c.welcome()

