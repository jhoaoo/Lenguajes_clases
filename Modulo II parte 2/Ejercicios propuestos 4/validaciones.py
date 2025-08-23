def validar_contraseña(password):
    # Longitud mínima de 8 caracteres
    if len(password) < 8:
        return "Contraseña no reúne requisitos mínimos"
    
    # No debe contener espacios
    if any(c.isspace() for c in password):
        return "Contraseña no reúne requisitos mínimos"
    
    # Validaciones de tipos de caracteres
    tiene_mayuscula = any(c.isupper() for c in password)
    tiene_minuscula = any(c.islower() for c in password)
    tiene_numero = any(c.isdigit() for c in password)

    if tiene_mayuscula and tiene_minuscula and tiene_numero:
        return True
    else:
        return "Contraseña no reúne requisitos mínimos"
