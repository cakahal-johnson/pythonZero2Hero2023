import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
root.title("cakahal johnson")
root.geometry("600x200")

photo = tk.PhotoImage(file="bg.jpg")

label = tk.Label(root, image=photo, bg="black", fg="yellow", width=600, height=200)

label.pack()

root.mainloop()