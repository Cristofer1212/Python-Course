# Creamos una etiqueta con tk.Label

import tkinter as tk

# Crear una ventana principal
ventana = tk.Tk()

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Bienvenido a la aplicación")

# Empaquetar la etiqueta en la ventana
etiqueta.pack()

# Ejecutar la ventana
ventana.mainloop()