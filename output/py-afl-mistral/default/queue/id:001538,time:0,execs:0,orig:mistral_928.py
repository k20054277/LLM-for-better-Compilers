
import wx

class MyApp(wx.Frame):
    def __init__(self, title):
        super().__init__(title=title, size=(300, 200))

        self.text_ctrl1 = wx.TextCtrl(self, id=101, size=(150, -1), style=wx.TE_PROCESS_ENTER)
        self.text_ctrl1.Bind(wx.EVT_TEXT, self.OnTextCtrl1)

        self.text_ctrl2 = wx.TextCtrl(self, id=102, size=(150, -1), style=wx.TE_READONLY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.text_ctrl1, 0, wx.ALL | wx.EXPAND)
        sizer.Add((50, 5), 0)
        sizer.Add(self.text_ctrl2, 0, wx.ALL | wx.EXPAND)
        self.SetSizerAndFit(sizer)

        self.button = wx.Button(self, label="Enable next text box", id=103)
        self.button.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

        sizer.Add((50, 10), 0)
        sizer.Add(self.button, 0, wx.ALL | wx.EXPAND)

        self.Centre()
        self.Show(True)

    def OnTextCtrl1(self, event):
        self.text_ctrl2.SetValue("")

    def OnButtonClicked(self, event):
        if len(self.text_ctrl1.GetValue()) > 0:
            self.text_ctrl2.Enable()
        else:
            wx.MessageBox("First text box cannot be empty", "Error", wx.ICON_ERROR)

app = MyApp("Python and wxPython Demo")
app.MainLoop()
