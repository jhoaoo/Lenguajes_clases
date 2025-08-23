from validaciones import validar_nombre, validar_direccion, validar_telefono
agenda = {}

def mostrar_menu():
    print("\n--- Menú de la Agenda ---")
    print("I. Opción 1: Registrar agenda.")
    print("II. Opción 2: Listar agenda.")
    print("III. Opción 3: Salir.")

def registrar_agenda():
    print("\n--- Registrar Nuevo Contacto ---")
    nombre = validar_nombre(input("Registrar nombre: "))
    direccion = validar_direccion(input("Registrar dirección: "))
    telefono = validar_telefono(input("Registrar número de teléfono o celular: "))
    agenda[nombre] = {
        'direccion': direccion,
        'telefono': telefono
    }
    print("¡Registro completado con éxito!")

def listar_agenda():
    if not agenda:
        print("\nLa agenda está vacía. No hay registros para mostrar.")
    else:
        print("\n--- Lista de Registros ---")
        for nombre, datos in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Dirección: {datos['direccion']}")
            print(f"Teléfono: {datos['telefono']}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción (1, 2, 3): ")
        
        if opcion == '1':
            registrar_agenda()
        elif opcion == '2':
            listar_agenda()
        elif opcion == '3':
            print("\n¡Gracias por usar la aplicación! Saliendo del programa.")
            break
        else:
            print("\nOpción no válida. Por favor, elija una de las opciones del menú.")
if __name__ == "__main__":
    main()