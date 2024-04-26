
import tkinter as tk

# Create a function that is called when the button is clicked
def on_button_click(event):
    # Set the value of 'should_quit' to False, and then set it back to True after a 2-second delay.
    global should_quit
    should_quit = False
    window.after(2000, lambda: should_quit = True)

# Create the main window and configure some settings
window = tk.Tk()
window.title("False and Tkinter Example")
window.geometry("300x150")

# Create a variable to store whether or not the application should quit
should_quit = True

# Create a label with some text
label = tk.Label(window, text="Click the button to toggle the value of 'False'!")
label.pack()

# Create a button and configure its settings
button = tk.Button(window, text="Toggle False", command=lambda: on_button_click(None))
button.pack()

# Start the main event loop
window.mainloop()

# The program continues running after the window is closed, so we exit when 'should_quit' becomes True again
while should_quit:
    pass
