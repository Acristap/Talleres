while True:
# Imprimir Resetas Fitness
    print("Sitio Resetas Fitness:")
    print("1. Desayunos")
    print("2. Almuerzos")
    print("3. Comidas")
    print("4. Salir")

    # Solicitar al usuario que ingrese una opción
    opcion = input("Ingrese el número de opción que desea: ")

    # Procesar la opción seleccionada
    if opcion == "1":
        print("Ha seleccionado la Opción la opción Desayunos.")
    elif opcion == "2":
        print("Ha seleccionado la Opción de Almuerzos.")
    elif opcion == "3":
        print("Ha seleccionado la Opción de Comidas.")
    elif opcion == "4":
        print("Saliendo del programa ... ")
        break # Salir del ciclo while

    else:
        print("Opción inválida. Por favor, ingrese un número válido.")