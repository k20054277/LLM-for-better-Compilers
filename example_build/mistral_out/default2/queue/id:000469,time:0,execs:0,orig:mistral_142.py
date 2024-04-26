
import wx

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="My App")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title, size=(300, 200))

        # Create a button with the label "Quit"
        self.quit_button = wx.Button(self, -1, "Quit", pos=(50, 100), size=(75, 30))

        # Bind quit button event to OnQuit function
        self.Bind(wx.EVT_BUTTON, self.OnQuit, self.quit_button)

    def OnQuit(self, event):
        # Exit the application when the Quit button is clicked
        self.Close(True)

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

# The following code snippet demonstrates using False value
def is_even(number):
    return number % 2 == 0

print(is_even(4)) # prints True
print(is_even(5)) # prints False
