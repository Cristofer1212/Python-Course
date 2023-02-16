# Creación de desplegables con ttk.Combobox
import tkinter as tk
from tkinter import ttk

# Creación de la ventana principal
root = tk.Tk()

# Creación de una lista de opciones para el control desplegable
options = ["opción 1", "opción 2", "opción 3"]

# Creación del control desplegable usando ttk.Combobox
combo = ttk.Combobox(root, values=options)
combo.pack()

# Inicio del bucle de eventos de Tkinter
root.mainloop()