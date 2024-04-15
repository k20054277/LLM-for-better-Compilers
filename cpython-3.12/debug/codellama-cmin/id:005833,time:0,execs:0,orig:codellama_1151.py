import tkinter as tk

root = tk.Tk()
root.title("My GUI")
root.geometry("200x100")

label = tk.Label(root, text="Hello World!")
label.pack()

root.mainloop()