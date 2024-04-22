
import wx

# Define a simple wxpython application
class MyApp(wx.App):
    def OnInit(self):
        # Create a frame
        frame = wx.Frame(None, title="wxpython Example")

        # Create a panel
        panel = wx.Panel(frame)

        # Create a label
        label = wx.Label(panel, label="Hello, wxpython!")

        # Show the frame
        frame.Show()

        return True

# Run the application
if __name__ == "__main__":
    app = MyApp()
    app.Run()
