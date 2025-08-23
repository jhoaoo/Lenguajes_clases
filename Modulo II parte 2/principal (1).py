from validaciones import validar_contraseña

contraseña = input("Ingrese una contraseña para validar: ")
resultado = validar_contraseña(contraseña)

if resultado is True:
    print("Contraseña válida")
else:
    print(resultado)