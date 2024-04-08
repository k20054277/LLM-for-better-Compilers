
import wx

# Define a simple wxPython application
class MyApp(wx.App):

    def OnInit(self):
        # Create a frame
        frame = wx.Frame(None, title="wxPython Example")

        # Create a panel
        panel = wx.Panel(frame)

        # Create a label
        label = wx.Label(panel, label="Hello, world!")

        # Show the frame
        frame.Show()

        return True

# Create an instance of the app
app = MyApp()

# Start the app
app.MainLoop()
