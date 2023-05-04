"""
let's try code for shutdown without GUI
first we import os since we will communicate with the system
"""
#
# import os
#
# print("1. Shutdown Computer Immediately")
# print("2. Shutdown Computer after Given Time")
# print("3. Restart Computer Immediately")
# print("4. Restart Computer after Given Time")
# print("5. Exit")
# print(end="Enter Your Choice: ")
# choice = int(input())
#
# if choice == 1:
#     os.system("shutdown /s /t 0")
#
# elif choice == 2:
#     print(end="Enter Number of Seconds: ")
#     sec = int(input())
#     strOne = "shutdown /s /t "
#     strTwo = str(sec)
#     str = strOne + strTwo
#     os.system(str)
#
# elif choice == 3:
#     os.system("shutdown /r /t 0")
#
# elif choice == 4:
#     print(end="Enter Number of seconds: ")
#     sec = int(input())
#     strOne = "shutdown /r /t "
#     strTwo = str(sec)
#     str = strOne + strTwo
#     os.system(str)
#
# elif choice == 5:
#     exit()
# else:
#     print("Opps! Wrong Choice!")

# =============================================== GUI for Os ==============================================

from tkinter import *
import os


# defining the function
def shutdown():
    return os.system("shutdown /s /t 1")


def restart():
    return os.system("shutdown /r /t 1")


def logout():
    return os.system("shutdown -1")


# tkinter object
master = Tk()

# setting the background color gray
master.configure(bg='light grey')

# creating a button using the widget
# Buttons that will call the submit function
Button(master, text="Shutdown", command=shutdown).grid(row=0)
Button(master, text="Restart", command=restart).grid(row=1)
Button(master, text="Exit", command=logout).grid(row=2)

mainloop()

