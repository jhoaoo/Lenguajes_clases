import math

def raiz_cuadrada(n):
    try:
        if n < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return round(math.sqrt(n), 2)
    except ValueError as e:
        return str(e)

def raiz_cubica(n):
    resultado = n ** (1/3)
    return round(resultado, 2)

def potencia_cuadrado(n):
    return round(n ** 2, 2)

def potencia_cubo(n):
    return round(n ** 3, 2)