# Cajas de Texto con tk.Entry
import tkinter as tk

# Creación de la ventana principal
root = tk.Tk()
root.title("Ventana con caja de texto")

# Creación de la caja de texto
entry = tk.Entry(root)
entry.pack()

# Bucle de la ventana principal
root.mainloop()