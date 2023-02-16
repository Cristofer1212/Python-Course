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

# Función para buscar un alumno por nombre y mostrar los datos por consola
def buscar_alumno(nombre):
    consulta = 'SELECT id, nombre, apellido FROM Alumnos WHERE nombre=?'
    cursor.execute(consulta, (nombre,))
    resultado = cursor.fetchone()
    if resultado:
        print('ID:', resultado[0])
        print('Nombre:', resultado[1])
        print('Apellido:', resultado[2])
    else:
        print('El alumno no se encontró.')

# Ejemplo de uso de la función buscar_alumno
buscar_alumno('Fernando')



# Guardar cambios y cerrar
conn.commit()                   
conn.close()

 

