# Python String

print("welcome to Python Strings")
print('Python is Awesome')

# How to assign String to a variable
Uba = "i'm learning Python"
print(Uba)

# Multiline Strings
family = """ this is a multiline String syntax it can be single quote or double 
so, what that is inside this quote is a string
"""

print(family)

print("===========Strings Array=========")
# Strings in Arrays
classRoom = "laptop, phones, ipads, books"
print(classRoom[2:])

#Strings in loop
for f in "family":
    print(f)
    # what happened here if that loop has char f as in family this is we run...

# Checking for String Length
# so we use the word len() function to check for the length of a string
count4me = "Python is Awesome"
print(len(count4me))

# checking for a certain phrase or character if it's present in a string, will use the world: in
myApps = "laptop, phones, ipads, books"
print("ipads" in myApps)
# so here if ipads is inside the string called myApps, it prints boolean value which true or false
print("car" in myApps)

my_Db = "Chidera, Uba, Peter, Cakahal, Johnson"
if "Joy" in my_Db:
    print("yes, 'Joy' is present")
else:
    print("No 'Joy' is not present")

# checking with key word: not in
my_Db1 = "Chidera, Uba, Peter, Cakahal, Johnson"
print("Johnson" not in my_Db1)

if "Uba" not in my_Db1:
    print("yes, 'Uba' is not present")

print("=========== String slicing ==============")
# Slicing a String
# This get the characters from position placed and also not included:
my_Db2 = my_Db1
print(my_Db2[0:8])
print(my_Db2[8:13])

# slice to the End
# picking from back, but always by leaving out the end index, the range it will go to the end..
# In this Example get the characters from position 2, and all the way to the end
print(my_Db2[8:])

# Negative Indexing
# This uses negative index to start the slice from end of the string
# classwork lets get the character: son
classwork = my_Db2

# String Format
sub = "python"
Class = sub + " is awesome"
print(Class)

# This strings format can combine strings and numbers by using the format() method
Rate = 570
# buyer = "i want BTC as " + Rate + "Rate"
# print(buyer) # TypeError: can only concatenate str (not "int") to str

RATEE = 870
Buyer = "i want some BTC at, {} rate"
print(Buyer.format(RATEE))

Qty = 1000
coin = "BTC"
# myOrder = "i want to buy {2}, {0} at {1} rate "
myOrder = "i want to buy {}, {} at {} rate "

print(myOrder.format(Qty, coin, Rate))


# Strings are surrounded by either single quotation marks, or double quotation marks

"""
Python Collections (Arrays)
 List: list are used to store multiple items in single variables with syntax using square brackets
List items: are ordered, changeable, and allow duplicate values
List items: are indexed, the first item has index[0], the second item has index[1]

Ordered: means that the items have a defined order, and that order, will not change
just like if you add new items to a list, the new items will be placed at the end of the list
NB: there are some list methods that will change the order, but in general the order of the items will not change

Changeable: means that we can change, add and remove items in a list after it has been created

Allow Duplicates: means since lists are indexed, then lists can have items with the same value. 

"""
# list() Constructor
thislist = list(("benz", "lexus", "zenza")) # note the double round-brackets
print(thislist)

"""
Tuple: is a collection which is ordered and unchangeable. Allows duplicate members
Set: is a collection which is unordered and unindexed. No duplicate members
Dictionary: is a collection which is unordered and changeable. No duplicate members
List: is a collection which is ordered and changeable. Allows duplicate members
"""

# String Modification: python sets this built-in methods that you can use on strings
eg = " hello, World "
print(eg)

print(eg.upper())
print(eg.lower())

# removing whitespace
print(eg.strip())

# Replacing a string with the keyword replace
print(eg.replace("World", "UBA"))

# split string
# this method split() the string into substrings if not finds instances of the separator:

print(eg.split(","))

"""
Escape Characters 
to insert characters that are illegal in string, we use an escape characters
An escape characters starts with \ backslash following by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes
"""

esp = "this is how i'm "
good_eg = "learning python is awesome once you're done with \"python basics\" as a programmer "
print(good_eg)

"""
list of escape character in programming lang.
\' to use Single Quote
\\ to use Backslash
\n to goto new line
\r to return Carriage for functions
\t to use a tab
\b to use backspace
\f to use form feed
\ooo Octal value
\#ccc Hex value

"""

"""
capitalize() This converts the first character to uppercase
casefold() converts strings into lowercase
center() Returns a centered string
count() Returns the number of time a specified value occurs in a string
encode() returns an encoded version of the string
index() searches the strings for a specified value and returns the position of where it was found
translate() returns a translated string
e.t.c...

"""

"""
Translate() method returns a string where some specified characters are replaced with the character described in a 
dictionary, or in mapping table, we use maketrans() to create a mapping table

Syntax
string.translate(table)
where table is Required. Either a dictionary, or a mapping table description how to perform the replace  

"""

Uba = "learning python"
mytable = Uba.maketrans("p", "Z")
print(Uba.translate(mytable))

uba = "Hi Sam"

p = "mSa"
l = "eVa"

mytable2 = uba.maketrans(p, l)
print(uba.translate(mytable2))

ubA = "good night Sam!"

k = "mSa"
j = "eJo"
v = "odnight"
Mytable = ubA.maketrans(k, j, v)
print(ubA.translate(Mytable))


# Count() return the number of time the value of var like "python" appears in the string
UBA = "i love python, b'cos python are my favorite lang. python is the best"
n = UBA.count("python")
print(n)

# syntax: string.count(value, start, end)
# value is Required, A string where the string to "value" to search for
#  start Optional, An Integer where to start the search Default is 0
# end Optional, An Integer where to end the search Default is the end of the string

t = UBA.count("python", 15, 30)
print(t)

