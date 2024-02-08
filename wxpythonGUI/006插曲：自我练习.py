"""
要使用wxpython显示图像有几个步骤:
1, 创建一个自定义化的Frame类
2, 在类里
"""
import wx


class Frame(wx.Frame):
    def __init__(self, image: wx.Image, parent=None, n_id=-1, title='DefaultTitle',
                 pos=wx.DefaultPosition):
        temp: wx.Bitmap = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent=parent, id=n_id, title=title, pos=pos, size=size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)


class App(wx.App):
    def OnInit(self):
        image = wx.Image('wx.jpg', wx.BITMAP_TYPE_JPEG)
        frame = Frame(image)
        frame.Show()
        # 前面调用self而不是wx,是因为这是一个单独app, 一个单独的窗口,所以其顶级框架只针对该实例化窗口而不是全局
        self.SetTopWindow(frame)

        return True


app = App()
app.MainLoop()
