while True:
# Imprimir sitio deportivo
    print("Sitio Deportivo:")
    print("1.Deportes en equipo")
    print("2. Deportes en solitario")
    print("3. Deportes acuaticos")
    print("4. Deportes Terrestres")
    print("5. Salir")

    # Solicitar al usuario que ingrese una opción
    opcion = input("Ingrese el número de opción que desea: ")

    # Procesar la opción seleccionada
    if opcion == "1":
        print("Ha seleccionado la Opción 1.")
    elif opcion == "2":
        print("Ha seleccionado la Opción 2.")
    elif opcion == "3":
        print("Ha seleccionado la Opción 3.")
    elif opcion == "4":
        print("Ha seleccionado la Opción 4.")
    elif opcion == "5":
        print("Saliendo del programa ... ")
        break # Salir del ciclo while

    else:
        print("Opción inválida. Por favor, ingrese un número válido.")