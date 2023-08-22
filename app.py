print("- - - - - - - - - - - - - - - - - - - - - - - -")
print("Practica 1 Lenguajes Formales y de Programacion")
print("- - - - - - - - - - - - - - - - - - - - - - - -")
while True:
    print()
    print("Elige una opcion por favor:")
    print()
    print("1. Cargar inventario inicial")
    print("2. Cargar instrucciones de movimientos")
    print("3. Crear informe de inventario")
    print("4. Salir")
    print()

    opcion = input("Ingresa una opcion: ")
    print()

    if opcion == "1":
        print("1. Cargar inventario inicial")
        print()
    elif opcion == "2":
        print("2. Cargar instrucciones de movimientos")
    elif opcion == "3":
        print("3. Crear informe de inventario")
    elif opcion == "4":
        print("4. Salir")
        break
    else:
        print("Por favor elige una opcion del menu.")