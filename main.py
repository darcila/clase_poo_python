import wx
from ventanas import Usuarios

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    usuarios = Usuarios(titulo='Listado de usuarios')