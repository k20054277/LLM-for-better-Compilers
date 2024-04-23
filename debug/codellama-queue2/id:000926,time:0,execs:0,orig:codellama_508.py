import wx

# Create a frame with a label and a text control
frame = wx.Frame(None, title="Example")
label = wx.StaticText(frame, -1, "Enter your name:")
text_ctrl = wx.TextCtrl(frame, -1, "")

# Add the widgets to the frame
vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(label)
vbox.Add(text_ctrl)
frame.SetSizer(vbox)

# Create a button and add it to the sizer
button = wx.Button(frame, -1, "Print Name")
vbox.Add(button)

# Bind the button to a function that will print the name when clicked
def print_name(event):
    name = text_ctrl.GetValue()
    if not name:
        name = "Anonymous"
    wx.MessageBox("Hello, " + name + "!", "Greeting")

button.Bind(wx.EVT_BUTTON, print_name)

# Create a menu bar and add it to the frame
menu_bar = wx.MenuBar()
file_menu = wx.Menu()
file_menu.Append(wx.ID_EXIT, "Exit")
menu_bar.Append(file_menu, "File")
frame.SetMenuBar(menu_bar)

# Create a status bar and add it to the frame
status_bar = wx.StatusBar(frame)
frame.SetStatusBar(status_bar)

# Show the frame and start the application's event loop
frame.Show()
app.MainLoop()