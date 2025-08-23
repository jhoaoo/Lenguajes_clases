from funciones_math import raiz_cuadrada, raiz_cubica, potencia_cuadrado, potencia_cubo

def mostrar_menu():
    print("\n--- MENÚ DE OPERACIONES ---")
    print("1. Raíz cuadrada")
    print("2. Raíz cúbica")
    print("3. Potencia al cuadrado")
    print("4. Potencia al cubo")
    print("5. Salir")

def main():
    try:
        numero = int(input("Ingrese un número entero: "))
    except ValueError:
        print("Debe ingresar un número entero válido.")
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Raíz cuadrada:", raiz_cuadrada(numero))
        elif opcion == "2":
            print("Raíz cúbica:", raiz_cubica(numero))
        elif opcion == "3":
            print("Potencia al cuadrado:", potencia_cuadrado(numero))
        elif opcion == "4":
            print("Potencia al cubo:", potencia_cubo(numero))
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()