# PYTHON DATE
# TO USE PYTHON DATE WE NEED TO import datetime as object
import datetime

# default values
import math

a = datetime.datetime.now()
b = datetime.datetime.utcnow()  # GMT time
print(a)
print(b)

# print day and year
c = datetime.datetime.now()
print(c.year)
print(c.strftime("%A"))

# class(constructor)
d = datetime.datetime(2023, 3, 28)
print(d)

# getting the month
print(d.strftime("%B"))

# Am and Pm
e = datetime.datetime.utcnow()
print(e.strftime("%p"))

# TimeZone
f = datetime.datetime.now()
print(f.strftime("%Z"))

# normal display
g = datetime.datetime.now()
print(g.strftime("%c"))

# using /
A = datetime.datetime.now()
print(A.strftime("%x"))

# using :
B = datetime.datetime.now()
print(B.strftime("%X"))

# using week classwork

"""
PYTHON MATH built-in function and built-in module
"""
# where we need to find the lowest or highest values in iterable:
z = min(5, 20, 15, 2)
y = max(50, 255, 89, 66)
print('the lowest number is: ', z)
print('The highest number is: ', y)

# abs() function returns the absolute(positive) value of specifed number
x = abs(-7.25)
print(x)

# pow(x, y) function returns the value of x to the power of y(x*)
# 4 to the power of 3(same as 4 * 4 * 4)
X = pow(4, 3)
print(X) # big letter X = 64


# to use math module we need to import math
C = math.sqrt(64)
print(C)

# math.ceil() method rounds a number upwards to its nearest integer while math.floor() rounds downwards

# D = math.ceil(1.5)
D = math.ceil(1.4)

# E = math.floor(1.5)
E = math.floor(1.4)

print(D) # returns 2
print(E)   # returns 1


F = math.pi
print(F)


"""
WHY WE USE % AS FORMATTER
The % SYMBOL is called the Modulo Operator which returns the remainder of dividing the left hand operand by right hand
operand

where have %s in out string as placeholder representing a string... it is used to indicate that a sting should be 
inserted at that position in the final string 

"""

for number in range(1, 10):
    if(number % 2 != 0):
        print(number)