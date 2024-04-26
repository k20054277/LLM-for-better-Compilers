
import tkinter as tk

# Create a Tk root window
root = tk.Tk()

# Set up a title and size for the window
root.title("Python Tkinter Example")
root.geometry("300x200")

# Define a function to handle the button click event
def button_clicked():
    message = "Hello, World!"
    label.config(text=message)

# Create a frame to hold the button and label
frame = tk.Frame(root)
frame.pack(pady=20)

# Create a button with the text "Click Me"
button = tk.Button(frame, text="Click Me", command=button_clicked)
button.pack(side=tk.LEFT)

# Create a label to display the message
label = tk.Label(frame, text="")
label.pack(side=tk.LEFT, padx=10)

# Start the Tk event loop
root.mainloop()
