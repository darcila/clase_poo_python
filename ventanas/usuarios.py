import wx
import requests
from components import Ventana


class Usuarios:
    __url_api = 'https://gorest.co.in/public/v1/'
    __endpoint = 'users'
    __ventana = None

    def __init__(self, titulo):
        self.__consultar_usuarios(1)
        self.__iniciar_ventana(titulo)


    def __iniciar_ventana(self, titulo):
        app = wx.App()
        frm = Ventana(None, title=titulo, size=(600, 600))
        frm.Show()
        app.MainLoop()

    def __consultar_usuarios(self):
        url = '{}/{}?page={}'.format(self.__url_api, self.__endpoint, self.pagina_actual)
        r = requests.get(url)
        usuarios_request = r.json()
        self.usuarios = usuarios_request['data']
        self.paginacion = usuarios_request['pagination']


