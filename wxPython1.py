import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title)
# создаем экземпляр класса MenuBar и экземпляр класса Menu
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        
# создаем пункт во вкладке fileMenu со строкой «Выход»
        # item = wx.MenuItem(fileMenu, wx.ID_EXIT, "Выход", "Выход из приложения")
# добавляем созданный пункт во вкладку fileMenu с помощью метода Append
        # fileMenu.Append(item)
# Вместо верхних двух строк можно:
        item = fileMenu.Append(wx.ID_EXIT, "Выход", "Выход из приложения")

# на панели menubar размещаем вкладку, также вызывая метод Append класса MenuBar
        menubar.Append(fileMenu, "&File")
# размещаем панель меню в нашем окне
        self.SetMenuBar(menubar)
# Вызываем метод закрытия окна при нажатии на 'Выход':
        self.Bind(wx.EVT_MENU, self.onQuit, item)

# Метод закрывает окно:
    def onQuit(self, event):
        self.Close()


app = wx.App()

wnd = MyFrame(None, 'Hello!')
wnd.Show()

app.MainLoop()
