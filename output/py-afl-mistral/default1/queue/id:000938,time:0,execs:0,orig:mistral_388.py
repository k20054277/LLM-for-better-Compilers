
import tkinter as tk

def main():
    # Create the root window
    root = tk.Tk()

    # Assign None to some variables
    var_entry = None
    button = None

    def button_clicked():
        if var_entry is not None:
            print("Entry value: ", var_entry.get())

    # Create a Label and Entry widget
    label = tk.Label(root, text="Enter some text here:")
    label.pack()
    var_entry = tk.StringVar()
    entry = tk.Entry(root, textvariable=var_entry)
    entry.pack()

    # Create a Button widget
    button = tk.Button(root, text="Click me!", command=button_clicked)
    button.pack()

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
