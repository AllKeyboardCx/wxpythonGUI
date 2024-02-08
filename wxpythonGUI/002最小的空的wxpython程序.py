import wx   # 导入必须的wxPython包


class App(wx.App):  # 子类化wxPython应用程序类
    def OnInit(self):  # 定义一个应用程序的初始化方法
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()
        return True


app = App()   # 创建一个应用程序类的实例
app.MainLoop()     # 进入这个应用程序的主事件循环
