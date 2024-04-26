
import sys
from wx.artProvider import ArtProvider, CHOICE_IMAGE_LIST
import wx

class Frame(wx.Frame):
    def __init__(self, parent, id=1):
        super().__Init__(parent, id="My Frame", size=(300, 200), style=wx.DEFAULT_FRAME_STYLE)

        self.centre()

        # Create a static text control and assign it to a variable
        self.staticText = wx.StaticText(self, id=-1, label="Hello World!", pos=(50, 50))

        # Set the size of the static text control and centre it horizontally and vertically
        self.staticText.SetSizeHints(minSize=(100, -1), maxSize=(300, -1))

        # Create a menu bar using an art provider
        artProvider = ArtProvider()
        imageList = artProvider.AddBitmaps(["images/menu_image.bmp"], CHOICE_IMAGE_LIST)

        self.menuBar = wx.Menu()

        fileMenuItem = self.menuBar.Append(wx.NewId(), "&File", bitmap=imageList[0])
        self.menuBar.AppendSeparator()
        exitMenuItem = self.menuBar.Append(wx.NewId(), "E&xit")

        # Bind event handlers for the menu items
        fileMenuItem.Bind(wx.EVT_MENU, self.onFile)
        exitMenuItem.Bind(wx.EVT_MENU, self.onExit)

        self.SetMenuBar(self.menuBar)

    def onFile(self, event):
        print("File menu was clicked!")

    def onExit(self, event):
        self.Close(True)

if __name__ == "__main__":
    app = wx.App()
    frame = Frame(None)
    frame.Show(True)
    sys.exit(app.MainLoop())
