
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.entry_number1 = tk.Entry(self.master, width=10)
        self.entry_number1.grid(row=0, column=0)

        self.entry_number2 = tk.Entry(self.master, width=10)
        self.entry_number2.grid(row=0, column=2)

        self.button_add = tk.Button(self.master, text="+", command=lambda: self.add())
        self.button_add.grid(row=1, column=0)

        self.result_label = tk.Label(self.master, text="Result")
        self.result_label.grid(row=1, column=1)

        self.result = tk.Label(self.master, text="", font=("Arial", 20))
        self.result.grid(row=1, column=3)

        self.master.title("Calculator")
        self.master.geometry("400x250+300+200")

    def add(self):
        try:
            number1 = float(self.entry_number1.get())
            number2 = float(self.entry_number2.get())
        except ValueError:
            self.show_error("Error: Please enter valid numbers.")
            return

        assert number1 and number2, "Error: Both numbers must be provided."

        result = number1 + number2
        self.update_result(result)

    def update_result(self, result):
        self.result.config(text=result)

    def show_error(self, error):
        tk.messagebox.showerror("Error", error)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
