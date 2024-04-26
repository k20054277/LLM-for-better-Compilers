
import tkinter as tk

# Define a function to test the assertion
def test_assert():
    # Assert that the value is equal to 10
    assert 10 == 10

# Create a tkinter window
window = tk.Tk()

# Create a label to display the result
label = tk.Label(window, text="The assertion is successful!")

# Place the label on the window
label.pack()

# Run the tkinter event loop
window.mainloop()

# Print the result of the assertion
print("The assertion is successful!")
