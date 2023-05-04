"""
PYTHON BOOLEANS
booleans represents one of two values: True or False

this can be used where we often need to know if an expression is True or False
also where you want to evaluate any expression in python, and get one of two answers, true or false
also where you want to compare two values, the expression is evaluated and python returns the Boolean answer
"""

# using Boolean in an Operators
print(10 > 9) # returns True
print(10 < 9) # returns False
print(10 == 9) # returns False
print(10 != 9) # True

# using boolean in function
a = 200
b = 199

if b > a:
    print("yes B is greater than A")
else:
    print("No B is not greater than A")


# using Boolean to evaluate values and variables
#  here using Booleans as a function methods we use bool() function which allows you to evaluate any values it also
#  returns True or False...

print(bool("My name is Cakahal"))
print(bool(15))

# using Bool to evaluate two variables
x = "Johnson"
age = 70

print(bool(x))
print(bool(age))

"""
Almost any value is evaluated to True if it has some sort of content
Any string is True, except empty string
Any number is true, excepts 0
any list tuple set dict are True excepts empty ones

"""

# one more value, or object in this case evaluates to false and that is if you have an object that is made from a
# class with a__len__ function that returns 0 or false as in OOp class


class Myclass:
    def __len__(self):
        return 0


myJob = Myclass()
print(bool(myJob))

