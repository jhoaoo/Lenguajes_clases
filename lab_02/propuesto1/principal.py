from validaciones import ingresar_numero
from geometria import area_triangulo, area_cuadrado
from aritmetica import suma, division
if __name__ == "__main__":
    base = ingresar_numero("Ingrese base del triángulo: ")
    altura = ingresar_numero("Ingrese altura del triángulo: ")
    print(f"Área del triángulo: {area_triangulo(base, altura)}")
    num1 = ingresar_numero("Ingrese primer número: ")
    num2 = ingresar_numero("Ingrese segundo número: ")
    print(f"Suma: {suma(num1, num2)}")
    print(f"División: {division(num1, num2)}")
