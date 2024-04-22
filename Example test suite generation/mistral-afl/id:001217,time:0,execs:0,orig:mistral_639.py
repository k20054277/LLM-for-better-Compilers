
import wx

class MyApp(wx.App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.frame = MyFrame(None, title="My App")
        self.frame.Show()

        self.is_greetings_shown = True

    def OnInit(self):
        pass

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent=None, title=title, size=(300, 200))

        self.CreateStatusBar()

        self.button = wx.Button(self, label="Hide Greetings")
        self.button.Bind(wx.EVT_BUTTON, self.on_hide_greeting)
        self.button.Create(pos=(100, 50))

        self.status_text = "Hello World"

        if self.app.is_greetings_shown:
            self.ShowStatusBar()
            self.SetStatusText(self.status_text)

    def on_hide_greeting(self, event):
        self.app.is_greetings_shown = False
        self.HideStatusBar()
        self.Layout()

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
