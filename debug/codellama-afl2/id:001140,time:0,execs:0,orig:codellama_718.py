import tkinter as tk

root = tk.Tk()

# create a button with text "Click Me!"
button = tk.Button(root, text="Click Me!", command=lambda: print("Hello World!"))
button.pack()

# set the value of the variable "x" to True
x = True

# if the variable "x" is True, then print "Hello World!"
if x == True:
    print("Hello World!")

root.mainloop()