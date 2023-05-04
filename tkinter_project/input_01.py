import tkinter as tk

root = tk.Tk()
root.title("Cakahal Johnson")
root.geometry("400x400")
# btn=tk.Button

# input without button
# va = tk.StringVar()
#
# entry = tk.Entry(root, textvariable = va)
# entry.place(x=180, y=180)
#
# label = tk.Label(root, textvariable = va)
# label.place(x=200, y=200)

# input button function
# entry = tk.Entry(root, show="*")
entry = tk.Entry(root)
entry.place(x=180, y=180)
# entry.insert(0, "Enter the password")

label = tk.Label(root, text="Empty label")
label.place(x=180, y=300)


def get_values():
    v = entry.get()
    label.config(text=v)
    # btn.config(text=v)


btn = tk.Button(root, text="Submit Update", command=get_values())
btn.place(x=180, y=250)


root.mainloop()