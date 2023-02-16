import time

# Creamos una variable que contenga la hora y la formateamos al forato deseado
hora = time.strftime("%H:%M")
# Convertimos el primer "%H" a entero 
hora_num = int(hora.split(':')[0]) 
# Convertimos "%M" en entero
minutos_num = int(hora.split(':')[1]) 
# Creamos una variable que de el vaor de 1 hora en minutos
hora_en_minutos = 60



if hora_num > 12 :
    hora_num = hora_num - 12
    sufijo = "PM"
else:
    sufijo = "AM"
# Pasamos todo lo que hicimos a hora con el formato f-string
hora = f"{hora_num:02d}:{hora.split(':')[1]} {sufijo}"

# creamos una función que indique cuanto falta para irno del trabajo
# Salimos del trabajo a las 7, entonces, si son más de las 7 PM, salimo
# Si son menos de las 7, el programa tiene que deolver cuant falta

hora_de_irnos = 7
hora_actual = int(hora.split(':')[0]) 

if int(hora_actual) >= int(hora_de_irnos):
    print("Es Hora de ir a casa")
else:
    falta_para_irnos_h = int(hora_de_irnos) - int(hora_actual)
    falta_para_irnos_m = int(hora_en_minutos) - int(minutos_num) 
    x = f"Faltan {falta_para_irnos_h} horas y {falta_para_irnos_m} minutos"
    print(x)

print(hora)
print(minutos_num)
print(hora_en_minutos)









