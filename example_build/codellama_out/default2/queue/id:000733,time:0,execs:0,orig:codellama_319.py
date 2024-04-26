import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.button = wx.Button(self, label="Click me!")
        self.button.Bind(wx.EVT_BUTTON, self.on_click)

    def on_click(self, event):
        print("Button clicked")

app = wx.App()
frame = MyFrame(None, "wxPython False Example")
frame.Show()
app.MainLoop()