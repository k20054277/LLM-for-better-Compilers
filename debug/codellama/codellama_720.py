import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="My Frame", size=(200, 100))
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label="Click me!")
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)

    def on_button_click(self, event):
        print("The button was clicked!")

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()