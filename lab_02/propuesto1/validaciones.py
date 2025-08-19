def ingresar_numero(mensaje):
    """Valida que el input sea un número"""
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("Error: Debe ingresar un número válido. Intente nuevamente.")