import tkinter as tk

# Creación de la ventana principal
root = tk.Tk()
root.title("Casilla de verificación")
root.geometry("300x200")

# Función para manejar el evento de la casilla de verificación
def handle_checkbox_event():
    if check_var.get() == 1:
        label.config(text="Casilla de verificación activada")
    else:
        label.config(text="Casilla de verificación desactivada")

# Creación de la variable booleana para la casilla de verificación
check_var = tk.IntVar()

# Creación de la casilla de verificación
checkbox = tk.Checkbutton(root, text="Activar", variable=check_var, command=handle_checkbox_event)
checkbox.pack()

# Creación de la etiqueta
label = tk.Label(root, text="Casilla de verificación desactivada")
label.pack()

# Inicio del bucle de eventos
root.mainloop()
