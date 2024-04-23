import tkinter as tk

root = tk.Tk()
root.title("False Example")
root.geometry("200x100")

# Create a label
label = tk.Label(root, text="Do you want to continue?", font=("Arial", 14))
label.pack()

# Create a button
button = tk.Button(root, text="Continue", command=lambda: root.destroy())
button.pack()

# Create an entry box
entry = tk.Entry(root)
entry.pack()

# Set the focus to the entry box
entry.focus_set()

# Start the main loop
root.mainloop()