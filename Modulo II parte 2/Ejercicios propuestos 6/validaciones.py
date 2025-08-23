def validar_nombre(nombre):
    while not nombre:
        nombre = input("El nombre no puede estar vacío. Por favor, ingrese un nombre: ")
    return nombre.title()

def validar_direccion(direccion):
    while not direccion:
        direccion = input("La dirección no puede estar vacía. Por favor, ingrese una dirección: ")
    return direccion.capitalize()

def validar_telefono(telefono):
    while not telefono.isdigit():
        telefono = input("El teléfono solo debe contener números. Por favor, ingrese un número de teléfono válido: ")
    return telefono