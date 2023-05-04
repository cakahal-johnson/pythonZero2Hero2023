"""
PYTHON CONDITIONS AND IF STATEMENTS
here we commonly use "if statements" and loops

keyword IF: indentation relies also as syntax

where:  Equals: a == b
        not Equals: a != b
        Less than: a < b
        less than or Equal to: a <= b
        Greater than or Equal to: a >= b
"""

a = 33
b = 342

# where we have only one condition to check for: we use only IF and return
if b > a:
    print("yes B is greater than a")

# where we have two or more conditions to check for: we use "if, elif,....else is also the default

# this elif: will execute if the if condition is not meant

c = 666
d = 666
e = 999
f = 9999

if d > c:
    print("yes d is greater than c")
elif d > f:
    print("No d is less than e")
else:
    print('printing for Else: ', "Non of the above is True")


# Short hand of If statement
if c < f: print('short hand for IF: ', "Yes c is less than f")

# Short hand of else statement
print("Yes") if e > f else print('short hand for else', "NO")


"""
where we have multiple else statements on the same line we use Ternary Operators or Conditional Expressions
"""
print("C") if c > d else print("=") if c == d else print("D")
# Returns =

# we can also use the AND keyword
if f > c and e > d:
    print('printing with AND keyword: ', "Both conditions is True")

# we can also use the OR keyword
if f > c or e < d:
    print('printing with OR keyword: ', "Both conditions is not True will execute b'cos of OR keyword")


"""
NESTED IF STATEMENT
here you can have if statements inside If statements, as a nested if statement

"""

inec = 100

if inec > 50:
    print("Yes is above 50")
    if inec > 80:
        print("Yes is above 80")
    else:
        print('Nested if statement: ', "but not either")


"""
The PASS Statement
since if statements cannot be empty, but if you for some reason have an if statement with no content, put in the PASS
statement to avoid getting an error...
"""
# if c > f: Returns Error

if c > f:
    pass


print("===========================next class is LOOPing==================================")




