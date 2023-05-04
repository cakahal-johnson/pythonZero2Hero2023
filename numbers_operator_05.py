"""
Python Operators are the constructs which can manipulate the values of operands
these symbols use:
    Arithmetic Operators
    Assignment Operators
    Comparison Operators
    Logical Operators
    Indentity Operators
    Membership Operators
    Bitwise Operators
"""

# Arithmetic Operations: which is + * / - %(modulus) **(Exponent) //(Floor Division)
a = 21
b = 10

# Addition
print("a + b : ", a + b)

# Subtraction
print("a - b : ", a - b)

# Multiplication
print("a - b : ", a * b)

# Division
print("a / b : ", a / b)

# Modulus
print("a % b :", a % b)

# Exponent base10
print("a ** b : ", a ** b)

# Floor Division
print("a // b : ", a // b)

# Assignment Operators: these is used to assign values to variables
# Examples: =, +=, -=, *=, /=, %=, //=, **=, &= (Bitwise 'AND'), |=, ^= (Bitwise XOR), >>=, <<=
print(b)

c = 2
d = c
print(d)
d += 6
print(d)

e = 5
e &= 3
print(e)  # returns 1


f = 5
f |= 3
print(f)  # returns 7

# Comparison Operators is used to compare the values on either sides of them and decide the relation among them, you
# can also be called Relational operators NB: it's a Boolean which returns True or false
# Example: == Equal, != Not Equal, > Greater Than, < Less Than, >= Greater than or Equal sign, <= Less than or EqualSign

# Equal To:
print(4 == 5) # Returns False

# Not Equal
print(4 != 5)  # Returns True

# When same value
print(4 == 4)  # Returns True

# Greater Than
print(4 > 5)  # Returns False

# Less Than
print(4 < 5)  # Returns True

# Greater Than or Equal to
print("4 Greater or Equal to 5 : ", 4 >= 5)  # Returns False

print('Less Than or Equal to')
print(4 <= 5)  # Returns True

# Logical Operation: is used to combine conditional statements:
# Example: AND -where if both the operands are true then condition becomes true
# OR - where if any of the two operands are non-zero then condition becomes true

# NOT -where we use to reverse the logical state of its operand
x = 10
y = 20

# AND Logical
print('a and b : ', a and b)  # is True

print('checking for x with AND', x > 3 and x < 11 )  # True
print('checking for x with AND', x > 3 and x <= 10) # True
print('checking for x with AND', x > 3 and x < 10)  # False


# OR Logical
print('a or b :', a or b)  # is true

print('checking for x with OR', x > 3 or x < 10)  # True


# NOT logical
print('a not b', not(a and b))  # is false

print('checking for x with NOT', not(x > 3 and x < 11))  # False


# Identity Operators
"""
these is used to compare the objects, not if they are equal, but if they are actually the same object, with the same
memory location

using: is keyword and is not keyword
where is: Returns True if both variables are the same object
    is not: Returns True if both variables are not the same object
"""
a = ["java", "python", "php"]
b = ["java", "python", "php"]
c = a
print('checking with is keyword for both strings: ', a is c)
# returns True b'cos c is the same object as a

print('checking with is keyword for string and number as data type: ', x is a)
# returns False b'cos x is a int while a is a string object

print('checking with is keyword for d/f array as memory location: ', b is a)
# returns False b'cos b is of d/f memory location in a object

print('checking with is keyword for d/f array as memory location: ', b == a)
# returns True b'cos b is equal to a object


# Python Membership Operators
"""
Is used to test if a sequence is presented in an Object

using in keyword and not in keyword
where in: Returns True if a sequence with the specified values is present in the object
    not in: Returns True if a sequence with the specified value is not present in the object
"""

course = ["java", "python", "php"]
print('checking with java is in the array: ', "java" in course)
# returns True b'cos a sequence wth the value java is in the list

print('checking with JAVA is IN the array: ', "JAVA" in course)
# returns False b'cos a sequence wth the value JAVA is in the list but case-sensitive


print('checking with JAVA is NOT IN the array: ', "JAVA" not in course)
# returns True b'cos a sequence wth the value JAVA is in the list but case-sensitive

"""
Operator        Name                Description
&               AND                 Sets each bit to 1 if both bits are 1
|               OR                  Sets each bit to 1 if one of two bits is 1
^               XOR                 Sets each bit to 1 if only one of two bts is 1
~               NOT                 Inverts all the bits
<<              Zero fill           Shift left by pushing zeros in from the right and let the leftmost bits fall off
                left shift  
>>              Signed right        Shift right by pushing copies of the leftmost bit in from the left, and let the  
                shift               rightmost bits fall off
"""



