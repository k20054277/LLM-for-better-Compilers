import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.button = wx.Button(self, label="Click me!", pos=(60, 30))
        self.button.Bind(wx.EVT_BUTTON, self.on_button)
    
    def on_button(self, event):
        # Do something when the button is clicked
        print("Button was clicked!")

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, title="My Frame")
    frame.Show()
    app.MainLoop()