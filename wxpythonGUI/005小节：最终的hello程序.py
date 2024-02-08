import wx


class Frame(wx.Frame):
    def __init__(self, image: wx.Image, parent=None, n_id=-1,
                 pos=wx.DefaultPosition,  # 默认在屏幕中间
                 title='Hello,wxPython!'):
        # 将图像转换为位图
        temp: wx.Image = image.ConvertToBitmap()
        # 获得图片的长宽
        size = temp.GetWidth(), temp.GetHeight()
        # 初始化frame窗口
        wx.Frame.__init__(self, parent, n_id, title, pos, size)
        # 显示图像(StaticBitmap只能显示位图,所以上面要转换)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)


class App(wx.App):
    def __init__(self, redirect=False, filename=None, useBestVisual=False, clearSigInt=True):
        super().__init__(redirect, filename, useBestVisual, clearSigInt)
        self.frame = None

    def OnInit(self):
        image = wx.Image('wx.jpg', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


def main():
    app = App()
    app.MainLoop()


main()
