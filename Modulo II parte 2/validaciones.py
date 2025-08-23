from datetime import datetime

def validar_fecha(fecha_str):
    """
    Valida si la fecha ingresada cumple el formato dd/mm/yyyy.
    Retorna True si es válida, de lo contrario devuelve un mensaje de error.
    """
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return "La fecha no es válida. Use el formato dd/mm/yyyy."