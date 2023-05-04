"""
Exception Handling
This helps us to know when an error occurs, or exception as in python or other programming lang. uses this exception to
stop you not to generate an error and also generate an error message

These Exception has Three sections which is the TRY BLOCK this try block lets you test a block of code for errors
The Except Block: is where we handles the code and it's errors
The Finally Block: this lets you execute code, regardless of the result of the TRY and Except Block

Example: where we try a line to generate an error, be'cos we use x which is not defined:

"""
# print(x)
try:
    print(x)
except:
    print("An exception occured") # Output will hit an error b'cos X is not defined

name = "cakahal"
print(name)

# where we have many block of code that we want to check for
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")  #   output: the try block will generate a NameError, b'cos x is not define


# here we use Else keyword to define a block of code to be executed if no errors were raised
try:
    print("Cakahal Johnson")
except:
    print("something went wrong")
else:
    print("nothing went wrong")     # Output: The try block does not raise any errors, so the else block is executed


# Finally Block is specified. which will be executed regardless if the try block raises an error or not
try:
    print(x)
except:
    print("something went wrong")
finally:
    print("The 'try except' is finished ")


# exception when we want to open a file in out project
try:
    f = open("demofile.txt")
    f.write("here is the content of the file")
except:
    print("something went wrong when writing to the file")
finally:
    f.close() # the program can continue without leaving the file object Open

# these Exception is when you want to throw an exception if a condition occurs
#  to throw (or raise) and Exception, use the keyword raise...

x = -1
if x < 0:
    raise Exception("sorry, no numbers below zero") # An error will occurs

n = "We are done here"
if not type(n) is int:
    raise TypeError("only integers are allowed")

