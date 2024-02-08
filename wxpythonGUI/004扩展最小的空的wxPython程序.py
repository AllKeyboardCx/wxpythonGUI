import wx


class Frame(wx.Frame):
    pass


class App(wx.App):
    def OnInit(self):
        self.frame = Frame(parent=None, title='nak')
        self.frame.Show()
        # 将frame设置为主要对话框
        self.SetTopWindow(self.frame)
        return True


app = App()
app.MainLoop()