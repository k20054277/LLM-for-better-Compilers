import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, event):
        assert False, "The window is being closed"

app = wx.App()
frame = MyFrame(None, -1, "My Window")
frame.Show()
app.MainLoop()