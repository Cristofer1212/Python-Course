import tkinter as tk

# Creación de la ventana principal
root = tk.Tk()
root.title("Botones de radio")
root.geometry("300x200")


# Función para manejar el evento de los botones de radio
def handle_radio_event():
    label.config(text="Opción seleccionada: " + str(var.get()))


# Creación de la variable de control para los botones de radio
var = tk.IntVar()


# Creación de los botones de radio
radio_1 = tk.Radiobutton(root, text="Opción 1", variable=var, value=1, command=handle_radio_event)
radio_2 = tk.Radiobutton(root, text="Opción 2", variable=var, value=2, command=handle_radio_event)
radio_3 = tk.Radiobutton(root, text="Opción 3", variable=var, value=3, command=handle_radio_event)


# Empaquetamiento de los botones de radio
radio_1.pack()
radio_2.pack()
radio_3.pack()


# Creación de la etiqueta
label = tk.Label(root, text="")
label.pack()

# Inicio del bucle de eventos
root.mainloop() 

