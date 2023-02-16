import tkinter as tk



# Creación de la ventana principal
root = tk.Tk()
root.title("Cristofer - Empanadero")
root.geometry("300x200")

# Funciones 
def precio ():
      label.config(text="El Precio es: S/" + str(var.get()) )

# Creación de la Variable de Control
var = tk.IntVar()

# Creación de los botones de radio
radio_1 = tk.Radiobutton(root, text="Empanada de pollo", variable=var, value= 3.50, command=precio)
radio_2 = tk.Radiobutton(root, text="Empanada de Carne", variable=var, value= 2.50 , command=precio)
radio_3 = tk.Radiobutton(root, text="Empanada de Jamon", variable=var, value= 1.50, command=precio)

# Empaquetamiento de los botones de radio
radio_1.pack()
radio_2.pack()
radio_3.pack()

# Creación de la etiqueta
label = tk.Label(root, text="")
label.pack()

# Inicio del bucle de eventos
root.mainloop() 