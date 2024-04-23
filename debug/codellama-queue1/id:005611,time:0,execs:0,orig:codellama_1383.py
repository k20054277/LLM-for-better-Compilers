import tkinter as tk

def calculate(x, y):
    try:
        result = x + y
        assert result >= 0
        return result
    except AssertionError:
        return "Invalid input"

root = tk.Tk()
root.title("Calculator")

# Create a label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Create two entry fields for the user to enter numbers
num1_entry = tk.Entry(root)
num2_entry = tk.Entry(root)

# Create a button to calculate the sum
calculate_button = tk.Button(root, text="Calculate", command=lambda: result_label["text"] = str(calculate(int(num1_entry.get()), int(num2_entry.get()))))
calculate_button.pack()

# Create a button to clear the entry fields
clear_button = tk.Button(root, text="Clear", command=lambda: num1_entry.delete(0, "end"), num2_entry.delete(0, "end"))
clear_button.pack()

root.mainloop()