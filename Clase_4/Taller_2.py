# Ejercicio 1
empleados = [
    {"Nombre": "Juan", "Horas Laborales": 40, "Horas Extras Nocturnas": 5},
    {"Nombre": "María", "Horas Laborales": 35, "Horas Extras Nocturnas": 3},
    {"Nombre": "Pedro", "Horas Laborales": 42, "Horas Extras Nocturnas": 6},
    {"Nombre": "Laura", "Horas Laborales": 38, "Horas Extras Nocturnas": 4}]
   
for empleado in empleados:
     print(f"Nombre: {empleado['Nombre']}, Horas Laborales: {empleado['Horas Laborales']}, Horas Extras Nocturnas: {empleado['Horas Extras Nocturnas']}")

#Ejercicio 2 Hacer un programa en Python 
#Para la gestión del centro deportivo.La facturación del servicio y descuento aplicado

cantidad_horas= input('ingrese cantidad horas:')
print('ingresaste:',cantidad_horas,'horas')
hora_bronce= 5000
hora_plata= 3500
hora_oro= 2000
if int(cantidad_horas )<= 15:
     print(f' la cantidad a pagar es:{int(cantidad_horas)*int(hora_bronce)}')
elif int(cantidad_horas) > 15 and int(cantidad_horas) <= 30:
     print(f' la cantidad a pagar es:{int(cantidad_horas)*int(hora_plata)}') 

elif int(cantidad_horas )> 30:
     print(f' la cantidad a pagar es:{int(cantidad_horas)*int(hora_oro)}')  
 
#Ejercicio 3 Crea un programa que permita calcular la calificación final de un estudiante
# a partir del promedio de sus notas.
#Superior: 90 - 100
#Alto: 80 - 89
#Básico: 70 - 79
#Bajo: 60 - 69
#Insuficiente: 0 - 59

nombre_estudiante= input('Ingrese el nombre del estudiante: ')
notas=(input('Ingrese las tres notas separadas por espacio: ').split())
notas=[float(nota) for nota in notas]
promedio= sum(notas)/ len(notas)
if   90 <= promedio <= 100:  calificación ='Superior'
elif 80 <= promedio <= 89: calificación ='Alto'
elif 70 <= promedio <= 79: calificación ='Básico'
elif 60 <= promedio <= 69: calificación ='Bájo'
elif  0 <= promedio <= 59: calificación ='Insuficiente'
print(f'nombre:{nombre_estudiante},promedio:{promedio},calificación:{calificación}')