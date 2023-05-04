import random

print("cakahal johnson")

# welcome to your desktop app python class with a single line comments
"""
this for multiline comments 
1. variables: is a container for storing data values

2. Numbers data type here we talk about Operators and Bloolean 

3. Arrays here we talk about sorting or collecting data from given list, dict ....

4. Conditional Statement here is about setting a conditions in which our code will be run

5.  Class and Objects this is how our codes will interact with each other

6. Functions in functions we talk about setting other class and methods


7. Projects.... 
"""

# Python Data TYPES
# these are the Data type created by python programmers and it's a built-in function by default, it's for identifying
# our data

# Data Types are:
# String - str is for text or words
# Numeric Types: int, float, complex
# Sequence Type: list, tuple, range...
# Mapping Types: dict
# Set Types: set, fronzenset
# Boolean type: condition which is True or False

# Assigning Data Types:

# String Example:
text = "This string is involues about 400 words max "

# Numeric Example:
int_number = 1234567890
float_number = 100.99
complex_num = 1j

# Sequence Example
list_word = ["car", "house", "money"]
tuple_word = ("car", "house", "money")
range_number = (8)

# Mapping Example
dict_word = {"keys": "values", "Name": "Chidera Johnson", "Age": 70}

# Set Example
set_word = {"car", "marriage", "money"}
frozenset_word = frozenset({"money", "marriage", "car"})

# Boolean Type Example
ON_light = True
Off_light = False

# Binary Types Example
bytes_number_checking = b"hello"
bytearray_number_checking = bytearray(8)
memoryview_checking = memoryview(bytes(500))


# here lets work Numbers
Age = 70
print(Age)

money = 1000.99
print(money)

kelven = 1j
print(kelven)


# methods for converting from one number Data types to another: which casting
print("====================================")
cov_age_into_float = float(Age)
print(cov_age_into_float)

float_into_int = int(money)
print(float_into_int)

float_into_compl = complex(money)
print(float_into_compl)


# Python Random Number
# to use python random we need to import the random into our workspace at number and just write import random
print("======Random Display ================")
print(random.randrange(0, 9))

# NExt Topic Python Strings thanks for your time.....
