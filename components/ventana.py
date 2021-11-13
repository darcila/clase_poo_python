#!/usr/bin/env python
import wx
import wx.grid
from datetime import datetime
import requests


class Ventana(wx.Frame):

    def __init__(self, *args, **kw):
        super(Ventana, self).__init__(*args, **kw)
        self.pnl = wx.Panel(self)

    def boton(self, label_boton, evento):
        self.my_btn = wx.Button(self.pnl, label=label_boton)
        self.my_btn.Bind(wx.EVT_BUTTON, evento)

    def cuadro_texto(self):
        self.text_ctrl = wx.TextCtrl(self.pnl)

    def tabla_entrada(self, main_sizer, columnas):
        self.list_ctrl = wx.ListCtrl(
            self.pnl, size=(-1, 200),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )

        for i, columna in enumerate(columnas):
            self.list_ctrl.InsertColumn(i, columna['nombre'], width=columna['ancho'])

        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)

    def actualizar_tabla(self, columnas, datos):
        self.list_ctrl.ClearAll()
        for i, columna in enumerate(columnas):
            self.list_ctrl.InsertColumn(i, columna.nombre, width=columna.ancho)


        for i, dato in enumerate(datos):
            self.list_ctrl.InsertItem(i, 0, dato.nombre)


    def consultar_usuarios(self, pagina):
        r = requests.get(f'https://gorest.co.in/public/v1/users?page={pagina}')
        usuarios = r.json()
        self.empleados = usuarios['data']
        self.actualizar_tabla()



