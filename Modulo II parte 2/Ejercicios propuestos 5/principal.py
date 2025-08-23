from validaciones import validar_fecha

fecha = input("Ingrese una fecha en formato dd/mm/yyyy: ")
resultado = validar_fecha(fecha)

if resultado is True:
    print("Fecha válida")
else:
    print(resultado)