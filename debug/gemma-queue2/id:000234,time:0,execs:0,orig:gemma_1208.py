
import wx

# Define a class to demonstrate the use of as and wxpython
class DemoFrame(wx.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a panel on the frame
        panel = wx.Panel(self)

        # Create a label on the panel
        label = wx.Label(panel, label="Hello, world!")

        # Show the frame
        self.Show()

# Create an instance of the DemoFrame class
frame = DemoFrame()

# Run the wxpython event loop
wx.Run()
