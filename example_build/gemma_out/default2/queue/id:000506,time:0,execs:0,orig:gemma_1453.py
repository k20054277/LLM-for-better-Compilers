
import wx

# Define a class to inherit from wx.Frame
class MyFrame(wx.Frame):

    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent)

        # Create a panel on the frame
        panel = wx.Panel(self)

        # Add a label to the panel
        label = wx.Label(panel, label="Hello, world!")

        # Assert that the label text is correct
        assert label.GetLabel() == "Hello, world!"

    def run(self):
        # Show the frame
        self.Show()

        # Event loop
        wx.EventLoop()


# Create an instance of the frame
frame = MyFrame()

# Run the frame
frame.run()
