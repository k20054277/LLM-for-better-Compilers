import tkinter as tk

root = tk.Tk()

# Create a label widget
label = tk.Label(root, text="Enter your name:")
label.pack()

# Create an entry widget for the user to enter their name
entry = tk.Entry(root)
entry.pack()

# Create a button widget to submit the user's name
button = tk.Button(root, text="Submit", command=lambda: None)
button.pack()

# Get the user's name from the entry widget and display it in the label
def get_name():
    name = entry.get()
    if name != "":
        label["text"] = f"Hello, {name}!"

button.configure(command=get_name)

root.mainloop()