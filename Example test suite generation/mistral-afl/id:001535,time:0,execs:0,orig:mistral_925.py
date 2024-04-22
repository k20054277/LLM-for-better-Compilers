
import tkinter as tk

# Function to check if two entered numbers are both greater than 10
def is_both_greater_than_ten(num1, num2):
 return num1 > 10 and num2 > 10

class MyApp:
 def __init__(self, master):
 self.master = master
 self.master.title("Python Tkinter Example")
 self.label = tk.Label(self.master, text="Enter two numbers:")
 self.label.pack()
 self.num1_entry = tk.Entry(self.master)
 self.num2_entry = tk.Entry(self.master)
 self.num1_entry.pack()
 self.num2_entry.pack()
 self.check_button = tk.Button(self.master, text="Check", command=self.check_numbers)
 self.check_button.pack()

 def check_numbers(self):
 num1 = int(self.num1_entry.get())
 num2 = int(self.num2_entry.get())
 if is_both_greater_than_ten(num1, num2):
 self.master.config(text="Both numbers are greater than 10")
 else:
 self.master.config(text="At least one number is not greater than 10")

root = tk.Tk()
app = MyApp(root)
app.mainloop()
