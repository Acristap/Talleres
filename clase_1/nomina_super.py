EJERCICIO NÓMINA
empleados = int(input("¿Cuántos empleados calculará?: "))

for i in range(empleados):
    tipoCalculo = int(input("Para calcular solo por horas escriba 1. Para calcular por horas por semanas escriba 2. Para calcular por horas por días escriba 3. Para salir marque otro número: "))    
    if (tipoCalculo == 1):
        nombre = input("Ingresa nombre empleado: ")
        horas = int(input("Ingresa número de horas laboradas: "))        
        valorHora = int(input("Ingresa valor de 1 hora laborada: "))        
        total = horas * valorHora        
        print(f'{nombre} trabajó {horas} horas, a {valorHora} COP. Por tanto se le paga {total}')    
    elif (tipoCalculo == 2):
        nombre = input("Ingresa nombre empleado: ")
        horas = int(input("Ingresa número de horas laboradas: "))        
        semanas = int(input("Ingresa número de semanas laboradas: "))        
        valorHora = int(input("Ingresa valor de 1 hora laborada: "))
        total = horas * semanas * valorHora
        print(f'{nombre} trabajó {horas} horas a la semana, durante {semanas} semanas, a {valorHora} COP. Por tanto se le paga {total}')        
    elif (tipoCalculo == 3):
        nombre = input("Ingresa nombre empleado: ")
        horas = int(input("Ingresa número de horas laboradas: "))        
        dias = int(input("Ingresa número de dias laborados: "))
        valorHora = int(input("Ingresa valor de 1 hora laborada: "))        
        total = horas * dias * valorHora
        print(f'{nombre} trabajó {horas} horas, durante {dias} días, a {valorHora} COP. Por tanto se le paga {total}')
    else:
        print("Hasta la próxima")