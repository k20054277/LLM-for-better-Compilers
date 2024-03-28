
# Import Tkinter module
from tkinter import *

def main():
    # Create the root window
    root = Tk()

    # Set window title and size
    root.title("Tkinter with as keyword")
    root.geometry("300x200")

    # Create a Label widget
    label = Label(root, text="Hello Tkinter!", font=("Arial", 18))

    # Pack the Label widget into the window
    label.pack(pady=20)

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
