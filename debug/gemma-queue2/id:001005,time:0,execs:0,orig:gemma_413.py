
import wx

# Define a simple wxpython application
class MyApp(wx.App):
    def OnInit(self):
        # Create a frame
        frame = wx.Frame(None, title="False and wxpython")

        # Create a panel
        panel = wx.Panel(frame)

        # Create a button
        button = wx.Button(panel, label="Click me")

        # Bind the button click event
        button.Bind(wx.EVT_BUTTON, lambda event: print("Hello, world!"))

        # Show the frame
        frame.Show()

        return True

# Create an instance of the application
app = MyApp()

# Start the application
app.MainLoop()
