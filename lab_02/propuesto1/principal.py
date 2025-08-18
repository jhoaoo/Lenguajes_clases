from propuesto1 import geometria, aritmetica
from . import validaciones

def pedir_numero(mensaje):
    while True:
        valor = input(mensaje)
        if validaciones.es_numero(valor):
            return float(valor)
        else:
            print("Por favor, ingrese un número válido.")

def main():
    print("Calculando áreas:")
    base = pedir_numero("Ingrese la base del triángulo: ")
    altura = pedir_numero("Ingrese la altura del triángulo: ")
    print("Área del triángulo:", geometria.area_triangulo(base, altura))

    lado = pedir_numero("Ingrese el lado del cuadrado: ")
    print("Área del cuadrado:", geometria.area_cuadrado(lado))

    base_r = pedir_numero("Ingrese la base del rectángulo: ")
    altura_r = pedir_numero("Ingrese la altura del rectángulo: ")
    print("Área del rectángulo:", geometria.area_rectangulo(base_r, altura_r))

    print("\nOperaciones aritméticas:")
    a = pedir_numero("Ingrese el primer número: ")
    b = pedir_numero("Ingrese el segundo número: ")
    print("Suma:", aritmetica.suma(a, b))
    print("Resta:", aritmetica.resta(a, b))
    print("Multiplicación:", aritmetica.multiplicacion(a, b))
    print("División:", aritmetica.division(a, b))
    print("Potencia:", aritmetica.potencia(a, b))
    print("Resto:", aritmetica.resto(a, b))

if __name__ == "__main__":
    main()
