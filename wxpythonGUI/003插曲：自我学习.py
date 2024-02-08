import wx


class App(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(parent=None, id=-1, title='nak')
        self.frame.Show()
        return True


app = App()
app.frame.Hide()
app.MainLoop()
