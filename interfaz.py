import tkinter as tk
from tkinter import ttk
from conversor import ConversorMonedas
from constantes import TASAS_CAMBIO

class InterfazConversor:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Monedas")

        self.conversor = ConversorMonedas(TASAS_CAMBIO)

        self.label_cantidad = tk.Label(root, text="Cantidad:")
        self.label_cantidad.grid(row=0, column=0)

        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.grid(row=0, column=1)

        self.label_origen = tk.Label(root, text="Moneda Origen:")
        self.label_origen.grid(row=1, column=0)

        self.moneda_origen = ttk.Combobox(root, values=list(TASAS_CAMBIO.keys()))
        self.moneda_origen.grid(row=1, column=1)

        self.label_destino = tk.Label(root, text="Moneda Destino:")
        self.label_destino.grid(row=2, column=0)

        self.moneda_destino = ttk.Combobox(root, values=list(TASAS_CAMBIO.keys()))
        self.moneda_destino.grid(row=2, column=1)

        self.boton_convertir = tk.Button(root, text="Convertir", command=self.convertir)
        self.boton_convertir.grid(row=3, column=0, columnspan=2)

        self.resultado = tk.Label(root, text="")
        self.resultado.grid(row=4, column=0, columnspan=2)

    def convertir(self):
        try:
            cantidad = float(self.entry_cantidad.get())
            origen = self.moneda_origen.get()
            destino = self.moneda_destino.get()
            resultado = self.conversor.convertir(cantidad, origen, destino)
            self.resultado.config(text=f"{cantidad} {origen} = {resultado} {destino}")
        except ValueError as e:
            self.resultado.config(text=f"Error: {e}")
