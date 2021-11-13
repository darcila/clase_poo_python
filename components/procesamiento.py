import pandas as pd

class ProcesamientoUsuarios:
    df = None

    def __init__(self):
        self.df = pd.DataFrame()

    def filtrar_edades(self, edad_minima):
        return self.df.loc[self.df['edad'] > edad_minima]

    def filtrar_coincidencia(self, columna, filtro):
        return self.df[self.df[columna] ]  #por favor completar esta linea

    def agregar_datos(self, datos):
        self.df = self.df(datos, ignore_index=True)