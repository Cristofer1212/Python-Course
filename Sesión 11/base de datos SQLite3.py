import sqlite3

# Crear una conexión a la base de datos
conn = sqlite3.connect('mi_base_de_datos.db')

# Crear una tabla
cursor = conn.cursor()
cursor.execute('CREATE TABLE clientes (id INTEGER, nombre TEXT)')

# Insertar datos en la tabla
cursor.execute('INSERT INTO clientes VALUES (?, ?)', (1, 'Juan Perez'))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
