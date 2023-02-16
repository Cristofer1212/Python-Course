import sqlite3 

# Crear Una conección
conn = sqlite3.connect('alumnos.db')

# Crear la tabla
# Tengo que conectar la  el archivo que he creado con el objeto cursor
cursor = conn.cursor()
cursor.execute('CREATE TABLE Alumnos (id INTEGER, nombre TEXT, apellido TEXT)')

# Insertar Datos en la tabla
lista = [ (12, 'Cristofer', 'Azaña'), (2, 'Fernando', 'Cherre'), (29, 'Kevin', 'Salinas')]
cursor.executemany('INSERT INTO Alumnos (id, nombre, apellido) VALUES (?,?,?)', lista)

# Guardar cambios y cerrar
conn.commit()
conn.close()  
 

