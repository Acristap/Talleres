while True:
# Imprimir Mascotas
    print("Sitio de Mascotas:")
    print("1. Esterilización")
    print("2. Vacunas")
    print("3. Alimentos")
    print("4. Guarderia")
    print("5. Salir")


    # Solicitar al usuario que ingrese una opción
    opcion = input("Ingrese el número de opción que desea: ")

    # Procesar la opción seleccionada
    if opcion == "1":
        print("Ha seleccionado la Opción la opción Esterilización.")
    elif opcion == "2":
        print("Ha seleccionado la Opción de Vacunas.")
    elif opcion == "3":
        print("Ha seleccionado la Opción de Alimentos.")
    elif opcion == "4":
        print("Ha seleccionado la Opción de Guarderia.")
    elif opcion == "5":
        print("Saliendo del programa ... ")
        break # Salir del ciclo while

    else:
        print("Opción inválida. Por favor, ingrese un número válido.")