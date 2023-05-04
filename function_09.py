"""
PYHTON FUNCTIONS
function is just a block of code which only runs when it is called out.
--You can data, known *args is a parameter which accepts an argument
---A function can return data as a result

CREATING A FUNCTION
we use the keyword "def"

NB: when an information is passed into function it's an Arguments
Arguments:
    this is specified after the function name, inside the parentheses. You can add as many args as you want,
    just separate them with a comma

    N:B if you try to call function with 1 or 3 args, without matching it with the call out function you will basically
        get an error

        Arbitrary Arguments. *args
        if you do not know how many argument that will be passed into your function, just add a * before the parameter
        name in the function definition this is best when handing tuples

        *Arbitrary keyword Arguments, **kwargs
        : same as *args but best for dict(dictionary)

"""

# Function Syntax
def my_Func():
    print("Python is awesome!")

my_Func()
my_Func()
my_Func()
my_Func()

# Function with an Argument
def my_func(firstname):
    print(firstname + " Cakahal")

my_func("Johnson")
my_func("John")
my_func("cakahal")
# my_func()

# Function with 2 arguments
def my_two(fname, lname):
    print("Welcome to python class " +fname + " " + lname)

my_two("cakahal", "johnson")
my_two("Peter", "Obi")
my_two("UBA", "OBI")


# Arbitrary Arguments, *args
def my_abi(*ppl):
    print("How many ppl loves python " + ppl[4] )

my_abi("cakahal", "johnson", "peter", "Uba", "obi")


# using Keyword as Args, in this case the order does not matter
def my_key(java2, c1, py3):
    print("The best computer programming lang is: " + py3)

my_key(py3 = "AI, App", java2 = "android", c1 = "gaming" )


# Arbitrary Keyword
def my_Abi(**kid):
    print("The last login name is: " + kid["lname"])

my_Abi(fname = "Obi", lname = "Datti")


# Using a Default Parameter Value
def my_Df(country="biafra"):
    print("I am from " + country)


my_Df("London")
my_Df("Uk")
my_Df("")
my_Df()
my_Df("Us")


# Using a LIST as an argument
def my_Lt(courses):
    for x in courses:
        print(x)

course = ["python", "java", "c++", "c"]
car = ["benz", "lexus", "venza", "Rx750"]

my_Lt(course)
my_Lt(car)


# Using Return statement
def my_RT(a):
    return 5 * a

print(my_RT(8))
print(my_RT(99))
print(my_RT(2))

# Using Return statement with args
def my_my(n, m):
    return n + m

print(my_my(8, 6))

# Using the Pass Statement: is always b'cos a function definitions cannot be empty, so we the pass statement to avoid
# getting as error

def my_Txt():
    pass

print("thanks for banking with us!")


# Recursion
"""
python Recursion means: a defined function that can call itself.
    is common with mathematical and programming concept. that benefit loop through a data to a reach result which is 
    easy to slip into functions. 

"""

def my_rec(k):
    if (k > 0):
        result = k + my_rec(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n \nRecursion Example Results: ")
my_rec(6)

"""
In this example, my_rec is a function that we have defined to call itself("recurse"). we use the k variable as the data
which decrements(-1) every time we recurse. the recursion ends when the condition is not greater than 0 (i.e when is 0)
"""

# printing a christmas tree pathern
# def triShape(v):
#     for i in range(v):
#         for j in range(v-i):
#             print(' ', end=' ')
#         for p in range(2*i+1):
#             print('*', end=' ')
#         print()
#
# # generating pole shape for the tree
# def poleShape(v):
#     for i in range(v - 1):
#         for j in range(v - 1):
#             print(' ', end=' ')
#         print('* * *')
#
# row = int(input('Enter Number of the Rows: '))
#
# triShape(row)
# triShape(row)
# poleShape(row)

# creating a Hourglass pattern
# we start with Reading or entering the rows
# row = int(input("Enter number of Rows: "))
#
# print("here we generate the Hourglass Pattern is: ")
# # Upper-half section
# for i in range(row, 0, -1):
#     for j in range(row-i):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
#     print()
#
# # Lower-half
# for i in range(2, row+1):
#     for j in range(row-i):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("+", end="")
#     print()


# creating a Hourglass empty pattern
# we start with Reading or entering the rows
# row = int(input("Enter number of Rows: "))
#
# print("here we generate the Hourglass Empty Pattern is: ")
# # Upper-half
# for i in range(row, 0, -1):
#     for j in range(row-i):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         if i == 1 or i == row or j == 1 or j == 2*i-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#
# # Lower-half
# for i in range(2, row+1):
#     for j in range(row-i):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
#     print()


# where the lower-half will also be empty

# Square Pattern shaded
# row = int(input("Enter number of Rows: "))
#
# print("here we generate the Shaded Square Pattern is: ")
# for i in range(1, row+1):
#     for j in range(1, row+1):
#         print("*", end="")
#     print()
#
# # Square Pattern empty
# print("\n \nFor empty Square")
# row1 = int(input("Enter number of rows: "))
#
# print("Empty Square Pattern")
# for h in range(1, row+1):
#     for g in range(1, row+1):
#         if h ==1 or h == row or g == 1 or g == row:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# Rectangular empty and shaded
# also try empty tri-angle

# Checking for Vowel or consonant using Function
# def checkVowel(s):


print("\n \nstarting from function vowel")


def checkVowel(u):
    if (w >= 'a' and w <= 'z') or (w >= 'A' and w <= 'Z'):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if w in vowels:
            return 1
        else:
            return 2

print(end="Enter a Character: ")
w = input()

size = len(w)
if size > 1:
    print("\nInvalid Input!")
else:
    chk = checkVowel(w)
    if chk == 1:
        print("\nVowel")
    elif chk == 2:
        print("\nConsonant")
    else:
        print("\n Neither Vowel nor Consonant")


