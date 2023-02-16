
from functools import reduce

numeros = [1, 2, 3, 4, 5, 6]

impares = list(filter(lambda x: x % 2 != 0, numeros))

resultado = reduce(lambda x, y: x + y, impares)

print(impares)
print(resultado) 
