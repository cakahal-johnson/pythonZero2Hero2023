import calendar

"""
PYTHON USER INPUT
this just allows for user input
in version 2.7 uses raw_input()
        3.6 uses input()


"""

username = input("Enter Username:")
print("Welcome to your Dashboard: " + username)

# checking for if Vowel or consonant or non using If statement
# print("Enter the Character: ")
# c = input()
#
# if c == 'a' or c == 'e' or c=='i' or c=='o' or c=='u':
#     print("\n It is a Vowel")
# elif c == "A" or c=="E" or c=="I" or c=='O' or c=='U':
#     print("\n It is a Vowel")
# else:
#     print("\n It is a Consonant")


# # another method using len() nested if statement
# print(end="Enter a Character: ")
# a = input()
#
# size = len(a)
# if size > 1:
#     print("\n Invalid Input")
# else:
#     if (a >= 'a' and a <= 'z') or (a >= 'A' and a <= 'Z'):
#         if a == 'a' or a == 'e' or a =='i' or a =='o' or a =='u':
#             print("\n\"" +a+ "\" is a Vowel")
#         elif a == "A" or a =="E" or a =="I" or a =='O' or a =='U':
#             print("\n\"" +a+ "\" is a Vowel")
#         else:
#             print("\n\"" +a+ "\" is a Consonant")
#     else:
#         print("\n\"" +a+ "\" is neither a Vowel or a Consonant")

# another method using len() lesser code
# print(end="Enter a Character: ")
# a = input()
#
# size = len(a)
# if size > 1:
#     print("\n Invalid Input")
# else:
#     if (a >= 'a' and a <= 'z') or (a >= 'A' and a <= 'Z'):
#         vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#         if a in vowels:
#             print("\n\"" +a+ "\" is a Vowel")
#         else:
#             print("\n\"" +a+ "\" is a Consonant")
#     else:
#         print("\n\"" +a+ "\" is neither a Vowel or a Consonant")



# TimeTable
# print(end="Enter a Number: ")
# num = int(input())
#
# k = 1
# print("\n Multiplication Table:")
# for i in range(10):
#     mul = num * k
#     print(mul)
#     k = k+1
#
# # Multiplication Table format:
# print(end="Enter a Number:")
# Num = int(input())
# j = 1
# print("\n Multiplication Table:")
# for n in range(1, 11):
#     print(str(Num)+ " * " +str(n)+ " = " +str(Num*n))


# Multiplication Table format: using a while
# print("Enter a Number Using while loop:")
# NUM = int(input())
# print("\n Multiplication Table:")
# b = 1
# while b < 11:
#     print(str(NUM)+ " * " +str(b)+ " = " +str(NUM*b))
#     b = b+1

# give Multiplication Table format: using a while but to get two input value
print("Enter The Range: ")
s = int(input())
e = int(input())

if s==e:
    numba = s
    print("-----Multiplication Table of " +str(numba)+ "--------")
    for p in range(1, 11):
        print(str(numba)+ " * " +str(p)+ " = " +str(numba*1))
elif s > e:
    numba = e
    while numba <= s:
        print("-----Multiplication Table of " + str(numba) + "--------")
        for p in range(1, 13):
            print(str(numba) + " * " + str(p) + " = " + str(numba * 1))
        numba = numba+1
else:
    numba = s
    while numba <= e:
        print("-----Multiplication Table of " + str(numba) + "--------")
        for p in range(1, 11):
            print(str(numba) + " * " + str(p) + " = " + str(numba * 1))
        numba = numba+1


# using a calender with input first we import the calendar
print("Enter Year: ")
yy = input()
print("\n Enter Month Number (1-12): ")
mm = input()

y = int(yy)
m = int(mm)
print("\n", calendar.month(y, m))

# Modified version by using try-except
# end = used in this program to skip inserting an automatic newline using print()
print("Enter Year", end="")

try:
    yyy = int(input())
    print("\n Enter Month Number (1-12): " , end="")
    try:
        mmm = int(input())
        if  mmm >= 1 and mmm<=12:
            print("\n", calendar.month(yyy, mmm))
        else:
            print("\nInvalid Month Number!")
    except ValueError:
        print("\nInvalid Input!")
except ValueError:
    print("\nInvalid Input!")



# Displaying all Month by using try-except
print("Enter Year", end="")
try:
    yyyy = int(input())
    print()
    mmmm = 1
    while mmmm <= 12:
        print(calendar.month(yyyy, mmmm))
        mmmmm = mmmmm+1
except ValueError:
    print(("\nInvalid Input!"))

