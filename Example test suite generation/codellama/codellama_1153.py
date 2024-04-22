import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300, 200))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

    def OnButtonClick(self, event):
        print("Button clicked")

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, "My GUI Application")
    frame.Show()
    app.MainLoop()