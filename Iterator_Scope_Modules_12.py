"""
PYTHON ITERATORS

An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values

its protocol, which consist of the methods __iter__() and __next__()

Iterator VS Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an
iterator from

All these objects have a iter() method which is used to get an iterator

"""
# here we return an iterator from tuple and print each value
myTuple = ("Java", "python", "Ruby", "php")
myity = iter(myTuple)

# print(myity) // error
print(next(myity))
print(next(myity))
print(next(myity))
print(next(myity))
# print(next(myity))  #  error

# String as iterable objects
myStr = "python"
myiti = iter(myStr)

print(next(myiti))

# getting all we use "for" loops through a tuple
mytuple = ("Java", "python", "Ruby", "php")
for a in mytuple:
    print(a)

# getting all we use "for" loops through a String
for b in myStr:
    print(b)


# for creating with object/class as an iterator
# where we return numbers, starting with 1 each sequence will increase by one (returning  1, 2, 3, 4, 5)

class MyNumbers:
    def __iter__(self):
        self.c = 1
        return self

    def __next__(self):
        d = self.c
        self.c += 1
        return d

myClass = MyNumbers()
myIter = iter(myClass)

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))


# adding control to stop at 20 iterations:
class myNumber:
    def __iter__(self):
        self.e = 1
        return self

    def __next__(self):
        if self.e <= 20:
            f = self.e
            self.e += 1
            return f
        else:
            raise StopIteration

MyClass = myNumber()
myItery = iter(MyClass)

for f in myItery:
    print(f)


"""
PYTHON SCOPE
a variable is only available from inside the region it is created. this is called scope

Local Scope: this is created inside a function belongs to the local scope of the function, can only be used inside that function


"""
x = 400

def Myfunc():
    x = 300
    print(x)

Myfunc()  # x is 300

print(x)   #  x is 400


def myFunc():
    x = 200
    def myinnerFunc():
        print(x)
    myinnerFunc()

myFunc()  #  x is 200


# Global Scope
"""
A variable created in the main body is the global scope

these Global variables are available from within any scope, global and local
"""


def myXfunc():
    print(x)

myXfunc() #  X is 400
print(x)   #  X is 400


"""
Naming Variables where both local and global is same name it will be treated as separate variables as where we have x 400
"""

# Global keyword
"""
if you need to create a global variable, but are stuck in local scope, you can use the global keyword
"""
print('printing X', x)

def myGfunc():
    global x
    x = 600

myGfunc()
print(x)
