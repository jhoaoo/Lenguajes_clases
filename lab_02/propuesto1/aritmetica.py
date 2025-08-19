def suma(a, b):
    """Suma dos números"""
    try:
        return a + b
    except TypeError:
        print("Error: Ambos valores deben ser numéricos")
        return None

def resta(a, b):
    """Resta dos números"""
    try:
        return a - b
    except TypeError:
        print("Error: Ambos valores deben ser numéricos")
        return None

def multiplicacion(a, b):
    """Multiplica dos números"""
    try:
        return a * b
    except TypeError:
        print("Error: Ambos valores deben ser numéricos")
        return None

def division(a, b):
    """Divide dos números con manejo de división por cero"""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
        return None
    except TypeError:
        print("Error: Ambos valores deben ser numéricos")
        return None

def potencia(a, b):
    """Calcula a elevado a la b"""
    try:
        return a ** b
    except TypeError:
        print("Error: Ambos valores deben ser numéricos")
        return None

def resto(a, b):
    """Calcula el resto de la división a/b"""
    try:
        return a % b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
        return None
    except TypeError:
        print("Error: Ambos valores deben ser numéricos")
        return None
