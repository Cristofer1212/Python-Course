# Crear el archivo de texto, el modo: Escritura (W)
f = open("nombre_del_archivo.txt", "w")

# Escribir en el Archivo
f.write("El Kevin ta loco \n")
f.write("Ademas es bien aragan ese csmr \n")

# Cerrando el Archivo
f.close()

# Abirneo el Archivo, modo: Lectura (r)
f = open("nombre_del_archivo.txt", "r")

# Leer el contenido del archivo
contenido = f.read()
print(contenido) 