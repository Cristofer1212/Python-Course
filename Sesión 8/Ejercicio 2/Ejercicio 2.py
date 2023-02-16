import pickle

class Vehículo ():
    def __init__(self, color, puertas, ruedas):
        self.color = color
        self.puertas = int(puertas)
        self.ruedas = int(ruedas)
    def __str__(self):
        return f"El carro es de color {self.color}, tiene {self.puertas} puertas y {self.ruedas} ruedas"
    
mi_Vehículo = Vehículo("negro", 4, 4)

print(mi_Vehículo)

f = open("mi_Vehículo_caracteristica", "w")

# Guardar el objeto en un archivo binario y convertir el objeto a binario
with open("mi_Vehículo_caracteristica", "wb") as f:
    pickle.dump(mi_Vehículo, f)

# Cargar el objeto desde el archivo  (leer y deserializar) 

with open("mi_Vehículo_caracteristica", "rb") as f:
    x = pickle.load(f)

# Imprimir el objeto cargado desde el archivo
print(x.color)
print(x.puertas)
print(x.ruedas)
