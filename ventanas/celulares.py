import wx
from components import Ventana, ScrappingCelulares, procesamiento

class Celulares:

    def __init__(self):
        self.cargar_celulares()
        self.procesar()
        self.__iniciar_ventana('Listado celulares')

    def __iniciar_ventana(self, titulo):
        app = wx.App()
        frm = Ventana(None, title=titulo, size=(600, 600))
        frm.Show()
        app.MainLoop()

    def cargar_celulares(self):
        celulares = ScrappingCelulares()

    def procesar(self, tope_minimo):
        pass
        #mostrar en el tabla los celulares que tengan un tope minimo en su valos