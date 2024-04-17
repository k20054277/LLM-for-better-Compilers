
import wx

class MyApp(wx.App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def OnInit(self):
        self.frame = MyFrame(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MyFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent=parent, title="My Frame", size=(300, 200))

        # Create a button with the label "Click Me" and bind it to an event handler
        self.button = wx.Button(self, label="Click Me")
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked, self.button)

        # Create a sizer to arrange the button in the frame
        box_sizer = wx.BoxSizer(wx.VERTICAL)
        box_sizer.Add(self.button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL)

        # Set the sizer for the frame
        self.SetSizer(box_sizer)

    def OnButtonClicked(self, event):
        # When the button is clicked, print a message to the console and reset the button label
        print("Button clicked!")
        self.button.SetLabel("Clicked!")

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
