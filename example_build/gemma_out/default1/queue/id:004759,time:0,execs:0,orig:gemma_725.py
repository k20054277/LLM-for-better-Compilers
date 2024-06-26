
import wx

# Define a simple wxpython frame
class MyFrame(wx.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a panel on the frame
        panel = wx.Panel(self)

        # Create a label on the panel
        label = wx.Label(panel, label="Hello, world!")

        # Create a button on the panel
        button = wx.Button(panel, label="Click me")

        # Bind the button click event to a function
        button.Bind(wx.EVT_BUTTON, self.on_click)

    def on_click(self, event):
        # Display a message box when the button is clicked
        wx.MessageBox("Hello, world!", "Message")

# Create an instance of the frame
frame = MyFrame()

# Show the frame
frame.Show()

# Start the wxpython event loop
wx.Run()
