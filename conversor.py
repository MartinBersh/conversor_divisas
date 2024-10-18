class ConversorMonedas:
    def __init__(self, tasas):
        self.tasas = tasas

    def convertir(self, cantidad, moneda_origen, moneda_destino):
        cantidad_str = self.entry_cantidad.get()

        if cantidad < 0:
            raise ValueError("La cantidad no puede ser nagativa")

        cantidad = float(cantidad_str)
        if moneda_origen not in self.tasas or moneda_destino not in self.tasas:
            raise ValueError("Moneda no soportada")

        cantidad_en_dolares = cantidad / self.tasas[moneda_origen]
        cantidad_convertida = cantidad_en_dolares * self.tasas[moneda_destino]
        return round(cantidad_convertida, 2)
