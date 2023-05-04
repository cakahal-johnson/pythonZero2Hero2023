"""
PYTHON LOOPS
This is also python primitive dataType
--- while loops
---for loops

where: while loop we can execute a set of statements as long as a condition is true

        for loops is used for iterating over a sequence(that is either a list, a tuple, a dictionary, a set, or a string
        with the FOR loop we can execute a set of statements, once for each item in a list, tuple, set ...
"""

print("while loops")

i = 1
while i < 6:
    print(i)
    i += 1

print("this increment i is important, or else the loop will continue forever")

# The Break Statement: we can stop the loop even if the while condition is true:
n = 1
while n < 6:
    print(n)
    if n == 4:
        break
    n += 1

# The continue Statement: where we can stop the current iteration and continue with the next:
a = 0
while a < 6:
    a += 1
    if a == 3:
        continue
    print(a)


# The else Statement where we can run a block of code once or when the condition no longer is true

b = 1
while b < 6:
    print(b)
    b += 1
else:
    print(" b is no longer less than 6")


print("For Loops Starts")
course = ["Java", "Python", "Php"]
for c in course:
    print(c)

# this For loop does not require an indexing variable to set beforehand

for d in "Python":
    print(d)

# FOR loop break statement
Course = ["Java", "Python", "Php"]
for e in Course:
    print(e)
    if e == "Python":
        break

Course = ["Java", "Python", "Php"]
for f in Course:
    if f == "Python":
        break
    print(f)

# FOR loop Continue Statement
Course = ["Java", "Python", "Php"]
for g in Course:
    if g == "Python":
        continue
    print(g)


print("Range() Start Function")
# This function returns a sequence of numbers starting from 0 by default, and increments by 1 (by defualt), and ends
# a specified number

for h in range(10):
    print(h)

# using 2 params
for j in range(5, 16):
    print(j)


# using 3rds where one we be the increment(the last fig)
for k in range(2, 30, 3):
    print(k)

# Else in FOR loop
for l in range(8):
    print(l)
else:
    print("finally finished!")

# this else block will NOt be executed if the loop is stopped by a break statement

for o in range(9):
    if o == 4:
        print(o)
    else:
        print("Finally finished!")

print("Nested Loops")
# A Nested loop is a loop inside a loop
# where the "inner loop" will be executed one time for each iteration of the "outer loop"

abc = ["A", "B", "C", "D"]
num = [1, 2, 3, 4]

for z in abc:
    for y in num:
        print(z, y)

print("Nested FOR loop")
Abc = ["A", "B", "C", "D"]
Num = ["a", "b", "c", "d"]

for s in Abc:
    for m in Num:
        print(s, m)

# The pass in FOR LOOP use to avoid getting an error
for p in [0, 1, 2, 3]:
    pass

print("LOOPs assignment before function")