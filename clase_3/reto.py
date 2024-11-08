#Reto
Capital_Inicial= input('Capital Inicial:')
print('El capital inicial es:',Capital_Inicial)
Tasa_interes_anual= input('Tasa Interes Anual:')
print('La Tasa de interes anual es:',Tasa_interes_anual)
Tiempo_años= input('Tiempo en años:')
print('La Tasa de interes anual es:',Tasa_interes_anual)
Interes= int(Capital_Inicial) * float(Tasa_interes_anual) *int(Tiempo_años)
print('El Interes es:',Interes)
Total_Deuda= int(Capital_Inicial) + Interes
print('Total de la deuda es:',Total_Deuda)